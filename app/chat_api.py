import json
import time

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from . import checks, deck_api, furigana, lessons, llm, tutor
from .db import connect, get_setting, set_setting

router = APIRouter(prefix="/api", tags=["chat"])

HISTORY_LIMIT = 20  # messages sent to the model; older ones stay in the database
BUSY_COOLDOWN = 300  # seconds to skip a model after it was overloaded

_busy_until: dict[tuple[str, str], float] = {}


# ---------- provider settings ----------

async def _current_llm() -> tuple[llm.Provider, str]:
    with connect() as conn:
        provider_id = get_setting(conn, "llm.provider", "gemini")
        model = get_setting(conn, "llm.model")
    provider = llm.PROVIDERS.get(provider_id, llm.PROVIDERS["gemini"])
    if not model:
        model = await llm.default_model(provider)
        if not model:
            raise llm.LLMError(f"{provider.label} has no chat models available.")
        with connect() as conn:
            set_setting(conn, "llm.model", model)
    return provider, model


@router.get("/llm/status")
def llm_status():
    with connect() as conn:
        current = {
            "provider": get_setting(conn, "llm.provider", "gemini"),
            "model": get_setting(conn, "llm.model"),
        }
    return {
        "providers": [
            {"id": p.id, "label": p.label, "configured": llm.is_configured(p)}
            for p in llm.PROVIDERS.values()
        ],
        "current": current,
    }


@router.get("/llm/models")
async def llm_models(provider: str):
    if provider not in llm.PROVIDERS:
        raise HTTPException(404, "unknown provider")
    try:
        return {"models": await llm.list_models(llm.PROVIDERS[provider])}
    except llm.LLMError as err:
        raise HTTPException(502, str(err)) from err


class LLMSettings(BaseModel):
    provider: str
    model: str = Field(min_length=1, max_length=200)


@router.put("/llm/settings")
def llm_settings(body: LLMSettings):
    if body.provider not in llm.PROVIDERS:
        raise HTTPException(404, "unknown provider")
    with connect() as conn:
        set_setting(conn, "llm.provider", body.provider)
        set_setting(conn, "llm.model", body.model)
    return {"ok": True}


# ---------- chats ----------

def _message_out(row) -> dict:
    return {
        "id": row["id"],
        "role": row["role"],
        "content": row["content"],
        "segments": furigana.annotate(row["content"]),
        "model": row["model"],
        "warnings": checks.romaji_mismatches(row["content"]) if row["role"] == "assistant" else [],
    }


@router.get("/chats")
def list_chats():
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, title, updated_at FROM chats ORDER BY updated_at DESC LIMIT 50"
        ).fetchall()
    return {"chats": [dict(r) for r in rows]}


@router.post("/chats")
def create_chat():
    now = time.time()
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO chats (title, created_at, updated_at) VALUES (?, ?, ?)",
            ("New chat", now, now),
        )
    return {"id": cur.lastrowid, "title": "New chat"}


@router.get("/chats/{chat_id}")
def get_chat(chat_id: int):
    with connect() as conn:
        chat = conn.execute("SELECT id, title, lesson_id FROM chats WHERE id = ?", (chat_id,)).fetchone()
        if chat is None:
            raise HTTPException(404, "chat not found")
        rows = conn.execute(
            "SELECT * FROM chat_messages WHERE chat_id = ? ORDER BY id", (chat_id,)
        ).fetchall()
    return {"id": chat["id"], "title": chat["title"], "lesson_id": chat["lesson_id"],
            "messages": [_message_out(r) for r in rows]}


@router.delete("/chats/{chat_id}")
def delete_chat(chat_id: int):
    with connect() as conn:
        conn.execute("DELETE FROM chats WHERE id = ?", (chat_id,))
    return {"ok": True}


class NewMessage(BaseModel):
    # None = retry: answer the last user message again without adding a new one.
    content: str | None = Field(default=None, max_length=2000)


def _sse(event: dict) -> str:
    return f"data: {json.dumps(event, ensure_ascii=False)}\n\n"


@router.post("/chats/{chat_id}/messages")
async def post_message(chat_id: int, body: NewMessage):
    content = body.content.strip() if body.content else None
    now = time.time()
    user_message = None

    with connect() as conn:
        chat = conn.execute("SELECT id, title, lesson_id FROM chats WHERE id = ?", (chat_id,)).fetchone()
        if chat is None:
            raise HTTPException(404, "chat not found")
        if content:
            cur = conn.execute(
                "INSERT INTO chat_messages (chat_id, role, content, created_at) VALUES (?, 'user', ?, ?)",
                (chat_id, content, now),
            )
            user_message = _message_out(
                conn.execute("SELECT * FROM chat_messages WHERE id = ?", (cur.lastrowid,)).fetchone())
            if chat["title"] == "New chat":
                title = content if len(content) <= 40 else content[:39] + "…"
                conn.execute("UPDATE chats SET title = ? WHERE id = ?", (title, chat_id))
            conn.execute("UPDATE chats SET updated_at = ? WHERE id = ?", (now, chat_id))

        history = conn.execute(
            "SELECT role, content FROM chat_messages WHERE chat_id = ? ORDER BY id DESC LIMIT ?",
            (chat_id, HISTORY_LIMIT),
        ).fetchall()[::-1]
        if not history or history[-1]["role"] != "user":
            raise HTTPException(400, "nothing to answer")
        system = tutor.system_prompt(conn)
        lesson = lessons.get(chat["lesson_id"]) if chat["lesson_id"] else None
        if lesson:
            system += lessons.tutor_brief(lesson)
        messages = [{"role": "system", "content": system}]
        messages += tutor.with_reminder([{"role": r["role"], "content": r["content"]} for r in history])

    async def events():
        if user_message:
            yield _sse({"type": "user", "message": user_message})
        parts = []
        try:
            provider, model = await _current_llm()
            skip_main = _busy_until.get((provider.id, model), 0) > time.time()
            shown = 0

            async def visible_deltas(model_id: str):
                # The reply may end with a hidden mistake log; never stream that part.
                nonlocal shown
                async for piece in llm.stream_chat(provider, model_id, messages):
                    parts.append(piece)
                    visible = tutor.visible_part("".join(parts))
                    if len(visible) > shown:
                        yield visible[shown:]
                        shown = len(visible)

            try:
                if skip_main:
                    raise llm.LLMError("recently overloaded", retryable=True)
                async for text in visible_deltas(model):
                    yield _sse({"type": "delta", "text": text})
            except llm.LLMError as err:
                # Free-tier models get overloaded; if nothing was shown yet,
                # quietly let the lighter fallback model answer instead.
                if parts or not err.retryable or not provider.fallback or model == provider.fallback:
                    raise
                if not skip_main:
                    _busy_until[(provider.id, model)] = time.time() + BUSY_COOLDOWN
                model = provider.fallback
                yield _sse({"type": "notice", "message": f"Main model busy, answering with {model}."})
                async for text in visible_deltas(model):
                    yield _sse({"type": "delta", "text": text})
            reply, corrections = tutor.split_corrections("".join(parts))
            if not reply:
                raise llm.LLMError(f"{provider.label} returned an empty reply. Try again.")
        except llm.LLMError as err:
            yield _sse({"type": "error", "message": str(err)})
            return

        with connect() as conn:
            cur = conn.execute(
                """INSERT INTO chat_messages (chat_id, role, content, provider, model, created_at)
                   VALUES (?, 'assistant', ?, ?, ?, ?)""",
                (chat_id, reply, provider.id, model, time.time()),
            )
            conn.execute("UPDATE chats SET updated_at = ? WHERE id = ?", (time.time(), chat_id))
            mistakes_saved = deck_api.save_mistakes(conn, chat_id, corrections)
            row = conn.execute("SELECT * FROM chat_messages WHERE id = ?", (cur.lastrowid,)).fetchone()
        yield _sse({"type": "done", "message": _message_out(row), "mistakes_saved": mistakes_saved})

    return StreamingResponse(events(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache"})


class FuriganaRequest(BaseModel):
    text: str = Field(max_length=5000)


@router.post("/furigana")
def post_furigana(body: FuriganaRequest):
    return {"segments": furigana.annotate(body.text)}
