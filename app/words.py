"""JLPT vocabulary lists (N5-N1) and example sentences for their words.

The lists are Jonathan Waller's JLPT word lists (tanos.co.uk, CC BY), cleaned
up from the open-anki-jlpt-decks project (MIT) into app/jlpt_words.tsv: one
word per line with its level, reading, meaning, a usage note, and the matching
JMdict entry. The JLPT has published no official word list since 2010, so these
are "closest to" lists, like the kanji lists.

Example sentences come from the hand-written lessons and listening scripts,
which have English translations, then from the reading passages (Japanese only:
their translations are per paragraph).

    python -m app.words      # check the list and show how many words have examples
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from . import dictionary, furigana, lessons, listening, reading

SOURCE = Path(__file__).with_name("jlpt_words.tsv")
LEVELS = ("N5", "N4", "N3", "N2", "N1")
_LESSON_ORDER = {les["id"]: i for i, les in enumerate(lessons.LESSONS)}


def _to_hiragana(text: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


@lru_cache(maxsize=1)
def all_words() -> list[dict]:
    """Every word in study order: by level, then words the lessons teach (in
    lesson order), then the most common first (JMdict's newspaper frequency)."""
    words = []
    for n, line in enumerate(SOURCE.read_text(encoding="utf-8").splitlines()):
        if not line or line.startswith("#"):
            continue
        level, word, reading, meaning, note, entry_id, priority = line.split("\t")
        words.append({"level": level, "word": word, "reading": reading, "meaning": meaning, "note": note,
                      "entry_id": int(entry_id) if entry_id else None, "priority": int(priority), "n": n})
    taught = _lesson_words()
    for w in words:
        # List words are dictionary forms already: look them up as they are, since the
        # analyzer would read 来る (きたる, "coming") as くる and 行き as 行く.
        w["lesson"] = taught.get((w["word"].strip("～"), _to_hiragana(w["reading"].strip("～"))))
        w["id"] = f"{w['level']}-{w['n']}"
    words.sort(key=lambda w: (LEVELS.index(w["level"]), _LESSON_ORDER.get(w["lesson"], 999), w["priority"], w["n"]))
    return words


def by_level(level: str) -> list[dict]:
    return [w for w in all_words() if w["level"] == level]


@lru_cache(maxsize=1)
def _by_id() -> dict[str, dict]:
    return {w["id"]: w for w in all_words()}


def get(word_id: str) -> dict | None:
    return _by_id().get(word_id)


@lru_cache(maxsize=1)
def _by_key() -> dict[tuple[str, str], dict]:
    index: dict[tuple[str, str], dict] = {}
    for w in all_words():
        word, reading = w["word"].strip("～"), _to_hiragana(w["reading"].strip("～"))
        index.setdefault((word, reading), w)
        # ゆっくりと is also ゆっくり.
        if len(word) > 2 and word[-1] == "と" and reading.endswith("と"):
            index.setdefault((word[:-1], reading[:-1]), w)
    return index


@lru_cache(maxsize=1)
def _by_entry() -> dict[int, dict]:
    index: dict[int, dict] = {}
    for w in all_words():
        if w["entry_id"]:
            index.setdefault(w["entry_id"], w)
    return index


@lru_cache(maxsize=8192)
def _keys(word: str, reading: str) -> tuple[tuple[str, str], ...]:
    """Ways a saved word can match a list word. Lessons teach polite forms, so
    行きます/いきます also matches 行く/いく, 勉強します matches 勉強, and
    一緒に matches 一緒."""
    word, reading = word.strip("～"), _to_hiragana(reading.strip("～"))
    keys = [(word, reading)]
    # Particles are only dropped after kanji: うえに isn't うえ + に the way 一緒に is 一緒 + に.
    for suffix in ("します", "する", "に", "と", "な"):
        if (word.endswith(suffix) and reading.endswith(suffix) and len(word) > len(suffix)
                and (len(suffix) > 1 or furigana._KANJI.search(word))):
            keys.append((word[: -len(suffix)], reading[: -len(suffix)]))
    tokens = list(furigana._tagger()(word))
    # One verb or adjective plus endings (ます, ている, ない...); not compounds like 降り出す or 考え方.
    if (tokens and tokens[0].feature.pos1 in ("動詞", "形容詞")
            and all(t.feature.pos1 in ("助動詞", "助詞") or getattr(t.feature, "orthBase", "") in ("居る", "いる")
                    for t in tokens[1:])):
        base = getattr(tokens[0].feature, "orthBase", None)
        kana = getattr(tokens[0].feature, "kanaBase", None)
        if base and base != "*" and kana and kana != "*":
            keys.append((base, _to_hiragana(kana)))
            # The analyzer spells some bases in kanji (分かる for わかる); keep the learner's kana too.
            if not furigana._KANJI.search(word):
                keys.append((_to_hiragana(kana), _to_hiragana(kana)))
    return tuple(dict.fromkeys(keys))


def match(word: str, reading: str, entry_id: int | None = None) -> dict | None:
    """The list word a saved word (from a lesson, the tutor chat, ...) stands for."""
    if entry_id and entry_id in _by_entry():
        return _by_entry()[entry_id]
    index = _by_key()
    keys = _keys(word, reading)
    found = next((index[k] for k in keys if k in index), None)
    if found or _grammar_word(word):
        return found
    # Other spellings of the same dictionary word: ほしい is listed as 欲しい, すぐ as 直ぐ.
    return next((_by_entry()[e] for k in keys for e in _entry_ids(*k) if e in _by_entry()), None)


@lru_cache(maxsize=8192)
def _grammar_word(word: str) -> bool:
    """Particles and endings (から, のに, でしょう): the particle から is not 空 (から, "empty")."""
    return all(t.feature.pos1 in ("助詞", "助動詞", "接続詞") for t in furigana._tagger()(word))


@lru_cache(maxsize=8192)
def _entry_ids(word: str, reading: str) -> tuple[int, ...]:
    """The most common dictionary entry spelt `word` and read `reading`. A word
    in kana must be the entry's main reading: the particle から is not 空
    (そら, also read から), and わけ is not 理由."""
    entries = [e for e in dictionary.lookup(word, reading, limit=10)
               if any(_to_hiragana(r) == reading for r in e["readings"])]
    if not furigana._KANJI.search(word):
        entries = [e for e in entries if len(word) > 1 and _to_hiragana(e["readings"][0]) == reading]
    return (entries[0]["id"],) if entries else ()


def level_of_entry(entry_id: int) -> str | None:
    w = _by_entry().get(entry_id)
    return w["level"] if w else None


def _lesson_words() -> dict[tuple[str, str], str]:
    """(word, reading) keys of the lesson vocabulary -> first lesson teaching it."""
    taught: dict[tuple[str, str], str] = {}
    for les in lessons.LESSONS:
        for v in les["vocab"]:
            for k in _keys(v["word"], v["reading"]):
                taught.setdefault(k, les["id"])
    return taught


# ---------- example sentences ----------

_SENTENCE = re.compile(r"[^。！？\n]+[。！？]?")


@lru_cache(maxsize=1)
def _sentences() -> list[dict]:
    """Sentences from the lessons, listening scripts and reading passages, with
    their words as (spelling, reading) pairs, dictionary forms included (so
    行きました is found under 行く/いく), and the whole sentence's reading."""
    found = []
    for les in lessons.LESSONS:
        for e in les["examples"]:
            found.append({"jp": e["jp"], "en": e["en"], "source": f"{lessons.label(les)}: {les['title']}",
                          "href": f"#lessons/{les['id']}", "level": lessons.level(les)})
    for item in listening.ITEMS:
        for _role, jp, en in item["lines"]:
            found.append({"jp": jp, "en": en, "source": f"Listening: {item['title']}",
                          "href": f"#listening/{item['id']}", "level": listening.level(item)})
    for p in reading.PASSAGES:
        for para in p["text"]:
            for jp in _SENTENCE.findall(para):
                # Whole sentences only: not headings, list items or long legal-style lines.
                if 3 < len(jp) <= 60 and jp[-1] in "。！？" and not re.search(r"[◆・]", jp):
                    found.append({"jp": jp, "en": None, "source": f"Reading: {p['title']}",
                                  "href": f"#reading/{p['id']}", "level": reading.level(p)})
    tagger = furigana._tagger()
    for s in found:
        pairs, tokens = set(), []
        for t in tagger(s["jp"]):
            said = furigana._reading(t) or _to_hiragana(t.surface)
            base, base_reading = furigana._base(t)
            tokens.append((t.surface, said))
            # Dictionary forms only: the まとめ in まとめて is the verb まとめる, not the noun.
            pairs.add((base, base_reading))
            # Kana spellings only of words written in kana: 今晩は must not count as こんばんは.
            if base_reading and not furigana._KANJI.search(t.surface):
                pairs.add((base_reading, base_reading))
        s["pairs"] = pairs
        s["tokens"] = tokens
        s["kana"] = "".join(said for _surface, said in tokens)
    return found


_PLAIN = re.compile(r"[～\s]")
_BARE = re.compile(r"[\s。、！？!?…]")


def examples(w: dict, limit: int = 3) -> list[dict]:
    """Up to `limit` (at most 3) sentences using the word: translated ones first,
    then the closest level, then the shortest."""
    return [dict(e) for e in _examples(w["id"])[:limit]]


@lru_cache(maxsize=16384)
def _examples(word_id: str) -> tuple[dict, ...]:
    w = get(word_id)
    word, reading = _PLAIN.sub("", w["word"]), _to_hiragana(_PLAIN.sub("", w["reading"]))
    if not word:
        return ()
    kana_only = not furigana._KANJI.search(word)
    # Also inside a longer word (図書 in 図書館) when the readings agree. Not for
    # affixes (～人 is its own word in 日本人, and 人口 is not ～人) or words in kana
    # (the まとめ in まとめて is the verb まとめる).
    inside = w["word"] == word and not kana_only and len(word) > 1

    def uses(s: dict) -> bool:
        if (word, reading) in s["pairs"]:
            return True
        if not inside or word not in s["jp"]:
            return False
        return (any(word in surface and reading in said for surface, said in s["tokens"])
                or reading in s["kana"])  # split over several tokens

    # Not a sentence that is only the word itself (こんにちは。).
    hits = [s for s in _sentences() if uses(s) and _BARE.sub("", s["jp"]) != word]
    hits.sort(key=lambda s: (s["en"] is None, abs(LEVELS.index(s["level"]) - LEVELS.index(w["level"])), len(s["jp"])))
    return tuple({k: s[k] for k in ("jp", "en", "source", "href")} for s in hits[:3])


def _check() -> None:
    words = all_words()
    problems = []
    seen = set()
    for w in words:
        if w["level"] not in LEVELS:
            problems.append(f"{w['word']}: unknown level {w['level']}")
        if not w["word"] or not w["reading"] or not w["meaning"]:
            problems.append(f"{w['id']}: empty field")
        if (w["word"], w["reading"]) in seen:
            problems.append(f"{w['word']} ({w['reading']}): listed twice")
        seen.add((w["word"], w["reading"]))
    for lvl in LEVELS:
        members = by_level(lvl)
        with_examples = sum(1 for w in members if examples(w, 1))
        taught = sum(1 for w in members if w["lesson"])
        print(f"{lvl}: {len(members)} words, {taught} taught in lessons, {with_examples} with example sentences")
    print(f"{len(words)} words, {len(problems)} problems")
    for p in problems:
        print("  " + p)


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    _check()
