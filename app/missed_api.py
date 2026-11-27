"""Reading and listening questions whose latest answer was wrong, from practice or a
mock test, to try again. Answering one right clears it."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import furigana, listening, reading
from .db import connect, record_attempts

router = APIRouter(prefix="/api/missed", tags=["missed"])

_LEVELS = ("N5", "N4", "N3", "N2", "N1")


def _question(kind: str, ref: str, index: int) -> dict | None:
    """What the list shows for a question, or None when the content no longer exists."""
    if kind == "reading":
        p = reading.get(ref)
        if p is None or index >= len(p["questions"]):
            return None
        return {"level": reading.level(p), "title": p["title"], "jp_title": p["jp_title"],
                "label": f"Reading · {p['kind']}", "prompt": p["questions"][index]["q"],
                "number": reading.number(p), "of": len(p["questions"])}
    item = listening.get(ref)
    if item is None:
        return None
    en, jp, _printed = listening.KINDS[item["kind"]]
    # Quick and utterance items have no written question: show the line or the situation.
    prompt = item["question"] or item["intro"] or item["lines"][0][1]
    return {"level": listening.level(item), "title": item["title"], "jp_title": jp,
            "label": f"Listening · {en}", "prompt": prompt, "number": listening.number(item), "of": 1}


def missed(conn) -> tuple[list[dict], int]:
    """Questions whose latest answer is wrong, in study order, and how many once-missed
    questions have since been answered right."""
    latest: dict[tuple, dict] = {}
    for r in conn.execute("SELECT kind, ref, question, correct, source, created_at FROM question_attempts "
                          "ORDER BY created_at, id"):
        e = latest.setdefault((r["kind"], r["ref"], r["question"]), {"wrong": 0})
        e["correct"] = bool(r["correct"])
        if not r["correct"]:
            e.update(wrong=e["wrong"] + 1, source=r["source"], missed_at=r["created_at"])
    out, cleared = [], 0
    for (kind, ref, index), e in latest.items():
        if not e["wrong"]:
            continue
        if e["correct"]:
            cleared += 1
            continue
        info = _question(kind, ref, index)
        if info:
            out.append({"kind": kind, "ref": ref, "question": index, "times_wrong": e["wrong"],
                        "source": e["source"], "missed_at": e["missed_at"], **info})
    out.sort(key=lambda q: (_LEVELS.index(q["level"]), q["kind"] != "reading", q["number"], q["question"]))
    return out, cleared


@router.get("")
def list_missed():
    with connect() as conn:
        questions, cleared = missed(conn)
    return {"questions": questions, "cleared": cleared}


class Answer(BaseModel):
    answer: int = Field(ge=0, le=9)


@router.post("/reading/{passage_id}/{index}")
def answer_reading(passage_id: str, index: int, body: Answer):
    """Check one question of a passage. Same shape as /api/reading/{id}/answers."""
    p = reading.get(passage_id)
    if p is None or not 0 <= index < len(p["questions"]):
        raise HTTPException(404, "question not found")
    q = p["questions"][index]
    ok = body.answer == q["answer"]
    with connect() as conn:
        record_attempts(conn, "reading", "retry", [(passage_id, index, ok)])
        saved = {(r["word"], r["reading"]) for r in conn.execute("SELECT word, reading FROM vocab")}
    return {
        "results": [{"chosen": body.answer, "answer": q["answer"], "correct": ok, "why": q["why"]}],
        "correct": int(ok), "total": 1,
        "translation": p["en"],
        "vocab": [{**v, "segments": furigana.annotate(v["word"]), "saved": (v["word"], v["reading"]) in saved}
                  for v in p["vocab"]],
    }
