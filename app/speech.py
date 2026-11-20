"""Speech-to-text with a local Whisper model (faster-whisper), plus a simple
"did Whisper understand what you meant to say?" comparison for shadowing.

The model runs on the CPU in int8: GPU mode would need over 1 GB of extra
NVIDIA libraries, and a short sentence takes only a few seconds on the CPU.
"""

from __future__ import annotations

import re
import threading
from difflib import SequenceMatcher
from typing import BinaryIO

from . import furigana
from .config import ROOT

MODEL_SIZE = "small"  # ~480 MB; "base" is smaller but much weaker at Japanese
MODEL_DIR = ROOT / "data" / "models"

_model = None
_lock = threading.Lock()          # one transcription (and one load) at a time
_state = {"downloading": False, "error": None}


def available() -> bool:
    try:
        import faster_whisper  # noqa: F401
    except ImportError:
        return False
    return True


def model_downloaded() -> bool:
    return any(MODEL_DIR.glob(f"**/*faster-whisper-{MODEL_SIZE}*/**/model.bin"))


def status() -> dict:
    return {
        "available": available(),
        "model_ready": _model is not None or model_downloaded(),
        "loaded": _model is not None,
        "downloading": _state["downloading"],
        "error": _state["error"],
        "model": MODEL_SIZE,
    }


def _load():
    global _model
    if _model is None:
        from faster_whisper import WhisperModel

        MODEL_DIR.mkdir(parents=True, exist_ok=True)
        _model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8", download_root=str(MODEL_DIR))
    return _model


def prepare_in_background() -> None:
    """Download and load the model without blocking the request."""
    if _model is not None or _state["downloading"] or not available():
        return

    def work():
        _state.update(downloading=True, error=None)
        try:
            with _lock:
                _load()
        except Exception as err:  # noqa: BLE001 - shown in the UI
            _state["error"] = str(err)
        finally:
            _state["downloading"] = False

    threading.Thread(target=work, daemon=True).start()


def _decode(audio: BinaryIO):
    """Any browser recording (webm/ogg/mp4/wav) -> 16 kHz mono float32 samples.

    faster-whisper has its own decoder, but 1.2.1 passes an option PyAV 19 no
    longer accepts, so we decode with PyAV's current API and hand over samples.
    """
    import av
    import numpy as np

    resampler = av.AudioResampler(format="s16", layout="mono", rate=16000)
    chunks = []
    with av.open(audio) as container:
        for frame in container.decode(audio=0):
            for out in resampler.resample(frame):
                chunks.append(out.to_ndarray().reshape(-1))
        for out in resampler.resample(None):  # flush
            chunks.append(out.to_ndarray().reshape(-1))
    if not chunks:
        return np.zeros(0, dtype=np.float32)
    return np.concatenate(chunks).astype(np.float32) / 32768.0


def transcribe(audio: BinaryIO) -> str:
    samples = _decode(audio)
    if samples.size < 1600:  # under 0.1 s: nothing to hear
        return ""
    with _lock:
        model = _load()
        # No initial_prompt on purpose: Whisper sometimes echoes it back when the
        # audio is unclear, which would make a mumbled attempt look perfect.
        segments, _info = model.transcribe(samples, language="ja", beam_size=5, vad_filter=True)
        return "".join(s.text for s in segments).strip()


_DIGITS = "〇一二三四五六七八九"


def _number_to_kanji(n: int) -> str:
    """7 -> 七, 12 -> 十二, 30 -> 三十, 2026 -> 二千二十六 (Whisper likes digits)."""
    if n == 0:
        return "〇"
    out = ""
    for value, unit in ((1000, "千"), (100, "百"), (10, "十")):
        q, n = divmod(n, value)
        if q:
            out += ("" if q == 1 else _DIGITS[q]) + unit
    return out + (_DIGITS[n] if n else "")


def _reading(text: str) -> str:
    """Whole-sentence reading in hiragana, without punctuation or spaces."""
    text = text.translate(str.maketrans("０１２３４５６７８９", "0123456789"))
    text = re.sub(r"\d{1,4}", lambda m: _number_to_kanji(int(m.group())), text)
    out = []
    for seg in furigana.annotate(text):
        out.append("".join(p.get("r", p["t"]) for p in seg["parts"]) if seg.get("parts") else seg["t"])
    hira = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in "".join(out))
    return "".join(c for c in hira if "ぁ" <= c <= "ゖ" or c == "ー")


def compare(target: str, heard: str) -> dict:
    """Compare by sound, not spelling, so 学校 and がっこう count as the same.

    Returns the target's reading split into runs Whisper did / didn't hear,
    and a 0-100 score.
    """
    want, got = _reading(target), _reading(heard)
    matcher = SequenceMatcher(None, want, got, autojunk=False)
    runs = []
    for tag, i1, i2, _j1, _j2 in matcher.get_opcodes():
        if i2 > i1:
            runs.append({"t": want[i1:i2], "ok": tag == "equal"})
    matched = sum(b.size for b in matcher.get_matching_blocks())
    # Divide by the longer reading so extra sounds count too (ました for ます).
    score = round(100 * matched / max(len(want), len(got), 1))
    return {"target_reading": want, "heard_reading": got, "runs": runs, "score": score,
            "perfect": want == got}
