"""Deterministic sanity checks on the tutor's replies.

While the learner can't read kana yet, the tutor writes pairs like
わたしは がくせいです (watashi wa gakusei desu). The model occasionally gets
the kana and the romaji out of sync (がいしゃいん next to "kaishain"), which a
beginner can't spot. We convert the kana ourselves and flag disagreements.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from functools import lru_cache

from . import kana

_EXTRA = {
    "ぁ": "a", "ぃ": "i", "ぅ": "u", "ぇ": "e", "ぉ": "o", "ゎ": "wa", "ゔ": "vu",
    "ゃ": "ya", "ゅ": "yu", "ょ": "yo",
    # combinations used for loanwords (mostly written in katakana)
    "てぃ": "ti", "でぃ": "di", "とぅ": "tu", "どぅ": "du",
    "ふぁ": "fa", "ふぃ": "fi", "ふぇ": "fe", "ふぉ": "fo",
    "うぃ": "wi", "うぇ": "we", "うぉ": "wo",
    "しぇ": "she", "ちぇ": "che", "じぇ": "je", "つぁ": "tsa",
    "ゔぁ": "va", "ゔぃ": "vi", "ゔぇ": "ve", "ゔぉ": "vo",
}

_KANA = r"ぁ-ゖァ-ヺー"
# A kana-only phrase (spaces and punctuation allowed inside) followed by (romaji).
_PAIR = re.compile(
    rf"(?<![㐀-鿿々{_KANA}])([{_KANA}][{_KANA}\s、。！？!?]*?)\s*[（(]([A-Za-zāīūēōÂâÔô' \-.,!?]+)[)）]"
)


@lru_cache(maxsize=1)
def _table() -> dict[str, str]:
    table = {i["kana"]: i["romaji"] for g in kana.groups("hiragana") for i in g["items"]}
    table.update(_EXTRA)
    return table


def kana_to_romaji(text: str) -> str | None:
    """Hepburn romaji for a kana string, or None if it holds anything else."""
    table = _table()
    hira = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" or c == "ヴ" else c for c in text)
    out: list[str] = []
    double_next = False
    i = 0
    while i < len(hira):
        c = hira[i]
        if c in " 　、。！？!?":
            i += 1
            continue
        if c == "っ":
            double_next = True
            i += 1
            continue
        if c == "ー":
            vowel = next((ch for ch in reversed("".join(out)) if ch in "aeiou"), "")
            out.append(vowel)
            i += 1
            continue
        syllable = table.get(hira[i:i + 2]) if i + 1 < len(hira) else None
        step = 2
        if syllable is None:
            syllable, step = table.get(c), 1
        if syllable is None:
            return None
        if double_next:
            syllable = syllable[0] + syllable
            double_next = False
        out.append(syllable)
        i += step
    return "".join(out)


def _canonical(romaji: str) -> str:
    """Erase spelling differences that don't change the word (ou/ō/oo, shi/si, wa/ha…)."""
    s = romaji.lower()
    for macron, plain in {"ā": "aa", "ī": "ii", "ū": "uu", "ē": "ee", "ō": "ou", "â": "aa", "ô": "ou"}.items():
        s = s.replace(macron, plain)
    s = re.sub(r"[^a-z]", "", s)
    s = re.sub(r"m(?=[bpm])", "n", s)          # shimbun -> shinbun
    s = s.replace("tch", "cch")                 # matcha / maccha
    for a, b in (("shi", "si"), ("sh", "sy"), ("chi", "ti"), ("ch", "ty"),
                 ("tsu", "tu"), ("fu", "hu"), ("ji", "zi"), ("j", "zy")):
        s = s.replace(a, b)
    s = s.replace("ou", "o").replace("ei", "e")
    s = re.sub(r"([aeiou])\1+", r"\1", s)       # long vowels
    # particles: は is "wa", へ is "e", を is "o"
    s = s.replace("wa", "ha").replace("he", "e").replace("wo", "o")
    return s


def _spaced_like(expected: str, written: str) -> str:
    """Copy the word breaks of `written` onto `expected` so the two line up:
    ("watashihagaishaindesu", "watashi wa kaishain desu") -> "watashi wa gaishain desu"."""
    words = written.lower().split()
    flat = "".join(words)
    breaks, pos = [], 0
    for w in words[:-1]:
        pos += len(w)
        breaks.append(pos)

    ops = SequenceMatcher(None, flat, expected, autojunk=False).get_opcodes()
    cuts = set()
    for p in breaks:
        for _tag, i1, i2, j1, j2 in ops:
            if i1 <= p < i2 or (p == i2 and i1 == i2):
                cuts.add(j1 + min(p - i1, j2 - j1))
                break
    spaced = "".join((" " if n in cuts else "") + ch for n, ch in enumerate(expected)).split()

    # Show particles the way they're pronounced: は "wa", へ "e", を "o".
    if len(spaced) == len(words):
        spaced = [w if (s, w) in {("ha", "wa"), ("he", "e"), ("wo", "o")} else s
                  for s, w in zip(spaced, words, strict=True)]
    return " ".join(spaced)


def romaji_mismatches(text: str) -> list[dict]:
    """[{"kana": "がいしゃいん", "expected": "gaishain", "written": "kaishain"}, ...]"""
    found = []
    for m in _PAIR.finditer(text):
        phrase, written = m.group(1).strip(), m.group(2).strip()
        expected = kana_to_romaji(phrase)
        if not expected:
            continue
        a, b = _canonical(expected), _canonical(written)
        if a == b:
            continue
        # Very different means the brackets hold a translation, not romaji.
        if SequenceMatcher(None, a, b).ratio() < 0.6:
            continue
        found.append({"kana": phrase, "expected": _spaced_like(expected, written), "written": written})
    return found
