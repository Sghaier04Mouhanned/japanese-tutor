import time

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import furigana, listening, tts
from .db import connect
from .lessons_api import add_words

router = APIRouter(prefix="/api/listening", tags=["listening"])


def _item_or_404(item_id: str) -> dict:
    item = listening.get(item_id)
    if item is None:
        raise HTTPException(404, "listening item not found")
    return item


async def _voices() -> dict[str, int] | None:
    """VOICEVOX speaker id per role, or None when the engine isn't running (the page
    then falls back to the browser's voice)."""
    if not await tts.running():
        return None
    try:
        available = {(v["name"], v["style"]): v["id"] for v in await tts.speakers()}
        default = await tts.default_speaker()
    except httpx.HTTPError:
        return None
    return {role: available.get(name_style, default) for role, name_style in listening.VOICES.items()}


def _results(conn) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in conn.execute("SELECT item_id, correct FROM listening_results ORDER BY created_at"):
        prev = out.get(r["item_id"])
        out[r["item_id"]] = {"last": bool(r["correct"]), "ever": bool(r["correct"]) or bool(prev and prev["ever"])}
    return out


def _kind(item: dict) -> dict:
    en, jp, printed = listening.KINDS[item["kind"]]
    return {"kind": item["kind"], "kind_en": en, "kind_jp": jp, "choices_printed": printed}


@router.get("")
def list_items():
    with connect() as conn:
        results = _results(conn)
    return {"items": [
        {"id": i["id"], "title": i["title"], **_kind(i), "level": listening.level(i),
         "number": listening.number(i), "result": results.get(i["id"])}
        for i in listening.ITEMS
    ]}


@router.get("/{item_id}")
async def get_item(item_id: str):
    """What to play and what to show before answering. Choices only heard on the
    test (summary, quick) come back as numbers; the answer comes with the check."""
    item = _item_or_404(item_id)
    index = listening.ITEMS.index(item)
    printed = listening.KINDS[item["kind"]][2]
    return {
        "id": item["id"], "title": item["title"], **_kind(item),
        "level": listening.level(item), "number": listening.number(item),
        "question": item["question"],
        "question_segments": furigana.annotate(item["question"]) if item["question"] else [],
        "choices": [furigana.annotate(c) for c in item["choices"]] if printed else [None] * len(item["choices"]),
        "script": [{"who": s["who"], "text": s["text"]} for s in listening.script(item)],  # no translations yet
        "voices": await _voices(),
        "next_id": listening.ITEMS[index + 1]["id"] if index + 1 < len(listening.ITEMS) else None,
    }


class Answer(BaseModel):
    answer: int = Field(ge=0, le=9)
    plays: int = Field(default=1, ge=0, le=100)


@router.post("/{item_id}/answer")
def check_answer(item_id: str, body: Answer):
    item = _item_or_404(item_id)
    correct = body.answer == item["answer"]
    with connect() as conn:
        conn.execute("INSERT INTO listening_results (item_id, correct, plays, created_at) VALUES (?, ?, ?, ?)",
                     (item_id, int(correct), body.plays, time.time()))
        saved = {(r["word"], r["reading"]) for r in conn.execute("SELECT word, reading FROM vocab")}
    return {
        "correct": correct, "answer": item["answer"], "why": item["why"],
        "choices": [furigana.annotate(c) for c in item["choices"]],
        "transcript": [{"who": s["who"], "label": listening.ROLE_LABELS[s["who"]], "jp": s["text"],
                        "segments": furigana.annotate(s["text"]), "en": s["en"]}
                       for s in listening.script(item)],
        "vocab": [{**v, "segments": furigana.annotate(v["word"]), "saved": (v["word"], v["reading"]) in saved}
                  for v in item["vocab"]],
    }


@router.post("/{item_id}/words")
def add_item_words(item_id: str):
    item = _item_or_404(item_id)
    with connect() as conn:
        added = add_words(conn, item["vocab"], source="listening")
    return {"words_added": added}
