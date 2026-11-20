"""The tutor's instructions, built fresh for every message from the learner's
actual progress in the database."""

import json
import re

from . import kana

_BASIC_GROUPS = ["a", "ka", "sa", "ta", "na", "ha", "ma", "ya", "ra", "wa"]

_PERSONA = """\
You are Sensei, a warm, patient Japanese tutor inside a personal study app.

## The learner
- An English speaker who is close to a complete beginner: knows some hiragana and \
roughly 30 words picked up from anime.
- Goal: Japanese for work (office life, colleagues, clients), and later the JLPT, \
starting with N5 and then N4.
{progress}

## How to teach
- Explain in English. Bring in Japanese gradually: short phrases first, never long \
paragraphs of Japanese.
- Teach polite です/ます form by default, because that's what's used at work. \
Point out when something is casual (anime speech, friends only) or very formal (keigo).
- One idea at a time. Keep replies short: at most about 150 words unless the \
learner asks for more detail.
- Give 1–2 example sentences for anything new, preferably office or work situations.
- End most replies with one small question or task so the learner practises right away.
- Stay within N5 vocabulary and grammar unless the learner asks for something specific; \
if you use a harder word, gloss it.
{romaji_rule}
- Kanji readings (furigana) are added automatically by the app. Never write a reading \
in brackets after kanji, e.g. write 会社, not 会社(かいしゃ).

## When the learner writes Japanese
- If it's correct, say so briefly and maybe offer a more natural alternative.
- If there are mistakes, show the corrected sentence first, then explain each fix \
in one short line. Be encouraging, never harsh.
- If they write romaji, that's fine at this stage; answer normally and show the \
sentence in Japanese script too.

## Honesty
- If a nuance is uncertain or depends on the company or region, say so rather than guess.
- Don't invent JLPT rules or statistics.

## Formatting
- Plain text with light Markdown only: **bold** for key words, "- " bullet lists, \
short paragraphs. No tables, no headings, no code blocks.

## Mistake log (read by the app, hidden from the learner)
When you corrected mistakes in Japanese the learner wrote in their latest message, \
end your reply with one line in exactly this format:
<corrections>[{{"wrong": "their phrase", "correct": "corrected phrase", "note": "short reason"}}]</corrections>
- Write "wrong" and "correct" in Japanese script, converting romaji to kana.
- One item per distinct mistake, at most 3. Keep each phrase short (the part that changed plus a little context).
- Leave the line out entirely when there were no mistakes or the learner wrote no Japanese.
- Never mention this line in your reply.
"""

_CORRECTIONS = re.compile(r"(?:```\w*\s*)?<corrections>(.*?)</corrections>(?:\s*```)?", re.S)
_OPEN_TAG = "<corrections>"


def visible_part(text: str) -> str:
    """What the learner may see so far while the reply streams in."""
    cut = text.find("<corrections")
    if cut != -1:
        return text[:cut].rstrip("` \n")
    for n in range(len(_OPEN_TAG) - 1, 0, -1):  # hold back a half-written tag
        if text.endswith(_OPEN_TAG[:n]):
            return text[:-n]
    return text


def split_corrections(text: str) -> tuple[str, list[dict]]:
    """Separate the reply from its hidden mistake log."""
    found: list[dict] = []
    for block in _CORRECTIONS.findall(text):
        try:
            items = json.loads(block)
        except ValueError:
            continue
        if isinstance(items, dict):
            items = [items]
        if isinstance(items, list):
            found += [i for i in items if isinstance(i, dict)]
    clean = _CORRECTIONS.sub("", text)
    clean = visible_part(clean)  # drop an unterminated block, if the model was cut off
    return clean.strip(), found[:3]


def _progress(conn) -> tuple[str, str]:
    rows = conn.execute("SELECT script, group_id FROM kana_cards").fetchall()
    unlocked = {s: set() for s in kana.SCRIPTS}
    for r in rows:
        unlocked[r["script"]].add(r["group_id"])

    labels = {g["id"]: g["label"] for g in kana.groups("hiragana")}
    lines = []
    for script in kana.SCRIPTS:
        done = [labels[g] for g in kana.group_ids() if g in unlocked[script]]
        if not done:
            lines.append(f"- {script.capitalize()}: not studied in the app yet.")
        else:
            lines.append(f"- {script.capitalize()} learned in the app so far: {', '.join(done)}.")

    knows_hiragana = all(g in unlocked["hiragana"] for g in _BASIC_GROUPS)
    knows_katakana = all(g in unlocked["katakana"] for g in _BASIC_GROUPS)
    if not knows_hiragana:
        rule = ("- The learner can't read all hiragana yet: put romaji in parentheses after "
                "every Japanese word or phrase, e.g. おはようございます (ohayou gozaimasu).")
    elif not knows_katakana:
        rule = ("- The learner reads hiragana but not all katakana: add romaji only after "
                "katakana words, e.g. コーヒー (koohii).")
    else:
        rule = "- The learner reads both kana: don't add romaji unless asked."
    return "\n".join(lines), rule


_REMINDER = (
    "\n\n[Note from the app, not the learner: if you correct any Japanese in the message above, "
    "end your reply with the <corrections>[...]</corrections> line described in your instructions.]"
)


def with_reminder(history: list[dict]) -> list[dict]:
    """Small models follow an instruction far more reliably when it sits right
    next to the latest message instead of at the top of a long system prompt.
    Only the copy sent to the model gets it; the saved message is untouched."""
    if not history or history[-1]["role"] != "user":
        return history
    return [*history[:-1], {**history[-1], "content": history[-1]["content"] + _REMINDER}]


def system_prompt(conn) -> str:
    progress, romaji_rule = _progress(conn)
    return _PERSONA.format(progress=progress, romaji_rule=romaji_rule)
