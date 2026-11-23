"""Progress dashboard data: activity over time, quiz trends, and the building
blocks of JLPT N5 (kana, lessons, vocabulary, quiz accuracy by section)."""

import json
import time
from datetime import date, timedelta

from fastapi import APIRouter

from . import kana, kanji, lessons, srs
from .db import connect

router = APIRouter(prefix="/api/progress", tags=["progress"])

ACTIVITY_DAYS = 30
# Commonly cited size of the N5 vocabulary; a rough target, not an official list.
N5_VOCAB_TARGET = 800


def _per_day(conn, sql: str, since: float) -> dict[str, int]:
    return {r[0]: r[1] for r in conn.execute(sql, (since,))}


@router.get("")
def progress():
    today = date.today()
    first_day = today - timedelta(days=ACTIVITY_DAYS - 1)
    since = time.mktime(first_day.timetuple())

    with connect() as conn:
        kana_days = _per_day(conn, """SELECT date(reviewed_at, 'unixepoch', 'localtime') d, COUNT(*)
                                      FROM kana_reviews WHERE reviewed_at >= ? GROUP BY d""", since)
        # Words, mistakes and kanji share the chart's second series.
        deck_days = _per_day(conn, """SELECT date(reviewed_at, 'unixepoch', 'localtime') d, COUNT(*) FROM (
                                          SELECT reviewed_at FROM deck_reviews UNION ALL
                                          SELECT reviewed_at FROM kanji_reviews)
                                      WHERE reviewed_at >= ? GROUP BY d""", since)
        quiz_days = _per_day(conn, """SELECT date(created_at, 'unixepoch', 'localtime') d, SUM(total)
                                      FROM quiz_sessions WHERE created_at >= ? GROUP BY d""", since)

        sessions = [dict(r) for r in conn.execute(
            "SELECT created_at, total, correct, by_type FROM quiz_sessions ORDER BY created_at DESC LIMIT 20")]

        kana_rows = conn.execute("SELECT script, state, stability FROM kana_cards").fetchall()
        vocab_rows = conn.execute(
            """SELECT c.state, c.stability FROM vocab v
               LEFT JOIN deck_cards c ON c.kind = 'vocab' AND c.ref_id = v.id""").fetchall()
        mistake_rows = conn.execute(
            """SELECT c.state, c.stability FROM mistakes m
               LEFT JOIN deck_cards c ON c.kind = 'mistake' AND c.ref_id = m.id""").fetchall()
        done_ids = {r[0] for r in conn.execute("SELECT lesson_id FROM lesson_progress WHERE status = 'done'")}
        kanji_rows = conn.execute("SELECT kanji, state, stability FROM kanji_cards").fetchall()

        all_days = {r[0] for r in conn.execute(
            """SELECT date(t, 'unixepoch', 'localtime') FROM (
                   SELECT reviewed_at t FROM kana_reviews UNION ALL
                   SELECT reviewed_at FROM deck_reviews UNION ALL
                   SELECT reviewed_at FROM kanji_reviews UNION ALL
                   SELECT created_at FROM quiz_sessions)""")}
        total_reviews = conn.execute(
            """SELECT (SELECT COUNT(*) FROM kana_reviews) + (SELECT COUNT(*) FROM deck_reviews)
                    + (SELECT COUNT(*) FROM kanji_reviews)""").fetchone()[0]
        total_quizzes = conn.execute("SELECT COUNT(*) FROM quiz_sessions").fetchone()[0]

    activity = []
    for n in range(ACTIVITY_DAYS):
        d = (first_day + timedelta(days=n)).isoformat()
        activity.append({"date": d, "kana": kana_days.get(d, 0), "deck": deck_days.get(d, 0),
                         "quiz": quiz_days.get(d, 0)})

    # Quiz accuracy per section over the last 10 quizzes.
    by_type: dict[str, list[int]] = {}
    for s in sessions[:10]:
        for qtype, (right, total) in json.loads(s["by_type"]).items():
            agg = by_type.setdefault(qtype, [0, 0])
            agg[0] += right
            agg[1] += total

    def counts(rows) -> dict:
        out = {"learning": 0, "known": 0, "mastered": 0}
        for r in rows:
            if r["state"] is not None:
                out[srs.status(r["state"], r["stability"])] += 1
        return out

    kana_total = sum(len(g["items"]) for g in kana.groups("hiragana"))
    scripts = {s: counts([r for r in kana_rows if r["script"] == s]) | {"total": kana_total} for s in kana.SCRIPTS}
    vocab = counts(vocab_rows) | {"saved": len(vocab_rows), "target": N5_VOCAB_TARGET}
    mistakes = counts(mistake_rows) | {"total": len(mistake_rows)}

    # Kanji per JLPT list (only when the kanji data is installed).
    kanji_progress = {}
    if kanji.available():
        index = kanji.all_kanji()
        for lvl in ("N5", "N4", "N3"):
            members = {k for k, e in index.items() if e["group"] == lvl}
            kanji_progress[lvl] = counts([r for r in kanji_rows if r["kanji"] in members]) | {"total": len(members)}

    return {
        "activity": activity,
        "quiz_history": [{"date": s["created_at"], "correct": s["correct"], "total": s["total"]}
                         for s in reversed(sessions)],
        "quiz_by_type": {t: {"correct": c, "total": n} for t, (c, n) in by_type.items()},
        "kana": scripts,
        # Per level, so the N5 building blocks only count N5 lessons.
        "lessons": {lvl: {"done": sum(1 for les in lessons.LESSONS if lessons.level(les) == lvl and les["id"] in done_ids),
                          "total": sum(1 for les in lessons.LESSONS if lessons.level(les) == lvl)}
                    for lvl in lessons.LEVELS},
        "vocab": vocab,
        "mistakes": mistakes,
        "kanji": kanji_progress,
        "totals": {"study_days": len(all_days), "reviews": total_reviews, "quizzes": total_quizzes},
    }
