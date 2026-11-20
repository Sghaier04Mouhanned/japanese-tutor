"""Readings for kanji come from a morphological analyzer (MeCab + UniDic via
fugashi), never from the language model, which can confidently get them wrong.

`annotate(text)` returns segments the UI renders as plain text or <ruby>:
    [{"t": "私"}, ...]  ->  [{"t": "私", "r": "わたし"}, {"t": "は"}, ...]
"""

from __future__ import annotations

import re
from functools import lru_cache

_KANJI = re.compile(r"[㐀-䶿一-鿿豈-﫿々〆ヵヶ]")


@lru_cache(maxsize=1)
def _tagger():
    from fugashi import Tagger  # imported lazily: loading the dictionary takes a moment

    return Tagger()


def _to_hiragana(text: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def _is_kana(c: str) -> bool:
    return "ぁ" <= c <= "ゖ" or "ァ" <= c <= "ヺ" or c == "ー"


def _split_okurigana(surface: str, reading: str) -> list[dict]:
    """Put readings only over the kanji: 飲み物/のみもの -> 飲(の)み物(もの).

    The surface is cut into kanji runs and kana runs; kana runs must appear
    literally in the reading, kanji runs soak up whatever lies between them.
    """
    runs = re.findall(r"[ぁ-ゖァ-ヺー]+|[^ぁ-ゖァ-ヺー]+", surface)
    pattern = "".join(
        re.escape(_to_hiragana(run)) if _is_kana(run[0]) else "(.+?)" for run in runs
    )
    match = re.fullmatch(pattern, reading)
    if not match:
        return [{"t": surface, "r": reading}]

    readings = iter(match.groups())
    return [{"t": run} if _is_kana(run[0]) else {"t": run, "r": next(readings)} for run in runs]


# UniDic sometimes prefers a formal or literary reading. For a learner, show
# the everyday one (私 is わたし in normal speech, not わたくし).
_EVERYDAY_READINGS = {
    "私": "わたし",
    "日本": "にほん",
    "明日": "あした",
    "昨日": "きのう",
    "今日": "きょう",
    "今朝": "けさ",
    "今年": "ことし",
    "一人": "ひとり",
    "二人": "ふたり",
    "上手": "じょうず",
    "下手": "へた",
}


def _reading(word) -> str | None:
    if word.surface in _EVERYDAY_READINGS:
        return _EVERYDAY_READINGS[word.surface]
    kana = getattr(word.feature, "kana", None)
    if not kana or kana == "*":
        return None
    return _to_hiragana(kana)


def annotate(text: str) -> list[dict]:
    segments: list[dict] = []

    def push(seg: dict) -> None:
        # Merge neighbouring plain text so the payload stays small.
        if "r" not in seg and segments and "r" not in segments[-1]:
            segments[-1]["t"] += seg["t"]
        else:
            segments.append(seg)

    lines = text.split("\n")
    for n, line in enumerate(lines):
        if _KANJI.search(line):
            for word in _tagger()(line):
                if word.white_space:
                    push({"t": word.white_space})
                surface = word.surface
                reading = _reading(word) if _KANJI.search(surface) else None
                if reading:
                    for part in _split_okurigana(surface, reading):
                        push(part)
                else:
                    push({"t": surface})
        elif line:
            push({"t": line})
        if n < len(lines) - 1:
            push({"t": "\n"})
    return segments
