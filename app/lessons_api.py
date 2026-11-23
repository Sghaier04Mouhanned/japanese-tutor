import time

from fastapi import APIRouter, HTTPException

from . import furigana, lessons
from .db import connect
from .deck_api import add_card

router = APIRouter(prefix="/api/lessons", tags=["lessons"])


def _progress(conn) -> dict[str, str]:
    return {r["lesson_id"]: r["status"] for r in conn.execute("SELECT lesson_id, status FROM lesson_progress")}


def _set_status(conn, lesson_id: str, status: str) -> None:
    conn.execute(
        """INSERT INTO lesson_progress (lesson_id, status, updated_at) VALUES (?, ?, ?)
           ON CONFLICT (lesson_id) DO UPDATE SET
             status = CASE WHEN lesson_progress.status = 'done' THEN 'done' ELSE excluded.status END,
             updated_at = excluded.updated_at""",
        (lesson_id, status, time.time()),
    )


def _lesson_or_404(lesson_id: str) -> dict:
    lesson = lessons.get(lesson_id)
    if lesson is None:
        raise HTTPException(404, "lesson not found")
    return lesson


@router.get("")
def list_lessons():
    with connect() as conn:
        progress = _progress(conn)
    return {"lessons": [
        {"id": les["id"], "title": les["title"], "jp_title": les["jp_title"], "goal": les["goal"],
         "level": lessons.level(les), "number": lessons.number(les),
         "status": progress.get(les["id"], "new")}
        for les in lessons.LESSONS
    ]}


@router.get("/{lesson_id}")
def get_lesson(lesson_id: str):
    lesson = _lesson_or_404(lesson_id)
    with connect() as conn:
        status = _progress(conn).get(lesson_id, "new")
        saved = {(r["word"], r["reading"]) for r in conn.execute("SELECT word, reading FROM vocab")}
    index = lessons.LESSONS.index(lesson)
    return {
        **lesson,
        "number": lessons.number(lesson),
        "level": lessons.level(lesson),
        "status": status,
        "next_id": lessons.LESSONS[index + 1]["id"] if index + 1 < len(lessons.LESSONS) else None,
        "points": [furigana.annotate(p) for p in lesson["points"]],
        "examples": [{**e, "segments": furigana.annotate(e["jp"])} for e in lesson["examples"]],
        "vocab": [{**v, "segments": furigana.annotate(v["word"]), "saved": (v["word"], v["reading"]) in saved}
                  for v in lesson["vocab"]],
    }


@router.post("/{lesson_id}/practice")
def start_practice(lesson_id: str):
    """Open a chat in which Sensei runs exercises on this lesson."""
    lesson = _lesson_or_404(lesson_id)
    now = time.time()
    title = f"{lessons.label(lesson)}: {lesson['title']}"
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO chats (title, created_at, updated_at, lesson_id) VALUES (?, ?, ?, ?)",
            (title, now, now, lesson_id),
        )
        _set_status(conn, lesson_id, "started")
    return {"chat_id": cur.lastrowid, "title": title}


def add_words(conn, vocab: list[dict], source: str = "lesson") -> int:
    """Hand-written vocabulary (lessons, reading passages) into the notebook and reviews."""
    added = 0
    for v in vocab:
        cur = conn.execute(
            """INSERT OR IGNORE INTO vocab (entry_id, word, reading, meaning, source, created_at)
               VALUES (NULL, ?, ?, ?, ?, ?)""",
            (v["word"], v["reading"], v["meaning"], source, time.time()),
        )
        if cur.rowcount:
            add_card(conn, "vocab", cur.lastrowid)
            added += 1
    return added


@router.post("/{lesson_id}/complete")
def complete_lesson(lesson_id: str):
    """Mark the lesson done and put its vocabulary into the review deck."""
    lesson = _lesson_or_404(lesson_id)
    with connect() as conn:
        _set_status(conn, lesson_id, "done")
        added = add_words(conn, lesson["vocab"])
    return {"ok": True, "words_added": added}
