import sqlite3
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
        conn.executescript(SCHEMA)
        for table, column, definition in MIGRATIONS:
            existing = {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}
            if column not in existing:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


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
