import time

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from . import furigana, kanji, reading
from .db import connect
from .lessons_api import add_words

router = APIRouter(prefix="/api/reading", tags=["reading"])


def _passage_or_404(passage_id: str) -> dict:
    passage = reading.get(passage_id)
    if passage is None:
        raise HTTPException(404, "passage not found")
    return passage


def _annotate(text: str) -> list[dict]:
    """Furigana segments, with words holding a kanji beyond the study lists marked
    "rare": like the JLPT, the page keeps their readings when furigana is off."""
    known = kanji.all_kanji() if kanji.available() else None
    segments = furigana.annotate(text)
    if known is not None:
        for seg in segments:
            if any(p.get("r") and any(furigana._KANJI.match(c) and c not in known for c in p["t"])
                   for p in seg.get("parts", [])):
                seg["rare"] = True
    return segments


def _results(conn) -> dict[str, dict]:
    """Best and latest score per passage."""
    out: dict[str, dict] = {}
    for r in conn.execute("SELECT passage_id, correct, total FROM reading_results ORDER BY created_at"):
        best = out.get(r["passage_id"], {}).get("best", -1)
        out[r["passage_id"]] = {"last": r["correct"], "total": r["total"], "best": max(best, r["correct"])}
    return out


@router.get("")
def list_passages():
    with connect() as conn:
        results = _results(conn)
    return {"passages": [
        {"id": p["id"], "title": p["title"], "jp_title": p["jp_title"], "kind": p["kind"],
         "minutes": p["minutes"], "questions": len(p["questions"]), "level": reading.level(p),
         "number": reading.number(p), "result": results.get(p["id"])}
        for p in reading.PASSAGES
    ]}


@router.get("/{passage_id}")
def get_passage(passage_id: str):
    """The passage and its questions, without the answers (those come back when
    the answers are sent)."""
    p = _passage_or_404(passage_id)
    index = reading.PASSAGES.index(p)
    return {
        "id": p["id"], "title": p["title"], "jp_title": p["jp_title"], "kind": p["kind"],
        "minutes": p["minutes"], "level": reading.level(p), "number": reading.number(p),
        "text": [{"jp": t, "segments": _annotate(t)} for t in p["text"]],
        "questions": [{"segments": _annotate(q["q"]), "choices": [_annotate(c) for c in q["choices"]]}
                      for q in p["questions"]],
        "next_id": reading.PASSAGES[index + 1]["id"] if index + 1 < len(reading.PASSAGES) else None,
    }


class Answers(BaseModel):
    answers: list[int] = Field(max_length=20)
    elapsed_ms: int | None = Field(default=None, ge=0)


@router.post("/{passage_id}/answers")
def check_answers(passage_id: str, body: Answers):
    p = _passage_or_404(passage_id)
    if len(body.answers) != len(p["questions"]):
        raise HTTPException(400, f"expected {len(p['questions'])} answers")
    results = [{"chosen": a, "answer": q["answer"], "correct": a == q["answer"], "why": q["why"]}
               for a, q in zip(body.answers, p["questions"])]
    correct = sum(r["correct"] for r in results)
    with connect() as conn:
        conn.execute("""INSERT INTO reading_results (passage_id, correct, total, elapsed_ms, created_at)
                        VALUES (?, ?, ?, ?, ?)""", (passage_id, correct, len(results), body.elapsed_ms, time.time()))
        saved = {(r["word"], r["reading"]) for r in conn.execute("SELECT word, reading FROM vocab")}
    return {
        "results": results, "correct": correct, "total": len(results),
        "translation": p["en"],
        "vocab": [{**v, "segments": furigana.annotate(v["word"]), "saved": (v["word"], v["reading"]) in saved}
                  for v in p["vocab"]],
    }


@router.post("/{passage_id}/words")
def add_passage_words(passage_id: str):
    """Put the passage's key words into the notebook and reviews."""
    p = _passage_or_404(passage_id)
    with connect() as conn:
        added = add_words(conn, p["vocab"], source="reading")
    return {"words_added": added}
