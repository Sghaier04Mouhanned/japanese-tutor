import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

from . import tts
from .db import connect, get_setting, set_setting

router = APIRouter(prefix="/api/tts", tags=["tts"])


def _settings() -> tuple[int | None, float]:
    with connect() as conn:
        speaker = get_setting(conn, "tts.speaker")
        speed = get_setting(conn, "tts.speed", "1.0")
    return (int(speaker) if speaker else None), float(speed)


@router.get("/status")
async def status():
    speaker, speed = _settings()
    running = await tts.running()
    name = None
    if running:
        try:
            if speaker is None:
                speaker = await tts.default_speaker()
            name = next((f"{v['name']} ({v['style']})" for v in await tts.speakers() if v["id"] == speaker), None)
        except httpx.HTTPError:
            running = False
    return {"installed": tts.installed(), "running": running, "speaker": speaker, "speaker_name": name, "speed": speed}


@router.get("/speakers")
async def speakers():
    try:
        return {"speakers": await tts.speakers()}
    except httpx.HTTPError as err:
        raise HTTPException(503, "The VOICEVOX engine isn't running.") from err


class TTSSettings(BaseModel):
    speaker: int
    speed: float = Field(default=1.0, ge=0.5, le=1.5)


@router.put("/settings")
def save_settings(body: TTSSettings):
    with connect() as conn:
        set_setting(conn, "tts.speaker", str(body.speaker))
        set_setting(conn, "tts.speed", f"{body.speed:.2f}")
    return {"ok": True}


@router.get("")
async def speak(text: str, speaker: int | None = None, speed: float | None = None):
    text = text.strip()
    if not text or len(text) > 300:
        raise HTTPException(400, "text must be 1-300 characters")
    saved_speaker, saved_speed = _settings()
    try:
        speaker = speaker if speaker is not None else saved_speaker
        if speaker is None:
            speaker = await tts.default_speaker()
        audio = await tts.synthesize(text, speaker, speed if speed is not None else saved_speed)
    except httpx.HTTPError as err:
        raise HTTPException(503, "The VOICEVOX engine isn't available.") from err
    return Response(audio, media_type="audio/wav", headers={"Cache-Control": "max-age=86400"})
