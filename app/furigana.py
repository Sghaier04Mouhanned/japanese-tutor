"""Readings for kanji come from a morphological analyzer (MeCab + UniDic via
fugashi), never from the language model, which can confidently get them wrong.

`annotate(text)` splits text into words the UI renders with <ruby> furigana and
makes clickable for dictionary lookups (see the function for the format).
"""

from __future__ import annotations

import re
from functools import lru_cache

_KANJI = re.compile(r"[㐀-䶿一-鿿豈-﫿々〆ヵヶ]")


@lru_cache(maxsize=1)
def _tagger():
    from fugashi import Tagger  # imported lazily: loading the dictionary takes a moment

    return Tagger()


def _to_hiragana(text: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def _is_kana(c: str) -> bool:
    return "ぁ" <= c <= "ゖ" or "ァ" <= c <= "ヺ" or c == "ー"


def _split_okurigana(surface: str, reading: str) -> list[dict]:
    """Put readings only over the kanji: 飲み物/のみもの -> 飲(の)み物(もの).

    The surface is cut into kanji runs and kana runs; kana runs must appear
    literally in the reading, kanji runs soak up whatever lies between them.
    """
    runs = re.findall(r"[ぁ-ゖァ-ヺー]+|[^ぁ-ゖァ-ヺー]+", surface)
    pattern = "".join(
        re.escape(_to_hiragana(run)) if _is_kana(run[0]) else "(.+?)" for run in runs
    )
    match = re.fullmatch(pattern, reading)
    if not match:
        return [{"t": surface, "r": reading}]

    readings = iter(match.groups())
    return [{"t": run} if _is_kana(run[0]) else {"t": run, "r": next(readings)} for run in runs]


# UniDic sometimes prefers a formal or literary reading. For a learner, show
# the everyday one (私 is わたし in normal speech, not わたくし).
_EVERYDAY_READINGS = {
    "私": "わたし",
    "日本": "にほん",
    "明日": "あした",
    "昨日": "きのう",
    "今日": "きょう",
    "今朝": "けさ",
    "今年": "ことし",
    "一人": "ひとり",
    "二人": "ふたり",
    "上手": "じょうず",
    "下手": "へた",
    "何時": "なんじ",  # なんどき is literary
    "富士山": "ふじさん",  # ふじやま is old-fashioned / poetic
    "山道": "やまみち",  # さんどう is the formal reading
    "箱": "はこ",  # on its own the analyzer can give the compound form ばこ
    "傷": "きず",  # しょう is only for compounds like 負傷
    "重そう": "おもそう",  # "looks heavy"; read as one noun it becomes じゅうそう (baking soda)
}

# The analyzer reads number + counter one character at a time (四時 as
# よんじ, 九時 as きゅうじ). These are the readings learners actually need.
# Each value is the ruby for (number, counter); a single string means the
# reading only works over the whole word (一人 = ひとり).
_NUM = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "何"]
_COUNTERS: dict[str, list] = {
    "時": [("いち", "じ"), ("に", "じ"), ("さん", "じ"), ("よ", "じ"), ("ご", "じ"), ("ろく", "じ"),
          ("しち", "じ"), ("はち", "じ"), ("く", "じ"), ("じゅう", "じ"), ("なん", "じ")],
    "分": [("いっ", "ぷん"), ("に", "ふん"), ("さん", "ぷん"), ("よん", "ぷん"), ("ご", "ふん"), ("ろっ", "ぷん"),
          ("なな", "ふん"), ("はっ", "ぷん"), ("きゅう", "ふん"), ("じゅっ", "ぷん"), ("なん", "ぷん")],
    "人": ["ひとり", "ふたり", ("さん", "にん"), ("よ", "にん"), ("ご", "にん"), ("ろく", "にん"),
          ("なな", "にん"), ("はち", "にん"), ("きゅう", "にん"), ("じゅう", "にん"), ("なん", "にん")],
    # 一日 is ついたち (the 1st) or いちにち (one day) depending on meaning, so it's left alone.
    "日": [None, "ふつか", "みっか", "よっか", "いつか", "むいか",
          "なのか", "ようか", "ここのか", "とおか", ("なん", "にち")],
    # Months: 四月 しがつ, 七月 しちがつ, 九月 くがつ.
    "月": [("いち", "がつ"), ("に", "がつ"), ("さん", "がつ"), ("し", "がつ"), ("ご", "がつ"), ("ろく", "がつ"),
          ("しち", "がつ"), ("はち", "がつ"), ("く", "がつ"), ("じゅう", "がつ"), ("なん", "がつ")],
    # Long objects (pens, bottles): sound changes after 1, 3, 6, 8, 10 and 何.
    "本": [("いっ", "ぽん"), ("に", "ほん"), ("さん", "ぼん"), ("よん", "ほん"), ("ご", "ほん"), ("ろっ", "ぽん"),
          ("なな", "ほん"), ("はっ", "ぽん"), ("きゅう", "ほん"), ("じゅっ", "ぽん"), ("なん", "ぼん")],
    # Small animals
    "匹": [("いっ", "ぴき"), ("に", "ひき"), ("さん", "びき"), ("よん", "ひき"), ("ご", "ひき"), ("ろっ", "ぴき"),
          ("なな", "ひき"), ("はっ", "ぴき"), ("きゅう", "ひき"), ("じゅっ", "ぴき"), ("なん", "びき")],
    # Times (occurrences)
    "回": [("いっ", "かい"), ("に", "かい"), ("さん", "かい"), ("よん", "かい"), ("ご", "かい"), ("ろっ", "かい"),
          ("なな", "かい"), ("はっ", "かい"), ("きゅう", "かい"), ("じゅっ", "かい"), ("なん", "かい")],
    # Floors: 三階 さんがい, 何階 なんがい
    "階": [("いっ", "かい"), ("に", "かい"), ("さん", "がい"), ("よん", "かい"), ("ご", "かい"), ("ろっ", "かい"),
          ("なな", "かい"), ("はっ", "かい"), ("きゅう", "かい"), ("じゅっ", "かい"), ("なん", "がい")],
    # Weeks: 一週間 いっしゅうかん, 八週間 はっしゅうかん
    "週間": [("いっ", "しゅうかん"), ("に", "しゅうかん"), ("さん", "しゅうかん"), ("よん", "しゅうかん"),
           ("ご", "しゅうかん"), ("ろく", "しゅうかん"), ("なな", "しゅうかん"), ("はっ", "しゅうかん"),
           ("きゅう", "しゅうかん"), ("じゅっ", "しゅうかん"), ("なん", "しゅうかん")],
    # Years: 四年 よねん (not よんねん or しねん), 七年 ななねん
    "年": [("いち", "ねん"), ("に", "ねん"), ("さん", "ねん"), ("よ", "ねん"), ("ご", "ねん"), ("ろく", "ねん"),
          ("なな", "ねん"), ("はち", "ねん"), ("きゅう", "ねん"), ("じゅう", "ねん"), ("なん", "ねん")],
    "年間": [("いち", "ねんかん"), ("に", "ねんかん"), ("さん", "ねんかん"), ("よ", "ねんかん"), ("ご", "ねんかん"),
           ("ろく", "ねんかん"), ("なな", "ねんかん"), ("はち", "ねんかん"), ("きゅう", "ねんかん"), ("じゅう", "ねんかん"),
           ("なん", "ねんかん")],
    # Nights' stay: 一泊 いっぱく, 三泊 さんぱく
    "泊": [("いっ", "ぱく"), ("に", "はく"), ("さん", "ぱく"), ("よん", "はく"), ("ご", "はく"), ("ろっ", "ぱく"),
          ("なな", "はく"), ("はっ", "ぱく"), ("きゅう", "はく"), ("じゅっ", "ぱく"), ("なん", "ぱく")],
    # Dishes, items: 一品 いっぴん
    "品": [("いっ", "ぴん"), ("に", "ひん"), ("さん", "ぴん"), ("よん", "ひん"), ("ご", "ひん"), ("ろっ", "ぴん"),
          ("なな", "ひん"), ("はっ", "ぴん"), ("きゅう", "ひん"), ("じゅっ", "ぴん"), ("なん", "ぴん")],
    # Books: 一冊 いっさつ, 八冊 はっさつ
    "冊": [("いっ", "さつ"), ("に", "さつ"), ("さん", "さつ"), ("よん", "さつ"), ("ご", "さつ"), ("ろく", "さつ"),
          ("なな", "さつ"), ("はっ", "さつ"), ("きゅう", "さつ"), ("じゅっ", "さつ"), ("なん", "さつ")],
    # Steps: 一歩 いっぽ, 三歩 さんぽ
    "歩": [("いっ", "ぽ"), ("に", "ほ"), ("さん", "ぽ"), ("よん", "ほ"), ("ご", "ほ"), ("ろっ", "ぽ"),
          ("なな", "ほ"), ("はっ", "ぽ"), ("きゅう", "ほ"), ("じゅっ", "ぽ"), ("なん", "ぽ")],
    # Cups and glasses: 一杯 いっぱい, 三杯 さんばい
    "杯": [("いっ", "ぱい"), ("に", "はい"), ("さん", "ばい"), ("よん", "はい"), ("ご", "はい"), ("ろっ", "ぱい"),
          ("なな", "はい"), ("はっ", "ぱい"), ("きゅう", "はい"), ("じゅっ", "ぱい"), ("なん", "ばい")],
    # Flat things (paper, tickets)
    "枚": [("いち", "まい"), ("に", "まい"), ("さん", "まい"), ("よん", "まい"), ("ご", "まい"), ("ろく", "まい"),
          ("なな", "まい"), ("はち", "まい"), ("きゅう", "まい"), ("じゅう", "まい"), ("なん", "まい")],
    # Age (二十歳 is はたち, handled by the analyzer as one word)
    "歳": [("いっ", "さい"), ("に", "さい"), ("さん", "さい"), ("よん", "さい"), ("ご", "さい"), ("ろく", "さい"),
          ("なな", "さい"), ("はっ", "さい"), ("きゅう", "さい"), ("じゅっ", "さい"), ("なん", "さい")],
}


# How the analyzer may read each digit at the end of a longer number.
_DIGIT_READINGS = {"一": ("いち",), "二": ("に",), "三": ("さん",), "四": ("よん", "し"), "五": ("ご",),
                   "六": ("ろく",), "七": ("なな", "しち"), "八": ("はち",), "九": ("きゅう", "く"), "十": ("じゅう",)}


def _context_reading(prev, word, nxt=None, prev2=None) -> str | None:
    """Readings that depend on the neighbouring words, where the analyzer guesses wrong."""
    # 辛い is からい (spicy) or つらい (painful). Learners meet "spicy" first, and
    # つらい is usually written in kana, so prefer から for this kanji.
    if word.surface.startswith("辛") and getattr(word.feature, "orthBase", "") == "辛い":
        kana = _reading(word) or ""
        if kana.startswith("つら"):
            return "から" + kana[2:]
    # 何 is なに before most particles (何が, 何を, 何も) and なん before です/の/counters.
    if word.surface == "何" and nxt is not None and nxt.surface in {"が", "を", "も", "か", "に", "へ", "より"}:
        return "なに"
    # 年 on its own (年のわりに, 年が近い) is とし "age"; after a number (2020年, 一年) it stays ねん.
    # ...except 年に一度 / 年に二回 (once a year), which is ねん.
    if word.surface == "年" and (prev is None or prev.feature.pos1 in {"助詞", "補助記号"}):
        return "ねん" if nxt is not None and nxt.surface == "に" else "とし"
    # Native counting with つ: 四つ よっつ (the analyzer gives よん).
    if word.surface == "四" and nxt is not None and nxt.surface == "つ":
        return "よっ"
    # 体 on its own before a particle is からだ (body); たい is for compounds like 体育.
    if word.surface == "体" and nxt is not None and nxt.surface in {"に", "が", "を", "は", "も", "の", "で"}:
        return "からだ"
    # "Throughout": 一日中 いちにちじゅう, 今日中 きょうじゅう, 世界中 せかいじゅう (not ちゅう).
    if word.surface == "中" and prev is not None and (
            prev.surface in _JUU_AFTER or (prev.surface in {"日", "年", "晩"} and prev2 is not None and prev2.surface == "一")):
        return "じゅう"
    # 三文の徳 (an old coin): もん.
    if word.surface == "文" and prev is not None and prev.surface == "三" and nxt is not None and nxt.surface == "の":
        return "もん"
    # Flours: 小麦粉 こむぎこ, パン粉 パンこ (the analyzer reads a split-off 粉 as こな).
    if word.surface == "粉" and prev is not None and prev.surface in {"小麦", "パン", "そば", "米"}:
        return "こ"
    # 水道管 すいどうかん: the analyzer splits it as 水 (みず) + 道管.
    if word.surface == "水" and nxt is not None and nxt.surface == "道管":
        return "すい"
    # 道案内 (giving directions) is みちあんない.
    if word.surface == "道" and nxt is not None and nxt.surface == "案内":
        return "みち"
    # 言う is いう; the analyzer gives the spoken ゆう.
    if getattr(word.feature, "orthBase", "") == "言う":
        kana = _reading(word) or ""
        if kana.startswith("ゆ"):
            return "い" + kana[1:]
    if prev is None:
        return None
    # Weekday in brackets after a date: 8日（月） is げつ, not がつ.
    if (word.surface in _WEEKDAYS and prev.surface in {"（", "("}
            and nxt is not None and nxt.surface in {"）", ")"}):
        return _WEEKDAYS[word.surface]
    # Family with お〜さん: お母さん おかあさん, お父さん おとうさん (not おははさん).
    if (word.surface in _HONORIFIC_FAMILY and prev.surface == "お"
            and nxt is not None and nxt.surface in {"さん", "様", "ちゃん"}):
        return _HONORIFIC_FAMILY[word.surface]
    # Nationality: アメリカ人, 日本人, 外国人 -> じん (not にん)
    if word.surface == "人" and word.feature.pos1 == "接尾辞" and (
            word.feature.pos3 == "一般" and prev.feature.pos3 == "地名" or prev.surface == "外国"):
        return "じん"
    # 今日 modified by a verb or adjective (物があふれる今日) means "nowadays": こんにち.
    if word.surface == "今日" and prev.feature.pos1 in {"動詞", "形容詞"}:
        return "こんにち"
    # 得る as a main verb after a particle (情報を得る) is える; あり得る keeps うる.
    if getattr(word.feature, "orthBase", "") == "得る" and prev.feature.pos1 == "助詞":
        kana = _reading(word) or ""
        if kana.startswith("う"):
            return "え" + kana[1:]
    # 気に入る (to like) is きにいる, not きにはいる.
    if getattr(word.feature, "orthBase", "") == "入る" and prev.surface == "に" and prev2 is not None and prev2.surface == "気":
        kana = _reading(word) or ""
        if kana.startswith("はい"):
            return kana[1:]
    # 開く: ドアが開く is あく (the textbook pair of 開ける); 本を開く keeps ひらく.
    if getattr(word.feature, "orthBase", "") == "開く" and prev.surface == "が":
        kana = _reading(word) or ""
        if kana.startswith("ひら"):
            return "あ" + kana[2:]
    # Polite plural 方 after people: 先生方 せんせいがた, あなた方 あなたがた, 皆様方 みなさまがた.
    if word.surface == "方" and (prev.surface in {"先生", "あなた", "皆様", "様"} or prev.surface.endswith("様")):
        return "がた"
    # 洗濯物 せんたくもの (not ぶつ); the analyzer splits off 物 after these nouns.
    if word.surface == "物" and prev.surface in _MONO_AFTER:
        return "もの"
    # 富士山 is ふじさん (the analyzer splits it and reads 山 as やま). Many other
    # mountains really are 〜やま, so this stays specific.
    if word.surface == "山" and prev.surface == "富士":
        return "さん"
    # Days: 土曜日, 何曜日 -> び; 誕生日 -> たんじょうび; and "noun + 日" days like
    # 収集日, 休館日, 定休日, 記念日 -> び (the analyzer reads them ひ or にち).
    if word.surface == "日" and (prev.surface.endswith("曜") or prev.surface == "誕生" or (
            word.feature.pos1 == "名詞" and prev.feature.pos1 == "名詞"
            and prev.feature.pos2 == "普通名詞" and _KANJI.search(prev.surface[-1]))):
        return "び"
    return None


_SPECIAL_COUNTED = {"二十歳": "はたち"}  # age 20 has its own word

_JUU_AFTER = {"今日", "明日", "今年", "世界", "一晩", "夜", "町", "家"}
_MONO_AFTER = {"洗濯", "忘れ", "落とし", "預かり", "届け", "買い"}
_WEEKDAYS = {"月": "げつ", "火": "か", "水": "すい", "木": "もく", "金": "きん", "土": "ど", "日": "にち"}
_HONORIFIC_FAMILY = {"母": "かあ", "父": "とう", "兄": "にい", "姉": "ねえ"}
_DIGITS = re.compile(r"^[0-9０-９]+$")


def _digit_counter(num: str, counter: str) -> dict | None:
    """The counter after Arabic digits (20分 -> ぷん, 3階 -> がい); the digits get no
    ruby. Words read as a whole (2人 ふたり, 5日 いつか) come back as one word."""
    if not _DIGITS.match(num) or counter not in _COUNTERS:
        return None
    value = int(num.translate(str.maketrans("０１２３４５６７８９", "0123456789")))
    last = value % 10
    ruby = _COUNTERS[counter][last - 1 if last else 9]  # a final 0 sounds like 十 (じゅっぷん)
    if isinstance(ruby, tuple):
        return {"t": counter, "b": counter, "k": ruby[1], "p": "suffix", "parts": [{"t": counter, "r": ruby[1]}]}
    if counter == "日" and value > 10:
        # Dates past the 10th: 20日 はつか, 14日 / 24日 end in よっか, the rest are 〜にち.
        if value == 20:
            return {"t": num + counter, "b": num + counter, "k": "はつか", "p": "noun", "whole": True,
                    "parts": [{"t": num + counter, "r": "はつか"}]}
        ruby = "か" if value % 10 == 4 else "にち"
        return {"t": counter, "b": counter, "k": ruby, "p": "suffix", "parts": [{"t": counter, "r": ruby}]}
    if ruby is None or not 1 <= value <= 10:
        return None  # 1日 is ついたち or いちにち depending on meaning: leave it to the analyzer
    ruby = _COUNTERS[counter][value - 1]
    return {"t": num + counter, "b": num + counter, "k": ruby, "p": "noun", "whole": True,
            "parts": [{"t": num + counter, "r": ruby}]}


def _counter_word(num: str, counter: str, num_reading: str | None = None) -> dict | None:
    if num + counter in _SPECIAL_COUNTED:
        word, reading = num + counter, _SPECIAL_COUNTED[num + counter]
        return {"t": word, "b": word, "k": reading, "p": "noun", "parts": [{"t": word, "r": reading}]}
    if counter not in _COUNTERS:
        return None
    if num in _NUM:
        ruby = _COUNTERS[counter][_NUM.index(num)]
    elif len(num) > 1 and all(c in "一二三四五六七八九十百" for c in num) and num_reading:
        # 三十分: the last digit decides the sound change (さんじゅう + ぷん -> さんじゅっぷん).
        last = _COUNTERS[counter][_NUM.index(num[-1])]
        plain = next((p for p in _DIGIT_READINGS[num[-1]] if num_reading.endswith(p)), None)
        if not isinstance(last, tuple) or plain is None:
            return None
        ruby = (num_reading[: -len(plain)] + last[0], last[1])
    else:
        return None
    if ruby is None:
        return None
    surface = num + counter
    if isinstance(ruby, str):
        return {"t": surface, "b": surface, "k": ruby, "p": "noun", "parts": [{"t": surface, "r": ruby}]}
    return {"t": surface, "b": surface, "k": ruby[0] + ruby[1], "p": "noun",
            "parts": [{"t": num, "r": ruby[0]}, {"t": counter, "r": ruby[1]}]}


def _reading(word) -> str | None:
    if word.surface in _EVERYDAY_READINGS:
        return _EVERYDAY_READINGS[word.surface]
    kana = getattr(word.feature, "kana", None)
    if not kana or kana == "*":
        return None
    return _to_hiragana(kana)


_JAPANESE = re.compile(r"[぀-ヿ㐀-䶿一-鿿々]")

_POS = {
    "名詞": "noun", "代名詞": "pronoun", "動詞": "verb", "形容詞": "i-adjective",
    "形状詞": "na-adjective", "副詞": "adverb", "助詞": "particle", "助動詞": "auxiliary",
    "接尾辞": "suffix", "接頭辞": "prefix", "感動詞": "interjection", "連体詞": "pre-noun",
    "接続詞": "conjunction",
}


def _base(word) -> tuple[str, str | None]:
    """Dictionary form and its reading: 飲み -> (飲む, のむ)."""
    base = getattr(word.feature, "orthBase", None) or word.surface
    if base == "*":
        base = word.surface
    if base in _EVERYDAY_READINGS:
        return base, _EVERYDAY_READINGS[base]
    kana = getattr(word.feature, "kanaBase", None)
    return base, (_to_hiragana(kana) if kana and kana != "*" else None)


def annotate(text: str) -> list[dict]:
    """Split text into plain runs and Japanese words.

    Plain:  {"t": "Hello "}
    Word:   {"t": "飲み", "b": "飲む", "k": "のむ", "p": "verb",
             "parts": [{"t": "飲", "r": "の"}, {"t": "み"}]}   # parts only when it has kanji
    """
    segments: list[dict] = []

    def push_plain(text_: str) -> None:
        # Merge neighbouring plain text so the payload stays small.
        if segments and set(segments[-1]) == {"t"}:
            segments[-1]["t"] += text_
        else:
            segments.append({"t": text_})

    lines = text.split("\n")
    for n, line in enumerate(lines):
        if _JAPANESE.search(line):
            words = list(_tagger()(line))
            skip = False
            for n_word, word in enumerate(words):
                if skip:
                    skip = False
                    continue
                if word.white_space:
                    push_plain(word.white_space)
                surface = word.surface
                following = words[n_word + 1] if n_word + 1 < len(words) else None
                # 十分か(もしれない) is "enough" (じゅうぶん), not ten minutes; the analyzer only splits
                # 十分 into 十 + 分 in this pattern.
                after = words[n_word + 2] if n_word + 2 < len(words) else None
                if surface == "十" and following is not None and following.surface == "分" and after is not None and after.surface == "か":
                    segments.append({"t": "十分", "b": "十分", "k": "じゅうぶん", "p": "na-adjective",
                                     "parts": [{"t": "十分", "r": "じゅうぶん"}]})
                    skip = True
                    continue
                if following is not None and not following.white_space:
                    counted = _counter_word(surface, following.surface, _reading(word))
                    if counted:
                        segments.append(counted)
                        skip = True
                        continue
                    # 1日 after a month (9月1日) is ついたち, the 1st; on its own (1日に3回) it's いちにち.
                    if surface in {"1", "１"} and following.surface == "日":
                        ruby = "ついたち" if n_word and words[n_word - 1].surface == "月" else "いちにち"
                        segments.append({"t": surface + "日", "b": surface + "日", "k": ruby, "p": "noun",
                                         "parts": [{"t": surface + "日", "r": ruby}]})
                        skip = True
                        continue
                    counter = _digit_counter(surface, following.surface)
                    if counter:
                        if not counter.pop("whole", False):
                            push_plain(surface)
                        segments.append(counter)
                        skip = True
                        continue
                # A number + counter the analyzer kept as one word (三本 read as the
                # surname みもと). 十分 is skipped: as one word it usually means "enough".
                if len(surface) == 2 and surface[0] in _NUM and surface[1] in _COUNTERS and surface[1] != "分":
                    counted = _counter_word(surface[0], surface[1])
                    if counted:
                        segments.append(counted)
                        continue
                pos = _POS.get(word.feature.pos1)
                if not pos or not _JAPANESE.search(surface):
                    push_plain(surface)
                    continue
                base, base_kana = _base(word)
                reading = _reading(word) if _KANJI.search(surface) else None
                fixed = _context_reading(words[n_word - 1] if n_word else None, word, following,
                                         words[n_word - 2] if n_word > 1 else None)
                if fixed:
                    reading = base_kana = fixed
                seg = {"t": surface, "b": base, "k": base_kana, "p": pos}
                if reading:
                    seg["parts"] = _split_okurigana(surface, reading)
                segments.append(seg)
        elif line:
            push_plain(line)
        if n < len(lines) - 1:
            push_plain("\n")
    return segments
