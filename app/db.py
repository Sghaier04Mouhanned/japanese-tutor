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
"""


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(SCHEMA)


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
