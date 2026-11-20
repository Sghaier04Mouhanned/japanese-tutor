"""Kana data: hiragana is defined by hand, katakana is derived from it.

Every katakana character in the ranges used here sits exactly 0x60 code
points after its hiragana counterpart (あ U+3042 -> ア U+30A2), so we only
have to maintain one table.
"""

from __future__ import annotations

SCRIPTS = ("hiragana", "katakana")

# (group_id, label, [(hiragana, romaji), ...]) in the order they should be learned.
_GROUPS: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("a", "Vowels", [("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o")]),
    ("ka", "K row", [("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko")]),
    ("sa", "S row", [("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so")]),
    ("ta", "T row", [("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to")]),
    ("na", "N row", [("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no")]),
    ("ha", "H row", [("は", "ha"), ("ひ", "hi"), ("ふ", "fu"), ("へ", "he"), ("ほ", "ho")]),
    ("ma", "M row", [("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo")]),
    ("ya", "Y row", [("や", "ya"), ("ゆ", "yu"), ("よ", "yo")]),
    ("ra", "R row", [("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro")]),
    ("wa", "W row + N", [("わ", "wa"), ("を", "wo"), ("ん", "n")]),
    ("ga", "G (dakuten)", [("が", "ga"), ("ぎ", "gi"), ("ぐ", "gu"), ("げ", "ge"), ("ご", "go")]),
    ("za", "Z (dakuten)", [("ざ", "za"), ("じ", "ji"), ("ず", "zu"), ("ぜ", "ze"), ("ぞ", "zo")]),
    ("da", "D (dakuten)", [("だ", "da"), ("ぢ", "ji"), ("づ", "zu"), ("で", "de"), ("ど", "do")]),
    ("ba", "B (dakuten)", [("ば", "ba"), ("び", "bi"), ("ぶ", "bu"), ("べ", "be"), ("ぼ", "bo")]),
    ("pa", "P (handakuten)", [("ぱ", "pa"), ("ぴ", "pi"), ("ぷ", "pu"), ("ぺ", "pe"), ("ぽ", "po")]),
    ("y1", "Combos: kya sha cha", [
        ("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"),
        ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"),
        ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"),
    ]),
    ("y2", "Combos: nya hya mya rya", [
        ("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo"),
        ("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo"),
        ("みゃ", "mya"), ("みゅ", "myu"), ("みょ", "myo"),
        ("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo"),
    ]),
    ("y3", "Combos: gya ja bya pya", [
        ("ぎゃ", "gya"), ("ぎゅ", "gyu"), ("ぎょ", "gyo"),
        ("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo"),
        ("びゃ", "bya"), ("びゅ", "byu"), ("びょ", "byo"),
        ("ぴゃ", "pya"), ("ぴゅ", "pyu"), ("ぴょ", "pyo"),
    ]),
]

# Other romanizations people commonly type (Nihon-shiki / IME style).
ALTERNATES: dict[str, set[str]] = {
    "shi": {"si"}, "chi": {"ti"}, "tsu": {"tu"}, "fu": {"hu"},
    "ji": {"zi", "di"}, "zu": {"du"}, "wo": {"o"}, "n": {"nn", "n'"},
    "sha": {"sya"}, "shu": {"syu"}, "sho": {"syo"},
    "cha": {"tya", "cya"}, "chu": {"tyu", "cyu"}, "cho": {"tyo", "cyo"},
    "ja": {"zya", "jya"}, "ju": {"zyu", "jyu"}, "jo": {"zyo", "jyo"},
}

# Short tips shown while learning. Keyed by hiragana; applied to katakana too
# unless the tip only makes sense for one script.
NOTES: dict[str, str] = {
    "を": "Pronounced like お (o). Almost only used as the object particle.",
    "は": "Read 'wa' when used as the topic particle (わたしは…).",
    "へ": "Read 'e' when used as the direction particle (にほんへ…).",
    "ん": "The only kana that is a lone consonant. Never starts a word.",
    "ぢ": "Rare. Sounds the same as じ (ji).",
    "づ": "Rare. Sounds the same as ず (zu).",
    "ふ": "Between 'fu' and 'hu' — blow gently, lips barely touching.",
    "つ": "A small っ/ッ doubles the next consonant (きって = kitte).",
}

_HIRAGANA_ONLY_NOTES = {"は", "へ"}  # particle readings don't apply to katakana


def to_katakana(text: str) -> str:
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in text)


def groups(script: str) -> list[dict]:
    """All groups for a script, in learning order."""
    if script not in SCRIPTS:
        raise ValueError(f"unknown script: {script}")
    out = []
    for group_id, label, items in _GROUPS:
        kana_items = []
        for hira, romaji in items:
            kana = hira if script == "hiragana" else to_katakana(hira)
            note = NOTES.get(hira)
            if script == "katakana" and hira in _HIRAGANA_ONLY_NOTES:
                note = None
            kana_items.append({
                "kana": kana,
                "romaji": romaji,
                "accept": sorted(accepted_answers(romaji)),
                "note": note,
            })
        out.append({"id": group_id, "label": label, "items": kana_items})
    return out


def group_ids() -> list[str]:
    return [g[0] for g in _GROUPS]


def lookup(script: str) -> dict[str, dict]:
    """kana -> item (with group id) for one script."""
    return {
        item["kana"]: {**item, "group": g["id"]}
        for g in groups(script)
        for item in g["items"]
    }


def accepted_answers(romaji: str) -> set[str]:
    return {romaji} | ALTERNATES.get(romaji, set())


def is_correct(romaji: str, answer: str) -> bool:
    return answer.strip().lower() in accepted_answers(romaji)
