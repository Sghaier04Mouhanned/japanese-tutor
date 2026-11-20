"""The N5 lesson path, written by hand so the core content is reliable.

The tutor builds practice sessions on top of this, but the explanations,
example sentences and vocabulary here are the ground truth. Each example has
its full reading in kana so `python -m app.lessons` can cross-check the romaji
and the automatic furigana against it.
"""

from __future__ import annotations

LESSONS: list[dict] = [
    {
        "id": "n5-01",
        "title": "Office greetings",
        "jp_title": "職場のあいさつ",
        "goal": "Greet coworkers correctly from the moment you arrive until you leave.",
        "points": [
            "**おはようございます** (ohayou gozaimasu) is the first greeting of the morning at work. "
            "おはよう alone is casual: friends and family only.",
            "**お疲れ様です** (otsukaresama desu) is the all-purpose office greeting: passing a colleague "
            "in the hallway, starting a call or email to a coworker. It literally means \"you must be tired\", "
            "but it works like \"thanks for your hard work\".",
            "**ありがとうございます** (arigatou gozaimasu) is the polite \"thank you\". "
            "**すみません** (sumimasen) means \"excuse me\" or a light \"sorry\".",
            "**失礼します** (shitsurei shimasu) is said when entering or leaving a room such as an office or "
            "meeting room. When you go home before others, say **お先に失礼します** (osaki ni shitsurei shimasu).",
        ],
        "examples": [
            {"jp": "おはようございます。", "kana": "おはようございます", "romaji": "ohayou gozaimasu", "en": "Good morning."},
            {"jp": "お疲れ様です。", "kana": "おつかれさまです", "romaji": "otsukaresama desu", "en": "Hi! (Thanks for your hard work.)"},
            {"jp": "お先に失礼します。", "kana": "おさきにしつれいします", "romaji": "osaki ni shitsurei shimasu", "en": "Excuse me for leaving before you. (Going home)"},
            {"jp": "お疲れ様でした。", "kana": "おつかれさまでした", "romaji": "otsukaresama deshita", "en": "Thanks for your work today. (Reply when someone leaves)"},
        ],
        "vocab": [
            {"word": "お疲れ様です", "reading": "おつかれさまです", "meaning": "thanks for your hard work (office greeting)"},
            {"word": "失礼します", "reading": "しつれいします", "meaning": "excuse me (entering or leaving a room)"},
            {"word": "お先に", "reading": "おさきに", "meaning": "before (you), ahead of others"},
            {"word": "すみません", "reading": "すみません", "meaning": "excuse me; sorry"},
            {"word": "ありがとうございます", "reading": "ありがとうございます", "meaning": "thank you (polite)"},
        ],
    },
    {
        "id": "n5-02",
        "title": "Introducing yourself",
        "jp_title": "自己紹介",
        "goal": "Give a short, polite self-introduction on your first day.",
        "points": [
            "**はじめまして** (hajimemashite) means \"nice to meet you\", only the first time you meet someone.",
            "**[name]です** means \"I'm [name]\". Japanese usually leaves out 私は (\"I\") when it's obvious.",
            "At work, people introduce themselves with their **family name**.",
            "**よろしくお願いします** (yoroshiku onegai shimasu) ends almost every introduction: "
            "\"I look forward to working with you.\" The reply is **こちらこそ** (kochira koso, \"likewise\").",
        ],
        "examples": [
            {"jp": "はじめまして。スミスです。", "kana": "はじめまして スミスです", "romaji": "hajimemashite. sumisu desu", "en": "Nice to meet you. I'm Smith."},
            {"jp": "よろしくお願いします。", "kana": "よろしくおねがいします", "romaji": "yoroshiku onegai shimasu", "en": "I look forward to working with you."},
            {"jp": "こちらこそ、よろしくお願いします。", "kana": "こちらこそ よろしくおねがいします", "romaji": "kochira koso, yoroshiku onegai shimasu", "en": "Likewise, I look forward to working with you."},
        ],
        "vocab": [
            {"word": "はじめまして", "reading": "はじめまして", "meaning": "nice to meet you (first meeting)"},
            {"word": "よろしくお願いします", "reading": "よろしくおねがいします", "meaning": "I look forward to working with you"},
            {"word": "こちらこそ", "reading": "こちらこそ", "meaning": "likewise; the pleasure is mine"},
            {"word": "名前", "reading": "なまえ", "meaning": "name"},
            {"word": "自己紹介", "reading": "じこしょうかい", "meaning": "self-introduction"},
        ],
    },
    {
        "id": "n5-03",
        "title": "A is B: です",
        "jp_title": "〜は〜です",
        "goal": "Say what someone or something is, and is not.",
        "points": [
            "**AはBです** means \"A is B\". は marks the topic. It's written は but read **wa**.",
            "The negative is **AはBじゃありません** (ja arimasen), \"A is not B\". "
            "ではありません (dewa arimasen) is the more formal version, common in writing.",
            "です never changes for I, you, he, she or they.",
            "Add **さん** (san) after other people's names, like Mr./Ms. Never use it for yourself.",
        ],
        "examples": [
            {"jp": "私は会社員です。", "kana": "わたしはかいしゃいんです", "romaji": "watashi wa kaishain desu", "en": "I'm an office worker."},
            {"jp": "田中さんはエンジニアです。", "kana": "たなかさんはエンジニアです", "romaji": "tanaka san wa enjinia desu", "en": "Ms. Tanaka is an engineer."},
            {"jp": "私は学生じゃありません。", "kana": "わたしはがくせいじゃありません", "romaji": "watashi wa gakusei ja arimasen", "en": "I'm not a student."},
        ],
        "vocab": [
            {"word": "私", "reading": "わたし", "meaning": "I, me"},
            {"word": "会社員", "reading": "かいしゃいん", "meaning": "office worker, company employee"},
            {"word": "学生", "reading": "がくせい", "meaning": "student"},
            {"word": "先生", "reading": "せんせい", "meaning": "teacher"},
            {"word": "社長", "reading": "しゃちょう", "meaning": "company president"},
        ],
    },
    {
        "id": "n5-04",
        "title": "Asking questions with か",
        "jp_title": "〜ですか",
        "goal": "Ask yes/no questions and answer them politely.",
        "points": [
            "Put **か** (ka) at the end of a sentence to make it a question: 田中さんですか。 \"Are you Mr. Tanaka?\"",
            "Answer yes with **はい、そうです** (hai, sou desu): \"Yes, that's right.\" "
            "Answer no with **いいえ、違います** (iie, chigaimasu): \"No, that's not right.\"",
            "Question words: **何** (nan, \"what\") and **誰** (dare, \"who\"). "
            "For \"who\" about someone senior, どなた (donata) is more polite.",
        ],
        "examples": [
            {"jp": "田中さんですか。", "kana": "たなかさんですか", "romaji": "tanaka san desu ka", "en": "Are you Mr. Tanaka?"},
            {"jp": "はい、そうです。", "kana": "はい そうです", "romaji": "hai, sou desu", "en": "Yes, that's right."},
            {"jp": "いいえ、違います。", "kana": "いいえ ちがいます", "romaji": "iie, chigaimasu", "en": "No, that's not right."},
            {"jp": "お名前は何ですか。", "kana": "おなまえはなんですか", "romaji": "onamae wa nan desu ka", "en": "What is your name?"},
        ],
        "vocab": [
            {"word": "はい", "reading": "はい", "meaning": "yes"},
            {"word": "いいえ", "reading": "いいえ", "meaning": "no"},
            {"word": "違います", "reading": "ちがいます", "meaning": "that's not right; is different"},
            {"word": "何", "reading": "なん", "meaning": "what"},
            {"word": "誰", "reading": "だれ", "meaning": "who"},
        ],
    },
    {
        "id": "n5-05",
        "title": "This, that, that over there",
        "jp_title": "これ・それ・あれ",
        "goal": "Point to things around the office.",
        "points": [
            "**これ** = this (near me), **それ** = that (near you), **あれ** = that over there (far from both of us). "
            "**どれ** = which one?",
            "Before a noun, use **この / その / あの / どの**: この資料 \"this document\".",
            "これ・それ・あれ stand alone; この・その・あの always need a noun after them.",
        ],
        "examples": [
            {"jp": "これは名刺です。", "kana": "これはめいしです", "romaji": "kore wa meishi desu", "en": "This is a business card."},
            {"jp": "それは何ですか。", "kana": "それはなんですか", "romaji": "sore wa nan desu ka", "en": "What is that?"},
            {"jp": "あれは会議室です。", "kana": "あれはかいぎしつです", "romaji": "are wa kaigishitsu desu", "en": "That (over there) is the meeting room."},
            {"jp": "この資料はどうですか。", "kana": "このしりょうはどうですか", "romaji": "kono shiryou wa dou desu ka", "en": "How is this document?"},
        ],
        "vocab": [
            {"word": "名刺", "reading": "めいし", "meaning": "business card"},
            {"word": "資料", "reading": "しりょう", "meaning": "documents, materials"},
            {"word": "会議室", "reading": "かいぎしつ", "meaning": "meeting room"},
            {"word": "パソコン", "reading": "パソコン", "meaning": "computer, PC"},
            {"word": "どれ", "reading": "どれ", "meaning": "which one"},
        ],
    },
    {
        "id": "n5-06",
        "title": "Possession with の",
        "jp_title": "〜の〜",
        "goal": "Say whose something is and where people belong.",
        "points": [
            "**AのB** means \"A's B\" or \"B of A\": 私の名刺 \"my business card\".",
            "It also shows where someone belongs: ABC商事のスミスです。 \"I'm Smith from ABC Trading.\"",
            "**誰の** asks \"whose\": これは誰のパソコンですか。",
        ],
        "examples": [
            {"jp": "これは私のパソコンです。", "kana": "これはわたしのパソコンです", "romaji": "kore wa watashi no pasokon desu", "en": "This is my computer."},
            {"jp": "それは誰の傘ですか。", "kana": "それはだれのかさですか", "romaji": "sore wa dare no kasa desu ka", "en": "Whose umbrella is that?"},
            {"jp": "田中さんは私の上司です。", "kana": "たなかさんはわたしのじょうしです", "romaji": "tanaka san wa watashi no joushi desu", "en": "Mr. Tanaka is my boss."},
        ],
        "vocab": [
            {"word": "上司", "reading": "じょうし", "meaning": "boss, superior"},
            {"word": "同僚", "reading": "どうりょう", "meaning": "coworker, colleague"},
            {"word": "電話", "reading": "でんわ", "meaning": "telephone"},
            {"word": "傘", "reading": "かさ", "meaning": "umbrella"},
            {"word": "人", "reading": "ひと", "meaning": "person"},
        ],
    },
    {
        "id": "n5-07",
        "title": "Polite verbs: ます and ません",
        "jp_title": "〜ます・〜ません",
        "goal": "Talk about what you do, will do, and don't do.",
        "points": [
            "Polite verbs end in **ます**: 行きます (ikimasu, go), 来ます (kimasu, come), 帰ります (kaerimasu, go home).",
            "The ます form covers both habits and the future: 会社に行きます = \"I go / I will go to the office\".",
            "The negative is **ません**: 行きません = \"I don't / won't go\". Add か for a question: 行きますか。",
            "に marks where you're going: 会社に行きます. (More about particles in lesson 9.)",
        ],
        "examples": [
            {"jp": "毎日会社に行きます。", "kana": "まいにちかいしゃにいきます", "romaji": "mainichi kaisha ni ikimasu", "en": "I go to the office every day."},
            {"jp": "今日は残業しません。", "kana": "きょうはざんぎょうしません", "romaji": "kyou wa zangyou shimasen", "en": "I won't do overtime today."},
            {"jp": "明日、会社に来ますか。", "kana": "あした かいしゃにきますか", "romaji": "ashita, kaisha ni kimasu ka", "en": "Will you come to the office tomorrow?"},
        ],
        "vocab": [
            {"word": "行きます", "reading": "いきます", "meaning": "to go"},
            {"word": "来ます", "reading": "きます", "meaning": "to come"},
            {"word": "帰ります", "reading": "かえります", "meaning": "to go home, return"},
            {"word": "働きます", "reading": "はたらきます", "meaning": "to work"},
            {"word": "毎日", "reading": "まいにち", "meaning": "every day"},
            {"word": "残業", "reading": "ざんぎょう", "meaning": "overtime work"},
        ],
    },
    {
        "id": "n5-08",
        "title": "Past tense: ました and ませんでした",
        "jp_title": "〜ました・〜ませんでした",
        "goal": "Talk about what you did yesterday or last week.",
        "points": [
            "Change ます to **ました** for the past: 行きました = \"I went\".",
            "Change ません to **ませんでした** for the negative past: 行きませんでした = \"I didn't go\".",
            "Time words: **昨日** (kinou, yesterday), **今日** (kyou, today), **明日** (ashita, tomorrow), "
            "**先週** (senshuu, last week), **来週** (raishuu, next week). These don't take に.",
        ],
        "examples": [
            {"jp": "昨日、残業しました。", "kana": "きのう ざんぎょうしました", "romaji": "kinou, zangyou shimashita", "en": "I did overtime yesterday."},
            {"jp": "先週、大阪に行きました。", "kana": "せんしゅう おおさかにいきました", "romaji": "senshuu, oosaka ni ikimashita", "en": "I went to Osaka last week."},
            {"jp": "昨日は会社に行きませんでした。", "kana": "きのうはかいしゃにいきませんでした", "romaji": "kinou wa kaisha ni ikimasen deshita", "en": "I didn't go to the office yesterday."},
        ],
        "vocab": [
            {"word": "昨日", "reading": "きのう", "meaning": "yesterday"},
            {"word": "今日", "reading": "きょう", "meaning": "today"},
            {"word": "明日", "reading": "あした", "meaning": "tomorrow"},
            {"word": "先週", "reading": "せんしゅう", "meaning": "last week"},
            {"word": "来週", "reading": "らいしゅう", "meaning": "next week"},
            {"word": "会議", "reading": "かいぎ", "meaning": "meeting"},
        ],
    },
    {
        "id": "n5-09",
        "title": "Particles を, に and で",
        "jp_title": "助詞 を・に・で",
        "goal": "Say what you do, where you go, and where or how you do it.",
        "points": [
            "**を** marks the object of a verb: メールを書きます \"I write an email\". It's written を but read **o**.",
            "**に** marks the destination: 会社に行きます. **へ** (read **e**) works the same way with movement verbs.",
            "**で** marks where an action happens: 会社で働きます \"I work at the company\". "
            "It also means \"by means of\": 電車で \"by train\".",
        ],
        "examples": [
            {"jp": "メールを書きます。", "kana": "メールをかきます", "romaji": "meeru o kakimasu", "en": "I write an email."},
            {"jp": "会議室で会議をします。", "kana": "かいぎしつでかいぎをします", "romaji": "kaigishitsu de kaigi o shimasu", "en": "We hold a meeting in the meeting room."},
            {"jp": "電車で会社に来ます。", "kana": "でんしゃでかいしゃにきます", "romaji": "densha de kaisha ni kimasu", "en": "I come to the office by train."},
        ],
        "vocab": [
            {"word": "電車", "reading": "でんしゃ", "meaning": "train"},
            {"word": "駅", "reading": "えき", "meaning": "station"},
            {"word": "書きます", "reading": "かきます", "meaning": "to write"},
            {"word": "読みます", "reading": "よみます", "meaning": "to read"},
            {"word": "します", "reading": "します", "meaning": "to do"},
            {"word": "メール", "reading": "メール", "meaning": "email"},
        ],
    },
    {
        "id": "n5-10",
        "title": "Telling the time",
        "jp_title": "〜時・〜分",
        "goal": "Say and ask what time things happen.",
        "points": [
            "**時** (ji) means o'clock. Watch the irregular ones: 4時 **よじ** (yoji), 7時 **しちじ** (shichiji), "
            "9時 **くじ** (kuji).",
            "**半** (han) means half past: 9時半 = 9:30. Minutes use **分** (fun/pun): 5分 ごふん, 10分 じゅっぷん.",
            "Use **に** for \"at\" a time: 9時に来ます. Ask with **何時** (nanji): 何時ですか。",
            "**から** = from, **まで** = until: 9時から5時まで \"from 9 to 5\".",
        ],
        "examples": [
            {"jp": "今、何時ですか。", "kana": "いま なんじですか", "romaji": "ima, nanji desu ka", "en": "What time is it now?"},
            {"jp": "会議は十時からです。", "kana": "かいぎはじゅうじからです", "romaji": "kaigi wa juuji kara desu", "en": "The meeting is from ten o'clock."},
            {"jp": "毎日九時に会社に来ます。", "kana": "まいにちくじにかいしゃにきます", "romaji": "mainichi kuji ni kaisha ni kimasu", "en": "I come to the office at nine every day."},
            {"jp": "六時半に帰ります。", "kana": "ろくじはんにかえります", "romaji": "rokuji han ni kaerimasu", "en": "I go home at six thirty."},
        ],
        "vocab": [
            {"word": "今", "reading": "いま", "meaning": "now"},
            {"word": "何時", "reading": "なんじ", "meaning": "what time"},
            {"word": "半", "reading": "はん", "meaning": "half (past)"},
            {"word": "午前", "reading": "ごぜん", "meaning": "a.m., morning"},
            {"word": "午後", "reading": "ごご", "meaning": "p.m., afternoon"},
        ],
    },
]

_BY_ID = {lesson["id"]: lesson for lesson in LESSONS}


def get(lesson_id: str) -> dict | None:
    return _BY_ID.get(lesson_id)


def tutor_brief(lesson: dict) -> str:
    """The lesson as instructions for a practice session with Sensei."""
    examples = "\n".join(f"- {e['jp']} ({e['romaji']}) = {e['en']}" for e in lesson["examples"])
    vocab = "\n".join(f"- {v['word']} ({v['reading']}): {v['meaning']}" for v in lesson["vocab"])
    points = "\n".join(f"- {p}" for p in lesson["points"])
    return f"""
## Current lesson: {lesson['title']} ({lesson['jp_title']})
Goal: {lesson['goal']}

Key points (the learner has just read these):
{points}

Verified example sentences (treat these as ground truth):
{examples}

Lesson vocabulary:
{vocab}

## Running this practice session
- Stay on this lesson. Use only its grammar and vocabulary plus anything from earlier, simpler lessons.
- Start with a two-sentence recap, then give ONE exercise at a time: translate English to Japanese, \
fill in a blank, answer a question in Japanese, or pick the right word.
- Wait for the answer, check it, explain briefly, then give the next exercise.
- After about 5 exercises, summarize what went well and what to review, and suggest marking the lesson complete.
"""


if __name__ == "__main__":
    # Consistency check for the hand-written content.
    from . import checks, furigana

    problems = 0
    for lesson in LESSONS:
        for ex in lesson["examples"]:
            expected = checks.kana_to_romaji(ex["kana"])
            if expected is None or checks._canonical(expected) != checks._canonical(ex["romaji"]):
                print(f"{lesson['id']} romaji mismatch: {ex['kana']} -> {expected} vs {ex['romaji']}")
                problems += 1
            reading = "".join(
                "".join(p.get("r", p["t"]) for p in s["parts"]) if s.get("parts") else s["t"]
                for s in furigana.annotate(ex["jp"])
            )
            clean = lambda s: "".join(c for c in s if c not in " 、。！？")  # noqa: E731
            to_hira = lambda s: "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)  # noqa: E731
            if to_hira(clean(reading)) != to_hira(clean(ex["kana"])):
                print(f"{lesson['id']} furigana differs: {ex['jp']} -> {clean(reading)} vs {clean(ex['kana'])}")
                problems += 1
        for v in lesson["vocab"]:
            if checks.kana_to_romaji(v["reading"]) is None:
                print(f"{lesson['id']} vocab reading isn't pure kana: {v['reading']}")
                problems += 1
    print(f"{len(LESSONS)} lessons checked, {problems} problem(s)")
