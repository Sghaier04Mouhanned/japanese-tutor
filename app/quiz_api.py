import json
import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import kanji, lessons, quiz
from .db import connect
from .deck_api import add_card
from .kanji_api import add_card as add_kanji_card

router = APIRouter(prefix="/api/quiz", tags=["quiz"])

KANJI_SOURCES = ("studied", "N5", "N4", "N3", "N2", "lessons")


def _saved_words(conn) -> list[dict]:
    return [dict(r) for r in conn.execute("SELECT word, reading, meaning FROM vocab")]


def _kanji_pool(conn, source: str) -> tuple[list[dict], list[dict]]:
    """(kanji to ask about, all kanji for wrong answers)."""
    if not kanji.available():
        return [], []
    index = kanji.all_kanji()
    if source == "studied":
        chosen = [index[r["kanji"]] for r in conn.execute("SELECT kanji FROM kanji_cards") if r["kanji"] in index]
    else:
        chosen = [e for e in index.values() if e["group"] == source]
    return chosen, list(index.values())


@router.get("/options")
def options():
    with connect() as conn:
        progress = {r["lesson_id"]: r["status"] for r in conn.execute("SELECT lesson_id, status FROM lesson_progress")}
        saved = conn.execute("SELECT COUNT(*) FROM vocab").fetchone()[0]
        studied_kanji = conn.execute("SELECT COUNT(*) FROM kanji_cards").fetchone()[0]
        recent = [dict(r) for r in conn.execute(
            "SELECT created_at, total, correct FROM quiz_sessions ORDER BY created_at DESC LIMIT 5")]
    return {
        "kanji_available": kanji.available(),
        "studied_kanji": studied_kanji,
        "lessons": [{"id": les["id"], "title": les["title"], "level": lessons.level(les),
                     "number": lessons.number(les), "status": progress.get(les["id"], "new")}
                    for les in lessons.LESSONS],
        "saved_words": saved,
        "types": list(quiz.TYPES),
        "recent": recent,
    }


class NewQuiz(BaseModel):
    lessons: list[str] = Field(default_factory=list, max_length=50)
    include_saved: bool = True
    count: int = Field(default=10, ge=1, le=40)
    types: list[str] = Field(default_factory=lambda: list(quiz.TYPES))
    kanji_source: str = "studied"


@router.post("/new")
def new_quiz(body: NewQuiz):
    types = tuple(t for t in body.types if t in quiz.TYPES)
    if not types:
        raise HTTPException(400, "choose at least one question type")
    if body.kanji_source not in KANJI_SOURCES:
        raise HTTPException(400, f"kanji_source must be one of {KANJI_SOURCES}")
    with connect() as conn:
        saved = _saved_words(conn) if body.include_saved else []
        kanji_items, kanji_all = _kanji_pool(conn, body.kanji_source) if set(types) & set(quiz.KANJI_TYPES) else ([], [])
    questions = quiz.build(body.lessons, saved, body.count, types, kanji_items, kanji_all)
    if not questions:
        raise HTTPException(400, "not enough material for these settings; add lessons or question types")
    return {"questions": questions}


class Result(BaseModel):
    type: str
    correct: bool


class Results(BaseModel):
    results: list[Result] = Field(max_length=100)


@router.post("/results")
def save_results(body: Results):
    by_type: dict[str, list[int]] = {}
    for r in body.results:
        stats = by_type.setdefault(r.type, [0, 0])
        stats[0] += int(r.correct)
        stats[1] += 1
    correct = sum(int(r.correct) for r in body.results)
    with connect() as conn:
        conn.execute(
            "INSERT INTO quiz_sessions (created_at, total, correct, by_type) VALUES (?, ?, ?, ?)",
            (time.time(), len(body.results), correct, json.dumps(by_type)),
        )
    return {"total": len(body.results), "correct": correct, "by_type": by_type}


class Word(BaseModel):
    word: str = Field(max_length=50)
    reading: str = Field(max_length=50)
    meaning: str = Field(max_length=300)


class AddWords(BaseModel):
    words: list[Word] = Field(default_factory=list, max_length=40)
    kanji: list[str] = Field(default_factory=list, max_length=40)


@router.post("/add-missed")
def add_missed(body: AddWords):
    """Put words and kanji the learner got wrong into the review deck."""
    added = 0
    with connect() as conn:
        for ch in body.kanji:
            if len(ch) == 1 and kanji.get(ch) and add_kanji_card(conn, ch):
                added += 1
        for w in body.words:
            cur = conn.execute(
                """INSERT OR IGNORE INTO vocab (entry_id, word, reading, meaning, source, created_at)
                   VALUES (NULL, ?, ?, ?, 'quiz', ?)""",
                (w.word, w.reading, w.meaning, time.time()),
            )
            if cur.rowcount:
                add_card(conn, "vocab", cur.lastrowid)
                added += 1
    return {"added": added}
