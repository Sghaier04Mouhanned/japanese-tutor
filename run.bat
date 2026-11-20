@echo off
cd /d "%~dp0"
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)
echo Checking packages...
.venv\Scripts\python.exe -m pip install --quiet --disable-pip-version-check -r requirements.txt
start "" http://127.0.0.1:8000
.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
