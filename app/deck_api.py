"""Dictionary lookups, the learner's saved words and mistakes, and their reviews."""

import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import checks, dictionary, srs
from .db import connect
from .srs import Rating

router = APIRouter(prefix="/api", tags=["deck"])

_RATINGS = {"again": Rating.Again, "hard": Rating.Hard, "good": Rating.Good, "easy": Rating.Easy}


def _has_kanji(text: str) -> bool:
    return any("㐀" <= c <= "鿿" or c == "々" for c in text)


# ---------- dictionary ----------

@router.get("/dict/lookup")
def dict_lookup(q: str, k: str | None = None, next: str = "", p: str | None = None):
    """Look up a clicked word. `next` holds the following words' text so that
    図書 + 館 can be found as 図書館; the longest match wins."""
    if not dictionary.available():
        return {"available": False, "entries": []}
    q, nxt = q[:30], next[:30]
    entries, matched = [], q
    for n in range(len(nxt), 0, -1):
        candidate = q + nxt[:n]
        entries = dictionary.lookup(candidate)
        if entries:
            matched = candidate
            break
    if not entries:
        entries = dictionary.lookup(q, k, pos=p)

    with connect() as conn:
        saved = {r["entry_id"] for r in conn.execute("SELECT entry_id FROM vocab WHERE entry_id IS NOT NULL")}
    return {
        "available": True,
        "matched": matched,
        "entries": [{**e, "senses": e["senses"][:5], "saved": e["id"] in saved} for e in entries[:3]],
    }


# ---------- vocab ----------

class SaveWord(BaseModel):
    entry_id: int
    word: str = Field(max_length=50)       # the form the learner clicked, e.g. 日本人
    source: str = "chat"


def add_card(conn, kind: str, ref_id: int) -> None:
    row = srs.to_row(srs.new_card())
    conn.execute(
        """INSERT OR IGNORE INTO deck_cards (kind, ref_id, state, stability, due_ts, fsrs, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (kind, ref_id, row["state"], row["stability"], row["due_ts"], row["fsrs"], time.time()),
    )


@router.post("/vocab")
def save_word(body: SaveWord):
    e = dictionary.entry(body.entry_id)
    if e is None:
        raise HTTPException(404, "dictionary entry not found")
    # Prefer the spelling that was clicked; fall back to the entry's main form.
    forms = e["kanji"] + e["readings"]
    word = body.word if body.word in forms else forms[0]
    reading = e["readings"][0]
    with connect() as conn:
        conn.execute(
            """INSERT OR IGNORE INTO vocab (entry_id, word, reading, meaning, source, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (e["id"], word, reading, dictionary.short_meaning(e), body.source, time.time()),
        )
        vocab_id = conn.execute("SELECT id FROM vocab WHERE word = ? AND reading = ?",
                                (word, reading)).fetchone()["id"]
        add_card(conn, "vocab", vocab_id)
    return {"id": vocab_id, "word": word, "reading": reading}


@router.get("/vocab")
def list_vocab():
    with connect() as conn:
        rows = conn.execute(
            """SELECT v.*, c.state, c.stability, c.due_ts FROM vocab v
               LEFT JOIN deck_cards c ON c.kind = 'vocab' AND c.ref_id = v.id
               ORDER BY v.created_at DESC"""
        ).fetchall()
    return {"words": [{**dict(r), "status": srs.status(r["state"], r["stability"])} for r in rows]}


@router.delete("/vocab/{vocab_id}")
def delete_vocab(vocab_id: int):
    with connect() as conn:
        conn.execute("DELETE FROM deck_cards WHERE kind = 'vocab' AND ref_id = ?", (vocab_id,))
        conn.execute("DELETE FROM vocab WHERE id = ?", (vocab_id,))
    return {"ok": True}


# ---------- mistakes ----------

def save_mistakes(conn, chat_id: int, mistakes: list[dict]) -> int:
    """Called by the chat when Sensei corrects the learner."""
    saved = 0
    for m in mistakes:
        wrong, correct = str(m.get("wrong", "")).strip(), str(m.get("correct", "")).strip()
        if not wrong or not correct or wrong == correct:
            continue
        cur = conn.execute(
            "INSERT INTO mistakes (chat_id, wrong, correct, note, created_at) VALUES (?, ?, ?, ?, ?)",
            (chat_id, wrong[:300], correct[:300], str(m.get("note", "")).strip()[:300], time.time()),
        )
        add_card(conn, "mistake", cur.lastrowid)
        saved += 1
    return saved


@router.get("/mistakes")
def list_mistakes():
    with connect() as conn:
        rows = conn.execute(
            """SELECT m.*, c.state, c.stability FROM mistakes m
               LEFT JOIN deck_cards c ON c.kind = 'mistake' AND c.ref_id = m.id
               ORDER BY m.created_at DESC"""
        ).fetchall()
    return {"mistakes": [{**dict(r), "status": srs.status(r["state"], r["stability"])} for r in rows]}


@router.delete("/mistakes/{mistake_id}")
def delete_mistake(mistake_id: int):
    with connect() as conn:
        conn.execute("DELETE FROM deck_cards WHERE kind = 'mistake' AND ref_id = ?", (mistake_id,))
        conn.execute("DELETE FROM mistakes WHERE id = ?", (mistake_id,))
    return {"ok": True}


# ---------- reviews ----------

def due_count(conn, now: float | None = None) -> int:
    return conn.execute("SELECT COUNT(*) FROM deck_cards WHERE due_ts <= ?",
                        (now or time.time(),)).fetchone()[0]


@router.get("/deck/review")
def deck_review(limit: int = 50):
    now = time.time()
    with connect() as conn:
        rows = conn.execute(
            """SELECT c.id, c.kind, c.ref_id,
                      v.word, v.reading, v.meaning,
                      m.wrong, m.correct, m.note
               FROM deck_cards c
               LEFT JOIN vocab v ON c.kind = 'vocab' AND v.id = c.ref_id
               LEFT JOIN mistakes m ON c.kind = 'mistake' AND m.id = c.ref_id
               WHERE c.due_ts <= ? ORDER BY c.due_ts LIMIT ?""",
            (now, limit),
        ).fetchall()
        count = due_count(conn, now)
        next_due = conn.execute("SELECT MIN(due_ts) FROM deck_cards WHERE due_ts > ?", (now,)).fetchone()[0]

    cards = []
    for r in rows:
        if r["kind"] == "vocab" and r["word"]:
            cards.append({"id": r["id"], "kind": "vocab", "word": r["word"], "reading": r["reading"],
                          "meaning": r["meaning"], "ask_reading": _has_kanji(r["word"])})
        elif r["kind"] == "mistake" and r["wrong"]:
            cards.append({"id": r["id"], "kind": "mistake", "wrong": r["wrong"],
                          "correct": r["correct"], "note": r["note"]})
    return {"cards": cards, "due_count": count, "next_due": next_due}


class ReadingCheck(BaseModel):
    reading: str = Field(max_length=50)
    answer: str = Field(max_length=50)


@router.post("/deck/check-reading")
def check_reading(body: ReadingCheck):
    return {"correct": checks.same_reading(body.reading, body.answer)}


class DeckAnswer(BaseModel):
    card_id: int
    rating: str
    elapsed_ms: int | None = Field(default=None, ge=0)


@router.post("/deck/review")
def deck_answer(ans: DeckAnswer):
    rating = _RATINGS.get(ans.rating)
    if rating is None:
        raise HTTPException(400, f"rating must be one of {list(_RATINGS)}")
    with connect() as conn:
        row = conn.execute("SELECT id, fsrs FROM deck_cards WHERE id = ?", (ans.card_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "card not found")
        new = srs.to_row(srs.review(row["fsrs"], rating, ans.elapsed_ms))
        conn.execute(
            "UPDATE deck_cards SET state = ?, stability = ?, due_ts = ?, fsrs = ? WHERE id = ?",
            (new["state"], new["stability"], new["due_ts"], new["fsrs"], row["id"]),
        )
        conn.execute(
            "INSERT INTO deck_reviews (card_id, rating, elapsed_ms, reviewed_at) VALUES (?, ?, ?, ?)",
            (row["id"], int(rating), ans.elapsed_ms, time.time()),
        )
    return {"next_due": new["due_ts"]}
