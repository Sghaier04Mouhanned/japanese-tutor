"""Readings for kanji come from a morphological analyzer (MeCab + UniDic via
fugashi), never from the language model, which can confidently get them wrong.

`annotate(text)` splits text into words the UI renders with <ruby> furigana and
makes clickable for dictionary lookups (see the function for the format).
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


_JAPANESE = re.compile(r"[぀-ヿ㐀-䶿一-鿿々]")

_POS = {
    "名詞": "noun", "代名詞": "pronoun", "動詞": "verb", "形容詞": "i-adjective",
    "形状詞": "na-adjective", "副詞": "adverb", "助詞": "particle", "助動詞": "auxiliary",
    "接尾辞": "suffix", "接頭辞": "prefix", "感動詞": "interjection", "連体詞": "pre-noun",
    "接続詞": "conjunction",
}


def _base(word) -> tuple[str, str | None]:
    """Dictionary form and its reading: 飲み -> (飲む, のむ)."""
    base = getattr(word.feature, "orthBase", None) or word.surface
    if base == "*":
        base = word.surface
    if base in _EVERYDAY_READINGS:
        return base, _EVERYDAY_READINGS[base]
    kana = getattr(word.feature, "kanaBase", None)
    return base, (_to_hiragana(kana) if kana and kana != "*" else None)


def annotate(text: str) -> list[dict]:
    """Split text into plain runs and Japanese words.

    Plain:  {"t": "Hello "}
    Word:   {"t": "飲み", "b": "飲む", "k": "のむ", "p": "verb",
             "parts": [{"t": "飲", "r": "の"}, {"t": "み"}]}   # parts only when it has kanji
    """
    segments: list[dict] = []

    def push_plain(text_: str) -> None:
        # Merge neighbouring plain text so the payload stays small.
        if segments and set(segments[-1]) == {"t"}:
            segments[-1]["t"] += text_
        else:
            segments.append({"t": text_})

    lines = text.split("\n")
    for n, line in enumerate(lines):
        if _JAPANESE.search(line):
            for word in _tagger()(line):
                if word.white_space:
                    push_plain(word.white_space)
                surface = word.surface
                pos = _POS.get(word.feature.pos1)
                if not pos or not _JAPANESE.search(surface):
                    push_plain(surface)
                    continue
                base, base_kana = _base(word)
                seg = {"t": surface, "b": base, "k": base_kana, "p": pos}
                reading = _reading(word) if _KANJI.search(surface) else None
                if reading:
                    seg["parts"] = _split_okurigana(surface, reading)
                segments.append(seg)
        elif line:
            push_plain(line)
        if n < len(lines) - 1:
            push_plain("\n")
    return segments
