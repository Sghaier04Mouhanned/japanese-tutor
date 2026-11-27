"""Backups of the progress database: a copy each day in data/backups (the last
KEEP are kept), a download on demand, and restore from a download or a daily copy.
Restoring first saves the current database, so a wrong restore can be undone."""

import asyncio
import re
import shutil
import sqlite3
import tempfile
import time
from datetime import date, datetime
from pathlib import Path

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from fastapi.responses import FileResponse

from .config import DB_PATH
from .db import init_db

router = APIRouter(prefix="/api/backup", tags=["backup"])

BACKUP_DIR = DB_PATH.parent / "backups"
KEEP = 14                      # daily copies
KEEP_BEFORE_RESTORE = 5        # copies saved just before a restore
MAX_UPLOAD = 500 * 1024 * 1024
# Tables every version of the app has had: a file without them isn't a tutor database.
REQUIRED_TABLES = {"kana_cards", "kana_reviews", "settings"}
_NAME = re.compile(r"^tutor-(\d{4}-\d{2}-\d{2})(-before-restore-\d{6})?\.db$")


def _copy(src: Path, dest: Path) -> None:
    """Consistent copy with SQLite's backup API (safe while the app is writing)."""
    tmp = dest.with_suffix(".part")
    with sqlite3.connect(src) as s, sqlite3.connect(tmp) as d:
        s.backup(d)
    s.close()
    d.close()
    tmp.replace(dest)


def _prune(pattern: str, keep: int) -> None:
    for old in sorted(BACKUP_DIR.glob(pattern))[:-keep]:
        old.unlink(missing_ok=True)


def daily_backup() -> Path | None:
    """Today's copy, unless it exists already (or there's nothing to back up yet)."""
    if not DB_PATH.exists():
        return None
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    dest = BACKUP_DIR / f"tutor-{date.today().isoformat()}.db"
    if not dest.exists():
        _copy(DB_PATH, dest)
        _prune("tutor-????-??-??.db", KEEP)
    return dest


async def keep_backing_up() -> None:
    """Runs while the app is up, so a computer left on for days still gets daily copies."""
    while True:
        try:
            await asyncio.to_thread(daily_backup)
        except Exception as e:  # a failed backup must never take the app down
            print(f"Daily backup failed: {e}")
        await asyncio.sleep(3600)


def _check(path: Path) -> None:
    """Refuse anything that isn't a healthy tutor database."""
    with open(path, "rb") as f:
        if f.read(16) != b"SQLite format 3\x00":
            raise HTTPException(400, "That file isn't a tutor backup (not an SQLite database).")
    try:
        conn = sqlite3.connect(path)
        try:
            if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                raise HTTPException(400, "That backup is damaged (integrity check failed).")
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        finally:
            conn.close()
    except sqlite3.DatabaseError as e:
        raise HTTPException(400, f"That backup can't be read: {e}")
    if not REQUIRED_TABLES <= tables:
        raise HTTPException(400, "That database isn't from this app (its tables are missing).")


def _restore(path: Path) -> str:
    """Save the current database, then copy the backup over it."""
    _check(path)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    safety = BACKUP_DIR / f"tutor-{datetime.now():%Y-%m-%d-before-restore-%H%M%S}.db"
    if DB_PATH.exists():
        _copy(DB_PATH, safety)
        _prune("tutor-*-before-restore-*.db", KEEP_BEFORE_RESTORE)
    # Copying pages into the live file (rather than swapping files) works while
    # other connections exist and keeps the file's place on disk.
    with sqlite3.connect(path) as src, sqlite3.connect(DB_PATH) as dest:
        src.backup(dest)
    src.close()
    dest.close()
    init_db()  # an older backup gets the tables and columns added since
    return safety.name


def _info(p: Path) -> dict:
    m = _NAME.match(p.name)
    st = p.stat()
    return {"name": p.name, "date": m.group(1), "before_restore": bool(m.group(2)),
            "size": st.st_size, "modified": st.st_mtime}


@router.get("")
def list_backups():
    files = sorted((p for p in BACKUP_DIR.glob("tutor-*.db") if _NAME.match(p.name)) if BACKUP_DIR.exists() else [],
                   key=lambda p: p.stat().st_mtime, reverse=True)
    return {
        "size": DB_PATH.stat().st_size if DB_PATH.exists() else 0,
        "folder": str(BACKUP_DIR),
        "keep": KEEP,
        "backups": [_info(p) for p in files],
    }


@router.get("/download")
def download(background: BackgroundTasks):
    tmp = Path(tempfile.mkdtemp()) / "tutor.db"
    _copy(DB_PATH, tmp)
    background.add_task(shutil.rmtree, tmp.parent, True)
    return FileResponse(tmp, media_type="application/vnd.sqlite3",
                        filename=f"tutor-backup-{datetime.now():%Y-%m-%d-%H%M}.db")


@router.post("/restore")
async def restore_upload(request: Request):
    """Restore from a downloaded backup, sent as the raw request body."""
    folder = Path(tempfile.mkdtemp())
    path = folder / "upload.db"
    try:
        size = 0
        with open(path, "wb") as f:
            async for chunk in request.stream():
                size += len(chunk)
                if size > MAX_UPLOAD:
                    raise HTTPException(413, "That file is too large to be a tutor backup.")
                f.write(chunk)
        if not size:
            raise HTTPException(400, "No file was sent.")
        saved = await asyncio.to_thread(_restore, path)
    finally:
        shutil.rmtree(folder, ignore_errors=True)
    return {"ok": True, "saved_as": saved, "restored_at": time.time()}


@router.post("/restore/{name}")
def restore_daily(name: str):
    """Restore one of the copies in data/backups."""
    if not _NAME.match(name) or not (BACKUP_DIR / name).is_file():
        raise HTTPException(404, "backup not found")
    # Work from a copy: the restore saves a new copy into the same folder and may prune it.
    folder = Path(tempfile.mkdtemp())
    try:
        shutil.copy2(BACKUP_DIR / name, folder / name)
        saved = _restore(folder / name)
    finally:
        shutil.rmtree(folder, ignore_errors=True)
    return {"ok": True, "saved_as": saved, "restored_at": time.time()}
