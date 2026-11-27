"""Timed JLPT mock tests, one per level, built from verified content only.

A test follows the real JLPT's parts and scoring, at about half the length:

- 言語知識（文字・語彙）: kanji readings, spellings and meanings of words from the
  level's word list (app/words.py), with kanji up to that level
- 言語知識（文法）: hand-written grammar questions (GRAMMAR below), plus particle
  questions from the lessons for N5 and N4
- 読解: passages of the level from app/reading.py
- 聴解: items of the level from app/listening.py, each heard once

N2 and N1 sit the language and reading parts together, as on the real test. The
score report scales each section to the JLPT's points (0-60 or 0-120) and
compares it with the real pass marks. The JLPT equates scores across tests, so
ours is an estimate.

    python -m app.mock             # check the grammar questions and build a test per level
    python -m app.mock --readings  # print the grammar questions' furigana to proofread
"""

from __future__ import annotations

import math
import random
import re
from functools import lru_cache

from . import dictionary, furigana, lessons, listening, quiz, reading, words

LEVELS = ("N5", "N4", "N3", "N2", "N1")

# Each level's timed parts (the real test's minutes in brackets in REAL_MINUTES), how
# many questions of each kind, and how the JLPT scores it.
SPEC = {
    "N5": {"vocab": 14, "grammar": 8, "particles": 4, "listening": 6, "joined": False},
    "N4": {"vocab": 14, "grammar": 8, "particles": 4, "listening": 6, "joined": False},
    "N3": {"vocab": 14, "grammar": 10, "particles": 0, "listening": 7, "joined": False},
    "N2": {"vocab": 14, "grammar": 10, "particles": 0, "listening": 7, "joined": True},
    "N1": {"vocab": 14, "grammar": 10, "particles": 0, "listening": 7, "joined": True},
}
REAL_MINUTES = {  # 言語知識（文字・語彙） / 言語知識（文法）・読解 / 聴解
    "N5": (20, 40, 30), "N4": (25, 55, 35), "N3": (30, 70, 40), "N2": (105, None, 50), "N1": (110, None, 55),
}
# Minutes allowed per question, on top of each passage's own suggested minutes.
VOCAB_MINUTES = 0.6
GRAMMAR_MINUTES = 0.8

# Scored sections: points, and which question groups count toward them.
SCORING = {
    "N5": {"pass": 80, "sections": [("language_reading", "言語知識（文字・語彙・文法）・読解", 120, 38),
                                     ("listening", "聴解", 60, 19)]},
    "N4": {"pass": 90, "sections": [("language_reading", "言語知識（文字・語彙・文法）・読解", 120, 38),
                                     ("listening", "聴解", 60, 19)]},
    "N3": {"pass": 95, "sections": [("language", "言語知識（文字・語彙・文法）", 60, 19), ("reading", "読解", 60, 19),
                                     ("listening", "聴解", 60, 19)]},
    "N2": {"pass": 90, "sections": [("language", "言語知識（文字・語彙・文法）", 60, 19), ("reading", "読解", 60, 19),
                                     ("listening", "聴解", 60, 19)]},
    "N1": {"pass": 100, "sections": [("language", "言語知識（文字・語彙・文法）", 60, 19), ("reading", "読解", 60, 19),
                                      ("listening", "聴解", 60, 19)]},
}
# Question group -> scored section, per scoring style.
_SECTION_OF = {
    "joined": {"vocab": "language_reading", "grammar": "language_reading", "reading": "language_reading",
               "listening": "listening"},
    "split": {"vocab": "language", "grammar": "language", "reading": "reading", "listening": "listening"},
}

GROUP_LABELS = {
    "kanji_reading": ("漢字読み", "Kanji reading"),
    "spelling": ("表記", "Spelling"),
    "meaning": ("語彙", "Word meaning"),
    "grammar": ("文法形式の判断", "Grammar"),
    "particle": ("助詞", "Particles"),
    "reading": ("読解", "Reading"),
    "listening": ("聴解", "Listening"),
}

# ---------------------------------------------------------------------------
# Grammar (文法形式の判断): choose what fits the blank. Hand-written so that exactly
# one choice is right; the distractors are other forms of the level that are wrong
# here in form or meaning.
# ---------------------------------------------------------------------------

GRAMMAR: dict[str, list[dict]] = {
    "N5": [
        {"q": "わたしは毎朝7時（　）おきます。", "choices": ["に", "で", "を", "が"], "answer": 0,
         "why": "A clock time takes に: 7時に (at 7 o'clock)."},
        {"q": "きのう、デパート（　）くつを買いました。", "choices": ["で", "に", "を", "へ"], "answer": 0,
         "why": "The place where an action happens takes で: デパートで買いました (bought at the department store)."},
        {"q": "A「この本は（　）ですか。」B「わたしのです。」", "choices": ["だれの", "だれ", "どれ", "なに"], "answer": 0,
         "why": "B answers わたしの (mine), so A asks whose: だれの本 / だれのですか."},
        {"q": "あした、いっしょに映画を（　）。", "choices": ["見ませんか", "見ました", "見ませんでした", "見ている"],
         "answer": 0, "why": "あした (tomorrow) and いっしょに (together): an invitation, 〜ませんか (won't you...?)."},
        {"q": "へやの中に、ねこが（　）。", "choices": ["います", "あります", "です", "いきます"], "answer": 0,
         "why": "Animals and people take います; things take あります."},
        {"q": "母は今、だいどころで料理を（　）。", "choices": ["しています", "しましょう", "してください", "しませんか"],
         "answer": 0, "why": "今 (now) and an action going on: 〜ています (is cooking)."},
        {"q": "このへやはしずか（　）、きれいです。", "choices": ["で", "くて", "と", "な"], "answer": 0,
         "why": "Joining a な-adjective to the next one: しずかで、きれいです (quiet and clean). くて is for い-adjectives."},
        {"q": "日本語は英語（　）むずかしいですか。", "choices": ["より", "まで", "から", "ほど"], "answer": 0,
         "why": "Comparing: AはBよりむずかしい (A is harder than B). ほど only comes with a negative (英語ほどむずかしくない)."},
        {"q": "ここで写真を（　）もいいですか。", "choices": ["とって", "とる", "とった", "とらない"], "answer": 0,
         "why": "Asking permission: て-form + もいいですか (may I take...?)."},
        {"q": "さむい（　）、まどをしめてください。", "choices": ["から", "が", "けど", "のに"], "answer": 0,
         "why": "Giving a reason: さむいから (because it's cold). が, けど and のに mean \"but\"."},
        {"q": "ここはきんえんです。ここでたばこを（　）ください。", "choices": ["すわないで", "すわなくて", "すわない", "すわないの"],
         "answer": 0, "why": "No smoking here, so a request not to: ない-form + でください (please don't smoke)."},
        {"q": "きのうは、とても（　）です。", "choices": ["さむかった", "さむいでした", "さむくでした", "さむかったでした"],
         "answer": 0, "why": "The past of an い-adjective: さむい → さむかったです. さむいでした is a common mistake."},
        {"q": "この本は、あまりおもしろ（　）ありません。", "choices": ["く", "い", "くて", "かった"], "answer": 0,
         "why": "The negative of an い-adjective: おもしろい → おもしろくありません."},
        {"q": "わたしのへやは、あまり（　）。", "choices": ["ひろくないです", "ひろいです", "ひろかったです", "ひろいでした"],
         "answer": 0, "why": "あまり (not very) needs a negative: ひろくないです (not very big)."},
        {"q": "つくえの上に、本が三さつ（　）。", "choices": ["あります", "います", "です", "あるです"], "answer": 0,
         "why": "Things take あります: 本があります. います is for people and animals."},
        {"q": "A「きのう、なにを（　）か。」B「テレビを見ました。」", "choices": ["しました", "します", "しましょう", "して"],
         "answer": 0, "why": "きのう (yesterday) and B answers in the past (見ました), so A asks in the past: なにをしましたか."},
        {"q": "日曜日、友だちと映画を（　）に行きます。", "choices": ["見", "見る", "見て", "見た"], "answer": 0,
         "why": "Going somewhere to do something: ます-stem + に行きます (見に行きます, go to see)."},
        {"q": "ばんごはんを（　）あとで、しゅくだいをします。", "choices": ["たべた", "たべる", "たべて", "たべ"], "answer": 0,
         "why": "After doing: た-form + あとで (たべたあとで, after eating)."},
        {"q": "ねる（　）、はをみがきます。", "choices": ["まえに", "あとで", "たり", "ながら"], "answer": 0,
         "why": "Before doing: dictionary form + まえに (ねるまえに, before going to bed). あとで needs the た-form."},
        {"q": "わたしは、あたらしいくつが（　）です。", "choices": ["ほしい", "ほしく", "ほしくて", "ほしかって"], "answer": 0,
         "why": "Wanting a thing: 〜がほしいです (I want new shoes)."},
        {"q": "A「どうして、きのう休みましたか。」B「あたまがいたかった（　）です。」", "choices": ["から", "けど", "まで", "ので"],
         "answer": 0, "why": "Answering どうして (why) with a reason: 〜からです (because...). ので can't come before です."},
        {"q": "じゅぎょうは、9時（　）12時までです。", "choices": ["から", "まで", "に", "で"], "answer": 0,
         "why": "From... until: 9時から12時まで."},
        {"q": "わたしは、すしが（　）です。", "choices": ["すき", "すきな", "すきだ", "すきに"], "answer": 0,
         "why": "すき is a な-adjective; before です it has no な: すきです (I like sushi)."},
        {"q": "A「もう、ひるごはんを食べましたか。」B「いいえ、（　）です。」", "choices": ["まだ", "もう", "よく", "とても"],
         "answer": 0, "why": "Not yet: いいえ、まだです. もう means \"already\"."},
        {"q": "わたしは、毎朝コーヒー（　）飲みます。", "choices": ["を", "に", "が", "で"], "answer": 0,
         "why": "The thing you drink is the object, marked with を: コーヒーを飲みます."},
        {"q": "学校へは、いつもバス（　）行きます。", "choices": ["で", "を", "が", "の"], "answer": 0,
         "why": "The means of transport takes で: バスで行きます (go by bus)."},
        {"q": "A「それは（　）の本ですか。」B「日本語の本です。」", "choices": ["なん", "だれ", "どこ", "いつ"], "answer": 0,
         "why": "B says what the book is about (日本語の本), so A asks なんの本 (a book on what?). だれの would ask whose."},
        {"q": "きのうは、どこへも（　）。", "choices": ["行きませんでした", "行きました", "行きます", "行きましょう"], "answer": 0,
         "why": "どこへも (anywhere) goes with a negative verb: どこへも行きませんでした (didn't go anywhere)."},
        {"q": "この店は、安くて（　）です。", "choices": ["おいしい", "おいしく", "おいしくて", "おいしいな"], "answer": 0,
         "why": "安くて links to a second adjective, which ends the sentence in its plain form: 安くておいしいです."},
        {"q": "きょうは、とても（　）天気ですね。", "choices": ["いい", "よく", "よくて", "いいな"], "answer": 0,
         "why": "An い-adjective goes straight before a noun: いい天気 (nice weather)."},
        {"q": "A「なにか食べましたか。」B「いいえ、なにも（　）。」", "choices": ["食べませんでした", "食べました", "食べます", "食べたいです"],
         "answer": 0, "why": "なにも (nothing) needs a negative verb: なにも食べませんでした (I didn't eat anything)."},
        {"q": "山田さんは、せが（　）、かみが長いです。", "choices": ["高くて", "高い", "高いで", "高く"], "answer": 0,
         "why": "To join two descriptions, an い-adjective takes the くて form: せが高くて、かみが長い (tall, with long hair)."},
        {"q": "田中さんは、とても（　）人です。", "choices": ["しんせつな", "しんせつ", "しんせつの", "しんせつに"], "answer": 0,
         "why": "A な-adjective takes な before a noun: しんせつな人 (a kind person)."},
        {"q": "へやを（　）から、出かけます。", "choices": ["そうじして", "そうじする", "そうじした", "そうじし"], "answer": 0,
         "why": "〜てから means \"after doing\": そうじしてから出かけます (I'll go out after cleaning)."},
        {"q": "駅の前（　）、ぎんこうがあります。", "choices": ["に", "を", "で", "へ"], "answer": 0,
         "why": "Where something is, with あります/います, takes に: 駅の前にぎんこうがあります."},
        {"q": "マリアさんは、英語（　）上手です。", "choices": ["が", "を", "に", "で"], "answer": 0,
         "why": "上手 (good at) takes が for the skill: 英語が上手です."},
        {"q": "もう少しゆっくり（　）ください。", "choices": ["話して", "話す", "話した", "話さ"], "answer": 0,
         "why": "Requests use the て-form + ください: 話してください (please speak)."},
        {"q": "A「コーヒーとこうちゃと、（　）がいいですか。」B「コーヒーがいいです。」", "choices": ["どちら", "どれ", "どこ", "だれ"],
         "answer": 0, "why": "Choosing between two things uses どちら. どれ is for three or more."},
        {"q": "電車に（　）、学校へ行きます。", "choices": ["乗って", "乗る", "乗った", "乗ら"], "answer": 0,
         "why": "The て-form links actions in order: 電車に乗って、学校へ行きます (take the train and go to school)."},
        {"q": "きのう買った本は、（　）おもしろかったです。", "choices": ["とても", "あまり", "ぜんぜん", "まだ"], "answer": 0,
         "why": "The sentence is positive, so とても (very). あまり and ぜんぜん need a negative: あまりおもしろくなかった."},
    ],
    "N4": [
        {"q": "わたしは一度、富士山に（　）ことがあります。", "choices": ["のぼった", "のぼる", "のぼって", "のぼり"],
         "answer": 0, "why": "Experience: た-form + ことがあります (I have climbed it once)."},
        {"q": "日曜日は、そうじをし（　）、せんたくをしたりします。", "choices": ["たり", "て", "ながら", "たら"],
         "answer": 0, "why": "〜たり〜たりします lists things you do, and the sentence already has したり."},
        {"q": "あしたテストがあるので、今晩勉強し（　）なりません。", "choices": ["なければ", "なくても", "ないで", "なくて"],
         "answer": 0, "why": "A test tomorrow: 〜なければなりません (I have to study). なくてもいい would mean \"don't have to\" and needs いい."},
        {"q": "わたしは先生に作文を（　）、うれしかったです。", "choices": ["ほめられて", "ほめて", "ほめようと", "ほめるので"],
         "answer": 0, "why": "The teacher praised me: passive, 先生に作文をほめられて (I was praised by the teacher)."},
        {"q": "母は子どもに野菜を（　）。", "choices": ["食べさせました", "食べました", "食べたいです", "食べましょう"],
         "answer": 0, "why": "The mother makes the child eat: causative, 子どもに食べさせました."},
        {"q": "空が暗くなってきました。もうすぐ雨が（　）。", "choices": ["ふりそうです", "ふりたいです", "ふってあげます", "ふりましょう"],
         "answer": 0, "why": "The sky is getting dark, so it looks like rain: ます-stem + そうです."},
        {"q": "友だちがわたしを駅まで車で送って（　）。", "choices": ["くれました", "あげました", "もらいました", "やりました"],
         "answer": 0, "why": "Someone does something for me (わたしを): 〜てくれました. あげる is never toward the speaker."},
        {"q": "音楽を聞き（　）、勉強します。", "choices": ["ながら", "て", "たり", "ば"], "answer": 0,
         "why": "Two things at once: ます-stem + ながら (while listening). 聞きて, 聞きたり and 聞きば aren't forms."},
        {"q": "日本語が話せる（　）、毎日練習しています。", "choices": ["ように", "ために", "そうに", "ことに"],
         "answer": 0, "why": "A goal with a potential verb takes ように: 話せるように (so that I can speak). ために needs a verb of will."},
        {"q": "この薬はとても苦くて、（　）にくいです。", "choices": ["飲み", "飲む", "飲んで", "飲ま"], "answer": 0,
         "why": "Hard to do: ます-stem + にくい (飲みにくい, hard to swallow)."},
        {"q": "時間がないので、タクシーで（　）。", "choices": ["行きましょう", "行ったことがあります", "行ったり", "行かせられます"],
         "answer": 0, "why": "No time, so a suggestion: 行きましょう (let's go by taxi)."},
        {"q": "雨が（　）ば、試合は中止です。", "choices": ["ふれ", "ふら", "ふり", "ふる"], "answer": 0,
         "why": "The conditional ば: ふる → ふれば (if it rains)."},
        {"q": "駅に着い（　）、電話してください。", "choices": ["たら", "たり", "ば", "ながら"], "answer": 0,
         "why": "When/once: た-form + ら (着いたら, when you arrive). 着いば and 着いながら aren't forms."},
        {"q": "この漢字の読み方を（　）いますか。", "choices": ["知って", "知り", "知る", "知った"], "answer": 0,
         "why": "知る (to get to know) is used as 知っています for \"know\"."},
        {"q": "部屋の電気がついて（　）。だれかいるようです。", "choices": ["います", "あります", "おきます", "みます"],
         "answer": 0, "why": "つく is intransitive, so a state takes ている: ついています (the light is on). てある goes with transitive verbs (つけてある)."},
        {"q": "暑いので、窓が開けて（　）。", "choices": ["あります", "います", "みます", "いきます"], "answer": 0,
         "why": "Transitive verb + てある shows the state someone left: 窓が開けてあります (the window has been opened)."},
        {"q": "日本に来て（　）、もう3年になります。", "choices": ["から", "まで", "ので", "ても"], "answer": 0,
         "why": "Since: て-form + から (日本に来てから, since I came to Japan)."},
        {"q": "この料理は、母（　）教えてもらいました。", "choices": ["に", "を", "で", "へ"], "answer": 0,
         "why": "The person who does it for you takes に with 〜てもらう: 母に教えてもらいました (my mother taught me)."},
        {"q": "弟は、毎日遊んで（　）います。", "choices": ["ばかり", "しか", "ほど", "まで"], "answer": 0,
         "why": "Doing nothing but: て-form + ばかりいる (遊んでばかりいます)."},
        {"q": "天気予報（　）、明日は雪だそうです。", "choices": ["によると", "について", "にとって", "として"], "answer": 0,
         "why": "The source of hearsay: 〜によると〜そうです (according to the forecast)."},
        {"q": "このケーキはおいし（　）ですね。", "choices": ["そう", "よう", "らしい", "みたい"], "answer": 0,
         "why": "Looks like: い-adjective without い + そう (おいしそう, looks tasty). よう, らしい and みたい need the full おいしい."},
        {"q": "わたしは、来年日本へ行く（　）です。", "choices": ["つもり", "ながら", "まま", "たり"], "answer": 0,
         "why": "A plan: dictionary form + つもりです (I intend to go)."},
        {"q": "電車の中で、さいふを（　）しまいました。", "choices": ["なくして", "なくし", "なくす", "なくした"], "answer": 0,
         "why": "Something regrettable: て-form + しまいました (I lost my wallet)."},
        {"q": "楽しみにしていたのに、妹にわたしのケーキを（　）。", "choices": ["食べられました", "食べました", "食べたがりました", "食べようとしました"],
         "answer": 0, "why": "Suffering passive: 妹に食べられました (my sister ate it, and I'm upset). The others can't take 妹に."},
        {"q": "この本は、字が大きいので、子どもでも（　）やすいです。", "choices": ["読み", "読む", "読んで", "読ま"], "answer": 0,
         "why": "〜やすい (easy to) follows the ます-stem: 読みやすい (easy to read)."},
        {"q": "雨が（　）も、サッカーの練習はあります。", "choices": ["降って", "降る", "降った", "降ら"], "answer": 0,
         "why": "〜ても means \"even if\": 雨が降っても (even if it rains), practice goes ahead."},
        {"q": "明日は、たぶん雪が（　）でしょう。", "choices": ["降る", "降って", "降り", "降れ"], "answer": 0,
         "why": "でしょう follows the plain form: 雪が降るでしょう (it will probably snow)."},
        {"q": "このアパートでは、ペットを（　）ことができません。", "choices": ["飼う", "飼って", "飼い", "飼った"], "answer": 0,
         "why": "ことができる follows the dictionary form: 飼うことができません (you can't keep pets)."},
        {"q": "試験に合格する（　）、毎日図書館で勉強しています。", "choices": ["ために", "ように", "のに", "ので"], "answer": 0,
         "why": "A goal you act towards with a volitional verb (合格する) takes ために. ように goes with a potential or non-volitional "
                "verb (合格できるように)."},
        {"q": "宿題を（　）、学校へ来てしまいました。", "choices": ["しないで", "しなくて", "しなかった", "しない"], "answer": 0,
         "why": "〜ないで means \"without doing\": 宿題をしないで来てしまった (came without doing the homework)."},
        {"q": "部屋が暗いですね。電気を（　）ましょうか。", "choices": ["つけ", "つく", "つけて", "つい"], "answer": 0,
         "why": "Offering to do something: ます-stem + ましょうか. 電気をつける takes を, so つけましょうか (shall I turn on the light?)."},
        {"q": "「この漢字は、何と（　）んですか。」「『かわ』と読みます。」", "choices": ["読む", "読み", "読んで", "読め"], "answer": 0,
         "why": "〜んですか follows the plain form: 何と読むんですか (how do you read it?)."},
        {"q": "昨日、お酒を飲み（　）、今日は頭が痛いです。", "choices": ["すぎて", "やすくて", "にくくて", "ながら"], "answer": 0,
         "why": "〜すぎる means \"too much\": 飲みすぎて頭が痛い (I drank too much, so my head hurts)."},
        {"q": "子どものとき、よく母に（　）。", "choices": ["しかられました", "しかりました", "しからせました", "しかれました"], "answer": 0,
         "why": "母に + passive: 母にしかられました (I was often scolded by my mother)."},
        {"q": "もし宝くじが（　）、世界旅行をしたいです。", "choices": ["当たったら", "当たって", "当たりながら", "当たるので"],
         "answer": 0, "why": "もし goes with a condition: 当たったら (if I won the lottery)."},
        {"q": "今にも雨が降り（　）ので、かさを持っていきます。", "choices": ["そうな", "そうだ", "ように", "らしい"], "answer": 0,
         "why": "Looks like: ます-stem + そうだ, which becomes そうな before ので: 降りそうなので (as it looks like rain)."},
        {"q": "「そのケーキ、おいしそうですね。」「一つ食べて（　）か。」", "choices": ["みます", "おきます", "あります", "います"],
         "answer": 0, "why": "〜てみる means \"try doing\": 食べてみますか (would you like to try one?)."},
        {"q": "妹は、甘いものが好き（　）、ケーキをよく食べます。", "choices": ["なので", "だので", "なのに", "だけど"], "answer": 0,
         "why": "A な-adjective takes な before ので: 好きなので (because she likes them). なのに and だけど would mean \"although\"."},
        {"q": "この道をまっすぐ行く（　）、駅に着きます。", "choices": ["と", "ので", "のに", "ながら"], "answer": 0,
         "why": "〜と for a natural result: まっすぐ行くと、駅に着きます (go straight and you'll reach the station)."},
        {"q": "夏休みの予定は、まだ決まって（　）。", "choices": ["いません", "ありません", "おきません", "みません"], "answer": 0,
         "why": "決まる (to be decided) + ている describes the state: まだ決まっていません (hasn't been decided yet)."},
    ],
    "N3": [
        {"q": "A「今、電話してもいい？」B「ごめん、今からご飯を食べる（　）なんだ。」", "choices": ["ところ", "うち", "まま", "ほど"],
         "answer": 0, "why": "Just about to do something: dictionary form + ところだ (I'm about to eat)."},
        {"q": "若い（　）、いろいろな国へ行ってみたい。", "choices": ["うちに", "ところに", "最中に", "たびに"],
         "answer": 0, "why": "While a state lasts, before it changes: 若いうちに (while I'm young)."},
        {"q": "弟はゲーム（　）していて、全然勉強しない。", "choices": ["ばかり", "しか", "ほど", "くらい"],
         "answer": 0, "why": "Doing nothing but: ゲームばかりしている. しか would need a negative verb."},
        {"q": "十年も日本に住んでいたんですか。日本語が上手な（　）ですね。", "choices": ["わけ", "ため", "ばかり", "まま"],
         "answer": 0, "why": "Now it makes sense: 上手なわけですね (no wonder you're good)."},
        {"q": "電車が遅れた（　）、会議に間に合わなかった。", "choices": ["せいで", "おかげで", "たびに", "うちに"],
         "answer": 0, "why": "A cause with a bad result: せいで. おかげで is for good results."},
        {"q": "この料理は、作り方（　）味がずいぶん変わる。", "choices": ["によって", "について", "にとって", "として"],
         "answer": 0, "why": "Varies depending on: 作り方によって (depending on how it's made)."},
        {"q": "窓を開けた（　）寝てしまって、風邪をひいた。", "choices": ["まま", "ずに", "ながら", "うちに"], "answer": 0,
         "why": "Left in a state: た-form + まま (with the window left open)."},
        {"q": "この歌を聞く（　）、子供のころを思い出す。", "choices": ["たびに", "うちに", "ところに", "最中に"],
         "answer": 0, "why": "Every time: dictionary form + たびに."},
        {"q": "社長（　）、この計画はとても大切なものだ。", "choices": ["にとって", "によって", "について", "に対して"],
         "answer": 0, "why": "From someone's point of view: 社長にとって (for the company president)."},
        {"q": "説明書の（　）に組み立てたのに、動かない。", "choices": ["とおり", "うち", "ほど", "わけ"], "answer": 0,
         "why": "Just as: 説明書のとおりに (exactly as the manual says)."},
        {"q": "こんな簡単な問題は、子供で（　）できる。", "choices": ["さえ", "しか", "ばかり", "ほど"], "answer": 0,
         "why": "Even: 子供でさえできる (even a child can do it). しか would need a negative."},
        {"q": "医者に、お酒を飲みすぎない（　）言われた。", "choices": ["ように", "ために", "そうに", "ことに"],
         "answer": 0, "why": "Reporting advice or an order: 〜ように言われた (I was told not to drink too much)."},
        {"q": "家を出た（　）、雨が降り出した。", "choices": ["とたん", "うちに", "まま", "最中"], "answer": 0,
         "why": "The moment: た-form + とたん (just as I left the house)."},
        {"q": "会議の（　）に、電話が鳴った。", "choices": ["最中", "とたん", "とおり", "まま"], "answer": 0,
         "why": "Right in the middle of: Nの最中に (in the middle of the meeting)."},
        {"q": "彼は、本当は知っている（　）、教えてくれない。", "choices": ["くせに", "おかげで", "ついでに", "ように"],
         "answer": 0, "why": "Although (with blame): 知っているくせに (even though he knows, he won't tell me)."},
        {"q": "この店は、値段が安い（　）、料理がおいしい。", "choices": ["わりに", "ために", "せいで", "たびに"], "answer": 0,
         "why": "Better than expected for: 安いわりに (for the low price, it's good)."},
        {"q": "練習すれば（　）ほど、上手になる。", "choices": ["する", "した", "して", "しよう"], "answer": 0,
         "why": "The more..., the more: 〜ば〜ほど repeats the verb: すればするほど."},
        {"q": "来月から、大阪の支店で働くことに（　）。会社が決めたので、しかたがない。", "choices": ["なった", "した", "みた", "いた"],
         "answer": 0, "why": "Decided by someone else: ことになった. ことにした is your own decision, but the company decided."},
        {"q": "あの店はいつも込んでいるから、おいしい（　）だ。", "choices": ["はず", "まま", "くせ", "ところ"], "answer": 0,
         "why": "A conclusion from evidence: 〜はずだ (it must be good, since it's always busy)."},
        {"q": "とてもまじめな人だから、彼がそんなことを言う（　）。", "choices": ["わけがない", "はずだ", "ことにする", "ようにする"],
         "answer": 0, "why": "No way: 〜わけがない (he'd never say that). はずだ would mean he's expected to say it."},
        {"q": "お金がない（　）ではないが、今は買いたくない。", "choices": ["わけ", "はず", "こと", "もの"], "answer": 0,
         "why": "Not that: 〜わけではない (it's not that I have no money)."},
        {"q": "子どものころは、よくこの川で泳いだ（　）だ。", "choices": ["もの", "ところ", "まま", "うち"], "answer": 0,
         "why": "Looking back on what you used to do: た-form + ものだ (I often used to swim here)."},
        {"q": "事故の原因（　）、今調べています。", "choices": ["について", "にとって", "によって", "として"], "answer": 0,
         "why": "About, concerning: 原因について調べる (look into the cause)."},
        {"q": "私は留学生（　）、この大学に来ました。", "choices": ["として", "にとって", "について", "に対して"], "answer": 0,
         "why": "In the role of: 留学生として (as an exchange student)."},
        {"q": "病気の父の（　）に、私が会議に出た。", "choices": ["かわり", "まま", "とおり", "ほど"], "answer": 0,
         "why": "Instead of: Nのかわりに (in place of my sick father)."},
        {"q": "コンビニへ行く（　）に、手紙を出してきた。", "choices": ["ついで", "まま", "とおり", "くせ"], "answer": 0,
         "why": "While you're at it: dictionary form + ついでに (on my way to the shop, I also posted a letter)."},
        {"q": "たとえ雨が降って（　）、試合は行われる。", "choices": ["も", "は", "が", "ば"], "answer": 0,
         "why": "Even if: たとえ〜ても (even if it rains)."},
        {"q": "まだ時間はたっぷりあるから、急ぐ（　）はない。", "choices": ["こと", "まま", "ところ", "うち"], "answer": 0,
         "why": "No need to: dictionary form + ことはない (there's no need to hurry)."},
        {"q": "日本の夏は、私の国（　）ずっと暑い。", "choices": ["に比べて", "に対して", "について", "にとって"], "answer": 0,
         "why": "Compared with: 私の国に比べて (compared with my country)."},
        {"q": "このパソコンは、使い方（　）分かれば、だれでも使える。", "choices": ["さえ", "しか", "ほど", "ばかり"], "answer": 0,
         "why": "As long as (only this is needed): 〜さえ〜ば (if you just know how to use it)."},
        {"q": "電車の中では、ほかの人のことを考えて、大きな声で話す（　）。", "choices": ["べきではない", "わけだ", "ところだ", "ばかりだ"],
         "answer": 0, "why": "Shouldn't (a rule of good conduct): dictionary form + べきではない."},
        {"q": "ちょっと寒いので、エアコンの温度を上げる（　）。", "choices": ["ことにした", "わけがない", "はずがない", "ところがない"],
         "answer": 0, "why": "Your own decision: dictionary form + ことにした (I decided to turn the temperature up)."},
    ],
    "N2": [
        {"q": "雨が降っている（　）、試合は予定通り行われた。", "choices": ["にもかかわらず", "からこそ", "次第", "ばかりか"],
         "answer": 0, "why": "Despite: 雨にもかかわらず / 降っているにもかかわらず (even though it was raining)."},
        {"q": "あなたのことを大切に思う（　）、厳しく言うのです。", "choices": ["からこそ", "にもかかわらず", "次第", "つつある"],
         "answer": 0, "why": "Precisely because: 思うからこそ (it's because I care that I'm strict)."},
        {"q": "あんなに練習したのだから、彼は合格する（　）。", "choices": ["に違いない", "ざるを得ない", "一方だ", "にすぎない"],
         "answer": 0, "why": "A confident guess: 〜に違いない (he's sure to pass). 合格するざるを得ない isn't a form."},
        {"q": "準備ができ（　）、すぐに出発します。", "choices": ["次第", "ものの", "うえに", "ばかりか"], "answer": 0,
         "why": "As soon as: ます-stem + 次第 (as soon as we're ready)."},
        {"q": "台風が来たので、旅行を中止せ（　）。", "choices": ["ざるを得なかった", "るにすぎなかった", "つつあった", "ないことはなかった"],
         "answer": 0, "why": "Had no choice but to: する → せざるを得ない. The others don't follow せ."},
        {"q": "この町の人口は、年々減る（　）だ。", "choices": ["一方", "次第", "反面", "うえ"], "answer": 0,
         "why": "Keeps going one way: dictionary form + 一方だ (keeps falling)."},
        {"q": "彼は英語（　）、中国語や韓国語も話せる。", "choices": ["ばかりか", "にもかかわらず", "にすぎず", "に限って"],
         "answer": 0, "why": "Not only... but also: 英語ばかりか中国語も."},
        {"q": "この病気は、子ども（　）大人もかかることがある。", "choices": ["に限らず", "に限って", "にすぎず", "にしては"],
         "answer": 0, "why": "Not limited to: 子どもに限らず大人も (not only children, adults too)."},
        {"q": "社長と言っても、彼は小さな会社の社長（　）。", "choices": ["にすぎない", "ざるを得ない", "一方だ", "次第だ"],
         "answer": 0, "why": "No more than: 〜にすぎない (he's only the head of a small company)."},
        {"q": "この雨が続けば、川の水があふれる（　）。", "choices": ["おそれがある", "次第だ", "反面だ", "にかけてはいる"],
         "answer": 0, "why": "A risk of something bad: dictionary form + おそれがある."},
        {"q": "約束した（　）、必ず守らなければならない。", "choices": ["からには", "ものの", "にしては", "反面"], "answer": 0,
         "why": "Now that, since: 約束したからには (since you promised, you must keep it)."},
        {"q": "初めて作った（　）、このケーキはとてもおいしい。", "choices": ["にしては", "からには", "次第", "上で"],
         "answer": 0, "why": "Considering: 初めて作ったにしては (for a first attempt, it's very good)."},
        {"q": "明日は大事な試験なので、今夜は遊びに行く（　）。", "choices": ["わけにはいかない", "に越したことはない", "にほかならない", "かねない"],
         "answer": 0, "why": "Can't (for social or moral reasons): dictionary form + わけにはいかない. かねない follows the ます-stem."},
        {"q": "彼の話があまりにおかしくて、笑わ（　）。", "choices": ["ずにはいられなかった", "わけにはいかなかった", "ことはなかった", "かねなかった"],
         "answer": 0, "why": "Couldn't help doing: ない-stem + ずにはいられない (笑わずにはいられなかった). The others don't follow 笑わ."},
        {"q": "年をとる（　）、体が弱くなってきた。", "choices": ["につれて", "に先立って", "をめぐって", "にわたって"], "answer": 0,
         "why": "As one thing changes, so does another: dictionary form + につれて (as I get older)."},
        {"q": "契約書をよく読んだ（　）、サインしてください。", "choices": ["上で", "末に", "ものの", "あげく"], "answer": 0,
         "why": "Do A first, then B: た-form + 上で (sign after reading it carefully)."},
        {"q": "3時間も話し合った（　）、やっと結論が出た。", "choices": ["末に", "ものの", "からといって", "に先立って"], "answer": 0,
         "why": "After a long process: た-form + 末に (after three hours of discussion, finally...)."},
        {"q": "お金がある（　）、幸せだとは限らない。", "choices": ["からといって", "からには", "からこそ", "ことから"], "answer": 0,
         "why": "Just because... doesn't mean: 〜からといって〜とは限らない."},
        {"q": "申し訳ありませんが、その意見には賛成し（　）。", "choices": ["かねます", "かねません", "がちです", "ぎみです"],
         "answer": 0, "why": "Politely unable to: ます-stem + かねます (I'm afraid I can't agree). かねません means \"might well\"."},
        {"q": "そんな乱暴な運転をしていたら、事故を起こし（　）よ。", "choices": ["かねない", "かねる", "がたい", "っこない"],
         "answer": 0, "why": "A risk of something bad: ます-stem + かねない (you could well cause an accident). っこない means \"no way\"."},
        {"q": "冬は、どうしても運動不足になり（　）だ。", "choices": ["がち", "っぽい", "げ", "ぶり"], "answer": 0,
         "why": "Tends to (usually something bad): ます-stem + がちだ."},
        {"q": "このあたりは、静か（　）、夜になると車の音がうるさい。", "choices": ["どころか", "ばかりか", "に限らず", "にもかかわらず"],
         "answer": 0, "why": "Far from it, quite the opposite: 静かどころか (far from quiet, it's noisy)."},
        {"q": "社長が来（　）、会議は始められない。", "choices": ["ないことには", "ずにはいられず", "ないわけにはいかず", "ざるをえず"],
         "answer": 0, "why": "Unless A happens, B can't: ない-form + ことには (unless the president comes)."},
        {"q": "材料の量は、人数（　）変えてください。", "choices": ["に応じて", "をめぐって", "にわたって", "に先立って"], "answer": 0,
         "why": "According to, in response to: 人数に応じて (depending on how many people)."},
        {"q": "新しい駅の建設（　）、住民の意見が分かれている。", "choices": ["をめぐって", "に応じて", "につれて", "に沿って"], "answer": 0,
         "why": "Over (a disputed issue): 建設をめぐって (opinions are split over the construction)."},
        {"q": "台風の影響で、東北地方では三日（　）大雨が続いた。", "choices": ["にわたって", "をめぐって", "に応じて", "につれて"],
         "answer": 0, "why": "Over a whole span of time or space: 三日にわたって (for three whole days)."},
        {"q": "留学（　）、日本の文化に興味を持つようになった。", "choices": ["をきっかけに", "にわたって", "にしては", "をめぐって"],
         "answer": 0, "why": "Triggered by: 留学をきっかけに (studying abroad got me interested)."},
        {"q": "あんな難しい試験、ぼくに受かり（　）よ。", "choices": ["っこない", "かねる", "がちだ", "ぎみだ"], "answer": 0,
         "why": "Casual \"no way\": ます-stem + っこない (there's no way I'll pass)."},
        {"q": "体に悪いのだから、たばこはやめる（　）。", "choices": ["に越したことはない", "にほかならない", "にすぎない", "かねない"],
         "answer": 0, "why": "It's best to: dictionary form + に越したことはない (it's best to quit)."},
        {"q": "赤ちゃんは、泣いた（　）、もう笑っている。", "choices": ["かと思うと", "からには", "末に", "上で"], "answer": 0,
         "why": "No sooner... than: た-form + かと思うと (it had barely cried and it's already laughing)."},
        {"q": "店の前の通り（　）、桜の木が植えられている。", "choices": ["に沿って", "に応じて", "をめぐって", "につれて"], "answer": 0,
         "why": "Along: 通りに沿って (along the street)."},
    ],
    "N1": [
        {"q": "この祭りは、この町（　）の伝統行事だ。", "choices": ["ならでは", "ともなると", "をよそに", "といえども"],
         "answer": 0, "why": "Only found here: 町ならではの伝統 (a tradition unique to this town)."},
        {"q": "大学生（　）、自分のことは自分で決めるべきだ。", "choices": ["ともなれば", "ならでは", "をもって", "なり"],
         "answer": 0, "why": "Once someone reaches that stage: 大学生ともなれば (once you're a university student)."},
        {"q": "家族の心配（　）、彼は危険な山へ一人で出かけた。", "choices": ["をよそに", "とあって", "ならではの", "たりとも"],
         "answer": 0, "why": "Ignoring others' feelings: 心配をよそに (paying no attention to his family's worry)."},
        {"q": "子どもは家に帰る（　）、かばんを置いて遊びに行った。", "choices": ["なり", "べく", "まじき", "ずくめ"],
         "answer": 0, "why": "The moment: dictionary form + なり (as soon as he got home)."},
        {"q": "試験に合格す（　）、毎日10時間勉強している。", "choices": ["べく", "なり", "がてら", "ながら"], "answer": 0,
         "why": "In order to: する → すべく (to pass the exam). The others don't follow す."},
        {"q": "一円（　）無駄にはできない。", "choices": ["たりとも", "ならでは", "をもって", "ずくめ"], "answer": 0,
         "why": "Not even one: 一円たりとも (not a single yen), with a negative."},
        {"q": "生徒に暴力をふるうなど、教師にある（　）行為だ。", "choices": ["まじき", "べく", "なり", "ならでは"],
         "answer": 0, "why": "Unbecoming of: あるまじき行為 (conduct unworthy of a teacher)."},
        {"q": "これ（　）、本日の会議を終わります。", "choices": ["をもって", "をよそに", "たりとも", "なり"], "answer": 0,
         "why": "Formal \"with this\": これをもって終わります (with this, the meeting ends)."},
        {"q": "散歩（　）、駅前の本屋に寄った。", "choices": ["がてら", "ずくめ", "まじき", "たりとも"], "answer": 0,
         "why": "While doing one thing, also do another: 散歩がてら (while out for a walk)."},
        {"q": "今日は朝から、いいこと（　）だった。", "choices": ["ずくめ", "がてら", "たりとも", "なり"], "answer": 0,
         "why": "Full of: いいことずくめ (nothing but good things)."},
        {"q": "被害者の話を聞いて、同情を（　）。", "choices": ["禁じ得なかった", "ものともしなかった", "よそにした", "きらいがあった"],
         "answer": 0, "why": "Couldn't help feeling: 同情を禁じ得ない (I can't help feeling sympathy)."},
        {"q": "彼は、物事を悪い方に考える（　）がある。", "choices": ["きらい", "べき", "まじき", "ならでは"], "answer": 0,
         "why": "A (bad) tendency: dictionary form + きらいがある."},
        {"q": "人気歌手が来る（　）、会場には朝から長い列ができた。", "choices": ["とあって", "といえども", "ともなく", "をおいて"],
         "answer": 0, "why": "Because of this special situation: 〜とあって (since a popular singer was coming)."},
        {"q": "彼は、足のけが（　）、最後まで走りきった。", "choices": ["をものともせず", "にひきかえ", "を皮切りに", "に即して"],
         "answer": 0, "why": "Undaunted by: 〜をものともせず (in spite of his injured leg)."},
        {"q": "兄は勉強家だ。それ（　）、弟は遊んでばかりいる。", "choices": ["にひきかえ", "をおいて", "とあって", "ともなると"],
         "answer": 0, "why": "In contrast to: それにひきかえ (by contrast, the younger brother...)."},
        {"q": "このプロジェクトを任せられるのは、彼（　）ほかにいない。", "choices": ["をおいて", "にひきかえ", "をものともせず", "を皮切りに"],
         "answer": 0, "why": "No one but: 〜をおいてほかにいない (there's no one but him)."},
        {"q": "東京公演（　）、全国20都市でコンサートが行われる。", "choices": ["を皮切りに", "をおいて", "にひきかえ", "に足る"],
         "answer": 0, "why": "Starting with: 東京公演を皮切りに (starting with the Tokyo show)."},
        {"q": "子どもたちの幸せを、心から願って（　）。", "choices": ["やみません", "たえません", "至りません", "極まりません"],
         "answer": 0, "why": "Never cease to (wish, hope): て-form + やまない (I sincerely wish)."},
        {"q": "彼のこれまでの仕事ぶりは、十分に信頼する（　）ものだ。", "choices": ["に足る", "とあって", "をおいて", "にひきかえ"],
         "answer": 0, "why": "Worthy of: dictionary form + に足る (worth trusting)."},
        {"q": "客に対するあの店員の態度は、失礼（　）。", "choices": ["極まりない", "ずくめだ", "まみれだ", "がてらだ"], "answer": 0,
         "why": "Extremely: な-adjective + 極まりない (extremely rude)."},
        {"q": "この映画は、見る人の心を動かさ（　）。", "choices": ["ずにはおかない", "ずくめだ", "まじき", "べく"], "answer": 0,
         "why": "Is bound to (cause): ない-stem + ずにはおかない (it can't fail to move people)."},
        {"q": "試験に合格せ（　）、彼は寝る時間も惜しんで勉強した。", "choices": ["んがため", "がてら", "ならでは", "まみれで"],
         "answer": 0, "why": "Formal \"in order to\": ない-stem + んがため (する → せんがため)."},
        {"q": "狭い（　）も、やっと自分の家を持つことができた。", "choices": ["ながら", "とあって", "をおいて", "にひきかえ"],
         "answer": 0, "why": "Although: 狭いながらも (small as it is, I finally have my own house)."},
        {"q": "相手がだれ（　）、失礼な態度は許されない。", "choices": ["であれ", "とあって", "をおいて", "なりに"], "answer": 0,
         "why": "Whoever it may be: だれであれ (no matter who)."},
        {"q": "どんなに反対され（　）、私の決心は変わらない。", "choices": ["ようが", "べく", "なり", "がてら"], "answer": 0,
         "why": "No matter how: volitional + が (どんなに反対されようが)."},
        {"q": "社長（　）、法律を守らなければならない。", "choices": ["といえども", "にひきかえ", "ならでは", "を皮切りに"],
         "answer": 0, "why": "Even (someone like): 社長といえども (even the president must obey the law)."},
        {"q": "このような賞をいただき、光栄（　）です。", "choices": ["の至り", "極まり", "めき", "ずくめ"], "answer": 0,
         "why": "The height of: 光栄の至りです (it's the greatest honour). 極まり needs ない: 光栄極まりない."},
        {"q": "風がやわらかくなり、だんだん春（　）きた。", "choices": ["めいて", "ぶって", "まみれて", "ずくめて"], "answer": 0,
         "why": "Showing signs of: 春めいてきた (it's starting to feel like spring)."},
        {"q": "子どもたちは、泥（　）になって遊んでいた。", "choices": ["まみれ", "ずくめ", "めき", "ぶり"], "answer": 0,
         "why": "Covered all over in (something messy): 泥まみれ (covered in mud)."},
        {"q": "あなたのことを思え（　）、厳しく言うのだ。", "choices": ["ばこそ", "ようが", "なり", "とあって"], "answer": 0,
         "why": "Precisely because: ば-form + こそ (思えばこそ, it's because I care about you)."},
        {"q": "彼は、何を見る（　）、窓の外を眺めていた。", "choices": ["ともなく", "とあって", "といえども", "をおいて"], "answer": 0,
         "why": "Without really meaning to: 〜ともなく (gazing out of the window, not looking at anything in particular)."},
        {"q": "判断は、個人の感情ではなく、事実（　）行わなければならない。", "choices": ["に即して", "をおいて", "にひきかえ", "を皮切りに"],
         "answer": 0, "why": "In line with, based on: 事実に即して (based on the facts)."},
    ],
}

# Reading: a mix like the test's mondai, by passage kind.
_READING_PLAN = {"Short passage": 2, "Medium passage": 1}
_READING_OTHER = 1  # plus one information search, comparison or long passage
LISTENING_ORDER = ("task", "point", "summary", "utterance", "quick", "integrated")

_KANJI = re.compile(r"[㐀-鿿々]")
_HIRAGANA = re.compile(r"^[ぁ-ゖー]+$")
_STOP = {"to", "a", "an", "the", "of", "be", "in", "on", "for", "one", "s", "e", "g", "etc", "something",
         "someone", "with", "and", "or", "as", "at", "by", "up", "out", "do", "get", "make", "take", "have"}


def level_of(test_level: str) -> int:
    return LEVELS.index(test_level)


def known_kanji(level: str) -> set[str] | None:
    from .reading_api import _known_kanji  # the passages' rule: study lists up to the level, plus lesson kanji
    return _known_kanji(level)


# ---------- vocabulary ----------

def _content_words(meaning: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", meaning.lower()) if w not in _STOP and len(w) > 2}


def _vocab_pool(level: str) -> list[dict]:
    known = known_kanji(level)
    pool = []
    for w in words.by_level(level):
        if "～" in w["word"] or not w["entry_id"]:
            continue
        kanji_ok = known is None or all(c in known for c in _KANJI.findall(w["word"]))
        pool.append({**w, "kanji_ok": kanji_ok})
    return pool


def _all_readings(w: dict) -> frozenset[str]:
    return _entry_readings(w["entry_id"]) or frozenset({w["reading"]})


@lru_cache(maxsize=16384)
def _entry_readings(entry_id: int | None) -> frozenset[str]:
    e = dictionary.entry(entry_id) if entry_id else None
    return frozenset(e["readings"]) if e else frozenset()


def _vocab_questions(level: str, count: int) -> list[dict]:
    pool = _vocab_pool(level)
    kanji_words = [w for w in pool if w["kanji_ok"] and _KANJI.search(w["word"]) and _HIRAGANA.match(w["reading"])
                   and len(w["word"]) <= 4]
    random.shuffle(kanji_words)
    plan = [("kanji_reading", round(count * 0.4)), ("spelling", round(count * 0.25))]
    plan.append(("meaning", count - sum(n for _t, n in plan)))
    used: set[str] = set()
    out: list[dict] = []
    for group, n in plan:
        source = kanji_words if group != "meaning" else random.sample(pool, len(pool))
        made = 0
        for w in source:
            if made == n:
                break
            if w["id"] in used:
                continue
            q = {"kanji_reading": _reading_q, "spelling": _spelling_q, "meaning": _meaning_q}[group](w, pool)
            if q:
                used.add(w["id"])
                out.append(q)
                made += 1
    return out


def _reading_q(w: dict, pool: list[dict]) -> dict | None:
    valid = _all_readings(w)
    # ぢ/づ only where the word has them: ぢゅうがっこう is no real-looking mistake.
    misses = [r for r in quiz._near_misses(w["reading"]) if r not in valid
              and not (set("ぢづ") & set(r)) - set(w["reading"])]
    random.shuffle(misses)
    others = [p["reading"] for p in pool if len(p["reading"]) == len(w["reading"]) and p["reading"] not in valid]
    random.shuffle(others)
    distractors = quiz._pick_distractors(w["reading"], misses + others)
    if not distractors:
        return None
    return _choice_q("kanji_reading", {"word": w["word"]}, w["reading"], distractors,
                     f"{w['word']} is read {w['reading']}: {w['meaning']}.", w)


def _spelling_q(w: dict, pool: list[dict]) -> dict | None:
    # Words read the same way would also be right (かわ: 川 and 皮), so they never appear.
    shared = set(_KANJI.findall(w["word"]))
    others = [p for p in pool if p["kanji_ok"] and _KANJI.search(p["word"]) and p["word"] != w["word"]
              and p["reading"] != w["reading"]]
    # Look-alikes first: the same shape (kanji only, or kanji and kana), sharing a kanji, the same length.
    shape = bool(re.search(r"[ぁ-ゖ]", w["word"]))
    others.sort(key=lambda p: (bool(re.search(r"[ぁ-ゖ]", p["word"])) != shape, not (set(p["word"]) & shared),
                               abs(len(p["word"]) - len(w["word"])), random.random()))
    others = [p for p in others[:20] if w["reading"] not in _all_readings(p)]
    distractors = quiz._pick_distractors(w["word"], [p["word"] for p in others[:12]])
    if not distractors:
        return None
    return _choice_q("spelling", {"reading": w["reading"]}, w["word"], distractors,
                     f"{w['reading']} is written {w['word']}: {w['meaning']}.", w)


def _meaning_q(w: dict, pool: list[dict]) -> dict | None:
    mine = _content_words(w["meaning"])
    if not mine:
        return None
    # No wrong answer may share a content word with the right one ("to finish" / "to finish off").
    others = [p["meaning"] for p in pool if p["id"] != w["id"] and not (_content_words(p["meaning"]) & mine)
              and _content_words(p["meaning"])]
    random.shuffle(others)
    distractors = quiz._pick_distractors(w["meaning"], others)
    if not distractors:
        return None
    from .words_api import _ruby_parts
    return _choice_q("meaning", {"word": w["word"], "parts": _ruby_parts(w["word"], w["reading"])}, w["meaning"],
                     distractors, f"{w['word']} ({w['reading']}) means \"{w['meaning']}\".", w)


def _choice_q(group: str, prompt: dict, correct: str, distractors: list[str], why: str, w: dict) -> dict:
    choices = [correct, *distractors]
    random.shuffle(choices)
    return {"group": group, "prompt": prompt, "choices": choices, "answer": choices.index(correct), "why": why,
            "word": {"word": w["word"], "reading": w["reading"], "meaning": w["meaning"]}}


# ---------- grammar ----------

def _freshest(pool: list, n: int, key, seen: dict | None, done: set | None = None) -> list:
    """n items of the pool, least seen in earlier mock tests first, then ones not done in
    practice, random among equals: a learner sees everything before anything repeats."""
    seen, done = seen or {}, done or set()
    return sorted(pool, key=lambda x: (seen.get(key(x), 0), key(x) in done, random.random()))[:n]


def _grammar_questions(level: str, count: int, particles: int, seen: dict | None = None) -> list[dict]:
    out = []
    for g in _freshest(GRAMMAR[level], count, lambda g: g["q"], seen):
        order = list(range(4))
        random.shuffle(order)
        out.append({"group": "grammar", "prompt": {"text": g["q"]}, "choices": [g["choices"][i] for i in order],
                    "answer": order.index(g["answer"]), "why": g["why"]})
    examples = [e for les in lessons.LESSONS if lessons.level(les) == level for e in les["examples"]]
    random.shuffle(examples)
    made = 0
    for ex in examples:
        if made == particles:
            break
        q = quiz._particle_q(ex)
        if q:
            # With the meaning, as in the practice quiz: 母（　）叱られました could take が or に otherwise.
            out.append({"group": "particle", "prompt": {"text": "".join(s["t"] for s in q["prompt"]["segments"]),
                                                        "hint": q["prompt"]["hint"]},
                        "choices": q["choices"], "answer": q["answer"], "why": q["explain"]})
            made += 1
    return out


# ---------- reading and listening ----------

def _passages(level: str, seen: dict | None = None, done: set | None = None) -> list[dict]:
    of_level = [p for p in reading.PASSAGES if reading.level(p) == level]
    pid = lambda p: p["id"]  # noqa: E731
    chosen = []
    for kind, n in _READING_PLAN.items():
        chosen += _freshest([p for p in of_level if p["kind"] == kind], n, pid, seen, done)
    others = [p for p in of_level if p["kind"] not in _READING_PLAN]
    chosen += _freshest(others, _READING_OTHER, pid, seen, done)
    return chosen


def _listening_items(level: str, count: int, seen: dict | None = None, done: set | None = None) -> list[dict]:
    of_level = _freshest([i for i in listening.ITEMS if listening.level(i) == level], 999,
                         lambda i: i["id"], seen, done)
    chosen, kinds = [], set()
    for i in of_level:  # one of each kind first
        if i["kind"] not in kinds:
            chosen.append(i)
            kinds.add(i["kind"])
    chosen = chosen[:count]
    seen = seen or {}
    while len(chosen) < count:  # then the freshest, from the kinds with the most unseen items left
        rest = [i for i in of_level if i not in chosen]
        left = {k: sum(1 for i in rest if i["kind"] == k and not seen.get(i["id"])) for k in kinds}
        chosen.append(min(rest, key=lambda i: (seen.get(i["id"], 0), -left[i["kind"]], rest.index(i))))
    return sorted(chosen, key=lambda i: LISTENING_ORDER.index(i["kind"]))


def seen_in(tests: list[dict]) -> dict[str, int]:
    """How often each passage, listening item and grammar question came up in these
    earlier tests (build()'s dicts), for build(seen=...)."""
    seen: dict[str, int] = {}
    for t in tests:
        keys = t["passages"] + [r["item"] for r in t["listening"]]
        keys += [q["prompt"]["text"] for q in t["grammar"] if q["group"] == "grammar"]
        for k in keys:
            seen[k] = seen.get(k, 0) + 1
    return seen


def fresh_tests(level: str, seen: dict) -> int:
    """How many more tests of this level can be made from passages, listening items and
    grammar questions not met in a mock test yet."""
    passages = [p for p in reading.PASSAGES if reading.level(p) == level and p["id"] not in seen]
    counts = [sum(p["kind"] == kind for p in passages) // n for kind, n in _READING_PLAN.items()]
    counts.append(sum(p["kind"] not in _READING_PLAN for p in passages) // _READING_OTHER)
    items = [i for i in listening.ITEMS if listening.level(i) == level]
    fresh = [i for i in items if i["id"] not in seen]
    per_kind = [sum(i["kind"] == k for i in fresh) for k in {i["kind"] for i in items}]  # each test needs one of each
    counts.append(min([len(fresh) // SPEC[level]["listening"]] + per_kind))
    counts.append(sum(g["q"] not in seen for g in GRAMMAR[level]) // SPEC[level]["grammar"])
    return min(counts)


# ---------- the test ----------

def build(level: str, seen: dict | None = None, done: set | None = None) -> dict:
    """A new test. Answers stay in this dict (stored server-side); public() strips them.
    seen (from seen_in) and done (passage and item ids practised) make it pick the
    content met least so far."""
    spec = SPEC[level]
    vocab = _vocab_questions(level, spec["vocab"])
    grammar = _grammar_questions(level, spec["grammar"], spec["particles"], seen)
    passages = _passages(level, seen, done)
    items = _listening_items(level, spec["listening"], seen, done)

    n = 0
    def qid() -> str:
        nonlocal n
        n += 1
        return f"q{n}"

    for q in vocab + grammar:
        q["id"] = qid()
    reading_qs = [{"id": qid(), "passage": p["id"], "index": i} for p in passages for i in range(len(p["questions"]))]
    listening_qs = [{"id": qid(), "item": i["id"]} for i in items]

    vocab_min = len(vocab) * VOCAB_MINUTES
    grammar_reading_min = len(grammar) * GRAMMAR_MINUTES + sum(p["minutes"] for p in passages)
    parts = []
    if spec["joined"]:
        parts.append({"key": "language_reading", "title": "言語知識（文字・語彙・文法）・読解",
                      "minutes": math.ceil(vocab_min + grammar_reading_min), "groups": ["vocab", "grammar", "reading"]})
    else:
        parts.append({"key": "vocab", "title": "言語知識（文字・語彙）", "minutes": math.ceil(vocab_min), "groups": ["vocab"]})
        parts.append({"key": "grammar_reading", "title": "言語知識（文法）・読解",
                      "minutes": math.ceil(grammar_reading_min), "groups": ["grammar", "reading"]})
    parts.append({"key": "listening", "title": "聴解", "minutes": None, "groups": ["listening"]})
    return {"level": level, "parts": parts, "vocab": vocab, "grammar": grammar,
            "passages": [p["id"] for p in passages], "reading": reading_qs, "listening": listening_qs}


def answer_key(test: dict) -> dict[str, dict]:
    """Question id -> {group, answer, why} for every question of a test."""
    key = {q["id"]: {"group": q["group"], "answer": q["answer"], "why": q["why"], "word": q.get("word")}
           for q in test["vocab"] + test["grammar"]}
    for r in test["reading"]:
        q = reading.get(r["passage"])["questions"][r["index"]]
        key[r["id"]] = {"group": "reading", "answer": q["answer"], "why": q["why"]}
    for r in test["listening"]:
        item = listening.get(r["item"])
        key[r["id"]] = {"group": "listening", "answer": item["answer"], "why": item["why"]}
    return key


def score(test: dict, answers: dict[str, int | None]) -> dict:
    """Raw counts per question group and estimated JLPT section scores."""
    level = test["level"]
    rules = SCORING[level]
    section_of = _SECTION_OF["joined" if level in ("N5", "N4") else "split"]
    key = answer_key(test)
    groups: dict[str, list[int]] = {}
    sections: dict[str, list[int]] = {}
    per_question = {}
    for qid, k in key.items():
        chosen = answers.get(qid)
        ok = chosen == k["answer"]
        per_question[qid] = {"chosen": chosen, "answer": k["answer"], "correct": ok, "why": k["why"]}
        if k.get("word"):
            per_question[qid]["word"] = k["word"]  # so missed words can go into the reviews
        g = groups.setdefault(k["group"], [0, 0])
        g[0] += ok
        g[1] += 1
        family = "grammar" if k["group"] in ("grammar", "particle") else (
            "vocab" if k["group"] in ("kanji_reading", "spelling", "meaning") else k["group"])
        s = sections.setdefault(section_of[family], [0, 0])
        s[0] += ok
        s[1] += 1
    report = []
    for key_name, title, points, minimum in rules["sections"]:
        right, total = sections.get(key_name, [0, 0])
        scaled = round(right / total * points) if total else 0
        report.append({"key": key_name, "title": title, "correct": right, "total": total, "score": scaled,
                       "max": points, "minimum": minimum, "met_minimum": scaled >= minimum})
    total_score = sum(s["score"] for s in report)
    return {
        "questions": per_question,
        "groups": {g: {"correct": c, "total": t} for g, (c, t) in groups.items()},
        "sections": report,
        "score": total_score, "max": sum(s["max"] for s in report), "pass_mark": rules["pass"],
        "passed": total_score >= rules["pass"] and all(s["met_minimum"] for s in report),
        "correct": sum(1 for q in per_question.values() if q["correct"]), "total": len(per_question),
    }


def _check(show_readings: bool = False) -> int:
    problems = []
    for level, qs in GRAMMAR.items():
        need = SPEC[level]["grammar"]
        if len(qs) < need:
            problems.append(f"{level}: {len(qs)} grammar questions, the test needs {need}")
        for g in qs:
            if g["q"].count("（　）") != 1:
                problems.append(f"{level} {g['q']}: needs exactly one blank （　）")
            if len(g["choices"]) != 4 or len(set(g["choices"])) != 4:
                problems.append(f"{level} {g['q']}: needs 4 different choices")
            if not 0 <= g["answer"] < len(g["choices"]):
                problems.append(f"{level} {g['q']}: answer out of range")
            if not g["why"]:
                problems.append(f"{level} {g['q']}: no explanation")
            if show_readings:
                filled = g["q"].replace("（　）", g["choices"][g["answer"]])
                segs = furigana.annotate(filled)
                print(level, "".join(f"{s['t']}({s['k']})" if s.get("parts") else s["t"] for s in segs))
    for level in LEVELS:
        for _ in range(20):  # random builds: every one must be complete
            test = build(level)
            spec = SPEC[level]
            if len(test["vocab"]) != spec["vocab"]:
                problems.append(f"{level}: built {len(test['vocab'])} vocabulary questions, expected {spec['vocab']}")
                break
            if len(test["grammar"]) != spec["grammar"] + spec["particles"]:
                problems.append(f"{level}: built {len(test['grammar'])} grammar questions")
                break
            if len(test["listening"]) != spec["listening"]:
                problems.append(f"{level}: built {len(test['listening'])} listening items")
                break
            for q in test["vocab"] + test["grammar"]:
                if len(set(q["choices"])) != len(q["choices"]):
                    problems.append(f"{level}: repeated choice in {q['choices']}")
        seen: dict[str, int] = {}
        fresh = fresh_tests(level, seen)
        for _ in range(fresh):  # back-to-back tests: nothing comes back while unseen content is left
            used = seen_in([build(level, seen)])
            if set(used) & set(seen):
                problems.append(f"{level}: a passage, item or grammar question repeated within {fresh} tests")
                break
            seen.update(used)
        if fresh < 3:
            problems.append(f"{level}: content for only {fresh} test(s) without repeats, aim for 3")
        t = build(level)
        mins =" + ".join(f"{p['title']} {p['minutes']} min" for p in t["parts"] if p["minutes"])
        print(f"{level}: {len(t['vocab'])} vocabulary, {len(t['grammar'])} grammar, {len(t['reading'])} reading "
              f"({len(t['passages'])} passages), {len(t['listening'])} listening · {mins}")
    print(f"{sum(len(q) for q in GRAMMAR.values())} grammar questions, {len(problems)} problem(s)")
    for p in problems:
        print("  " + p)
    return len(problems)


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(1 if _check("--readings" in sys.argv) else 0)
