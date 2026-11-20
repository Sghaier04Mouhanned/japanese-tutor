"""Japanese-English dictionary lookups backed by JMdict.

JMdict is © the Electronic Dictionary Research and Development Group, used
under CC BY-SA 4.0 (https://www.edrdg.org/edrdg/licence.html). The raw file is
downloaded into data/dict/ (git-ignored) and indexed once into SQLite:

    python -m app.dictionary            # build data/dict/jmdict.db from JMdict_e.gz
"""

from __future__ import annotations

import gzip
import json
import sqlite3
import sys
import time
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

from .config import ROOT

DICT_DIR = ROOT / "data" / "dict"
SOURCE = DICT_DIR / "JMdict_e.gz"
INDEX = DICT_DIR / "jmdict.db"

# Frequency markers JMdict uses for "common" words.
_COMMON = {"news1", "ichi1", "spec1", "spec2", "gai1"}


def _priority(pri_tags: list[str]) -> int:
    """Lower is more common. nfXX ranks words in 500-word bands of newspaper frequency."""
    best = 99
    for tag in pri_tags:
        if tag.startswith("nf"):
            best = min(best, int(tag[2:]))
        elif tag in _COMMON:
            best = min(best, 48)
    return best


def build(source: Path = SOURCE, index: Path = INDEX) -> int:
    if not source.exists():
        raise FileNotFoundError(f"{source} not found — download JMdict_e.gz first")
    tmp = index.with_suffix(".tmp")
    tmp.unlink(missing_ok=True)
    conn = sqlite3.connect(tmp)
    conn.executescript("""
        CREATE TABLE entries (id INTEGER PRIMARY KEY, priority INTEGER NOT NULL, data TEXT NOT NULL);
        CREATE TABLE forms (form TEXT NOT NULL, entry_id INTEGER NOT NULL, kind TEXT NOT NULL);
    """)

    count = 0
    with gzip.open(source) as f:
        # JMdict expands entities like &n; to "noun (common) (futsuumeishi)".
        for _event, elem in ET.iterparse(f, events=("end",)):
            if elem.tag != "entry":
                continue
            kanji = [{"text": k.findtext("keb"), "pri": [p.text for p in k.findall("ke_pri")]}
                     for k in elem.findall("k_ele")]
            readings = [{"text": r.findtext("reb"), "pri": [p.text for p in r.findall("re_pri")]}
                        for r in elem.findall("r_ele")]
            senses = []
            for s in elem.findall("sense"):
                glosses = [g.text for g in s.findall("gloss") if g.text]
                if glosses:
                    senses.append({
                        "pos": [p.text for p in s.findall("pos")],
                        "gloss": glosses,
                        "misc": [m.text for m in s.findall("misc")],
                        "info": [i.text for i in s.findall("s_inf")],
                    })
            entry_id = int(elem.findtext("ent_seq"))
            priority = _priority([p for x in kanji + readings for p in x["pri"]])
            data = {
                "id": entry_id,
                "kanji": [k["text"] for k in kanji],
                "readings": [r["text"] for r in readings],
                "senses": senses,
                "common": priority < 99,
            }
            conn.execute("INSERT INTO entries VALUES (?, ?, ?)",
                         (entry_id, priority, json.dumps(data, ensure_ascii=False)))
            conn.executemany("INSERT INTO forms VALUES (?, ?, ?)",
                             [(k["text"], entry_id, "k") for k in kanji] +
                             [(r["text"], entry_id, "r") for r in readings])
            count += 1
            elem.clear()

    conn.execute("CREATE INDEX idx_forms_form ON forms (form)")
    conn.commit()
    conn.close()
    tmp.replace(index)
    _connection.cache_clear()
    return count


@lru_cache(maxsize=1)
def _connection() -> sqlite3.Connection | None:
    if not INDEX.exists():
        return None
    conn = sqlite3.connect(f"file:{INDEX}?mode=ro", uri=True, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def available() -> bool:
    return _connection() is not None


# Our part-of-speech labels (from furigana.py) -> words JMdict uses for them.
_POS_HINTS = {
    "noun": ("noun",), "pronoun": ("pronoun",), "verb": ("verb",),
    "i-adjective": ("adjective (keiyoushi)",), "na-adjective": ("keiyodoshi",),
    "adverb": ("adverb",), "particle": ("particle",), "auxiliary": ("auxiliary", "copula"),
    "suffix": ("suffix",), "prefix": ("prefix",), "interjection": ("interjection",),
    "pre-noun": ("pre-noun",), "conjunction": ("conjunction",),
}


def lookup(word: str, reading: str | None = None, limit: int = 5, pos: str | None = None) -> list[dict]:
    """Entries whose kanji or kana form is exactly `word`, best match first.

    `pos` keeps grammar words straight (the particle は, not 葉 "leaf");
    `reading` (hiragana) breaks ties between homographs: 生 as せい vs なま.
    """
    conn = _connection()
    if conn is None or not word:
        return []
    rows = conn.execute(
        """SELECT DISTINCT e.data, e.priority FROM forms f JOIN entries e ON e.id = f.entry_id
           WHERE f.form = ? ORDER BY e.priority, e.id LIMIT 30""",
        (word,),
    ).fetchall()
    entries = [json.loads(r["data"]) for r in rows]
    to_hira = lambda s: "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)  # noqa: E731
    hints = _POS_HINTS.get(pos or "", ())

    def rank(e: dict) -> tuple[bool, bool]:
        pos_ok = not hints or any(h in p for s in e["senses"] for p in s["pos"] for h in hints)
        reading_ok = not reading or any(to_hira(reading) == to_hira(r) for r in e["readings"])
        return (not pos_ok, not reading_ok)  # sort is stable, so frequency order is kept within ties

    entries.sort(key=rank)
    return entries[:limit]


def entry(entry_id: int) -> dict | None:
    conn = _connection()
    if conn is None:
        return None
    row = conn.execute("SELECT data FROM entries WHERE id = ?", (entry_id,)).fetchone()
    return json.loads(row["data"]) if row else None


def short_meaning(e: dict, senses: int = 2) -> str:
    return "; ".join(", ".join(s["gloss"][:3]) for s in e["senses"][:senses])


if __name__ == "__main__":
    start = time.time()
    n = build()
    print(f"Indexed {n} entries into {INDEX} in {time.time() - start:.0f}s", file=sys.stderr)
