"""The JLPT word lists (app/words.py): browse a level, add words to the reviews."""

import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import furigana, lessons, srs, words
from .db import connect
from .deck_api import add_card

router = APIRouter(prefix="/api/words", tags=["words"])


def statuses(conn) -> dict[str, str]:
    """List word id -> review status, for every saved word that stands for a list
    word (lessons save 行きます, which is the list's 行く)."""
    rows = conn.execute(
        """SELECT v.word, v.reading, v.entry_id, c.state, c.stability FROM vocab v
           LEFT JOIN deck_cards c ON c.kind = 'vocab' AND c.ref_id = v.id""").fetchall()
    rank = {"learning": 1, "known": 2, "mastered": 3}
    out: dict[str, str] = {}
    for r in rows:
        w = words.match(r["word"], r["reading"], r["entry_id"])
        if w is None:
            continue
        status = srs.status(r["state"], r["stability"]) if r["state"] is not None else "learning"
        if rank[status] > rank.get(out.get(w["id"]), 0):
            out[w["id"]] = status
    return out


def _require_level(level: str) -> None:
    if level not in words.LEVELS:
        raise HTTPException(404, f"level must be one of {list(words.LEVELS)}")


def _save(conn, w: dict) -> None:
    cur = conn.execute(
        """INSERT OR IGNORE INTO vocab (entry_id, word, reading, meaning, source, created_at)
           VALUES (?, ?, ?, ?, 'jlpt', ?)""",
        (w["entry_id"], w["word"], w["reading"], w["meaning"], time.time()),
    )
    if cur.rowcount:
        add_card(conn, "vocab", cur.lastrowid)


def _ruby_parts(word: str, reading: str) -> list[dict] | None:
    """Furigana from the list's own reading (the analyzer can misread a word on
    its own, like 生ける), with affix marks kept bare: ～人 is ～ + 人(じん)."""
    core = word.strip("～")
    if not furigana._KANJI.search(core):
        return None
    parts = furigana._split_okurigana(core, furigana._to_hiragana(reading.strip("～")))
    return [{"t": "～"}] * word.startswith("～") + parts + [{"t": "～"}] * word.endswith("～")


@router.get("")
def list_words(level: str = "N5"):
    _require_level(level)
    with connect() as conn:
        status = statuses(conn)
    return {
        "counts": {lvl: len(words.by_level(lvl)) for lvl in words.LEVELS},
        "words": [{"id": w["id"], "word": w["word"], "reading": w["reading"], "meaning": w["meaning"],
                   "note": w["note"], "lesson": w["lesson"], "status": status.get(w["id"], "locked")}
                  for w in words.by_level(level)],
    }


class LearnNext(BaseModel):
    level: str
    count: int = Field(default=10, ge=1, le=30)


@router.post("/learn-next")
def learn_next(body: LearnNext):
    """Add the next few not-yet-studied words of a level to the reviews."""
    _require_level(body.level)
    with connect() as conn:
        status = statuses(conn)
        todo = [w for w in words.by_level(body.level) if w["id"] not in status][: body.count]
        for w in todo:
            _save(conn, w)
    return {"added": [w["word"] for w in todo]}


@router.get("/{word_id}")
def word_detail(word_id: str):
    w = words.get(word_id)
    if w is None:
        raise HTTPException(404, "word not in the lists")
    lesson = lessons.get(w["lesson"]) if w["lesson"] else None
    order = [x["id"] for x in words.by_level(w["level"])]
    i = order.index(word_id)
    with connect() as conn:
        status = statuses(conn).get(word_id, "locked")
    return {
        **{k: w[k] for k in ("id", "level", "word", "reading", "meaning", "note", "lesson")},
        "status": status,
        "parts": _ruby_parts(w["word"], w["reading"]),
        "lesson_label": f"{lessons.label(lesson)}: {lesson['title']}" if lesson else None,
        "examples": [{**e, "segments": furigana.annotate(e["jp"])} for e in words.examples(w)],
        "prev": order[i - 1] if i > 0 else None,
        "next": order[i + 1] if i + 1 < len(order) else None,
        "position": i + 1, "level_size": len(order),
    }


@router.post("/{word_id}/learn")
def learn(word_id: str):
    w = words.get(word_id)
    if w is None:
        raise HTTPException(404, "word not in the lists")
    with connect() as conn:
        if word_id not in statuses(conn):
            _save(conn, w)
    return {"ok": True}
