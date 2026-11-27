import json
import sqlite3
import time
from contextlib import contextmanager

from .config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS kana_cards (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    script      TEXT    NOT NULL,
    kana        TEXT    NOT NULL,
    group_id    TEXT    NOT NULL,
    state       INTEGER NOT NULL,   -- fsrs.State
    stability   REAL,               -- days; NULL until first review
    due_ts      REAL    NOT NULL,   -- unix seconds
    fsrs        TEXT    NOT NULL,   -- fsrs.Card as JSON
    created_at  REAL    NOT NULL,
    UNIQUE (script, kana)
);
CREATE INDEX IF NOT EXISTS idx_kana_cards_due ON kana_cards (due_ts);

CREATE TABLE IF NOT EXISTS kana_reviews (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id     INTEGER NOT NULL REFERENCES kana_cards (id),
    answer      TEXT    NOT NULL,
    correct     INTEGER NOT NULL,
    rating      INTEGER NOT NULL,   -- fsrs.Rating
    elapsed_ms  INTEGER,
    reviewed_at REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_kana_reviews_time ON kana_reviews (reviewed_at);

CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chats (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    created_at  REAL    NOT NULL,
    updated_at  REAL    NOT NULL
);

CREATE TABLE IF NOT EXISTS chat_messages (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id     INTEGER NOT NULL REFERENCES chats (id) ON DELETE CASCADE,
    role        TEXT    NOT NULL CHECK (role IN ('user', 'assistant')),
    content     TEXT    NOT NULL,
    provider    TEXT,               -- which model wrote an assistant reply
    model       TEXT,
    created_at  REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_chat_messages_chat ON chat_messages (chat_id, id);

-- Words the learner saved (from chat lookups or lessons).
CREATE TABLE IF NOT EXISTS vocab (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id    INTEGER,            -- JMdict entry, when known
    word        TEXT    NOT NULL,
    reading     TEXT    NOT NULL,   -- hiragana/katakana
    meaning     TEXT    NOT NULL,
    source      TEXT    NOT NULL,   -- 'chat' | 'lesson' | 'reading' | 'listening' | 'jlpt' (word lists)
    created_at  REAL    NOT NULL,
    UNIQUE (word, reading)
);

-- Corrections Sensei made to the learner's Japanese.
CREATE TABLE IF NOT EXISTS mistakes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id     INTEGER REFERENCES chats (id) ON DELETE SET NULL,
    wrong       TEXT    NOT NULL,
    correct     TEXT    NOT NULL,
    note        TEXT    NOT NULL DEFAULT '',
    created_at  REAL    NOT NULL
);

-- Spaced-repetition cards for vocab and mistakes (kana have their own table).
CREATE TABLE IF NOT EXISTS deck_cards (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT    NOT NULL CHECK (kind IN ('vocab', 'mistake')),
    ref_id      INTEGER NOT NULL,
    state       INTEGER NOT NULL,
    stability   REAL,
    due_ts      REAL    NOT NULL,
    fsrs        TEXT    NOT NULL,
    created_at  REAL    NOT NULL,
    UNIQUE (kind, ref_id)
);
CREATE INDEX IF NOT EXISTS idx_deck_cards_due ON deck_cards (due_ts);

-- Kanji the learner is studying (spaced repetition, like kana_cards).
CREATE TABLE IF NOT EXISTS kanji_cards (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji       TEXT    NOT NULL UNIQUE,
    state       INTEGER NOT NULL,
    stability   REAL,
    due_ts      REAL    NOT NULL,
    fsrs        TEXT    NOT NULL,
    created_at  REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_kanji_cards_due ON kanji_cards (due_ts);

CREATE TABLE IF NOT EXISTS kanji_reviews (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id     INTEGER NOT NULL REFERENCES kanji_cards (id) ON DELETE CASCADE,
    rating      INTEGER NOT NULL,
    elapsed_ms  INTEGER,
    reviewed_at REAL    NOT NULL
);

CREATE TABLE IF NOT EXISTS quiz_sessions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at  REAL    NOT NULL,
    total       INTEGER NOT NULL,
    correct     INTEGER NOT NULL,
    by_type     TEXT    NOT NULL    -- JSON: {"reading": [correct, total], ...}
);

CREATE TABLE IF NOT EXISTS lesson_progress (
    lesson_id   TEXT    PRIMARY KEY,
    status      TEXT    NOT NULL CHECK (status IN ('started', 'done')),
    updated_at  REAL    NOT NULL
);

-- Answers to the reading passages (app/reading.py), one row per attempt.
CREATE TABLE IF NOT EXISTS reading_results (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    passage_id  TEXT    NOT NULL,
    correct     INTEGER NOT NULL,
    total       INTEGER NOT NULL,
    elapsed_ms  INTEGER,
    created_at  REAL    NOT NULL
);

-- Answers to the listening items (app/listening.py), one row per attempt.
CREATE TABLE IF NOT EXISTS listening_results (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id     TEXT    NOT NULL,
    correct     INTEGER NOT NULL,
    plays       INTEGER NOT NULL DEFAULT 1,
    created_at  REAL    NOT NULL
);

-- Mock tests (app/mock.py): the test with its answer key, and the result once submitted.
CREATE TABLE IF NOT EXISTS mock_tests (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    level       TEXT    NOT NULL,
    data        TEXT    NOT NULL,   -- JSON from mock.build()
    created_at  REAL    NOT NULL,
    finished_at REAL,
    correct     INTEGER,
    total       INTEGER,
    score       INTEGER,            -- estimated JLPT points
    passed      INTEGER,
    result      TEXT                -- JSON: answers, per-question results, section scores, time used
);

-- Every answer to a reading or listening question, wherever it was given: the
-- mistakes page brings back the questions whose latest answer was wrong.
CREATE TABLE IF NOT EXISTS question_attempts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    kind        TEXT    NOT NULL CHECK (kind IN ('reading', 'listening')),
    ref         TEXT    NOT NULL,   -- passage or listening item id
    question    INTEGER NOT NULL,   -- question index in the passage (0 for listening)
    correct     INTEGER NOT NULL,
    source      TEXT    NOT NULL CHECK (source IN ('practice', 'mock', 'retry')),
    created_at  REAL    NOT NULL
);
CREATE INDEX IF NOT EXISTS question_attempts_ref ON question_attempts (kind, ref, question);

CREATE TABLE IF NOT EXISTS deck_reviews (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id     INTEGER NOT NULL REFERENCES deck_cards (id) ON DELETE CASCADE,
    rating      INTEGER NOT NULL,
    elapsed_ms  INTEGER,
    reviewed_at REAL    NOT NULL
);
"""


# Columns added after a table first shipped: (table, column, definition).
MIGRATIONS = [
    ("chats", "lesson_id", "TEXT"),  # practice chats belong to a lesson
    ("kanji_reviews", "source", "TEXT NOT NULL DEFAULT 'recall'"),  # 'recall' (self-graded) or 'writing'
]


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        had_attempts = conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'question_attempts'").fetchone()
        conn.executescript(SCHEMA)
        if not had_attempts:
            _backfill_attempts(conn)
        for table, column, definition in MIGRATIONS:
            existing = {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}
            if column not in existing:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def record_attempts(conn, kind: str, source: str, answers: list[tuple[str, int, bool]]) -> None:
    """Log answers to reading or listening questions: (passage or item id, question index, correct)."""
    now = time.time()
    conn.executemany("""INSERT INTO question_attempts (kind, ref, question, correct, source, created_at)
                        VALUES (?, ?, ?, ?, ?, ?)""", [(kind, ref, q, int(ok), source, now) for ref, q, ok in answers])


def _backfill_attempts(conn) -> None:
    """Fill question_attempts from what was saved before it existed: listening answers,
    finished mock tests, and reading scores where the score tells which questions were
    right (all or none; a partial score doesn't say which ones were missed)."""
    rows = [("listening", r["item_id"], 0, r["correct"], "practice", r["created_at"])
            for r in conn.execute("SELECT item_id, correct, created_at FROM listening_results")]
    for r in conn.execute("SELECT passage_id, correct, total, created_at FROM reading_results"):
        if r["correct"] in (0, r["total"]):
            rows += [("reading", r["passage_id"], i, int(r["correct"] > 0), "practice", r["created_at"])
                     for i in range(r["total"])]
    for r in conn.execute("SELECT data, result, finished_at FROM mock_tests WHERE finished_at IS NOT NULL"):
        test, result = json.loads(r["data"]), json.loads(r["result"])["questions"]
        rows += [("reading", q["passage"], q["index"], int(result[q["id"]]["correct"]), "mock", r["finished_at"])
                 for q in test["reading"] if q["id"] in result]
        rows += [("listening", q["item"], 0, int(result[q["id"]]["correct"]), "mock", r["finished_at"])
                 for q in test["listening"] if q["id"] in result]
    conn.executemany("""INSERT INTO question_attempts (kind, ref, question, correct, source, created_at)
                        VALUES (?, ?, ?, ?, ?, ?)""", rows)


def get_setting(conn, key: str, default: str | None = None) -> str | None:
    row = conn.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


def set_setting(conn, key: str, value: str) -> None:
    conn.execute(
        "INSERT INTO settings (key, value) VALUES (?, ?) "
        "ON CONFLICT (key) DO UPDATE SET value = excluded.value",
        (key, value),
    )


@contextmanager
def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
