"""Today's study plan for the home page: a short checklist built from where the learner
is (due reviews, kana, the next lesson, new words, one passage and one listening item
at their level, missed questions). Steps tick themselves off from what was done today."""

import json
import math
import time
from datetime import date, datetime, timedelta

from fastapi import APIRouter

from . import kana, lessons, listening, reading
from .db import connect, get_setting, set_setting
from .missed_api import missed

router = APIRouter(prefix="/api/plan", tags=["plan"])

NEW_WORDS = 10     # new words a day
RETRIES = 5        # missed questions to retry a day
REVIEW_SECONDS = 10


def _start_of_today() -> float:
    now = datetime.now().astimezone()
    return now.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()


def _level(done_ids: set[str]) -> tuple[str, dict | None]:
    """The learner's level is the level of the next lesson they haven't finished."""
    nxt = next((les for les in lessons.LESSONS if les["id"] not in done_ids), None)
    return (lessons.level(nxt) if nxt else lessons.LEVELS[-1]), nxt


def _pick(pool: list[dict], last_seen: dict[str, float]) -> dict | None:
    """The first item never practised, otherwise the one practised longest ago."""
    fresh = [x for x in pool if x["id"] not in last_seen]
    if fresh:
        return fresh[0]
    return min(pool, key=lambda x: last_seen[x["id"]], default=None)


def _streak(days: set[str]) -> int:
    """Days in a row with the whole plan done, ending today or yesterday."""
    day = date.today()
    if day.isoformat() not in days:
        day -= timedelta(days=1)
    n = 0
    while day.isoformat() in days:
        n += 1
        day -= timedelta(days=1)
    return n


def plan(conn) -> dict:
    now, today = time.time(), _start_of_today()
    steps = []

    # 1. Reviews: everything in the Review tab.
    due, cards, reviewed = conn.execute(
        """SELECT (SELECT COUNT(*) FROM kana_cards WHERE due_ts <= :now)
                + (SELECT COUNT(*) FROM deck_cards WHERE due_ts <= :now)
                + (SELECT COUNT(*) FROM kanji_cards WHERE due_ts <= :now),
                  (SELECT COUNT(*) FROM kana_cards) + (SELECT COUNT(*) FROM deck_cards)
                + (SELECT COUNT(*) FROM kanji_cards),
                  (SELECT COUNT(*) FROM kana_reviews WHERE reviewed_at >= :today)
                + (SELECT COUNT(*) FROM deck_reviews WHERE reviewed_at >= :today)
                + (SELECT COUNT(*) FROM kanji_reviews WHERE reviewed_at >= :today)""",
        {"now": now, "today": today}).fetchone()
    if cards:
        steps.append({
            "id": "reviews", "title": f"Review {due} card{'s' * (due != 1)}" if due else "Reviews",
            "detail": ("Kana, words, kanji and corrections that are due" if due
                       else f"All caught up · {reviewed} reviewed today" if reviewed else "Nothing due right now"),
            "href": "#review", "done": due == 0,
            "minutes": max(1, math.ceil(due * REVIEW_SECONDS / 60)) if due else 0})

    # 2. Kana: the next set, hiragana first.
    learned_today = conn.execute("SELECT COUNT(*) FROM kana_cards WHERE created_at >= ?", (today,)).fetchone()[0]
    unlocked = {(r[0], r[1]) for r in conn.execute("SELECT DISTINCT script, group_id FROM kana_cards")}
    kana_left = None
    for script in kana.SCRIPTS:
        nxt = next((g for g in kana.groups(script) if (script, g["id"]) not in unlocked), None)
        if nxt:
            kana_left = (script, nxt)
            break
    hiragana_done = kana_left is None or kana_left[0] != "hiragana"
    if kana_left or learned_today:
        script, group = kana_left or (None, None)
        steps.append({
            "id": "kana", "title": "Learn a new kana set",
            "detail": (f"{learned_today} new kana today" if learned_today
                       else f"{script.capitalize()}: {group['label']}"),
            "href": "#learn", "script": script, "done": learned_today > 0, "minutes": 5})

    # 3. The next lesson.
    progress = {r["lesson_id"]: (r["status"], r["updated_at"])
                for r in conn.execute("SELECT lesson_id, status, updated_at FROM lesson_progress")}
    done_ids = {i for i, (s, _) in progress.items() if s == "done"}
    level, next_lesson = _level(done_ids)
    finished_today = [lessons.get(i) for i, (s, t) in progress.items() if s == "done" and t >= today]
    finished_today = [les for les in finished_today if les]
    if finished_today:
        les = max(finished_today, key=lambda x: progress[x["id"]][1])
        steps.append({"id": "lesson", "title": f"Lesson: {les['title']}",
                      "detail": f"{lessons.level(les)} · Lesson {lessons.number(les)} finished today",
                      "href": f"#lessons/{les['id']}", "done": True, "minutes": 15})
    elif next_lesson:
        started = progress.get(next_lesson["id"], ("new",))[0] == "started"
        steps.append({"id": "lesson", "title": f"Lesson: {next_lesson['title']}",
                      "detail": f"{level} · Lesson {lessons.number(next_lesson)}" + (" · started" if started else ""),
                      "href": f"#lessons/{next_lesson['id']}", "done": False, "minutes": 15})

    # Words, reading and listening need hiragana first: from the kana trainer, or shown
    # by a finished lesson.
    if hiragana_done or done_ids:
        # 4. New words: anything saved today counts (word lists, lessons, passages).
        new_words = conn.execute("SELECT COUNT(*) FROM vocab WHERE created_at >= ?", (today,)).fetchone()[0]
        steps.append({"id": "words", "title": f"Add {NEW_WORDS} new {level} words",
                      "detail": f"{min(new_words, NEW_WORDS)} / {NEW_WORDS} added today",
                      "href": "#words", "level": level, "done": new_words >= NEW_WORDS, "minutes": 5})

        # 5–6. One passage and one listening item at the level; practice and mock tests both count.
        attempted = {r[0] for r in conn.execute(
            "SELECT DISTINCT kind FROM question_attempts WHERE created_at >= ? AND source != 'retry'", (today,))}
        read_at = {r[0]: r[1] for r in conn.execute(
            "SELECT passage_id, MAX(created_at) FROM reading_results GROUP BY passage_id")}
        p = _pick([x for x in reading.PASSAGES if reading.level(x) == level], read_at)
        if p:
            steps.append({"id": "reading", "title": f"Read: {p['title']}",
                          "detail": f"{level} · {p['kind']}" + (" · read again" if p["id"] in read_at else ""),
                          "jp": p["jp_title"], "href": f"#reading/{p['id']}",
                          "done": "reading" in attempted, "minutes": p["minutes"]})
        heard_at = {r[0]: r[1] for r in conn.execute(
            "SELECT item_id, MAX(created_at) FROM listening_results GROUP BY item_id")}
        item = _pick([x for x in listening.ITEMS if listening.level(x) == level], heard_at)
        if item:
            en = listening.KINDS[item["kind"]][0]
            steps.append({"id": "listening", "title": f"Listen: {item['title']}",
                          "detail": f"{level} · {en}" + (" · listen again" if item["id"] in heard_at else ""),
                          "href": f"#listening/{item['id']}", "done": "listening" in attempted, "minutes": 3})

    # 7. Missed reading and listening questions.
    questions, _cleared = missed(conn)
    retried = conn.execute(
        "SELECT COUNT(*) FROM question_attempts WHERE source = 'retry' AND created_at >= ?", (today,)).fetchone()[0]
    if questions or retried:
        goal = min(RETRIES, len(questions) + retried)
        steps.append({"id": "missed", "title": f"Retry {goal} missed question{'s' * (goal != 1)}",
                      "detail": f"{min(retried, goal)} / {goal} today · {len(questions)} on the list",
                      "href": "#missed", "done": retried >= goal, "minutes": 0 if retried >= goal else 4})

    complete = bool(steps) and all(s["done"] for s in steps)
    days = set(json.loads(get_setting(conn, "plan_days", "[]")))
    if complete and date.today().isoformat() not in days:
        days.add(date.today().isoformat())
        set_setting(conn, "plan_days", json.dumps(sorted(days)[-400:]))
    return {
        "level": level,
        "steps": steps,
        "complete": complete,
        "minutes_left": sum(s["minutes"] for s in steps if not s["done"]),
        "streak": _streak(days),
        "days_done": len(days),
    }


@router.get("")
def get_plan():
    with connect() as conn:
        return plan(conn)
