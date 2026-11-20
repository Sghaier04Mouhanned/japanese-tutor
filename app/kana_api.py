import time
from datetime import date, datetime, timedelta

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import kana, srs
from .db import connect

router = APIRouter(prefix="/api/kana", tags=["kana"])


def _check_script(script: str) -> None:
    if script not in kana.SCRIPTS:
        raise HTTPException(400, f"script must be one of {kana.SCRIPTS}")


def _unlocked_groups(conn, script: str) -> set[str]:
    rows = conn.execute(
        "SELECT DISTINCT group_id FROM kana_cards WHERE script = ?", (script,)
    ).fetchall()
    return {r["group_id"] for r in rows}


def _start_of_today() -> float:
    now = datetime.now().astimezone()
    return now.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()


@router.get("/groups")
def get_groups(script: str = "hiragana"):
    """Every group with its kana and how far along you are with each one."""
    _check_script(script)
    with connect() as conn:
        rows = conn.execute(
            "SELECT kana, state, stability FROM kana_cards WHERE script = ?", (script,)
        ).fetchall()
    card_status = {r["kana"]: srs.status(r["state"], r["stability"]) for r in rows}

    groups = kana.groups(script)
    next_group = None
    for g in groups:
        for item in g["items"]:
            item["status"] = card_status.get(item["kana"], "locked")
        g["unlocked"] = any(i["status"] != "locked" for i in g["items"])
        if not g["unlocked"] and next_group is None:
            next_group = g["id"]
    return {"script": script, "groups": groups, "next_group": next_group}


class UnlockRequest(BaseModel):
    script: str
    group: str


@router.post("/unlock")
def unlock(req: UnlockRequest):
    """Add a group's kana to your reviews. Groups unlock in order."""
    _check_script(req.script)
    order = kana.group_ids()
    if req.group not in order:
        raise HTTPException(404, "unknown group")

    with connect() as conn:
        unlocked = _unlocked_groups(conn, req.script)
        if req.group in unlocked:
            return {"added": 0}
        first_locked = next(g for g in order if g not in unlocked)
        if req.group != first_locked:
            raise HTTPException(409, f"learn '{first_locked}' first")

        group = next(g for g in kana.groups(req.script) if g["id"] == req.group)
        now = time.time()
        for item in group["items"]:
            row = srs.to_row(srs.new_card())
            conn.execute(
                """INSERT INTO kana_cards
                   (script, kana, group_id, state, stability, due_ts, fsrs, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (req.script, item["kana"], req.group, row["state"], row["stability"],
                 row["due_ts"], row["fsrs"], now),
            )
    return {"added": len(group["items"])}


@router.get("/review")
def get_review(limit: int = 50):
    """Cards due now (both scripts), most overdue first."""
    now = time.time()
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, script, kana FROM kana_cards WHERE due_ts <= ? ORDER BY due_ts LIMIT ?",
            (now, limit),
        ).fetchall()
        due_count = conn.execute(
            "SELECT COUNT(*) FROM kana_cards WHERE due_ts <= ?", (now,)
        ).fetchone()[0]
        next_due = conn.execute(
            "SELECT MIN(due_ts) FROM kana_cards WHERE due_ts > ?", (now,)
        ).fetchone()[0]

    lookups = {s: kana.lookup(s) for s in kana.SCRIPTS}
    cards = []
    for r in rows:
        item = lookups[r["script"]][r["kana"]]
        cards.append({"id": r["id"], "script": r["script"], **item})
    return {"cards": cards, "due_count": due_count, "next_due": next_due}


class ReviewAnswer(BaseModel):
    card_id: int
    answer: str = Field(max_length=20)
    elapsed_ms: int | None = Field(default=None, ge=0)


@router.post("/review")
def post_review(ans: ReviewAnswer):
    with connect() as conn:
        row = conn.execute(
            "SELECT id, script, kana, fsrs FROM kana_cards WHERE id = ?", (ans.card_id,)
        ).fetchone()
        if row is None:
            raise HTTPException(404, "card not found")

        item = kana.lookup(row["script"])[row["kana"]]
        correct = kana.is_correct(item["romaji"], ans.answer)
        rating = srs.rating_for(correct, ans.elapsed_ms)
        card = srs.review(row["fsrs"], rating, ans.elapsed_ms)
        new = srs.to_row(card)

        conn.execute(
            "UPDATE kana_cards SET state = ?, stability = ?, due_ts = ?, fsrs = ? WHERE id = ?",
            (new["state"], new["stability"], new["due_ts"], new["fsrs"], row["id"]),
        )
        conn.execute(
            """INSERT INTO kana_reviews (card_id, answer, correct, rating, elapsed_ms, reviewed_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (row["id"], ans.answer.strip().lower(), int(correct), int(rating),
             ans.elapsed_ms, time.time()),
        )

    return {
        "correct": correct,
        "romaji": item["romaji"],
        "accept": item["accept"],
        "rating": rating.name,
        "next_due": new["due_ts"],
    }


@router.get("/stats")
def get_stats():
    now = time.time()
    today = _start_of_today()
    with connect() as conn:
        per_script = {}
        for script in kana.SCRIPTS:
            rows = conn.execute(
                "SELECT state, stability FROM kana_cards WHERE script = ?", (script,)
            ).fetchall()
            counts = {"learning": 0, "known": 0, "mastered": 0}
            for r in rows:
                counts[srs.status(r["state"], r["stability"])] += 1
            total = sum(len(g["items"]) for g in kana.groups(script))
            per_script[script] = {**counts, "unlocked": len(rows), "total": total}

        due_count = conn.execute(
            "SELECT COUNT(*) FROM kana_cards WHERE due_ts <= ?", (now,)
        ).fetchone()[0]
        next_due = conn.execute(
            "SELECT MIN(due_ts) FROM kana_cards WHERE due_ts > ?", (now,)
        ).fetchone()[0]
        reviews_today, correct_today = conn.execute(
            "SELECT COUNT(*), COALESCE(SUM(correct), 0) FROM kana_reviews WHERE reviewed_at >= ?",
            (today,),
        ).fetchone()
        review_days = [
            r[0] for r in conn.execute(
                """SELECT DISTINCT date(reviewed_at, 'unixepoch', 'localtime') AS d
                   FROM kana_reviews ORDER BY d DESC"""
            ).fetchall()
        ]

    return {
        "scripts": per_script,
        "due_count": due_count,
        "next_due": next_due,
        "reviews_today": reviews_today,
        "accuracy_today": round(correct_today / reviews_today, 3) if reviews_today else None,
        "streak_days": _streak(review_days),
    }


def _streak(days_desc: list[str]) -> int:
    """Consecutive days with at least one review, ending today or yesterday."""
    if not days_desc:
        return 0
    seen = {date.fromisoformat(d) for d in days_desc}
    day = date.today()
    if day not in seen:
        day -= timedelta(days=1)
    streak = 0
    while day in seen:
        streak += 1
        day -= timedelta(days=1)
    return streak
