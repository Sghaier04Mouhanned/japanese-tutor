"""JLPT N5-style quiz questions, generated from verified data only.

Sources are the hand-written lessons and the learner's saved words, never the
language model, so every answer key is right. Question types follow the real
test: kanji reading (漢字読み), spelling (表記), vocabulary meaning, particles
(文法) and listening (聴解).
"""

from __future__ import annotations

import random
import re

from . import furigana, lessons

TYPES = ("reading", "writing", "meaning", "particle", "listening")

_KANJI = re.compile(r"[㐀-鿿々]")

# Dakuten pairs, both directions: か<->が, は<->ば/ぱ ...
_VOICED = dict(zip("かきくけこさしすせそたちつてとはひふへほ", "がぎぐげござじずぜぞだぢづでどばびぶべぼ"))
_VOICED.update({v: k for k, v in list(_VOICED.items())})
_VOICED.update(dict(zip("ばびぶべぼ", "ぱぴぷぺぽ")))
_SMALL = dict(zip("ゃゅょっ", "やゆよつ"))
_SMALL.update({v: k for k, v in _SMALL.items()})


def _near_misses(reading: str) -> list[str]:
    """Plausible wrong readings, the way the JLPT builds distractors:
    がっこう -> がこう (no small っ), かっこう (no dakuten), がっこ (short vowel)..."""
    out: set[str] = set()
    for i, c in enumerate(reading):
        if c in _VOICED:
            out.add(reading[:i] + _VOICED[c] + reading[i + 1:])
        if c in _SMALL:
            out.add(reading[:i] + _SMALL[c] + reading[i + 1:])
        if c == "っ":
            out.add(reading[:i] + reading[i + 1:])
        if c in "うい" and i > 0:  # long vowels: こう -> こ, せい -> せ
            out.add(reading[:i] + reading[i + 1:])
    for i in range(1, len(reading)):  # add a small っ where there was none (never after ん or a small kana)
        if reading[i] in "かきくけこさしすせそたちつてとぱぴぷぺぽ" and reading[i - 1] not in "っんゃゅょー":
            out.add(reading[:i] + "っ" + reading[i:])
    if reading.endswith(("ょ", "ゅ", "こ", "そ", "と", "ろ", "よ")):
        out.add(reading + "う")
    out.discard(reading)
    return [r for r in out if r]


def _pick_distractors(correct: str, candidates: list[str], n: int = 3) -> list[str] | None:
    seen, picked = {correct}, []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            picked.append(c)
        if len(picked) == n:
            return picked
    return None


def _question(qtype: str, prompt: dict, correct: str, distractors: list[str], explain: str, item: dict) -> dict:
    choices = [correct, *distractors]
    random.shuffle(choices)
    return {"type": qtype, "prompt": prompt, "choices": choices, "answer": choices.index(correct),
            "explain": explain, "item": item}


def _reading_q(v: dict, pool: list[dict]) -> dict | None:
    if not _KANJI.search(v["word"]):
        return None
    misses = _near_misses(v["reading"])
    random.shuffle(misses)
    others = [p["reading"] for p in pool if len(p["reading"]) == len(v["reading"])]
    random.shuffle(others)
    distractors = _pick_distractors(v["reading"], misses + others)
    if not distractors:
        return None
    return _question("reading", {"word": v["word"], "instruction": "How is this word read?"},
                     v["reading"], distractors, f"{v['word']} is read {v['reading']}: {v['meaning']}.", v)


def _writing_q(v: dict, pool: list[dict]) -> dict | None:
    if not _KANJI.search(v["word"]):
        return None
    others = [p["word"] for p in pool if _KANJI.search(p["word"]) and p["word"] != v["word"]]
    # Words of the same length look most alike, so offer those first.
    others.sort(key=lambda w: (abs(len(w) - len(v["word"])), random.random()))
    distractors = _pick_distractors(v["word"], others)
    if not distractors:
        return None
    return _question("writing", {"reading": v["reading"], "instruction": "Which is the right way to write this word?"},
                     v["word"], distractors, f"{v['reading']} is written {v['word']}: {v['meaning']}.", v)


def _meaning_q(v: dict, pool: list[dict]) -> dict | None:
    others = [p["meaning"] for p in pool if p["meaning"] != v["meaning"]]
    random.shuffle(others)
    distractors = _pick_distractors(v["meaning"], others)
    if not distractors:
        return None
    return _question("meaning", {"segments": furigana.annotate(v["word"]), "instruction": "What does this mean?"},
                     v["meaning"], distractors, f"{v['word']} ({v['reading']}) means \"{v['meaning']}\".", v)


_PARTICLES = ["は", "を", "に", "で", "の", "か", "と", "が", "も", "へ", "から", "まで"]
# Particles that would also be correct (or nearly) in the same slot never appear as distractors.
_ALSO_OK = {"は": {"が", "も"}, "が": {"は", "も"}, "も": {"は", "が"}, "に": {"へ"}, "へ": {"に"}, "か": {"の"}}


def _particle_q(ex: dict) -> dict | None:
    segs = furigana.annotate(ex["jp"])
    slots = [i for i, s in enumerate(segs) if s.get("p") == "particle" and s["t"] in _PARTICLES]
    if not slots:
        return None
    i = random.choice(slots)
    answer = segs[i]["t"]
    pool = [p for p in _PARTICLES if p != answer and p not in _ALSO_OK.get(answer, set())]
    random.shuffle(pool)
    blanked = [*segs[:i], {"t": "（　）"}, *segs[i + 1:]]
    return _question("particle", {"segments": blanked, "hint": ex["en"],
                                  "instruction": "Which particle goes in the blank?"},
                     answer, pool[:3], f"{ex['jp']} ({ex['romaji']}) = {ex['en']}", {"example": ex["jp"]})


def _listening_q(ex: dict, examples: list[dict]) -> dict | None:
    others = [e["en"] for e in examples if e["jp"] != ex["jp"]]
    random.shuffle(others)
    distractors = _pick_distractors(ex["en"], others)
    if not distractors:
        return None
    return _question("listening", {"audio": ex["jp"], "instruction": "Listen. What does the sentence mean?"},
                     ex["en"], distractors, f"You heard: {ex['jp']} ({ex['romaji']})",
                     {"example": ex["jp"], "segments": furigana.annotate(ex["jp"])})


def build(lesson_ids: list[str], saved_words: list[dict], count: int = 10,
          types: tuple[str, ...] = TYPES) -> list[dict]:
    chosen = [les for les in lessons.LESSONS if les["id"] in lesson_ids] or lessons.LESSONS[:1]
    vocab = [v for les in chosen for v in les["vocab"]]
    vocab += [w for w in saved_words if w["word"] not in {v["word"] for v in vocab}]
    examples = [e for les in chosen for e in les["examples"]]
    # Distractor pool: every lesson's words, so even a small quiz has options.
    pool = [v for les in lessons.LESSONS for v in les["vocab"]] + saved_words

    all_examples = [e for les in lessons.LESSONS for e in les["examples"]]
    makers: dict[str, list] = {
        "reading": [lambda v=v: _reading_q(v, pool) for v in vocab],
        "writing": [lambda v=v: _writing_q(v, pool) for v in vocab],
        "meaning": [lambda v=v: _meaning_q(v, pool) for v in vocab],
        "particle": [lambda e=e: _particle_q(e) for e in examples],
        "listening": [lambda e=e: _listening_q(e, all_examples) for e in examples],
    }
    queues = {t: random.sample(makers[t], len(makers[t])) for t in types if t in makers}

    # Take one question of each type in turn so the mix stays balanced.
    questions, seen = [], set()
    while len(questions) < count and any(queues.values()):
        for t in random.sample(list(queues), len(queues)):
            while queues[t]:
                q = queues[t].pop()()
                if q is None:
                    continue
                key = (q["type"], q["choices"][q["answer"]])
                if key not in seen:
                    seen.add(key)
                    questions.append(q)
                    break
            if len(questions) == count:
                break
    random.shuffle(questions)
    return questions
