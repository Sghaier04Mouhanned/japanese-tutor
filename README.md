# 日本語 Tutor

A personal Japanese tutor that runs in the browser — built for going from zero to
work-ready Japanese (and JLPT N5 → N4), powered by a free AI API or a local model.

## Features

**Kana trainer** (available now)
- Learn hiragana and katakana set by set: study each character with audio, then pass a quick check
- Spaced-repetition reviews (FSRS) so each kana comes back right before you'd forget it
- Free practice in two directions: type the reading, or pick the kana from four choices
- Progress chart, daily streak and accuracy
- Accepts common alternative spellings (si/shi, tu/tsu, zya/ja…)

**Coming next:** AI tutor chat with furigana, N5 lessons in polite form, word lookup
(JMdict), mistake tracking, work role-plays, voice practice, JLPT quizzes.

## Run it

Requires Python 3.11+. On Windows, double-click `run.bat`, or:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000.

Audio uses your browser's built-in Japanese voice. Microsoft Edge has the best
ones on Windows; in Chrome, the "Google 日本語" voice works well.

## Project layout

```
app/
  main.py       FastAPI app
  kana_api.py   kana endpoints (groups, unlock, review, stats)
  kana.py       kana tables and answer checking
  srs.py        FSRS spaced-repetition wrapper
  db.py         SQLite schema
  static/       web UI (HTML/CSS/JS)
data/           your progress database (git-ignored)
```
