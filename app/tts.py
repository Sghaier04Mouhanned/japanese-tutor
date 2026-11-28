"""Natural Japanese speech with a local VOICEVOX engine.

The engine is a separate program (data/voicevox/engine, git-ignored) with its
own HTTP API. The app starts it in the background if it's installed and falls
back to the browser's voice otherwise. Generated audio is cached on disk, so
each sentence is synthesized once.

VOICEVOX voices are free to use with credit: "VOICEVOX:<character name>".
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys

import httpx

from .config import ROOT

ENGINE_DIR = ROOT / "data" / "voicevox" / "engine"
CACHE_DIR = ROOT / "data" / "tts_cache"
ENGINE_URL = os.getenv("VOICEVOX_URL", "http://127.0.0.1:50021")
DEFAULT_SPEAKER_NAME = "四国めたん"  # a clear, standard-sounding voice

_process: subprocess.Popen | None = None
_job = None  # Windows job object that ties the engine's lifetime to ours


def _kill_with_us(proc: subprocess.Popen) -> None:
    """On Windows, put the engine in a job object that is closed when this
    process exits, however it exits (Ctrl+C, closed window, crash). Otherwise a
    hard stop of the app would leave a ~1 GB engine running in the background."""
    global _job
    if sys.platform != "win32":
        return
    import ctypes
    from ctypes import wintypes

    class IoCounters(ctypes.Structure):
        _fields_ = [(n, ctypes.c_ulonglong) for n in (
            "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
            "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

    class BasicLimits(ctypes.Structure):
        _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong), ("PerJobUserTimeLimit", ctypes.c_longlong),
                    ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                    ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                    ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                    ("SchedulingClass", wintypes.DWORD)]

    class ExtendedLimits(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", BasicLimits), ("IoInfo", IoCounters),
                    ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                    ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateJobObjectW.restype = wintypes.HANDLE
    kernel32.OpenProcess.restype = wintypes.HANDLE
    job = kernel32.CreateJobObjectW(None, None)
    if not job:
        return
    limits = ExtendedLimits()
    limits.BasicLimitInformation.LimitFlags = 0x2000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    extended_limit_information = 9
    kernel32.SetInformationJobObject(wintypes.HANDLE(job), extended_limit_information,
                                     ctypes.byref(limits), ctypes.sizeof(limits))
    handle = kernel32.OpenProcess(0x0100 | 0x0001, False, proc.pid)  # SET_QUOTA | TERMINATE
    if handle:
        kernel32.AssignProcessToJobObject(wintypes.HANDLE(job), wintypes.HANDLE(handle))
        kernel32.CloseHandle(wintypes.HANDLE(handle))
    _job = job  # keep the handle open for our whole lifetime


def _executable():
    found = sorted(ENGINE_DIR.glob("**/run.exe")) if ENGINE_DIR.exists() else []
    return found[0] if found else None


def installed() -> bool:
    return _executable() is not None


async def running() -> bool:
    try:
        async with httpx.AsyncClient(timeout=2) as client:
            return (await client.get(f"{ENGINE_URL}/version")).status_code == 200
    except httpx.HTTPError:
        return False


async def start() -> None:
    """Launch the engine if it's installed and not already running."""
    global _process
    if _process is not None and _process.poll() is None:
        return
    exe = _executable()
    if exe is None or await running():
        return
    port = ENGINE_URL.rsplit(":", 1)[-1].split("/")[0]
    flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    _process = subprocess.Popen(
        [str(exe), "--host", "127.0.0.1", "--port", port],
        cwd=str(exe.parent), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags,
    )
    _kill_with_us(_process)


def stop() -> None:
    global _process
    if _process is not None and _process.poll() is None:
        _process.terminate()
        try:
            _process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            _process.kill()
    _process = None


async def speakers() -> list[dict]:
    """[{"id": 2, "name": "四国めたん", "style": "ノーマル"}, ...]"""
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(f"{ENGINE_URL}/speakers")
        r.raise_for_status()
    # Speaking styles are typed "talk" or (newer engines) "streaming_talk"; skip singing ones.
    return [{"id": s["id"], "name": sp["name"], "style": s["name"]}
            for sp in r.json() for s in sp["styles"] if "talk" in s.get("type", "talk")]


async def default_speaker() -> int | None:
    voices = await speakers()
    for v in voices:
        if v["name"] == DEFAULT_SPEAKER_NAME and v["style"] == "ノーマル":
            return v["id"]
    return voices[0]["id"] if voices else None


# Spellings the engine misreads, rewritten in kana before synthesis (何ですか is
# なんですか, but the engine says なにですか).
_SAY_FIXES = [("何ですか", "なんですか"), ("何でしょう", "なんでしょう"), ("何だろう", "なんだろう"),
              ("何なのか", "なんなのか"), ("何だと", "なんだと"),
              ("海の幸", "うみのさち"),  # the engine says うみのこう
              ("自由な分", "じゆうなぶん"),  # the engine says じゆうなわけ
              ("同じ味", "おなじあじ"),  # the engine says どうじみ
              ("何と言", "なんと言"), ("何階", "なんがい"),
              ("お手数", "おてすう"),  # the engine says おてかず
              ("果物狩り", "くだものがり"), ("ぶどう狩り", "ぶどうがり"), ("ぶどう畑", "ぶどうばたけ"),  # it drops the rendaku
              ("日本", "にほん")]  # the engine sometimes says にっぽん; the furigana shows にほん


def _for_engine(text: str) -> str:
    for written, said in _SAY_FIXES:
        text = text.replace(written, said)
    return text


async def synthesize(text: str, speaker: int, speed: float = 1.0) -> bytes:
    """WAV audio for `text`, from the cache when possible."""
    text = _for_engine(text)
    key = hashlib.sha256(f"{speaker}|{speed:.2f}|{text}".encode()).hexdigest()
    path = CACHE_DIR / f"{key}.wav"
    if path.exists():
        return path.read_bytes()

    async with httpx.AsyncClient(timeout=60) as client:
        q = await client.post(f"{ENGINE_URL}/audio_query", params={"text": text, "speaker": speaker})
        q.raise_for_status()
        query = q.json()
        query["speedScale"] = speed
        r = await client.post(f"{ENGINE_URL}/synthesis", params={"speaker": speaker}, json=query)
        r.raise_for_status()

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_bytes(r.content)
    return r.content
