from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import (chat_api, deck_api, furigana, kana_api, kanji_api, lessons_api, listening_api, missed_api, mock_api,
               plan_api, progress_api, quiz_api, reading_api, speech_api, tts, tts_api, words_api)
from .config import STATIC_DIR
from .db import init_db


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    furigana.annotate("日本")  # load the dictionary now, not on the first chat message
    await tts.start()  # VOICEVOX, if installed; it warms up in the background
    yield
    tts.stop()


app = FastAPI(title="Japanese Tutor", lifespan=lifespan)


@app.middleware("http")
async def revalidate_ui_files(request, call_next):
    # Without this, browsers keep running an old app.js after an update.
    response = await call_next(request)
    if request.url.path == "/" or request.url.path.startswith("/static/"):
        response.headers["Cache-Control"] = "no-cache"
    return response


app.include_router(kana_api.router)
app.include_router(chat_api.router)
app.include_router(deck_api.router)
app.include_router(lessons_api.router)
app.include_router(quiz_api.router)
app.include_router(speech_api.router)
app.include_router(progress_api.router)
app.include_router(tts_api.router)
app.include_router(kanji_api.router)
app.include_router(reading_api.router)
app.include_router(listening_api.router)
app.include_router(words_api.router)
app.include_router(mock_api.router)
app.include_router(missed_api.router)
app.include_router(plan_api.router)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")
