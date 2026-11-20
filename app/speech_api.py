import io

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from . import furigana, lessons, speech

router = APIRouter(prefix="/api/speech", tags=["speech"])

MAX_AUDIO_BYTES = 10 * 1024 * 1024  # ~10 minutes of compressed speech; far more than a sentence


@router.get("/status")
def status():
    return speech.status()


@router.post("/prepare")
def prepare():
    speech.prepare_in_background()
    return speech.status()


@router.post("/transcribe")
def transcribe(audio: UploadFile = File(...)):
    if not speech.available():
        raise HTTPException(503, "Speech recognition isn't installed yet.")
    if not speech.status()["model_ready"]:
        speech.prepare_in_background()
        raise HTTPException(503, "The speech model is still downloading. Try again in a few minutes.")
    data = audio.file.read(MAX_AUDIO_BYTES + 1)
    if len(data) > MAX_AUDIO_BYTES:
        raise HTTPException(413, "Recording is too long.")
    if not data:
        raise HTTPException(400, "Empty recording.")
    try:
        text = speech.transcribe(io.BytesIO(data))
    except Exception as err:  # noqa: BLE001 - bad audio, decoder errors
        raise HTTPException(400, f"Couldn't understand the recording: {err}") from err
    return {"text": text, "segments": furigana.annotate(text) if text else []}


class Compare(BaseModel):
    target: str = Field(max_length=300)
    heard: str = Field(max_length=500)


@router.post("/compare")
def compare(body: Compare):
    return speech.compare(body.target, body.heard)


@router.get("/sentences")
def sentences():
    """Shadowing material: every verified lesson example."""
    return {"sentences": [
        {"lesson": les["id"], "lesson_title": les["title"], "jp": e["jp"], "romaji": e["romaji"], "en": e["en"],
         "segments": furigana.annotate(e["jp"])}
        for les in lessons.LESSONS for e in les["examples"]
    ]}
