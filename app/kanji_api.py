import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import furigana, kanji, lessons, srs
from .db import connect
from .kanji_meanings import cue
from .srs import Rating

router = APIRouter(prefix="/api/kanji", tags=["kanji"])

_RATINGS = {"again": Rating.Again, "hard": Rating.Hard, "good": Rating.Good, "easy": Rating.Easy}
_LESSON_ORDER = {les["id"]: i for i, les in enumerate(lessons.LESSONS)}


def _ordered(group: str) -> list[dict]:
    """A group's kanji in study order: frequency for the N5/N4 lists, lesson
    order for kanji that only come from the lessons. The N3, N2 and N1 lists put kanji
    the lessons use first (in lesson order), then lower school grades, so they
    don't open with newspaper kanji like 政 and 議."""
    items = [e for e in kanji.all_kanji().values() if e["group"] == group]
    if group == "lessons":
        return sorted(items, key=lambda e: (_LESSON_ORDER.get(e["lesson"], 999), e["strokes"]))
    if group in ("N3", "N2", "N1"):
        return sorted(items, key=lambda e: (_LESSON_ORDER.get(e["lesson"], 999), e["grade"] or 9, e["freq"] or 9999))
    return sorted(items, key=lambda e: (e["freq"] or 9999, e["strokes"]))


def _statuses(conn) -> dict[str, str]:
    return {r["kanji"]: srs.status(r["state"], r["stability"])
            for r in conn.execute("SELECT kanji, state, stability FROM kanji_cards")}


def _require_data() -> None:
    if not kanji.available():
        raise HTTPException(503, "Kanji data isn't installed (data/dict/kanjidic2.xml.gz).")


def add_card(conn, ch: str) -> bool:
    row = srs.to_row(srs.new_card())
    cur = conn.execute(
        """INSERT OR IGNORE INTO kanji_cards (kanji, state, stability, due_ts, fsrs, created_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (ch, row["state"], row["stability"], row["due_ts"], row["fsrs"], time.time()),
    )
    return cur.rowcount > 0


@router.get("")
def list_kanji():
    if not kanji.available():
        return {"available": False, "groups": {}}
    with connect() as conn:
        status = _statuses(conn)
    return {"available": True, "groups": {
        group: [{"kanji": e["kanji"], "meaning": (e["meanings"] or [""])[0], "strokes": e["strokes"],
                 "in_lessons": bool(e["lesson"]), "status": status.get(e["kanji"], "locked")}
                for e in _ordered(group)]
        for group in kanji.GROUPS
    }}


# ---------- reviews (declared before /{ch} so "review" isn't read as a kanji) ----------

def due_count(conn, now: float | None = None) -> int:
    return conn.execute("SELECT COUNT(*) FROM kanji_cards WHERE due_ts <= ?", (now or time.time(),)).fetchone()[0]


@router.get("/review")
def kanji_review(limit: int = 50):
    now = time.time()
    with connect() as conn:
        rows = conn.execute("SELECT id, kanji FROM kanji_cards WHERE due_ts <= ? ORDER BY due_ts LIMIT ?",
                            (now, limit)).fetchall()
        count = due_count(conn, now)
        next_due = conn.execute("SELECT MIN(due_ts) FROM kanji_cards WHERE due_ts > ?", (now,)).fetchone()[0]
    cards = []
    for r in rows:
        e = kanji.get(r["kanji"])
        if e:
            cards.append({"id": r["id"], "kanji": e["kanji"], "meanings": e["meanings"],
                          "cue": cue(e["kanji"], e["meanings"][:3]), "on": e["on"],
                          "kun": e["kun"], "examples": e["examples"][:2], "strokes": kanji.strokes(e["kanji"])})
    return {"cards": cards, "due_count": count, "next_due": next_due}


class KanjiAnswer(BaseModel):
    card_id: int
    rating: str
    elapsed_ms: int | None = Field(default=None, ge=0)


@router.post("/review")
def kanji_answer(ans: KanjiAnswer):
    rating = _RATINGS.get(ans.rating)
    if rating is None:
        raise HTTPException(400, f"rating must be one of {list(_RATINGS)}")
    with connect() as conn:
        row = conn.execute("SELECT id, fsrs FROM kanji_cards WHERE id = ?", (ans.card_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "card not found")
        new = srs.to_row(srs.review(row["fsrs"], rating, ans.elapsed_ms))
        conn.execute("UPDATE kanji_cards SET state = ?, stability = ?, due_ts = ?, fsrs = ? WHERE id = ?",
                     (new["state"], new["stability"], new["due_ts"], new["fsrs"], row["id"]))
        conn.execute("INSERT INTO kanji_reviews (card_id, rating, elapsed_ms, reviewed_at) VALUES (?, ?, ?, ?)",
                     (row["id"], int(rating), ans.elapsed_ms, time.time()))
    return {"next_due": new["due_ts"]}


REVIEW_GAP = 12 * 3600  # don't re-grade a kanji that isn't due and was reviewed this recently


def rating_for_writing(mistakes: int, hinted: bool) -> Rating:
    """How a from-memory drawing counts as a review."""
    if hinted or mistakes >= 3:
        return Rating.Again
    if mistakes:
        return Rating.Hard
    return Rating.Good


class Written(BaseModel):
    mistakes: int = Field(ge=0, le=200)
    hinted: bool = False
    elapsed_ms: int | None = Field(default=None, ge=0)


@router.post("/{ch}/written")
def written(ch: str, body: Written):
    """Grade a kanji's review from a from-memory drawing.

    Kanji not in the reviews aren't touched, and a card that isn't due yet and
    was reviewed in the last 12 hours is left alone, so repeated practice
    can't inflate its schedule."""
    rating = rating_for_writing(body.mistakes, body.hinted)
    now = time.time()
    with connect() as conn:
        row = conn.execute("SELECT id, fsrs, due_ts FROM kanji_cards WHERE kanji = ?", (ch,)).fetchone()
        if row is None:
            return {"counted": False, "reason": "not_in_reviews", "rating": rating.name}
        last = conn.execute("SELECT MAX(reviewed_at) FROM kanji_reviews WHERE card_id = ?", (row["id"],)).fetchone()[0]
        if row["due_ts"] > now and last and now - last < REVIEW_GAP:
            return {"counted": False, "reason": "reviewed_recently", "rating": rating.name, "next_due": row["due_ts"]}
        new = srs.to_row(srs.review(row["fsrs"], rating, body.elapsed_ms))
        conn.execute("UPDATE kanji_cards SET state = ?, stability = ?, due_ts = ?, fsrs = ? WHERE id = ?",
                     (new["state"], new["stability"], new["due_ts"], new["fsrs"], row["id"]))
        conn.execute("""INSERT INTO kanji_reviews (card_id, rating, elapsed_ms, reviewed_at, source)
                        VALUES (?, ?, ?, ?, 'writing')""", (row["id"], int(rating), body.elapsed_ms, now))
    return {"counted": True, "rating": rating.name, "next_due": new["due_ts"]}


class LearnNext(BaseModel):
    group: str
    count: int = Field(default=5, ge=1, le=20)


@router.post("/learn-next")
def learn_next(body: LearnNext):
    """Add the next few not-yet-studied kanji of a group to the reviews."""
    _require_data()
    if body.group not in kanji.GROUPS:
        raise HTTPException(404, "unknown group")
    with connect() as conn:
        status = _statuses(conn)
        todo = [e["kanji"] for e in _ordered(body.group) if e["kanji"] not in status][: body.count]
        for ch in todo:
            add_card(conn, ch)
    return {"added": todo}


@router.get("/writing-set")
def writing_set(source: str = "studied", limit: int = 10):
    """Kanji to practise writing from memory: the learner's own kanji (most
    overdue first), or the first not-yet-studied ones of a list."""
    _require_data()
    limit = max(1, min(limit, 30))
    with connect() as conn:
        if source == "studied":
            chosen = [r["kanji"] for r in conn.execute("SELECT kanji FROM kanji_cards ORDER BY due_ts LIMIT ?", (limit,))]
        elif source in kanji.GROUPS:
            status = _statuses(conn)
            ordered = _ordered(source)
            chosen = ([e["kanji"] for e in ordered if e["kanji"] in status] + [e["kanji"] for e in ordered if e["kanji"] not in status])[:limit]
        else:
            raise HTTPException(400, "source must be 'studied' or a kanji group")
    items = []
    for ch in chosen:
        e = kanji.get(ch)
        paths = kanji.strokes(ch)
        if e and paths:
            items.append({"kanji": ch, "meanings": cue(ch, e["meanings"][:3]), "on": e["on"][:2], "kun": e["kun"][:2],
                          "strokes": len(paths), "stroke_paths": paths})
    return {"items": items}


# ---------- single kanji ----------

@router.get("/{ch}")
def kanji_detail(ch: str):
    _require_data()
    e = kanji.get(ch)
    if e is None:
        raise HTTPException(404, "kanji not in the study set")
    order = [x["kanji"] for x in _ordered(e["group"])]
    i = order.index(ch)
    with connect() as conn:
        status = _statuses(conn).get(ch, "locked")
    lesson = lessons.get(e["lesson"]) if e["lesson"] else None
    return {
        **e,
        "status": status,
        "stroke_paths": kanji.strokes(ch),
        "examples": [{**x, "segments": furigana.annotate(x["word"])} for x in e["examples"]],
        "lesson_label": f"{lessons.label(lesson)}: {lesson['title']}" if lesson else None,
        "prev": order[i - 1] if i > 0 else None,
        "next": order[i + 1] if i + 1 < len(order) else None,
        "position": i + 1, "group_size": len(order),
    }


@router.post("/{ch}/learn")
def learn(ch: str):
    _require_data()
    if kanji.get(ch) is None:
        raise HTTPException(404, "kanji not in the study set")
    with connect() as conn:
        added = add_card(conn, ch)
    return {"added": added}
