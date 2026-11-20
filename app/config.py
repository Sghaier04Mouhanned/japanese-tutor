import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DB_PATH = Path(os.getenv("TUTOR_DB_PATH", ROOT / "data" / "tutor.db"))
STATIC_DIR = Path(__file__).resolve().parent / "static"
