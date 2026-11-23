"""Kanji study data from KANJIDIC2 (readings, meanings, stroke counts) and
KanjiVG (stroke order), plus example words from the lessons and JMdict.

KANJIDIC2 and JMdict are © the Electronic Dictionary Research and Development
Group (CC BY-SA 4.0); KanjiVG is © Ulrich Apel (CC BY-SA 3.0). All files live in
data/ (git-ignored). The index is built once into data/dict/kanji.json:

    python -m app.kanji
"""

from __future__ import annotations

import gzip
import json
import re
import sqlite3
import threading
import time
import xml.etree.ElementTree as ET
from functools import lru_cache

from . import dictionary, lessons
from .config import ROOT

SOURCE = ROOT / "data" / "dict" / "kanjidic2.xml.gz"
INDEX = ROOT / "data" / "dict" / "kanji.json"
STROKES_DIR = ROOT / "data" / "kanjivg" / "kanji"

# KANJIDIC only has the pre-2010 four-level JLPT tags. Old level 4 is the closest
# match for today's N5, old level 3 for N4. We say "closest to", not "official".
OLD_JLPT_TO_LEVEL = {4: "N5", 3: "N4"}
GROUPS = ("N5", "N4", "lessons")  # "lessons": in the lessons but on neither list

_KANJI_CHAR = re.compile(r"[一-鿿々]")
_lock = threading.Lock()


def _lesson_kanji() -> dict[str, str]:
    """Kanji used anywhere in the lessons -> id of the first lesson using it."""
    first: dict[str, str] = {}
    for les in lessons.LESSONS:
        texts = [e["jp"] for e in les["examples"]] + [v["word"] for v in les["vocab"]] + les["points"]
        for text in texts:
            for ch in _KANJI_CHAR.findall(text):
                if ch != "々":
                    first.setdefault(ch, les["id"])
    return first


def _kun(reading: str) -> str:
    """KANJIDIC marks okurigana with a dot: まな.ぶ -> まな(ぶ); drops affix dashes."""
    reading = reading.strip("-")
    return re.sub(r"\.(.+)$", r"(\1)", reading)


def build() -> int:
    if not SOURCE.exists():
        raise FileNotFoundError(f"{SOURCE} not found")
    in_lessons = _lesson_kanji()
    entries: dict[str, dict] = {}

    with gzip.open(SOURCE) as f:
        for _event, elem in ET.iterparse(f, events=("end",)):
            if elem.tag != "character":
                continue
            literal = elem.findtext("literal")
            jlpt = elem.findtext("misc/jlpt")
            level = OLD_JLPT_TO_LEVEL.get(int(jlpt)) if jlpt else None
            if level or literal in in_lessons:
                rm = elem.find("reading_meaning/rmgroup")
                on = [r.text for r in rm.findall("reading[@r_type='ja_on']")] if rm is not None else []
                kun = [_kun(r.text) for r in rm.findall("reading[@r_type='ja_kun']")] if rm is not None else []
                # English meanings, minus radical names like "one radical (no.1)".
                meanings = [m.text for m in rm.findall("meaning")
                            if "m_lang" not in m.attrib and "radical (no" not in m.text] if rm is not None else []
                freq = elem.findtext("misc/freq")
                entries[literal] = {
                    "kanji": literal,
                    "group": level or "lessons",
                    "on": on[:4], "kun": list(dict.fromkeys(kun))[:5], "meanings": meanings[:5],
                    "strokes": int(elem.findtext("misc/stroke_count") or 0),
                    "grade": int(elem.findtext("misc/grade") or 0) or None,
                    "freq": int(freq) if freq else None,
                    "lesson": in_lessons.get(literal),
                }
            elem.clear()

    _add_examples(entries)
    INDEX.write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    _load.cache_clear()
    return len(entries)


def _add_examples(entries: dict[str, dict]) -> None:
    """Up to 6 example words per kanji: lesson vocabulary first (hand-checked),
    then common JMdict words, short ones first."""
    for e in entries.values():
        e["examples"] = []
    seen: dict[str, set] = {k: set() for k in entries}
    for les in lessons.LESSONS:
        for v in les["vocab"]:
            for ch in set(v["word"]) & entries.keys():
                if v["word"] not in seen[ch] and len(entries[ch]["examples"]) < 3:
                    entries[ch]["examples"].append({"word": v["word"], "reading": v["reading"],
                                                    "meaning": v["meaning"], "lesson": les["id"]})
                    seen[ch].add(v["word"])

    if not dictionary.INDEX.exists():
        return
    conn = sqlite3.connect(dictionary.INDEX)
    rows = conn.execute(
        """SELECT f.form, e.data, e.priority, e.id FROM forms f JOIN entries e ON e.id = f.entry_id
           WHERE f.kind = 'k' AND e.priority < 99 AND length(f.form) BETWEEN 2 AND 4"""
    ).fetchall()
    conn.close()
    # JMdict ranks by newspaper frequency (日米, 同日 rank high). For learners,
    # first prefer words whose kanji are all on the N5/N4 lists.
    beginner = {k for k, e in entries.items() if e["group"] in ("N5", "N4")}
    rows.sort(key=lambda r: (not set(_KANJI_CHAR.findall(r[0])) <= beginner, r[2], len(r[0])))
    for form, data, _priority, entry_id in rows:
        for ch in set(form) & entries.keys():
            # One example per dictionary entry (見通 and 見通し are the same word).
            if len(entries[ch]["examples"]) >= 6 or form in seen[ch] or entry_id in seen[ch]:
                continue
            entry = json.loads(data)
            entries[ch]["examples"].append({"word": form, "reading": entry["readings"][0],
                                            "meaning": dictionary.short_meaning(entry, senses=1)})
            seen[ch].update({form, entry_id, *entry["kanji"]})


def available() -> bool:
    return INDEX.exists() or SOURCE.exists()


@lru_cache(maxsize=1)
def _load() -> dict[str, dict]:
    with _lock:
        if not INDEX.exists():
            build()
        return json.loads(INDEX.read_text(encoding="utf-8"))


def all_kanji() -> dict[str, dict]:
    return _load()


def get(ch: str) -> dict | None:
    return _load().get(ch)


def strokes(ch: str) -> list[str]:
    """SVG path data for each stroke, in writing order (109×109 canvas)."""
    if len(ch) != 1:
        return []
    path = STROKES_DIR / f"{ord(ch):05x}.svg"
    if not path.exists():
        return []
    svg = path.read_text(encoding="utf-8")
    # Stroke paths carry ids like kvg:05b66-s1; take their d attributes in order.
    found = re.findall(r'<path\s+id="kvg:[0-9a-f]+-s(\d+)"[^>]*?\sd="([^"]+)"', svg)
    return [d for _n, d in sorted(found, key=lambda t: int(t[0]))]


if __name__ == "__main__":
    start = time.time()
    n = build()
    print(f"Indexed {n} kanji into {INDEX} in {time.time() - start:.1f}s")
