"""Timed JLPT mock tests (app/mock.py): start one, submit the answers, see the report."""

import json
import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import listening, mock, reading
from .db import connect, record_attempts
from .listening_api import public_item, review_item, voices
from .reading_api import _annotate

router = APIRouter(prefix="/api/mock", tags=["mock"])


def _level_or_404(level: str) -> str:
    if level not in mock.LEVELS:
        raise HTTPException(404, f"level must be one of {list(mock.LEVELS)}")
    return level


def _seen(conn, level: str) -> dict[str, int]:
    """What earlier tests of this level used, abandoned ones too (their content was seen)."""
    rows = conn.execute("SELECT data FROM mock_tests WHERE level = ?", (level,))
    return mock.seen_in([json.loads(r["data"]) for r in rows])


def _practised(conn) -> set[str]:
    rows = conn.execute("SELECT passage_id FROM reading_results UNION SELECT item_id FROM listening_results")
    return {r[0] for r in rows}


@router.get("")
def overview():
    with connect() as conn:
        history = [dict(r) for r in conn.execute(
            """SELECT id, level, created_at, finished_at, correct, total, score, passed FROM mock_tests
               WHERE finished_at IS NOT NULL ORDER BY finished_at DESC LIMIT 30""")]
    levels = []
    for level in mock.LEVELS:
        sample = mock.build(level)  # cheap; gives this level's parts and typical timings
        rules = mock.SCORING[level]
        done = [h for h in history if h["level"] == level]
        with connect() as conn:
            seen = _seen(conn, level)
        levels.append({
            "level": level,
            "parts": [{"title": p["title"], "minutes": p["minutes"]} for p in sample["parts"]],
            "questions": {"vocab": len(sample["vocab"]), "grammar": len(sample["grammar"]),
                          "reading": len(sample["reading"]), "listening": len(sample["listening"])},
            "real_minutes": mock.REAL_MINUTES[level],
            "pass_mark": rules["pass"],
            "max": sum(s[2] for s in rules["sections"]),
            "sections": [{"title": t, "max": m, "minimum": mn} for _k, t, m, mn in rules["sections"]],
            "best": max((h["score"] for h in done), default=None),
            "last": done[0] if done else None,
            "fresh_tests": mock.fresh_tests(level, seen),
        })
    return {"levels": levels, "history": history}


def _public(test_id: int, test: dict, voice_map: dict | None) -> dict:
    """The test as the learner sees it: no answers, no explanations."""
    known = mock.known_kanji(test["level"])

    def question(q: dict) -> dict:
        prompt = dict(q["prompt"])
        jp_choices = q["group"] != "meaning"
        if "text" in prompt:
            prompt["segments"] = _annotate(prompt.pop("text"), known)
        return {"id": q["id"], "group": q["group"], "prompt": prompt,
                "choices": [_annotate(c, known) for c in q["choices"]] if q["group"] in ("grammar", "particle")
                else q["choices"], "jp_choices": jp_choices}

    passages = []
    for pid in test["passages"]:
        p = reading.get(pid)
        qids = [r["id"] for r in test["reading"] if r["passage"] == pid]
        passages.append({
            "id": pid, "jp_title": p["jp_title"], "kind": p["kind"],
            "text": [{"jp": t, "segments": _annotate(t, known)} for t in p["text"]],
            "questions": [{"id": qid, "segments": _annotate(q["q"], known), "choices": [_annotate(c, known) for c in q["choices"]]}
                          for qid, q in zip(qids, p["questions"])],
        })
    items = [{"qid": r["id"], **public_item(listening.get(r["item"]))} for r in test["listening"]]
    return {
        "id": test_id, "level": test["level"], "parts": test["parts"],
        "vocab": [question(q) for q in test["vocab"]],
        "grammar": [question(q) for q in test["grammar"]],
        "passages": passages,
        "listening": items, "voices": voice_map,
        "pass_mark": mock.SCORING[test["level"]]["pass"],
    }


@router.post("/{level}/start")
async def start(level: str):
    _level_or_404(level)
    with connect() as conn:
        test = mock.build(level, _seen(conn, level), _practised(conn))
        cur = conn.execute("INSERT INTO mock_tests (level, data, created_at) VALUES (?, ?, ?)",
                           (level, json.dumps(test, ensure_ascii=False), time.time()))
        test_id = cur.lastrowid
    return _public(test_id, test, await voices())


class Submit(BaseModel):
    answers: dict[str, int | None] = Field(default_factory=dict)
    elapsed_ms: dict[str, int] = Field(default_factory=dict)  # time used per part


def _report(test: dict, result: dict) -> dict:
    """The score plus what the review needs: transcripts, spoken choices, translations."""
    return {
        **result,
        "level": test["level"],
        "listening_review": {r["id"]: review_item(listening.get(r["item"])) for r in test["listening"]},
        "translations": {pid: reading.get(pid)["en"] for pid in test["passages"]},
    }


@router.post("/{test_id}/submit")
def submit(test_id: int, body: Submit):
    with connect() as conn:
        row = conn.execute("SELECT data, finished_at FROM mock_tests WHERE id = ?", (test_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "test not found")
        if row["finished_at"] is not None:
            raise HTTPException(409, "this test was already submitted")
        test = json.loads(row["data"])
        valid = set(mock.answer_key(test))
        answers = {k: v for k, v in body.answers.items() if k in valid}
        result = mock.score(test, answers)
        result["elapsed_ms"] = {k: max(0, v) for k, v in body.elapsed_ms.items()}
        conn.execute(
            """UPDATE mock_tests SET finished_at = ?, correct = ?, total = ?, score = ?, passed = ?, result = ?
               WHERE id = ?""",
            (time.time(), result["correct"], result["total"], result["score"], int(result["passed"]),
             json.dumps(result, ensure_ascii=False), test_id))
        # Unanswered questions count as missed: they come back on the mistakes page.
        got = result["questions"]
        record_attempts(conn, "reading", "mock", [(q["passage"], q["index"], got[q["id"]]["correct"]) for q in test["reading"]])
        record_attempts(conn, "listening", "mock", [(q["item"], 0, got[q["id"]]["correct"]) for q in test["listening"]])
    return _report(test, result)


@router.get("/{test_id}")
async def review(test_id: int):
    """A finished test with its report, to look back at the answers."""
    with connect() as conn:
        row = conn.execute("SELECT data, result FROM mock_tests WHERE id = ? AND finished_at IS NOT NULL",
                           (test_id,)).fetchone()
    if row is None:
        raise HTTPException(404, "no finished test with this id")
    test = json.loads(row["data"])
    return {"test": _public(test_id, test, await voices()), "report": _report(test, json.loads(row["result"]))}
