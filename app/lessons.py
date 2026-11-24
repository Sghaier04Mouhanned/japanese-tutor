"""The JLPT lesson path (N5 to N1), written by hand so the core content is reliable.

The tutor builds practice sessions on top of this, but the explanations,
example sentences and vocabulary here are the ground truth. Each example has
its full reading in kana so `python -m app.lessons` can cross-check the romaji
and the automatic furigana against it.
"""

from __future__ import annotations

LESSONS: list[dict] = [
    {
        "id": "n5-01",
        "title": "Everyday greetings",
        "jp_title": "あいさつ",
        "goal": "Greet people politely at any time of day.",
        "points": [
            "**おはようございます** (ohayou gozaimasu) = good morning. **こんにちは** (konnichiwa) = hello / good afternoon. "
            "**こんばんは** (konbanwa) = good evening.",
            "In こんにちは and こんばんは the final は is read **wa**, just like the topic particle.",
            "**ありがとうございます** (arigatou gozaimasu) is the polite \"thank you\"; ありがとう alone is casual. "
            "**すみません** (sumimasen) means \"excuse me\" or a light \"sorry\".",
            "**さようなら** (sayounara) = goodbye, and **おやすみなさい** (oyasuminasai) = good night.",
        ],
        "examples": [
            {"jp": "おはようございます。", "kana": "おはようございます", "romaji": "ohayou gozaimasu", "en": "Good morning."},
            {"jp": "こんにちは。", "kana": "こんにちは", "romaji": "konnichiwa", "en": "Hello."},
            {"jp": "すみません、ありがとうございます。", "kana": "すみません ありがとうございます", "romaji": "sumimasen, arigatou gozaimasu", "en": "Excuse me, thank you very much."},
            {"jp": "おやすみなさい。", "kana": "おやすみなさい", "romaji": "oyasuminasai", "en": "Good night."},
        ],
        "vocab": [
            {"word": "こんにちは", "reading": "こんにちは", "meaning": "hello, good afternoon"},
            {"word": "こんばんは", "reading": "こんばんは", "meaning": "good evening"},
            {"word": "ありがとうございます", "reading": "ありがとうございます", "meaning": "thank you (polite)"},
            {"word": "すみません", "reading": "すみません", "meaning": "excuse me; sorry"},
            {"word": "さようなら", "reading": "さようなら", "meaning": "goodbye"},
        ],
    },
    {
        "id": "n5-02",
        "title": "Introducing yourself",
        "jp_title": "自己紹介",
        "goal": "Give a short, polite self-introduction.",
        "points": [
            "**はじめまして** (hajimemashite) means \"nice to meet you\", only the first time you meet someone.",
            "**[name]です** means \"I'm [name]\". Japanese usually leaves out 私は (\"I\") when it's obvious.",
            "Country + **人** (jin) gives the nationality: アメリカ人 (amerikajin), 日本人 (nihonjin). "
            "**[country]から来ました** (kara kimashita) means \"I'm from [country]\".",
            "**よろしくお願いします** (yoroshiku onegai shimasu) ends almost every introduction, a bit like "
            "\"pleased to meet you\". The reply is **こちらこそ** (kochira koso, \"likewise\").",
        ],
        "examples": [
            {"jp": "はじめまして。スミスです。", "kana": "はじめまして スミスです", "romaji": "hajimemashite. sumisu desu", "en": "Nice to meet you. I'm Smith."},
            {"jp": "アメリカから来ました。", "kana": "アメリカからきました", "romaji": "amerika kara kimashita", "en": "I'm from America."},
            {"jp": "よろしくお願いします。", "kana": "よろしくおねがいします", "romaji": "yoroshiku onegai shimasu", "en": "Pleased to meet you."},
            {"jp": "こちらこそ、よろしくお願いします。", "kana": "こちらこそ よろしくおねがいします", "romaji": "kochira koso, yoroshiku onegai shimasu", "en": "Likewise, pleased to meet you."},
        ],
        "vocab": [
            {"word": "はじめまして", "reading": "はじめまして", "meaning": "nice to meet you (first meeting)"},
            {"word": "よろしくお願いします", "reading": "よろしくおねがいします", "meaning": "pleased to meet you; please treat me well"},
            {"word": "こちらこそ", "reading": "こちらこそ", "meaning": "likewise; the pleasure is mine"},
            {"word": "名前", "reading": "なまえ", "meaning": "name"},
            {"word": "国", "reading": "くに", "meaning": "country"},
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
            "ではありません (dewa arimasen) is the more formal version, common in writing and on the test.",
            "です never changes for I, you, he, she or they.",
            "Add **さん** (san) after other people's names, like Mr./Ms. Never use it for yourself.",
        ],
        "examples": [
            {"jp": "私は学生です。", "kana": "わたしはがくせいです", "romaji": "watashi wa gakusei desu", "en": "I'm a student."},
            {"jp": "田中さんは先生です。", "kana": "たなかさんはせんせいです", "romaji": "tanaka san wa sensei desu", "en": "Ms. Tanaka is a teacher."},
            {"jp": "私は日本人じゃありません。", "kana": "わたしはにほんじんじゃありません", "romaji": "watashi wa nihonjin ja arimasen", "en": "I'm not Japanese."},
        ],
        "vocab": [
            {"word": "私", "reading": "わたし", "meaning": "I, me"},
            {"word": "学生", "reading": "がくせい", "meaning": "student"},
            {"word": "先生", "reading": "せんせい", "meaning": "teacher"},
            {"word": "日本人", "reading": "にほんじん", "meaning": "Japanese person"},
            {"word": "医者", "reading": "いしゃ", "meaning": "doctor"},
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
            "For \"who\" about someone you should be polite to, どなた (donata) is more polite.",
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
        "goal": "Point to things and ask what they are or what they cost.",
        "points": [
            "**これ** = this (near me), **それ** = that (near you), **あれ** = that over there (far from both of us). "
            "**どれ** = which one?",
            "Before a noun, use **この / その / あの / どの**: この本 \"this book\".",
            "これ・それ・あれ stand alone; この・その・あの always need a noun after them.",
            "**いくら** (ikura) asks the price: これはいくらですか。 \"How much is this?\"",
        ],
        "examples": [
            {"jp": "これは本です。", "kana": "これはほんです", "romaji": "kore wa hon desu", "en": "This is a book."},
            {"jp": "それは何ですか。", "kana": "それはなんですか", "romaji": "sore wa nan desu ka", "en": "What is that?"},
            {"jp": "あれは駅です。", "kana": "あれはえきです", "romaji": "are wa eki desu", "en": "That (over there) is the station."},
            {"jp": "この時計はいくらですか。", "kana": "このとけいはいくらですか", "romaji": "kono tokei wa ikura desu ka", "en": "How much is this watch?"},
        ],
        "vocab": [
            {"word": "本", "reading": "ほん", "meaning": "book"},
            {"word": "駅", "reading": "えき", "meaning": "station"},
            {"word": "時計", "reading": "とけい", "meaning": "watch, clock"},
            {"word": "辞書", "reading": "じしょ", "meaning": "dictionary"},
            {"word": "いくら", "reading": "いくら", "meaning": "how much (price)"},
        ],
    },
    {
        "id": "n5-06",
        "title": "Possession with の",
        "jp_title": "〜の〜",
        "goal": "Say whose something is and what kind it is.",
        "points": [
            "**AのB** means \"A's B\" or \"B of A\": 私の本 \"my book\".",
            "It also describes what kind of thing B is: 日本語の本 \"a Japanese-language book\", "
            "日本語の先生 \"a Japanese teacher\".",
            "**誰の** asks \"whose\": これは誰の傘ですか。",
        ],
        "examples": [
            {"jp": "これは私の本です。", "kana": "これはわたしのほんです", "romaji": "kore wa watashi no hon desu", "en": "This is my book."},
            {"jp": "それは誰の傘ですか。", "kana": "それはだれのかさですか", "romaji": "sore wa dare no kasa desu ka", "en": "Whose umbrella is that?"},
            {"jp": "山田さんは日本語の先生です。", "kana": "やまださんはにほんごのせんせいです", "romaji": "yamada san wa nihongo no sensei desu", "en": "Mr. Yamada is a Japanese teacher."},
        ],
        "vocab": [
            {"word": "日本語", "reading": "にほんご", "meaning": "Japanese (language)"},
            {"word": "友達", "reading": "ともだち", "meaning": "friend"},
            {"word": "傘", "reading": "かさ", "meaning": "umbrella"},
            {"word": "電話", "reading": "でんわ", "meaning": "telephone"},
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
            "The ます form covers both habits and the future: 学校に行きます = \"I go / I will go to school\".",
            "The negative is **ません**: 行きません = \"I don't / won't go\". Add か for a question: 行きますか。",
            "に marks where you're going: 学校に行きます. (More about particles in lesson 9.)",
        ],
        "examples": [
            {"jp": "毎日学校に行きます。", "kana": "まいにちがっこうにいきます", "romaji": "mainichi gakkou ni ikimasu", "en": "I go to school every day."},
            {"jp": "土曜日は勉強しません。", "kana": "どようびはべんきょうしません", "romaji": "doyoubi wa benkyou shimasen", "en": "I don't study on Saturdays."},
            {"jp": "明日、来ますか。", "kana": "あした きますか", "romaji": "ashita, kimasu ka", "en": "Will you come tomorrow?"},
        ],
        "vocab": [
            {"word": "行きます", "reading": "いきます", "meaning": "to go"},
            {"word": "来ます", "reading": "きます", "meaning": "to come"},
            {"word": "帰ります", "reading": "かえります", "meaning": "to go home, return"},
            {"word": "勉強します", "reading": "べんきょうします", "meaning": "to study"},
            {"word": "毎日", "reading": "まいにち", "meaning": "every day"},
            {"word": "学校", "reading": "がっこう", "meaning": "school"},
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
            {"jp": "昨日、勉強しました。", "kana": "きのう べんきょうしました", "romaji": "kinou, benkyou shimashita", "en": "I studied yesterday."},
            {"jp": "先週、京都に行きました。", "kana": "せんしゅう きょうとにいきました", "romaji": "senshuu, kyouto ni ikimashita", "en": "I went to Kyoto last week."},
            {"jp": "昨日は学校に行きませんでした。", "kana": "きのうはがっこうにいきませんでした", "romaji": "kinou wa gakkou ni ikimasen deshita", "en": "I didn't go to school yesterday."},
        ],
        "vocab": [
            {"word": "昨日", "reading": "きのう", "meaning": "yesterday"},
            {"word": "今日", "reading": "きょう", "meaning": "today"},
            {"word": "明日", "reading": "あした", "meaning": "tomorrow"},
            {"word": "先週", "reading": "せんしゅう", "meaning": "last week"},
            {"word": "来週", "reading": "らいしゅう", "meaning": "next week"},
            {"word": "週末", "reading": "しゅうまつ", "meaning": "weekend"},
        ],
    },
    {
        "id": "n5-09",
        "title": "Particles を, に and で",
        "jp_title": "助詞 を・に・で",
        "goal": "Say what you do, where you go, and where or how you do it.",
        "points": [
            "**を** marks the object of a verb: 本を読みます \"I read a book\". It's written を but read **o**.",
            "**に** marks the destination: 学校に行きます. **へ** (read **e**) works the same way with movement verbs.",
            "**で** marks where an action happens: 図書館で勉強します \"I study at the library\". "
            "It also means \"by means of\": 電車で \"by train\".",
        ],
        "examples": [
            {"jp": "本を読みます。", "kana": "ほんをよみます", "romaji": "hon o yomimasu", "en": "I read a book."},
            {"jp": "図書館で勉強します。", "kana": "としょかんでべんきょうします", "romaji": "toshokan de benkyou shimasu", "en": "I study at the library."},
            {"jp": "電車で学校に来ます。", "kana": "でんしゃでがっこうにきます", "romaji": "densha de gakkou ni kimasu", "en": "I come to school by train."},
        ],
        "vocab": [
            {"word": "電車", "reading": "でんしゃ", "meaning": "train"},
            {"word": "図書館", "reading": "としょかん", "meaning": "library"},
            {"word": "書きます", "reading": "かきます", "meaning": "to write"},
            {"word": "読みます", "reading": "よみます", "meaning": "to read"},
            {"word": "飲みます", "reading": "のみます", "meaning": "to drink"},
            {"word": "します", "reading": "します", "meaning": "to do"},
        ],
    },
    {
        "id": "n5-10",
        "title": "Telling the time",
        "jp_title": "〜時・〜分",
        "goal": "Say and ask what time things happen.",
        "points": [
            "**時** (ji) means o'clock. Watch the irregular ones, a JLPT favourite: 4時 **よじ** (yoji), "
            "7時 **しちじ** (shichiji), 9時 **くじ** (kuji).",
            "**半** (han) means half past: 9時半 = 9:30. Minutes use **分** (fun/pun): 5分 ごふん, 10分 じゅっぷん.",
            "Use **に** for \"at\" a time: 7時に起きます. Ask with **何時** (nanji): 何時ですか。",
            "**から** = from, **まで** = until: 9時から5時まで \"from 9 to 5\".",
        ],
        "examples": [
            {"jp": "今、何時ですか。", "kana": "いま なんじですか", "romaji": "ima, nanji desu ka", "en": "What time is it now?"},
            {"jp": "銀行は九時からです。", "kana": "ぎんこうはくじからです", "romaji": "ginkou wa kuji kara desu", "en": "The bank is open from nine o'clock."},
            {"jp": "毎日七時に起きます。", "kana": "まいにちしちじにおきます", "romaji": "mainichi shichiji ni okimasu", "en": "I get up at seven every day."},
            {"jp": "六時半に帰ります。", "kana": "ろくじはんにかえります", "romaji": "rokuji han ni kaerimasu", "en": "I go home at six thirty."},
        ],
        "vocab": [
            {"word": "今", "reading": "いま", "meaning": "now"},
            {"word": "何時", "reading": "なんじ", "meaning": "what time"},
            {"word": "半", "reading": "はん", "meaning": "half (past)"},
            {"word": "起きます", "reading": "おきます", "meaning": "to get up, wake up"},
            {"word": "午前", "reading": "ごぜん", "meaning": "a.m., morning"},
            {"word": "午後", "reading": "ごご", "meaning": "p.m., afternoon"},
        ],
    },
    {
        "id": "n5-11",
        "title": "い-adjectives",
        "jp_title": "い形容詞",
        "goal": "Describe things as big, cheap, delicious, cold...",
        "points": [
            "**い-adjectives** end in い: 高い (takai, expensive / tall), 安い (yasui, cheap), "
            "大きい (ookii, big), 小さい (chiisai, small), おいしい (oishii, delicious).",
            "Put them before a noun, 高い時計 \"an expensive watch\", or at the end with です: この時計は高いです。",
            "Negative: drop the final い and add **くないです**: 高い → 高くないです \"not expensive\".",
            "**いい** (good) is irregular: its negative is **よくないです**.",
        ],
        "examples": [
            {"jp": "この本は高いです。", "kana": "このほんはたかいです", "romaji": "kono hon wa takai desu", "en": "This book is expensive."},
            {"jp": "東京は大きいです。", "kana": "とうきょうはおおきいです", "romaji": "toukyou wa ookii desu", "en": "Tokyo is big."},
            {"jp": "このカレーはおいしいです。", "kana": "このカレーはおいしいです", "romaji": "kono karee wa oishii desu", "en": "This curry is delicious."},
            {"jp": "今日は寒くないです。", "kana": "きょうはさむくないです", "romaji": "kyou wa samuku nai desu", "en": "It isn't cold today."},
        ],
        "vocab": [
            {"word": "高い", "reading": "たかい", "meaning": "expensive; tall, high"},
            {"word": "安い", "reading": "やすい", "meaning": "cheap"},
            {"word": "大きい", "reading": "おおきい", "meaning": "big"},
            {"word": "小さい", "reading": "ちいさい", "meaning": "small"},
            {"word": "おいしい", "reading": "おいしい", "meaning": "delicious"},
            {"word": "寒い", "reading": "さむい", "meaning": "cold (weather)"},
        ],
    },
    {
        "id": "n5-12",
        "title": "な-adjectives",
        "jp_title": "な形容詞",
        "goal": "Use adjectives like quiet, pretty and famous, and say what you like.",
        "points": [
            "Some adjectives need **な** before a noun: きれいな花 (kirei na hana, a pretty flower), "
            "静かな部屋 (shizuka na heya, a quiet room).",
            "At the end of a sentence there's no な: この部屋は静かです。",
            "The negative works like a noun: **じゃありません**: 静かじゃありません \"not quiet\".",
            "**きれい** ends in い but is a な-adjective, a classic JLPT trap.",
            "**好き** (suki, liked) is a な-adjective too. The thing you like takes **が**: 私はコーヒーが好きです。",
        ],
        "examples": [
            {"jp": "この部屋は静かです。", "kana": "このへやはしずかです", "romaji": "kono heya wa shizuka desu", "en": "This room is quiet."},
            {"jp": "きれいな花です。", "kana": "きれいなはなです", "romaji": "kirei na hana desu", "en": "It's a pretty flower."},
            {"jp": "私は日本の音楽が好きです。", "kana": "わたしはにほんのおんがくがすきです", "romaji": "watashi wa nihon no ongaku ga suki desu", "en": "I like Japanese music."},
            {"jp": "この町は有名じゃありません。", "kana": "このまちはゆうめいじゃありません", "romaji": "kono machi wa yuumei ja arimasen", "en": "This town isn't famous."},
        ],
        "vocab": [
            {"word": "静か", "reading": "しずか", "meaning": "quiet"},
            {"word": "きれい", "reading": "きれい", "meaning": "pretty; clean"},
            {"word": "好き", "reading": "すき", "meaning": "liked (to like)"},
            {"word": "有名", "reading": "ゆうめい", "meaning": "famous"},
            {"word": "元気", "reading": "げんき", "meaning": "healthy, energetic"},
            {"word": "部屋", "reading": "へや", "meaning": "room"},
        ],
    },
    {
        "id": "n5-13",
        "title": "There is: あります and います",
        "jp_title": "あります・います",
        "goal": "Say what is where, for things and for living beings.",
        "points": [
            "**あります** = there is (things and plants): 本があります。 **います** = there is (people and animals): 猫がいます。",
            "What exists takes **が**, the place takes **に**: 机の上に本があります。 \"There is a book on the desk.\"",
            "Position words: **上** (ue, on / above), **下** (shita, under), **中** (naka, inside), "
            "**前** (mae, in front), **後ろ** (ushiro, behind). Join them with の: 机の下 \"under the desk\".",
            "Negative: **ありません** / **いません**.",
        ],
        "examples": [
            {"jp": "机の上に本があります。", "kana": "つくえのうえにほんがあります", "romaji": "tsukue no ue ni hon ga arimasu", "en": "There is a book on the desk."},
            {"jp": "部屋に猫がいます。", "kana": "へやにねこがいます", "romaji": "heya ni neko ga imasu", "en": "There is a cat in the room."},
            {"jp": "かばんの中に何がありますか。", "kana": "かばんのなかになにがありますか", "romaji": "kaban no naka ni nani ga arimasu ka", "en": "What is in the bag?"},
            {"jp": "教室に先生がいません。", "kana": "きょうしつにせんせいがいません", "romaji": "kyoushitsu ni sensei ga imasen", "en": "The teacher isn't in the classroom."},
        ],
        "vocab": [
            {"word": "机", "reading": "つくえ", "meaning": "desk"},
            {"word": "猫", "reading": "ねこ", "meaning": "cat"},
            {"word": "上", "reading": "うえ", "meaning": "on, above, top"},
            {"word": "下", "reading": "した", "meaning": "under, below"},
            {"word": "中", "reading": "なか", "meaning": "inside, in"},
            {"word": "後ろ", "reading": "うしろ", "meaning": "behind, back"},
        ],
    },
    {
        "id": "n5-14",
        "title": "Here, there, where",
        "jp_title": "ここ・そこ・あそこ・どこ",
        "goal": "Ask where places and people are, and point to them.",
        "points": [
            "**ここ** = here, **そこ** = there (near you), **あそこ** = over there, **どこ** = where? "
            "Same pattern as これ・それ・あれ・どれ.",
            "Ask where something is with **〜はどこですか**: トイレはどこですか。 Answer: あそこです。",
            "For people you can also say **どこにいますか**: 田中さんはどこにいますか。",
            "Shops and stations use the politer **こちら / そちら / あちら / どちら**.",
        ],
        "examples": [
            {"jp": "すみません、トイレはどこですか。", "kana": "すみません トイレはどこですか", "romaji": "sumimasen, toire wa doko desu ka", "en": "Excuse me, where is the toilet?"},
            {"jp": "駅はあそこです。", "kana": "えきはあそこです", "romaji": "eki wa asoko desu", "en": "The station is over there."},
            {"jp": "田中さんはどこにいますか。", "kana": "たなかさんはどこにいますか", "romaji": "tanaka san wa doko ni imasu ka", "en": "Where is Mr. Tanaka?"},
            {"jp": "ここは図書館です。", "kana": "ここはとしょかんです", "romaji": "koko wa toshokan desu", "en": "This is the library. (Here is the library.)"},
        ],
        "vocab": [
            {"word": "ここ", "reading": "ここ", "meaning": "here"},
            {"word": "そこ", "reading": "そこ", "meaning": "there (near you)"},
            {"word": "あそこ", "reading": "あそこ", "meaning": "over there"},
            {"word": "どこ", "reading": "どこ", "meaning": "where"},
            {"word": "トイレ", "reading": "トイレ", "meaning": "toilet, restroom"},
            {"word": "教室", "reading": "きょうしつ", "meaning": "classroom"},
        ],
    },
    {
        "id": "n5-15",
        "title": "Wanting: たい and ほしい",
        "jp_title": "〜たい・ほしい",
        "goal": "Say what you want to do and what you want to have.",
        "points": [
            "To want to do something, replace ます with **たいです**: 飲みます → 飲みたいです \"I want to drink\".",
            "Its negative is **たくないです**: 行きたくないです \"I don't want to go\". The object can take が or を.",
            "To want a thing, use **ほしいです** with が: 新しいかばんがほしいです。",
            "These describe your own wishes. Asking a teacher or a stranger 〜たいですか directly can sound pushy.",
        ],
        "examples": [
            {"jp": "水が飲みたいです。", "kana": "みずがのみたいです", "romaji": "mizu ga nomitai desu", "en": "I want to drink some water."},
            {"jp": "日本に行きたいです。", "kana": "にほんにいきたいです", "romaji": "nihon ni ikitai desu", "en": "I want to go to Japan."},
            {"jp": "新しいかばんがほしいです。", "kana": "あたらしいかばんがほしいです", "romaji": "atarashii kaban ga hoshii desu", "en": "I want a new bag."},
            {"jp": "今日は何もしたくないです。", "kana": "きょうはなにもしたくないです", "romaji": "kyou wa nani mo shitaku nai desu", "en": "I don't want to do anything today."},
        ],
        "vocab": [
            {"word": "水", "reading": "みず", "meaning": "water"},
            {"word": "かばん", "reading": "かばん", "meaning": "bag"},
            {"word": "新しい", "reading": "あたらしい", "meaning": "new"},
            {"word": "ほしい", "reading": "ほしい", "meaning": "wanted (I want)"},
            {"word": "買います", "reading": "かいます", "meaning": "to buy"},
            {"word": "旅行", "reading": "りょこう", "meaning": "travel, trip"},
        ],
    },
    {
        "id": "n5-16",
        "title": "Requests: てください",
        "jp_title": "〜てください",
        "goal": "Ask someone politely to do something.",
        "points": [
            "**[verb て-form] + ください** = please do ...: 待ってください \"please wait\".",
            "The て-form follows rules by verb group that take practice. Start with these: 待ちます → 待って, "
            "見ます → 見て, 書きます → 書いて, 話します → 話して, 来ます → 来て, します → して.",
            "**ちょっと** (chotto, a little) softens a request: ちょっと待ってください。",
            "To ask for a thing, use **[noun]をください**: コーヒーをください。",
        ],
        "examples": [
            {"jp": "ちょっと待ってください。", "kana": "ちょっとまってください", "romaji": "chotto matte kudasai", "en": "Please wait a moment."},
            {"jp": "ここに名前を書いてください。", "kana": "ここになまえをかいてください", "romaji": "koko ni namae o kaite kudasai", "en": "Please write your name here."},
            {"jp": "ゆっくり話してください。", "kana": "ゆっくりはなしてください", "romaji": "yukkuri hanashite kudasai", "en": "Please speak slowly."},
            {"jp": "コーヒーをください。", "kana": "コーヒーをください", "romaji": "koohii o kudasai", "en": "A coffee, please."},
        ],
        "vocab": [
            {"word": "待ちます", "reading": "まちます", "meaning": "to wait"},
            {"word": "話します", "reading": "はなします", "meaning": "to speak, talk"},
            {"word": "見ます", "reading": "みます", "meaning": "to see, watch, look"},
            {"word": "ください", "reading": "ください", "meaning": "please (give / do)"},
            {"word": "ちょっと", "reading": "ちょっと", "meaning": "a little; a moment"},
            {"word": "ゆっくり", "reading": "ゆっくり", "meaning": "slowly"},
        ],
    },
    {
        "id": "n5-17",
        "title": "Invitations: ませんか and ましょう",
        "jp_title": "〜ませんか・〜ましょう",
        "goal": "Invite someone, and accept or decline politely.",
        "points": [
            "**〜ませんか** (\"won't you ...?\") is the polite way to invite: 一緒に映画を見ませんか。",
            "**〜ましょう** = \"let's ...\": 見ましょう。 It's also a common way to accept.",
            "Accept with **いいですね** (that sounds good). Decline with **すみません、ちょっと…**: "
            "trailing off is normal and polite.",
            "**一緒に** (issho ni) = together.",
        ],
        "examples": [
            {"jp": "一緒に映画を見ませんか。", "kana": "いっしょにえいがをみませんか", "romaji": "issho ni eiga o mimasen ka", "en": "Would you like to watch a movie together?"},
            {"jp": "いいですね。見ましょう。", "kana": "いいですね みましょう", "romaji": "ii desu ne. mimashou", "en": "Sounds good. Let's watch it."},
            {"jp": "土曜日にテニスをしませんか。", "kana": "どようびにテニスをしませんか", "romaji": "doyoubi ni tenisu o shimasen ka", "en": "Would you like to play tennis on Saturday?"},
            {"jp": "すみません、土曜日はちょっと…。", "kana": "すみません どようびはちょっと", "romaji": "sumimasen, doyoubi wa chotto", "en": "Sorry, Saturday is a bit... (declining)"},
        ],
        "vocab": [
            {"word": "一緒に", "reading": "いっしょに", "meaning": "together"},
            {"word": "映画", "reading": "えいが", "meaning": "movie"},
            {"word": "土曜日", "reading": "どようび", "meaning": "Saturday"},
            {"word": "日曜日", "reading": "にちようび", "meaning": "Sunday"},
            {"word": "テニス", "reading": "テニス", "meaning": "tennis"},
        ],
    },
    {
        "id": "n5-18",
        "title": "Adjectives in the past",
        "jp_title": "〜かったです・〜でした",
        "goal": "Say how things were: it was cold, the trip was fun.",
        "points": [
            "い-adjectives: replace い with **かったです**: 寒い → 寒かったです \"it was cold\".",
            "Negative past: **くなかったです**: 寒くなかったです \"it wasn't cold\".",
            "な-adjectives and nouns use **でした** / **じゃありませんでした**: 静かでした, 雨でした.",
            "**いい** becomes **よかったです** (it was good).",
        ],
        "examples": [
            {"jp": "昨日は寒かったです。", "kana": "きのうはさむかったです", "romaji": "kinou wa samukatta desu", "en": "It was cold yesterday."},
            {"jp": "旅行は楽しかったです。", "kana": "りょこうはたのしかったです", "romaji": "ryokou wa tanoshikatta desu", "en": "The trip was fun."},
            {"jp": "テストは難しくなかったです。", "kana": "テストはむずかしくなかったです", "romaji": "tesuto wa muzukashiku nakatta desu", "en": "The test wasn't difficult."},
            {"jp": "公園は静かでした。", "kana": "こうえんはしずかでした", "romaji": "kouen wa shizuka deshita", "en": "The park was quiet."},
        ],
        "vocab": [
            {"word": "楽しい", "reading": "たのしい", "meaning": "fun, enjoyable"},
            {"word": "難しい", "reading": "むずかしい", "meaning": "difficult"},
            {"word": "暑い", "reading": "あつい", "meaning": "hot (weather)"},
            {"word": "天気", "reading": "てんき", "meaning": "weather"},
            {"word": "公園", "reading": "こうえん", "meaning": "park"},
            {"word": "テスト", "reading": "テスト", "meaning": "test"},
        ],
    },
    {
        "id": "n5-19",
        "title": "Counting things and prices",
        "jp_title": "〜つ・〜円",
        "goal": "Count objects, ask how many, and understand prices.",
        "points": [
            "Many objects are counted with **つ**: ひとつ, ふたつ, みっつ, よっつ, いつつ (1–5), "
            "むっつ, ななつ, やっつ, ここのつ, とお (6–10). Ask with **いくつ** (how many).",
            "Prices use **円** (en, yen): 百円 (hyaku en, 100 yen), 千円 (sen en, 1,000 yen). "
            "Watch the sound changes: 三百 さんびゃく, 六百 ろっぴゃく, 八百 はっぴゃく, 三千 さんぜん, 八千 はっせん.",
            "To order or buy: **[thing]を[number]ください**: りんごを三つください。",
        ],
        "examples": [
            {"jp": "りんごを三つください。", "kana": "りんごをみっつください", "romaji": "ringo o mittsu kudasai", "en": "Three apples, please."},
            {"jp": "このかばんは三千円です。", "kana": "このかばんはさんぜんえんです", "romaji": "kono kaban wa sanzen en desu", "en": "This bag is 3,000 yen."},
            {"jp": "卵はいくつありますか。", "kana": "たまごはいくつありますか", "romaji": "tamago wa ikutsu arimasu ka", "en": "How many eggs are there?"},
            {"jp": "全部で八百円です。", "kana": "ぜんぶではっぴゃくえんです", "romaji": "zenbu de happyaku en desu", "en": "That's 800 yen in total."},
        ],
        "vocab": [
            {"word": "りんご", "reading": "りんご", "meaning": "apple"},
            {"word": "卵", "reading": "たまご", "meaning": "egg"},
            {"word": "円", "reading": "えん", "meaning": "yen"},
            {"word": "いくつ", "reading": "いくつ", "meaning": "how many"},
            {"word": "全部", "reading": "ぜんぶ", "meaning": "all; in total"},
            {"word": "百", "reading": "ひゃく", "meaning": "hundred"},
            {"word": "千", "reading": "せん", "meaning": "thousand"},
        ],
    },
    {
        "id": "n5-20",
        "title": "Doing it now: ています",
        "jp_title": "〜ています",
        "goal": "Say what is happening right now, and describe ongoing states.",
        "points": [
            "**[verb て-form] + います** describes an action in progress: 今、本を読んでいます \"I'm reading a book now\".",
            "It also describes a lasting state: 東京に住んでいます \"I live in Tokyo\".",
            "て-forms in this lesson: 読みます → 読んで, 住みます → 住んで, 降ります → 降って, します → して.",
            "Negative: **〜ていません**: 読んでいません \"I'm not reading\".",
        ],
        "examples": [
            {"jp": "今、本を読んでいます。", "kana": "いま ほんをよんでいます", "romaji": "ima, hon o yonde imasu", "en": "I'm reading a book now."},
            {"jp": "東京に住んでいます。", "kana": "とうきょうにすんでいます", "romaji": "toukyou ni sunde imasu", "en": "I live in Tokyo."},
            {"jp": "雨が降っています。", "kana": "あめがふっています", "romaji": "ame ga futte imasu", "en": "It's raining."},
            {"jp": "田中さんは今、電話をしています。", "kana": "たなかさんはいま でんわをしています", "romaji": "tanaka san wa ima, denwa o shite imasu", "en": "Mr. Tanaka is on the phone now."},
        ],
        "vocab": [
            {"word": "住みます", "reading": "すみます", "meaning": "to live (somewhere)"},
            {"word": "雨", "reading": "あめ", "meaning": "rain"},
            {"word": "降ります", "reading": "ふります", "meaning": "to fall (rain, snow)"},
            {"word": "知っています", "reading": "しっています", "meaning": "to know"},
            {"word": "結婚します", "reading": "けっこんします", "meaning": "to get married"},
        ],
    },
    {
        "id": "n5-21",
        "title": "Days and dates",
        "jp_title": "曜日・日付",
        "goal": "Say the day of the week, months and dates, and ask when.",
        "points": [
            "Days: 月曜日 (getsuyoubi, Mon), 火曜日 (kayoubi), 水曜日 (suiyoubi), 木曜日 (mokuyoubi), "
            "金曜日 (kin'youbi), 土曜日 (doyoubi), 日曜日 (nichiyoubi). Ask **何曜日ですか**.",
            "Months are number + **月** (gatsu). Watch 四月 **しがつ**, 七月 **しちがつ**, 九月 **くがつ**.",
            "Dates 1–10 are special: 一日 **ついたち**, 二日 ふつか, 三日 みっか, 四日 よっか, 五日 いつか, "
            "六日 むいか, 七日 なのか, 八日 ようか, 九日 ここのか, 十日 とおか, and 二十日 **はつか**. "
            "Most others are number + にち.",
            "**いつ** = when: 誕生日はいつですか。",
        ],
        "examples": [
            {"jp": "今日は何曜日ですか。", "kana": "きょうはなんようびですか", "romaji": "kyou wa nan'youbi desu ka", "en": "What day of the week is it today?"},
            {"jp": "今日は金曜日です。", "kana": "きょうはきんようびです", "romaji": "kyou wa kin'youbi desu", "en": "Today is Friday."},
            {"jp": "誕生日はいつですか。", "kana": "たんじょうびはいつですか", "romaji": "tanjoubi wa itsu desu ka", "en": "When is your birthday?"},
            {"jp": "四月一日です。", "kana": "しがつついたちです", "romaji": "shigatsu tsuitachi desu", "en": "It's April 1st."},
        ],
        "vocab": [
            {"word": "月曜日", "reading": "げつようび", "meaning": "Monday"},
            {"word": "金曜日", "reading": "きんようび", "meaning": "Friday"},
            {"word": "いつ", "reading": "いつ", "meaning": "when"},
            {"word": "誕生日", "reading": "たんじょうび", "meaning": "birthday"},
            {"word": "今月", "reading": "こんげつ", "meaning": "this month"},
            {"word": "来月", "reading": "らいげつ", "meaning": "next month"},
        ],
    },
    {
        "id": "n5-22",
        "title": "Because and but: から and が",
        "jp_title": "〜から・〜が",
        "goal": "Give reasons and contrast two ideas.",
        "points": [
            "**[reason]から、[result]** = because ..., so ...: 雨ですから、行きません。 \"It's raining, so I won't go.\"",
            "**〜が、〜** = ..., but ...: 高いですが、おいしいです。 \"It's expensive, but delicious.\"",
            "**でも** starts a new sentence with \"but\": 高いです。でも、おいしいです。",
            "Ask why with **どうして** (doushite). The answer often ends in から.",
        ],
        "examples": [
            {"jp": "雨ですから、行きません。", "kana": "あめですから いきません", "romaji": "ame desu kara, ikimasen", "en": "It's raining, so I won't go."},
            {"jp": "このカレーは辛いですが、おいしいです。", "kana": "このカレーはからいですが おいしいです", "romaji": "kono karee wa karai desu ga, oishii desu", "en": "This curry is spicy, but delicious."},
            {"jp": "どうして食べませんか。", "kana": "どうしてたべませんか", "romaji": "doushite tabemasen ka", "en": "Why aren't you eating?"},
            {"jp": "お腹がいっぱいですから。", "kana": "おなかがいっぱいですから", "romaji": "onaka ga ippai desu kara", "en": "Because I'm full."},
        ],
        "vocab": [
            {"word": "から", "reading": "から", "meaning": "because, so"},
            {"word": "でも", "reading": "でも", "meaning": "but, however"},
            {"word": "どうして", "reading": "どうして", "meaning": "why"},
            {"word": "辛い", "reading": "からい", "meaning": "spicy, hot"},
            {"word": "お腹", "reading": "おなか", "meaning": "stomach"},
            {"word": "いっぱい", "reading": "いっぱい", "meaning": "full; a lot"},
        ],
    },
    {
        "id": "n5-23",
        "title": "Linking with the て-form",
        "jp_title": "〜て、〜",
        "goal": "Join actions in order, and join adjectives.",
        "points": [
            "Join actions in order with the **て-form**: 朝ご飯を食べて、学校に行きます。 \"I eat breakfast, then go to school.\"",
            "Only the last verb shows the tense: 起きて、顔を洗いました。 \"I got up and washed my face.\"",
            "Join い-adjectives with **くて**: 安くておいしいです \"cheap and tasty\". "
            "Join な-adjectives and nouns with **で**: 静かできれいです \"quiet and clean\".",
            "**いい** becomes **よくて**.",
        ],
        "examples": [
            {"jp": "朝ご飯を食べて、学校に行きます。", "kana": "あさごはんをたべて がっこうにいきます", "romaji": "asagohan o tabete, gakkou ni ikimasu", "en": "I eat breakfast and then go to school."},
            {"jp": "起きて、顔を洗いました。", "kana": "おきて かおをあらいました", "romaji": "okite, kao o araimashita", "en": "I got up and washed my face."},
            {"jp": "この店は安くておいしいです。", "kana": "このみせはやすくておいしいです", "romaji": "kono mise wa yasukute oishii desu", "en": "This restaurant is cheap and tasty."},
            {"jp": "私の部屋は静かできれいです。", "kana": "わたしのへやはしずかできれいです", "romaji": "watashi no heya wa shizuka de kirei desu", "en": "My room is quiet and clean."},
        ],
        "vocab": [
            {"word": "朝ご飯", "reading": "あさごはん", "meaning": "breakfast"},
            {"word": "食べます", "reading": "たべます", "meaning": "to eat"},
            {"word": "顔", "reading": "かお", "meaning": "face"},
            {"word": "洗います", "reading": "あらいます", "meaning": "to wash"},
            {"word": "店", "reading": "みせ", "meaning": "shop, restaurant"},
            {"word": "出かけます", "reading": "でかけます", "meaning": "to go out"},
        ],
    },
    {
        "id": "n5-24",
        "title": "Comparisons",
        "jp_title": "〜より・いちばん",
        "goal": "Compare two things and say which is the most.",
        "points": [
            "**AはBより[adjective]です** = A is more ... than B: 東京は大阪より大きいです。",
            "Ask which of two: **AとBとどちらが[adjective]ですか**. Answer: **Aのほうが[adjective]です**.",
            "The most: **[group]の中で[X]が一番[adjective]です**. 一番 (ichiban) literally means \"number one\".",
            "Ask \"which is the most\" with 何が, どれが or 誰が + 一番.",
        ],
        "examples": [
            {"jp": "東京は大阪より大きいです。", "kana": "とうきょうはおおさかよりおおきいです", "romaji": "toukyou wa oosaka yori ookii desu", "en": "Tokyo is bigger than Osaka."},
            {"jp": "犬と猫とどちらが好きですか。", "kana": "いぬとねことどちらがすきですか", "romaji": "inu to neko to dochira ga suki desu ka", "en": "Which do you like more, dogs or cats?"},
            {"jp": "猫のほうが好きです。", "kana": "ねこのほうがすきです", "romaji": "neko no hou ga suki desu", "en": "I like cats more."},
            {"jp": "果物の中でりんごが一番好きです。", "kana": "くだもののなかでりんごがいちばんすきです", "romaji": "kudamono no naka de ringo ga ichiban suki desu", "en": "Of all fruit, I like apples best."},
        ],
        "vocab": [
            {"word": "より", "reading": "より", "meaning": "than"},
            {"word": "どちら", "reading": "どちら", "meaning": "which (of two)"},
            {"word": "一番", "reading": "いちばん", "meaning": "the most; number one"},
            {"word": "犬", "reading": "いぬ", "meaning": "dog"},
            {"word": "果物", "reading": "くだもの", "meaning": "fruit"},
        ],
    },
    {
        "id": "n5-25",
        "title": "Already, not yet, how often",
        "jp_title": "もう・まだ・よく",
        "goal": "Say whether you've done something yet, and how often you do things.",
        "points": [
            "**もう〜ました** = already did: もう食べました。",
            "**まだです** or **まだ〜ていません** = not yet: まだ食べていません。",
            "How often: **よく** (often), **時々** (tokidoki, sometimes), **あまり〜ません** (not much), "
            "**ぜんぜん〜ません** (not at all).",
            "あまり and ぜんぜん need a negative verb: あまり見ません, never あまり見ます.",
        ],
        "examples": [
            {"jp": "もう昼ご飯を食べましたか。", "kana": "もうひるごはんをたべましたか", "romaji": "mou hirugohan o tabemashita ka", "en": "Have you had lunch yet?"},
            {"jp": "いいえ、まだです。", "kana": "いいえ まだです", "romaji": "iie, mada desu", "en": "No, not yet."},
            {"jp": "よく図書館で勉強します。", "kana": "よくとしょかんでべんきょうします", "romaji": "yoku toshokan de benkyou shimasu", "en": "I often study at the library."},
            {"jp": "テレビはあまり見ません。", "kana": "テレビはあまりみません", "romaji": "terebi wa amari mimasen", "en": "I don't watch TV much."},
        ],
        "vocab": [
            {"word": "もう", "reading": "もう", "meaning": "already"},
            {"word": "まだ", "reading": "まだ", "meaning": "not yet; still"},
            {"word": "よく", "reading": "よく", "meaning": "often; well"},
            {"word": "時々", "reading": "ときどき", "meaning": "sometimes"},
            {"word": "あまり", "reading": "あまり", "meaning": "(not) much"},
            {"word": "ぜんぜん", "reading": "ぜんぜん", "meaning": "(not) at all"},
            {"word": "昼ご飯", "reading": "ひるごはん", "meaning": "lunch"},
        ],
    },
    {
        "id": "n5-26",
        "title": "Can do, good at, understand",
        "jp_title": "できます・上手・分かります",
        "goal": "Talk about abilities, skills and understanding.",
        "points": [
            "**〜ができます** = can do: 日本語ができます。",
            "**〜が上手です** (jouzu) = good at, **〜が下手です** (heta) = bad at. Calling yourself 上手 sounds "
            "like bragging; when praised, people often say いいえ、まだまだです.",
            "**〜が分かります** (wakarimasu) = understand: 英語が分かりますか。",
            "All three take **が** for the skill or thing, not を.",
        ],
        "examples": [
            {"jp": "英語ができますか。", "kana": "えいごができますか", "romaji": "eigo ga dekimasu ka", "en": "Can you speak English?"},
            {"jp": "田中さんは歌が上手です。", "kana": "たなかさんはうたがじょうずです", "romaji": "tanaka san wa uta ga jouzu desu", "en": "Ms. Tanaka is good at singing."},
            {"jp": "私は料理が下手です。", "kana": "わたしはりょうりがへたです", "romaji": "watashi wa ryouri ga heta desu", "en": "I'm bad at cooking."},
            {"jp": "すみません、分かりません。", "kana": "すみません わかりません", "romaji": "sumimasen, wakarimasen", "en": "Sorry, I don't understand."},
        ],
        "vocab": [
            {"word": "できます", "reading": "できます", "meaning": "can do"},
            {"word": "上手", "reading": "じょうず", "meaning": "good at, skillful"},
            {"word": "下手", "reading": "へた", "meaning": "bad at, unskillful"},
            {"word": "分かります", "reading": "わかります", "meaning": "to understand"},
            {"word": "英語", "reading": "えいご", "meaning": "English (language)"},
            {"word": "歌", "reading": "うた", "meaning": "song"},
            {"word": "料理", "reading": "りょうり", "meaning": "cooking; dish"},
        ],
    },
    {
        "id": "n5-27",
        "title": "Permission and rules",
        "jp_title": "〜てもいいです・〜てはいけません",
        "goal": "Ask if something is allowed, and understand what isn't.",
        "points": [
            "**[て-form] + もいいですか** asks permission: 写真を撮ってもいいですか。 \"May I take a photo?\"",
            "Say yes with **はい、どうぞ** (please go ahead). Say no softly with **すみません、ちょっと…**.",
            "**[て-form] + はいけません** = you must not: ここでたばこを吸ってはいけません。",
            "て-forms here: 撮ります → 撮って, 入ります → 入って, 座ります → 座って, 吸います → 吸って.",
        ],
        "examples": [
            {"jp": "写真を撮ってもいいですか。", "kana": "しゃしんをとってもいいですか", "romaji": "shashin o totte mo ii desu ka", "en": "May I take a photo?"},
            {"jp": "はい、どうぞ。", "kana": "はい どうぞ", "romaji": "hai, douzo", "en": "Yes, go ahead."},
            {"jp": "ここでたばこを吸ってはいけません。", "kana": "ここでたばこをすってはいけません", "romaji": "koko de tabako o sutte wa ikemasen", "en": "You must not smoke here."},
            {"jp": "この部屋に入ってもいいですか。", "kana": "このへやにはいってもいいですか", "romaji": "kono heya ni haitte mo ii desu ka", "en": "May I come into this room?"},
        ],
        "vocab": [
            {"word": "写真", "reading": "しゃしん", "meaning": "photo"},
            {"word": "撮ります", "reading": "とります", "meaning": "to take (a photo)"},
            {"word": "入ります", "reading": "はいります", "meaning": "to enter"},
            {"word": "座ります", "reading": "すわります", "meaning": "to sit"},
            {"word": "どうぞ", "reading": "どうぞ", "meaning": "please (go ahead), here you are"},
            {"word": "たばこ", "reading": "たばこ", "meaning": "cigarette, tobacco"},
        ],
    },
    {
        "id": "n5-28",
        "title": "Please don't: ないでください",
        "jp_title": "〜ないでください",
        "goal": "Ask someone not to do something, using the ない-form.",
        "points": [
            "The **ない-form** is the plain negative. For most verbs, change the sound before ます from い to あ "
            "and add ない: 行きます → 行かない, 飲みます → 飲まない, 撮ります → 撮らない. 会います → 会わない (い → わ).",
            "For る-verbs, drop ます and add ない: 食べます → 食べない, 見ます → 見ない.",
            "Irregular: します → しない, 来ます → 来ない (こない).",
            "**[ない-form] + でください** = please don't ...: 忘れないでください。",
        ],
        "examples": [
            {"jp": "忘れないでください。", "kana": "わすれないでください", "romaji": "wasurenaide kudasai", "en": "Please don't forget."},
            {"jp": "ここで泳がないでください。", "kana": "ここでおよがないでください", "romaji": "koko de oyoganaide kudasai", "en": "Please don't swim here."},
            {"jp": "写真を撮らないでください。", "kana": "しゃしんをとらないでください", "romaji": "shashin o toranaide kudasai", "en": "Please don't take photos."},
            {"jp": "電車の中で電話しないでください。", "kana": "でんしゃのなかででんわしないでください", "romaji": "densha no naka de denwa shinaide kudasai", "en": "Please don't make phone calls on the train."},
        ],
        "vocab": [
            {"word": "忘れます", "reading": "わすれます", "meaning": "to forget"},
            {"word": "泳ぎます", "reading": "およぎます", "meaning": "to swim"},
            {"word": "使います", "reading": "つかいます", "meaning": "to use"},
            {"word": "開けます", "reading": "あけます", "meaning": "to open"},
            {"word": "閉めます", "reading": "しめます", "meaning": "to close"},
        ],
    },
    {
        "id": "n5-29",
        "title": "Dictionary form",
        "jp_title": "辞書形",
        "goal": "Make the plain dictionary form of verbs and say \"before doing\".",
        "points": [
            "Every verb has a plain **dictionary form**, the one you look up: 行く (iku), 食べる (taberu), する, 来る (kuru).",
            "From the ます-form: most verbs change the い-sound before ます to the う-sound: 行きます → 行く, "
            "飲みます → 飲む, 話します → 話す. る-verbs drop ます and add る: 食べます → 食べる.",
            "Irregular: します → **する**, 来ます → **来る** (kuru).",
            "**[dictionary form] + 前に** = before doing ...: 寝る前に本を読みます。",
        ],
        "examples": [
            {"jp": "寝る前に本を読みます。", "kana": "ねるまえにほんをよみます", "romaji": "neru mae ni hon o yomimasu", "en": "I read a book before I go to sleep."},
            {"jp": "食べる前に手を洗います。", "kana": "たべるまえにてをあらいます", "romaji": "taberu mae ni te o araimasu", "en": "I wash my hands before eating."},
            {"jp": "日本に来る前に、日本語を勉強しました。", "kana": "にほんにくるまえに にほんごをべんきょうしました", "romaji": "nihon ni kuru mae ni, nihongo o benkyou shimashita", "en": "I studied Japanese before coming to Japan."},
        ],
        "vocab": [
            {"word": "寝ます", "reading": "ねます", "meaning": "to sleep, go to bed"},
            {"word": "手", "reading": "て", "meaning": "hand"},
            {"word": "前に", "reading": "まえに", "meaning": "before"},
            {"word": "行く", "reading": "いく", "meaning": "to go (dictionary form)"},
            {"word": "来る", "reading": "くる", "meaning": "to come (dictionary form)"},
            {"word": "する", "reading": "する", "meaning": "to do (dictionary form)"},
        ],
    },
    {
        "id": "n5-30",
        "title": "Counters",
        "jp_title": "助数詞",
        "goal": "Count people, flat things, long things, animals and times.",
        "points": [
            "The counter after a number depends on the kind of thing: **人** (people), **枚** (flat things: "
            "paper, tickets), **本** (long things: pens, bottles), **匹** (small animals), **回** (times).",
            "People: 一人 **ひとり**, 二人 **ふたり**, then 三人 さんにん, 四人 **よにん**.",
            "本, 匹 and 回 change sound: 一本 いっぽん, 三本 さんぼん, 六本 ろっぽん; 一匹 いっぴき, "
            "三匹 さんびき; 一回 いっかい.",
            "Ask with 何 + counter: 何人 (nannin), 何枚 (nanmai), 何本 (nanbon).",
        ],
        "examples": [
            {"jp": "家族は四人です。", "kana": "かぞくはよにんです", "romaji": "kazoku wa yonin desu", "en": "There are four people in my family."},
            {"jp": "切手を二枚ください。", "kana": "きってをにまいください", "romaji": "kitte o nimai kudasai", "en": "Two stamps, please."},
            {"jp": "ペンが三本あります。", "kana": "ペンがさんぼんあります", "romaji": "pen ga sanbon arimasu", "en": "There are three pens."},
            {"jp": "犬が一匹います。", "kana": "いぬがいっぴきいます", "romaji": "inu ga ippiki imasu", "en": "There is one dog."},
            {"jp": "一週間に二回、プールに行きます。", "kana": "いっしゅうかんににかい プールにいきます", "romaji": "isshuukan ni nikai, puuru ni ikimasu", "en": "I go to the pool twice a week."},
        ],
        "vocab": [
            {"word": "家族", "reading": "かぞく", "meaning": "family"},
            {"word": "切手", "reading": "きって", "meaning": "postage stamp"},
            {"word": "紙", "reading": "かみ", "meaning": "paper"},
            {"word": "一週間", "reading": "いっしゅうかん", "meaning": "one week"},
            {"word": "何人", "reading": "なんにん", "meaning": "how many people"},
            {"word": "何回", "reading": "なんかい", "meaning": "how many times"},
        ],
    },
    # ------------------------------------------------------------------ N4
    {
        "id": "n4-01",
        "title": "Plain forms",
        "jp_title": "普通形",
        "goal": "Make the casual (plain) forms used with friends and inside N4 grammar.",
        "points": [
            "Polite forms have plain twins used with friends and family, and inside longer sentences: "
            "行きます → **行く**, 行きません → **行かない**, 行きました → **行った**, 行きませんでした → **行かなかった**.",
            "The plain past (た-form) is made like the て-form, with た instead of て: 書いて → 書いた, "
            "飲んで → 飲んだ, 食べて → 食べた, して → した, 来て → 来た (きた).",
            "Adjectives: 高い → 高かった / 高くない. な-adjectives and nouns use **だ**: 静かだ, 学生だ; "
            "past **だった**, negative **じゃない**.",
            "Most N4 patterns attach to plain forms: 行ったことがある, 行くつもり, 行くと思う.",
        ],
        "examples": [
            {"jp": "明日、学校に行く？", "kana": "あした がっこうにいく", "romaji": "ashita, gakkou ni iku?", "en": "Are you going to school tomorrow?"},
            {"jp": "うん、行く。", "kana": "うん いく", "romaji": "un, iku", "en": "Yeah, I'm going."},
            {"jp": "昨日は何も食べなかった。", "kana": "きのうはなにもたべなかった", "romaji": "kinou wa nani mo tabenakatta", "en": "I didn't eat anything yesterday."},
            {"jp": "このケーキ、おいしかった。", "kana": "このケーキ おいしかった", "romaji": "kono keeki, oishikatta", "en": "This cake was delicious."},
        ],
        "vocab": [
            {"word": "うん", "reading": "うん", "meaning": "yeah (casual yes)"},
            {"word": "ううん", "reading": "ううん", "meaning": "nope (casual no)"},
            {"word": "普通", "reading": "ふつう", "meaning": "normal, ordinary"},
            {"word": "ケーキ", "reading": "ケーキ", "meaning": "cake"},
            {"word": "食べる", "reading": "たべる", "meaning": "to eat (plain form)"},
            {"word": "飲む", "reading": "のむ", "meaning": "to drink (plain form)"},
        ],
    },
    {
        "id": "n4-02",
        "title": "Have you ever...?",
        "jp_title": "〜たことがあります",
        "goal": "Talk about things you have (or have never) done.",
        "points": [
            "**[plain past] + ことがあります** = have done something at least once: 富士山に登ったことがあります。",
            "Ask with 〜たことがありますか。 Answer はい、あります or いいえ、ありません.",
            "**一度** (ichido) = once, **何度も** (nando mo) = many times. **一度もありません** = never, not even once.",
            "Negative: **〜たことがありません** = have never ...",
        ],
        "examples": [
            {"jp": "富士山に登ったことがあります。", "kana": "ふじさんにのぼったことがあります", "romaji": "fujisan ni nobotta koto ga arimasu", "en": "I have climbed Mt. Fuji."},
            {"jp": "すしを食べたことがありますか。", "kana": "すしをたべたことがありますか", "romaji": "sushi o tabeta koto ga arimasu ka", "en": "Have you ever eaten sushi?"},
            {"jp": "いいえ、一度もありません。", "kana": "いいえ いちどもありません", "romaji": "iie, ichido mo arimasen", "en": "No, never once."},
            {"jp": "日本の映画を何度も見たことがあります。", "kana": "にほんのえいがをなんどもみたことがあります", "romaji": "nihon no eiga o nando mo mita koto ga arimasu", "en": "I have watched Japanese movies many times."},
        ],
        "vocab": [
            {"word": "登ります", "reading": "のぼります", "meaning": "to climb"},
            {"word": "一度", "reading": "いちど", "meaning": "once, one time"},
            {"word": "何度も", "reading": "なんども", "meaning": "many times"},
            {"word": "経験", "reading": "けいけん", "meaning": "experience"},
            {"word": "富士山", "reading": "ふじさん", "meaning": "Mt. Fuji"},
        ],
    },
    {
        "id": "n4-03",
        "title": "Doing things like...",
        "jp_title": "〜たり〜たりします",
        "goal": "Give a few examples of what you do, without listing everything.",
        "points": [
            "**[plain past]り、[plain past]りします** lists some example actions: "
            "週末は映画を見たり、買い物をしたりします。 \"On weekends I do things like watch movies and go shopping.\"",
            "Add り to the た-form: 見た → 見たり, 読んだ → 読んだり, 行った → 行ったり.",
            "The tense goes on the final します: 〜たりしました = did things like ...",
            "With only one action it means \"things like ...\": 本を読んだりします。",
        ],
        "examples": [
            {"jp": "週末は映画を見たり、買い物をしたりします。", "kana": "しゅうまつはえいがをみたり かいものをしたりします", "romaji": "shuumatsu wa eiga o mitari, kaimono o shitari shimasu", "en": "On weekends I do things like watching movies and shopping."},
            {"jp": "休みの日は、本を読んだり、音楽を聞いたりします。", "kana": "やすみのひは ほんをよんだり おんがくをきいたりします", "romaji": "yasumi no hi wa, hon o yondari, ongaku o kiitari shimasu", "en": "On my days off I read books, listen to music and so on."},
            {"jp": "夏休みに泳いだり、山に登ったりしました。", "kana": "なつやすみにおよいだり やまにのぼったりしました", "romaji": "natsuyasumi ni oyoidari, yama ni nobottari shimashita", "en": "In the summer holidays I did things like swimming and climbing mountains."},
        ],
        "vocab": [
            {"word": "買い物", "reading": "かいもの", "meaning": "shopping"},
            {"word": "休み", "reading": "やすみ", "meaning": "day off, holiday"},
            {"word": "聞きます", "reading": "ききます", "meaning": "to listen; to ask"},
            {"word": "夏休み", "reading": "なつやすみ", "meaning": "summer vacation"},
            {"word": "山", "reading": "やま", "meaning": "mountain"},
            {"word": "音楽", "reading": "おんがく", "meaning": "music"},
        ],
    },
    {
        "id": "n4-04",
        "title": "Can do: the potential form",
        "jp_title": "可能形",
        "goal": "Say what you can and can't do with the potential form.",
        "points": [
            "The **potential form** says what you can do: 話せます (can speak), 食べられます (can eat).",
            "Most verbs change the い-sound before ます to the え-sound: 話します → **話せます**, 書きます → **書けます**, "
            "読みます → **読めます**, 泳ぎます → **泳げます**.",
            "る-verbs replace ます with **られます**: 食べます → 食べられます, 見ます → 見られます.",
            "Irregular: します → **できます**, 来ます → **来られます** (koraremasu). The thing you can do usually takes **が**.",
        ],
        "examples": [
            {"jp": "日本語が少し話せます。", "kana": "にほんごがすこしはなせます", "romaji": "nihongo ga sukoshi hanasemasu", "en": "I can speak a little Japanese."},
            {"jp": "漢字が読めますか。", "kana": "かんじがよめますか", "romaji": "kanji ga yomemasu ka", "en": "Can you read kanji?"},
            {"jp": "辛い料理は食べられません。", "kana": "からいりょうりはたべられません", "romaji": "karai ryouri wa taberaremasen", "en": "I can't eat spicy food."},
            {"jp": "明日は来られますか。", "kana": "あしたはこられますか", "romaji": "ashita wa koraremasu ka", "en": "Can you come tomorrow?"},
        ],
        "vocab": [
            {"word": "少し", "reading": "すこし", "meaning": "a little"},
            {"word": "漢字", "reading": "かんじ", "meaning": "kanji, Chinese characters"},
            {"word": "話せます", "reading": "はなせます", "meaning": "can speak"},
            {"word": "読めます", "reading": "よめます", "meaning": "can read"},
            {"word": "食べられます", "reading": "たべられます", "meaning": "can eat"},
        ],
    },
    {
        "id": "n4-05",
        "title": "I think, they said",
        "jp_title": "〜と思います・〜と言いました",
        "goal": "Give your opinion and pass on what someone said.",
        "points": [
            "**[plain form] + と思います** = I think (that) ...: 明日は雨が降ると思います。",
            "After nouns and な-adjectives add **だ**: あの人は先生だと思います。",
            "**[plain form] + と言いました** reports what someone said: 先生は明日テストがあると言いました。",
            "**〜と言っていました** (\"was saying\") is the natural way to pass on a message.",
        ],
        "examples": [
            {"jp": "明日は雨が降ると思います。", "kana": "あしたはあめがふるとおもいます", "romaji": "ashita wa ame ga furu to omoimasu", "en": "I think it will rain tomorrow."},
            {"jp": "この本はおもしろいと思います。", "kana": "このほんはおもしろいとおもいます", "romaji": "kono hon wa omoshiroi to omoimasu", "en": "I think this book is interesting."},
            {"jp": "田中さんは来ないと言っていました。", "kana": "たなかさんはこないといっていました", "romaji": "tanaka san wa konai to itte imashita", "en": "Mr. Tanaka said he isn't coming."},
            {"jp": "あの人は先生だと思います。", "kana": "あのひとはせんせいだとおもいます", "romaji": "ano hito wa sensei da to omoimasu", "en": "I think that person is a teacher."},
        ],
        "vocab": [
            {"word": "思います", "reading": "おもいます", "meaning": "to think"},
            {"word": "言います", "reading": "いいます", "meaning": "to say"},
            {"word": "おもしろい", "reading": "おもしろい", "meaning": "interesting; funny"},
            {"word": "多分", "reading": "たぶん", "meaning": "probably, maybe"},
            {"word": "意見", "reading": "いけん", "meaning": "opinion"},
        ],
    },
    {
        "id": "n4-06",
        "title": "Plans: つもり and 予定",
        "jp_title": "〜つもりです・〜予定です",
        "goal": "Talk about what you intend to do and what is scheduled.",
        "points": [
            "**[dictionary form] + つもりです** = I intend to: 来年日本に行くつもりです。 It's your own decision.",
            "Intend not to: **〜ないつもりです**: お酒を飲まないつもりです。",
            "**[dictionary form] + 予定です** = it's planned / scheduled: 電車は十時に着く予定です。",
            "つもり is about your intention; 予定 is about an arranged plan or timetable.",
        ],
        "examples": [
            {"jp": "来年、日本に行くつもりです。", "kana": "らいねん にほんにいくつもりです", "romaji": "rainen, nihon ni iku tsumori desu", "en": "I intend to go to Japan next year."},
            {"jp": "今晩はお酒を飲まないつもりです。", "kana": "こんばんはおさけをのまないつもりです", "romaji": "konban wa osake o nomanai tsumori desu", "en": "I don't intend to drink tonight."},
            {"jp": "電車は十時に着く予定です。", "kana": "でんしゃはじゅうじにつくよていです", "romaji": "densha wa juuji ni tsuku yotei desu", "en": "The train is scheduled to arrive at ten."},
            {"jp": "来週、友達と旅行する予定です。", "kana": "らいしゅう ともだちとりょこうするよていです", "romaji": "raishuu, tomodachi to ryokou suru yotei desu", "en": "I'm planning a trip with friends next week."},
        ],
        "vocab": [
            {"word": "つもり", "reading": "つもり", "meaning": "intention"},
            {"word": "予定", "reading": "よてい", "meaning": "plan, schedule"},
            {"word": "来年", "reading": "らいねん", "meaning": "next year"},
            {"word": "今晩", "reading": "こんばん", "meaning": "tonight, this evening"},
            {"word": "着きます", "reading": "つきます", "meaning": "to arrive"},
            {"word": "お酒", "reading": "おさけ", "meaning": "alcohol; sake"},
        ],
    },
    {
        "id": "n4-07",
        "title": "Let's / I'm thinking of: the volitional form",
        "jp_title": "意向形",
        "goal": "Suggest things casually and say what you're planning to do.",
        "points": [
            "The **volitional form** is the plain version of ましょう: 行きましょう → **行こう**, 食べましょう → **食べよう**.",
            "Most verbs change the い-sound before ます to the お-sound + う: 飲みます → 飲もう, 帰ります → 帰ろう, "
            "買います → 買おう. る-verbs drop ます and add よう: 見よう. Irregular: **しよう**, **来よう** (koyou).",
            "Between friends it means \"let's\": 一緒に帰ろう。",
            "**[volitional] + と思っています** = I'm thinking of doing: 新しいパソコンを買おうと思っています。",
        ],
        "examples": [
            {"jp": "一緒に帰ろう。", "kana": "いっしょにかえろう", "romaji": "issho ni kaerou", "en": "Let's go home together."},
            {"jp": "少し休もう。", "kana": "すこしやすもう", "romaji": "sukoshi yasumou", "en": "Let's take a short break."},
            {"jp": "新しいパソコンを買おうと思っています。", "kana": "あたらしいパソコンをかおうとおもっています", "romaji": "atarashii pasokon o kaou to omotte imasu", "en": "I'm thinking of buying a new computer."},
            {"jp": "来年から毎日運動しようと思っています。", "kana": "らいねんからまいにちうんどうしようとおもっています", "romaji": "rainen kara mainichi undou shiyou to omotte imasu", "en": "I'm thinking of exercising every day from next year."},
        ],
        "vocab": [
            {"word": "休みます", "reading": "やすみます", "meaning": "to rest; to take a day off"},
            {"word": "運動", "reading": "うんどう", "meaning": "exercise"},
            {"word": "始めます", "reading": "はじめます", "meaning": "to begin, start"},
            {"word": "やめます", "reading": "やめます", "meaning": "to quit, stop"},
            {"word": "決めます", "reading": "きめます", "meaning": "to decide"},
        ],
    },
    {
        "id": "n4-08",
        "title": "Must and don't have to",
        "jp_title": "〜なければなりません・〜なくてもいいです",
        "goal": "Say what you must do, and what you don't need to do.",
        "points": [
            "**[ない-form without い] + ければなりません** = must: 行かない → **行かなければなりません**.",
            "**[ない-form without い] + くてもいいです** = don't have to: 行かない → **行かなくてもいいです**.",
            "Compare lesson N5-27: 〜てもいいです = you may do; 〜なくてもいいです = you needn't do.",
            "In casual speech you'll hear the short **〜なきゃ**: 行かなきゃ。 \"I've got to go.\"",
        ],
        "examples": [
            {"jp": "明日は早く起きなければなりません。", "kana": "あしたははやくおきなければなりません", "romaji": "ashita wa hayaku okinakereba narimasen", "en": "I have to get up early tomorrow."},
            {"jp": "薬を飲まなければなりません。", "kana": "くすりをのまなければなりません", "romaji": "kusuri o nomanakereba narimasen", "en": "I have to take my medicine."},
            {"jp": "土曜日は学校に行かなくてもいいです。", "kana": "どようびはがっこうにいかなくてもいいです", "romaji": "doyoubi wa gakkou ni ikanakute mo ii desu", "en": "You don't have to go to school on Saturday."},
            {"jp": "全部食べなくてもいいですよ。", "kana": "ぜんぶたべなくてもいいですよ", "romaji": "zenbu tabenakute mo ii desu yo", "en": "You don't have to eat it all."},
        ],
        "vocab": [
            {"word": "早く", "reading": "はやく", "meaning": "early; quickly"},
            {"word": "薬", "reading": "くすり", "meaning": "medicine"},
            {"word": "宿題", "reading": "しゅくだい", "meaning": "homework"},
            {"word": "出します", "reading": "だします", "meaning": "to hand in; to take out"},
            {"word": "払います", "reading": "はらいます", "meaning": "to pay"},
        ],
    },
    {
        "id": "n4-09",
        "title": "Because and although: ので and のに",
        "jp_title": "〜ので・〜のに",
        "goal": "Give soft, polite reasons and express surprising contrasts.",
        "points": [
            "**〜ので** = because, so: softer and more polite than から: 雨が降っているので、出かけません。",
            "Nouns and な-adjectives take **な** before ので: テストなので, 静かなので.",
            "**〜のに** = although, even though, often with surprise or disappointment: "
            "薬を飲んだのに、まだ頭が痛いです。",
            "のに follows the same な rule: 日曜日なのに、学校に行きました。",
        ],
        "examples": [
            {"jp": "雨が降っているので、出かけません。", "kana": "あめがふっているので でかけません", "romaji": "ame ga futte iru node, dekakemasen", "en": "It's raining, so I won't go out."},
            {"jp": "明日はテストなので、今晩勉強します。", "kana": "あしたはテストなので こんばんべんきょうします", "romaji": "ashita wa tesuto na node, konban benkyou shimasu", "en": "I have a test tomorrow, so I'll study tonight."},
            {"jp": "薬を飲んだのに、まだ頭が痛いです。", "kana": "くすりをのんだのに まだあたまがいたいです", "romaji": "kusuri o nonda noni, mada atama ga itai desu", "en": "Even though I took medicine, my head still hurts."},
            {"jp": "日曜日なのに、学校に行きました。", "kana": "にちようびなのに がっこうにいきました", "romaji": "nichiyoubi na noni, gakkou ni ikimashita", "en": "Even though it was Sunday, I went to school."},
        ],
        "vocab": [
            {"word": "ので", "reading": "ので", "meaning": "because, so"},
            {"word": "のに", "reading": "のに", "meaning": "although, even though"},
            {"word": "頭", "reading": "あたま", "meaning": "head"},
            {"word": "痛い", "reading": "いたい", "meaning": "painful, sore"},
            {"word": "熱", "reading": "ねつ", "meaning": "fever"},
            {"word": "風邪", "reading": "かぜ", "meaning": "a cold"},
        ],
    },
    {
        "id": "n4-10",
        "title": "If and when: たら and と",
        "jp_title": "〜たら・〜と",
        "goal": "Talk about conditions, and what happens when something happens.",
        "points": [
            "**[plain past] + ら** = if / when: 雨が降ったら、行きません。 For future events it also means "
            "\"once ...\": 駅に着いたら、電話してください。",
            "**[dictionary form] + と** = whenever / it naturally follows: 春になると、花が咲きます。 "
            "It's also used for directions: まっすぐ行くと、右に銀行があります。",
            "と can't be followed by a request or an intention (〜てください, 〜つもり); use たら for those.",
            "Adjectives work too: 安かったら (if it's cheap), 暇だったら (if you're free).",
        ],
        "examples": [
            {"jp": "雨が降ったら、行きません。", "kana": "あめがふったら いきません", "romaji": "ame ga futtara, ikimasen", "en": "If it rains, I won't go."},
            {"jp": "駅に着いたら、電話してください。", "kana": "えきについたら でんわしてください", "romaji": "eki ni tsuitara, denwa shite kudasai", "en": "Please call me when you get to the station."},
            {"jp": "春になると、花が咲きます。", "kana": "はるになると はながさきます", "romaji": "haru ni naru to, hana ga sakimasu", "en": "When spring comes, flowers bloom."},
            {"jp": "この道をまっすぐ行くと、右に銀行があります。", "kana": "このみちをまっすぐいくと みぎにぎんこうがあります", "romaji": "kono michi o massugu iku to, migi ni ginkou ga arimasu", "en": "Go straight along this street and there's a bank on the right."},
        ],
        "vocab": [
            {"word": "春", "reading": "はる", "meaning": "spring"},
            {"word": "咲きます", "reading": "さきます", "meaning": "to bloom"},
            {"word": "曲がります", "reading": "まがります", "meaning": "to turn"},
            {"word": "右", "reading": "みぎ", "meaning": "right (side)"},
            {"word": "道", "reading": "みち", "meaning": "road, street; way"},
            {"word": "暇", "reading": "ひま", "meaning": "free (time)"},
        ],
    },
    {
        "id": "n4-11",
        "title": "Giving and receiving",
        "jp_title": "あげる・くれる・もらう",
        "goal": "Say who gave what to whom, with the right verb for each direction.",
        "points": [
            "**あげます** = give, from me (or my side) to someone else: 私は友達に本をあげました。",
            "**くれます** = give **to me** (or my family): 友達が本をくれました。 Someone giving to you is never あげる.",
            "**もらいます** = receive: 私は友達に本をもらいました。 The giver takes **に** (or から).",
            "The same event can be said with くれる or もらう: 友達がくれました = 友達にもらいました.",
        ],
        "examples": [
            {"jp": "私は妹に誕生日のプレゼントをあげました。", "kana": "わたしはいもうとにたんじょうびのプレゼントをあげました", "romaji": "watashi wa imouto ni tanjoubi no purezento o agemashita", "en": "I gave my little sister a birthday present."},
            {"jp": "友達が花をくれました。", "kana": "ともだちがはなをくれました", "romaji": "tomodachi ga hana o kuremashita", "en": "A friend gave me flowers."},
            {"jp": "先生に辞書をもらいました。", "kana": "せんせいにじしょをもらいました", "romaji": "sensei ni jisho o moraimashita", "en": "I got a dictionary from my teacher."},
            {"jp": "これは母がくれた時計です。", "kana": "これはははがくれたとけいです", "romaji": "kore wa haha ga kureta tokei desu", "en": "This is a watch my mother gave me."},
        ],
        "vocab": [
            {"word": "あげます", "reading": "あげます", "meaning": "to give (to someone else)"},
            {"word": "くれます", "reading": "くれます", "meaning": "to give (to me)"},
            {"word": "もらいます", "reading": "もらいます", "meaning": "to receive"},
            {"word": "プレゼント", "reading": "プレゼント", "meaning": "present, gift"},
            {"word": "妹", "reading": "いもうと", "meaning": "(my) younger sister"},
            {"word": "母", "reading": "はは", "meaning": "(my) mother"},
        ],
    },
    {
        "id": "n4-12",
        "title": "Doing favours",
        "jp_title": "〜てあげる・〜てくれる・〜てもらう",
        "goal": "Say who did something for whom, and ask for favours politely.",
        "points": [
            "Put あげる / くれる / もらう after a て-form to show a favour, with the same directions as lesson 11.",
            "**〜てあげます** = do for someone: 友達に料理を作ってあげました。 Saying it to a superior can sound condescending.",
            "**〜てくれます** = someone does it for me: 母がお弁当を作ってくれました。 "
            "**〜てもらいます** = I have someone do it for me: 兄に宿題を手伝ってもらいました。",
            "Polite requests: **〜てくれませんか** / **〜てもらえませんか** = could you (please) ...?",
        ],
        "examples": [
            {"jp": "友達に料理を作ってあげました。", "kana": "ともだちにりょうりをつくってあげました", "romaji": "tomodachi ni ryouri o tsukutte agemashita", "en": "I cooked for my friend."},
            {"jp": "母がお弁当を作ってくれました。", "kana": "ははがおべんとうをつくってくれました", "romaji": "haha ga obentou o tsukutte kuremashita", "en": "My mother made me a packed lunch."},
            {"jp": "兄に宿題を手伝ってもらいました。", "kana": "あににしゅくだいをてつだってもらいました", "romaji": "ani ni shukudai o tetsudatte moraimashita", "en": "My older brother helped me with my homework."},
            {"jp": "ちょっと手伝ってもらえませんか。", "kana": "ちょっとてつだってもらえませんか", "romaji": "chotto tetsudatte moraemasen ka", "en": "Could you help me for a moment?"},
        ],
        "vocab": [
            {"word": "作ります", "reading": "つくります", "meaning": "to make"},
            {"word": "手伝います", "reading": "てつだいます", "meaning": "to help"},
            {"word": "お弁当", "reading": "おべんとう", "meaning": "packed lunch, bento"},
            {"word": "兄", "reading": "あに", "meaning": "(my) older brother"},
            {"word": "貸します", "reading": "かします", "meaning": "to lend"},
        ],
    },
    {
        "id": "n4-13",
        "title": "The passive",
        "jp_title": "受身形",
        "goal": "Say what was done to you: praised, scolded, stepped on.",
        "points": [
            "The **passive** says something is done to someone: 先生に褒められました。 \"I was praised by the teacher.\"",
            "Most verbs change the い-sound before ます to the あ-sound + **れます**: 叱ります → 叱られます, "
            "踏みます → 踏まれます, 言います → 言われます (い → わ).",
            "る-verbs: ます → **られます** (it looks like the potential form): 見ます → 見られます. "
            "Irregular: します → されます, 来ます → 来られます.",
            "The doer takes **に**. Japanese also uses the passive for annoying things that happen to you: "
            "雨に降られました \"I got caught in the rain.\"",
        ],
        "examples": [
            {"jp": "先生に褒められました。", "kana": "せんせいにほめられました", "romaji": "sensei ni homeraremashita", "en": "I was praised by my teacher."},
            {"jp": "母に叱られました。", "kana": "ははにしかられました", "romaji": "haha ni shikararemashita", "en": "I was scolded by my mother."},
            {"jp": "電車で足を踏まれました。", "kana": "でんしゃであしをふまれました", "romaji": "densha de ashi o fumaremashita", "en": "Someone stepped on my foot on the train."},
            {"jp": "昨日、雨に降られました。", "kana": "きのう あめにふられました", "romaji": "kinou, ame ni furaremashita", "en": "I got caught in the rain yesterday."},
        ],
        "vocab": [
            {"word": "褒めます", "reading": "ほめます", "meaning": "to praise"},
            {"word": "叱ります", "reading": "しかります", "meaning": "to scold"},
            {"word": "踏みます", "reading": "ふみます", "meaning": "to step on"},
            {"word": "足", "reading": "あし", "meaning": "foot, leg"},
            {"word": "盗みます", "reading": "ぬすみます", "meaning": "to steal"},
        ],
    },
    {
        "id": "n4-14",
        "title": "The causative",
        "jp_title": "使役形",
        "goal": "Say who makes or lets someone do something.",
        "points": [
            "The **causative** means make or let someone do something: 子供に野菜を食べさせます。",
            "Most verbs change the い-sound before ます to the あ-sound + **せます**: 行きます → 行かせます, "
            "読みます → 読ませます, 買います → 買わせます (い → わ).",
            "る-verbs: ます → **させます**: 食べます → 食べさせます. Irregular: します → させます, 来ます → 来させます (kosasemasu).",
            "The person made to act usually takes **に**. **〜させてください** = please let me ...: 私に払わせてください。",
        ],
        "examples": [
            {"jp": "母は子供に野菜を食べさせます。", "kana": "はははこどもにやさいをたべさせます", "romaji": "haha wa kodomo ni yasai o tabesasemasu", "en": "My mother makes the kids eat vegetables."},
            {"jp": "先生は学生に作文を書かせました。", "kana": "せんせいはがくせいにさくぶんをかかせました", "romaji": "sensei wa gakusei ni sakubun o kakasemashita", "en": "The teacher had the students write an essay."},
            {"jp": "父は私を一人で旅行に行かせてくれました。", "kana": "ちちはわたしをひとりでりょこうにいかせてくれました", "romaji": "chichi wa watashi o hitori de ryokou ni ikasete kuremashita", "en": "My father let me travel on my own."},
            {"jp": "私に払わせてください。", "kana": "わたしにはらわせてください", "romaji": "watashi ni harawasete kudasai", "en": "Please let me pay."},
        ],
        "vocab": [
            {"word": "子供", "reading": "こども", "meaning": "child"},
            {"word": "野菜", "reading": "やさい", "meaning": "vegetables"},
            {"word": "作文", "reading": "さくぶん", "meaning": "essay, composition"},
            {"word": "父", "reading": "ちち", "meaning": "(my) father"},
            {"word": "一人で", "reading": "ひとりで", "meaning": "alone, by oneself"},
        ],
    },
    {
        "id": "n4-15",
        "title": "Looks like / I heard: そうです",
        "jp_title": "〜そうです",
        "goal": "Say how things look, and pass on what you've heard.",
        "points": [
            "**Looks like** (from what you see): adjective without い / な + **そうです**: おいしい → おいしそうです, "
            "元気 → 元気そうです. いい becomes **よさそうです**.",
            "With a verb's ます-stem it means \"looks like it will\": 雨が降りそうです。",
            "**I heard** (hearsay): plain form + **そうです**: 明日は雨が降るそうです。 Often with **〜によると** (according to).",
            "Don't mix them up: 降り**そう**です = looks like rain; 降る**そう**です = I heard it will rain.",
        ],
        "examples": [
            {"jp": "このケーキはおいしそうです。", "kana": "このケーキはおいしそうです", "romaji": "kono keeki wa oishisou desu", "en": "This cake looks delicious."},
            {"jp": "空が暗いですね。雨が降りそうです。", "kana": "そらがくらいですね あめがふりそうです", "romaji": "sora ga kurai desu ne. ame ga furisou desu", "en": "The sky is dark. It looks like it's going to rain."},
            {"jp": "天気予報によると、明日は雪が降るそうです。", "kana": "てんきよほうによると あしたはゆきがふるそうです", "romaji": "tenki yohou ni yoru to, ashita wa yuki ga furu sou desu", "en": "According to the forecast, it will snow tomorrow."},
            {"jp": "田中さんは来月結婚するそうです。", "kana": "たなかさんはらいげつけっこんするそうです", "romaji": "tanaka san wa raigetsu kekkon suru sou desu", "en": "I heard Ms. Tanaka is getting married next month."},
        ],
        "vocab": [
            {"word": "空", "reading": "そら", "meaning": "sky"},
            {"word": "暗い", "reading": "くらい", "meaning": "dark"},
            {"word": "天気予報", "reading": "てんきよほう", "meaning": "weather forecast"},
            {"word": "雪", "reading": "ゆき", "meaning": "snow"},
            {"word": "によると", "reading": "によると", "meaning": "according to"},
        ],
    },
    {
        "id": "n4-16",
        "title": "In advance, and by accident",
        "jp_title": "〜ておく・〜てしまう",
        "goal": "Say you'll do something in advance, or that something got done (often by mistake).",
        "points": [
            "**〜ておきます** = do in advance, or leave as it is: 旅行の前にホテルを予約しておきます。",
            "**〜てしまいます** = do completely, or (very often) do by accident and regret it: 財布をなくしてしまいました。",
            "Casual speech shortens them: ておく → **とく** (予約しとく); てしまう → **ちゃう**, でしまう → **じゃう** "
            "(忘れちゃった, 飲んじゃった).",
            "窓を開けておいてください = please open the window (and leave it open).",
        ],
        "examples": [
            {"jp": "旅行の前にホテルを予約しておきます。", "kana": "りょこうのまえにホテルをよやくしておきます", "romaji": "ryokou no mae ni hoteru o yoyaku shite okimasu", "en": "I'll book a hotel before the trip."},
            {"jp": "窓を開けておいてください。", "kana": "まどをあけておいてください", "romaji": "mado o akete oite kudasai", "en": "Please leave the window open."},
            {"jp": "財布をなくしてしまいました。", "kana": "さいふをなくしてしまいました", "romaji": "saifu o nakushite shimaimashita", "en": "I've lost my wallet."},
            {"jp": "宿題を忘れちゃった。", "kana": "しゅくだいをわすれちゃった", "romaji": "shukudai o wasurechatta", "en": "Oops, I forgot my homework."},
        ],
        "vocab": [
            {"word": "予約", "reading": "よやく", "meaning": "reservation, booking"},
            {"word": "窓", "reading": "まど", "meaning": "window"},
            {"word": "財布", "reading": "さいふ", "meaning": "wallet"},
            {"word": "なくします", "reading": "なくします", "meaning": "to lose"},
            {"word": "ホテル", "reading": "ホテル", "meaning": "hotel"},
        ],
    },
    {
        "id": "n4-17",
        "title": "While, after",
        "jp_title": "〜ながら・〜てから・〜た後で",
        "goal": "Describe two actions at the same time, or one after the other.",
        "points": [
            "**[ます-stem] + ながら** = while doing; one person, two actions, the main one last: 音楽を聞きながら勉強します。",
            "**〜てから** = after doing, then: 手を洗ってから、ご飯を食べます。",
            "**[plain past] + 後で** = after (focus on the order in time): 授業が終わった後で、図書館に行きます。 "
            "With nouns: 食事の後で.",
            "The opposite, **〜前に** (before), is in N5 lesson 29.",
        ],
        "examples": [
            {"jp": "音楽を聞きながら勉強します。", "kana": "おんがくをききながらべんきょうします", "romaji": "ongaku o kikinagara benkyou shimasu", "en": "I study while listening to music."},
            {"jp": "手を洗ってから、ご飯を食べます。", "kana": "てをあらってから ごはんをたべます", "romaji": "te o aratte kara, gohan o tabemasu", "en": "I wash my hands, then eat."},
            {"jp": "授業が終わった後で、図書館に行きます。", "kana": "じゅぎょうがおわったあとで としょかんにいきます", "romaji": "jugyou ga owatta ato de, toshokan ni ikimasu", "en": "After class finishes, I'll go to the library."},
            {"jp": "食事の後で、コーヒーを飲みましょう。", "kana": "しょくじのあとで コーヒーをのみましょう", "romaji": "shokuji no ato de, koohii o nomimashou", "en": "Let's have coffee after the meal."},
        ],
        "vocab": [
            {"word": "ながら", "reading": "ながら", "meaning": "while (doing)"},
            {"word": "授業", "reading": "じゅぎょう", "meaning": "class, lesson"},
            {"word": "終わります", "reading": "おわります", "meaning": "to end, finish"},
            {"word": "食事", "reading": "しょくじ", "meaning": "meal"},
            {"word": "後で", "reading": "あとで", "meaning": "later; after"},
            {"word": "ご飯", "reading": "ごはん", "meaning": "cooked rice; meal"},
        ],
    },
    {
        "id": "n4-18",
        "title": "Changes and decisions",
        "jp_title": "〜ようになる・〜ことにする",
        "goal": "Talk about gradual changes and decisions.",
        "points": [
            "**[dictionary / potential form] + ようになりました** = came to (be able to) ...: 日本語が話せるようになりました。",
            "A change to not doing: **〜なくなりました**: 肉を食べなくなりました \"I stopped eating meat.\"",
            "**[dictionary form] + ことにしました** = I decided to: 毎朝走ることにしました。",
            "**〜ことになりました** = it's been decided (by others or by circumstances): 来月、大阪に引っ越すことになりました。",
        ],
        "examples": [
            {"jp": "日本語が少し話せるようになりました。", "kana": "にほんごがすこしはなせるようになりました", "romaji": "nihongo ga sukoshi hanaseru you ni narimashita", "en": "I've become able to speak a little Japanese."},
            {"jp": "最近、肉を食べなくなりました。", "kana": "さいきん にくをたべなくなりました", "romaji": "saikin, niku o tabenaku narimashita", "en": "Recently I've stopped eating meat."},
            {"jp": "毎朝走ることにしました。", "kana": "まいあさはしることにしました", "romaji": "maiasa hashiru koto ni shimashita", "en": "I've decided to run every morning."},
            {"jp": "来月、大阪に引っ越すことになりました。", "kana": "らいげつ おおさかにひっこすことになりました", "romaji": "raigetsu, oosaka ni hikkosu koto ni narimashita", "en": "It's been decided that I'll move to Osaka next month."},
        ],
        "vocab": [
            {"word": "最近", "reading": "さいきん", "meaning": "recently, lately"},
            {"word": "肉", "reading": "にく", "meaning": "meat"},
            {"word": "走ります", "reading": "はしります", "meaning": "to run"},
            {"word": "毎朝", "reading": "まいあさ", "meaning": "every morning"},
            {"word": "引っ越します", "reading": "ひっこします", "meaning": "to move (house)"},
        ],
    },
    {
        "id": "n4-19",
        "title": "Maybe and probably",
        "jp_title": "〜かもしれません・〜でしょう",
        "goal": "Express how sure you are about something.",
        "points": [
            "**[plain form] + かもしれません** = might, maybe (roughly 50/50): 明日は雪が降るかもしれません。",
            "**[plain form] + でしょう** = probably (more confident). Weather forecasts love it: 明日は晴れるでしょう。",
            "Nouns and な-adjectives attach directly, without だ: 病気かもしれません, 静かでしょう.",
            "**〜でしょう？** with a rising tone asks for agreement: 疲れたでしょう？ \"You must be tired, right?\"",
        ],
        "examples": [
            {"jp": "明日は雪が降るかもしれません。", "kana": "あしたはゆきがふるかもしれません", "romaji": "ashita wa yuki ga furu kamo shiremasen", "en": "It might snow tomorrow."},
            {"jp": "田中さんは今日来ないかもしれません。", "kana": "たなかさんはきょうこないかもしれません", "romaji": "tanaka san wa kyou konai kamo shiremasen", "en": "Mr. Tanaka might not come today."},
            {"jp": "明日は晴れるでしょう。", "kana": "あしたははれるでしょう", "romaji": "ashita wa hareru deshou", "en": "It will probably be sunny tomorrow."},
            {"jp": "長い旅行でしたね。疲れたでしょう？", "kana": "ながいりょこうでしたね つかれたでしょう", "romaji": "nagai ryokou deshita ne. tsukareta deshou?", "en": "That was a long trip. You must be tired, right?"},
        ],
        "vocab": [
            {"word": "かもしれません", "reading": "かもしれません", "meaning": "might, maybe"},
            {"word": "でしょう", "reading": "でしょう", "meaning": "probably; ..., right?"},
            {"word": "晴れます", "reading": "はれます", "meaning": "to be sunny, clear up"},
            {"word": "疲れます", "reading": "つかれます", "meaning": "to get tired"},
            {"word": "病気", "reading": "びょうき", "meaning": "illness, sick"},
            {"word": "長い", "reading": "ながい", "meaning": "long"},
        ],
    },
    {
        "id": "n4-20",
        "title": "Keigo basics",
        "jp_title": "敬語の基本",
        "goal": "Recognize and use the most common respectful and humble expressions.",
        "points": [
            "**Respectful language** (尊敬語) raises the other person, with special verbs: **いらっしゃる** "
            "(be / go / come), **召し上がる** (eat / drink), **おっしゃる** (say), **ご覧になる** (see).",
            "**Humble language** (謙譲語) lowers yourself: **参る** (go / come), **申す** (say, give your name), "
            "**いただく** (receive / eat), **拝見する** (see).",
            "Regular verbs: respectful **お[ます-stem]になります** (お待ちになります); humble **お[ます-stem]します** (お持ちします).",
            "Fixed phrases you'll hear in shops: **いらっしゃいませ** (welcome), **少々お待ちください** (one moment please).",
        ],
        "examples": [
            {"jp": "先生はいらっしゃいますか。", "kana": "せんせいはいらっしゃいますか", "romaji": "sensei wa irasshaimasu ka", "en": "Is the teacher in?"},
            {"jp": "何を召し上がりますか。", "kana": "なにをめしあがりますか", "romaji": "nani o meshiagarimasu ka", "en": "What would you like to eat?"},
            {"jp": "私はスミスと申します。", "kana": "わたしはスミスともうします", "romaji": "watashi wa sumisu to moushimasu", "en": "My name is Smith. (humble)"},
            {"jp": "荷物をお持ちします。", "kana": "にもつをおもちします", "romaji": "nimotsu o omochi shimasu", "en": "Let me carry your luggage."},
            {"jp": "少々お待ちください。", "kana": "しょうしょうおまちください", "romaji": "shoushou omachi kudasai", "en": "One moment, please."},
        ],
        "vocab": [
            {"word": "いらっしゃいます", "reading": "いらっしゃいます", "meaning": "to be / go / come (respectful)"},
            {"word": "召し上がります", "reading": "めしあがります", "meaning": "to eat / drink (respectful)"},
            {"word": "申します", "reading": "もうします", "meaning": "to be called; to say (humble)"},
            {"word": "いただきます", "reading": "いただきます", "meaning": "to receive / eat (humble)"},
            {"word": "荷物", "reading": "にもつ", "meaning": "luggage, baggage"},
            {"word": "少々", "reading": "しょうしょう", "meaning": "a little, a moment (polite)"},
        ],
    },
    {
        "id": "n4-21",
        "title": "If: the ば conditional",
        "jp_title": "〜ば",
        "goal": "State a condition for a result, and say what you wish you had done.",
        "points": [
            "**ば-form**: most verbs change the い-sound before ます to the え-sound + ば: 行きます → 行けば, "
            "買います → 買えば. る-verbs: ます → **れば**: 食べれば. Irregular: **すれば**, **来れば** (kureba).",
            "い-adjectives: い → **ければ**: 安い → 安ければ; いい → よければ. Nouns and な-adjectives use **なら**: 暇なら.",
            "ば names the condition that leads to a result: 安ければ、買います。 Negative: 〜なければ: 急がなければ、遅れます。",
            "**〜ばよかった** = I wish I had ...: もっと勉強すればよかった。",
        ],
        "examples": [
            {"jp": "安ければ、買います。", "kana": "やすければ かいます", "romaji": "yasukereba, kaimasu", "en": "If it's cheap, I'll buy it."},
            {"jp": "毎日練習すれば、上手になります。", "kana": "まいにちれんしゅうすれば じょうずになります", "romaji": "mainichi renshuu sureba, jouzu ni narimasu", "en": "If you practice every day, you'll get good."},
            {"jp": "急がなければ、遅れますよ。", "kana": "いそがなければ おくれますよ", "romaji": "isoganakereba, okuremasu yo", "en": "If you don't hurry, you'll be late."},
            {"jp": "もっと勉強すればよかった。", "kana": "もっとべんきょうすればよかった", "romaji": "motto benkyou sureba yokatta", "en": "I wish I had studied more."},
        ],
        "vocab": [
            {"word": "練習", "reading": "れんしゅう", "meaning": "practice"},
            {"word": "急ぎます", "reading": "いそぎます", "meaning": "to hurry"},
            {"word": "遅れます", "reading": "おくれます", "meaning": "to be late"},
            {"word": "もっと", "reading": "もっと", "meaning": "more"},
            {"word": "間に合います", "reading": "まにあいます", "meaning": "to be in time"},
        ],
    },
    {
        "id": "n4-22",
        "title": "In order to: ために and ように",
        "jp_title": "〜ために・〜ように",
        "goal": "Say why you do something: for a goal, or so that something happens.",
        "points": [
            "**[dictionary form / noun の] + ために** = in order to, for: 日本に留学するために、お金を貯めています。 "
            "Use it with actions you decide to do.",
            "**[dictionary / potential / ない-form] + ように** = so that: 忘れないように、メモします。 "
            "Use it when the result isn't directly in your control (potential forms, ない, things that just happen).",
            "Rule of thumb: ために + an intentional verb; ように + 聞こえる, できる, 〜ない and similar.",
            "**〜ようにしています** = I make a point of ...: 毎日野菜を食べるようにしています。",
        ],
        "examples": [
            {"jp": "日本に留学するために、お金を貯めています。", "kana": "にほんにりゅうがくするために おかねをためています", "romaji": "nihon ni ryuugaku suru tame ni, okane o tamete imasu", "en": "I'm saving money to study in Japan."},
            {"jp": "健康のために、毎朝歩いています。", "kana": "けんこうのために まいあさあるいています", "romaji": "kenkou no tame ni, maiasa aruite imasu", "en": "I walk every morning for my health."},
            {"jp": "忘れないように、メモします。", "kana": "わすれないように メモします", "romaji": "wasurenai you ni, memo shimasu", "en": "I'll make a note so I don't forget."},
            {"jp": "後ろの人にも聞こえるように、大きい声で話してください。", "kana": "うしろのひとにもきこえるように おおきいこえではなしてください", "romaji": "ushiro no hito ni mo kikoeru you ni, ookii koe de hanashite kudasai", "en": "Please speak loudly so the people at the back can hear too."},
        ],
        "vocab": [
            {"word": "留学", "reading": "りゅうがく", "meaning": "studying abroad"},
            {"word": "貯めます", "reading": "ためます", "meaning": "to save (money)"},
            {"word": "健康", "reading": "けんこう", "meaning": "health"},
            {"word": "歩きます", "reading": "あるきます", "meaning": "to walk"},
            {"word": "声", "reading": "こえ", "meaning": "voice"},
            {"word": "聞こえます", "reading": "きこえます", "meaning": "to be audible, can hear"},
        ],
    },
    {
        "id": "n4-23",
        "title": "Too much: すぎる",
        "jp_title": "〜すぎる",
        "goal": "Say something is too much: too expensive, ate too much.",
        "points": [
            "**[ます-stem] + すぎます** = do too much: 食べすぎました \"I ate too much\".",
            "**Adjective without い / な + すぎます**: 高い → 高すぎます, 静か → 静かすぎます. いい → **よすぎます**.",
            "すぎる conjugates like a る-verb: すぎた, すぎない, すぎて.",
            "The て-form gives a reason: 難しすぎて、分かりません \"It's too hard, so I don't understand.\"",
        ],
        "examples": [
            {"jp": "昨日は飲みすぎました。", "kana": "きのうはのみすぎました", "romaji": "kinou wa nomisugimashita", "en": "I drank too much yesterday."},
            {"jp": "この靴は大きすぎます。", "kana": "このくつはおおきすぎます", "romaji": "kono kutsu wa ookisugimasu", "en": "These shoes are too big."},
            {"jp": "この問題は難しすぎて、分かりません。", "kana": "このもんだいはむずかしすぎて わかりません", "romaji": "kono mondai wa muzukashisugite, wakarimasen", "en": "This question is too difficult; I don't understand it."},
            {"jp": "部屋が静かすぎて、眠くなりました。", "kana": "へやがしずかすぎて ねむくなりました", "romaji": "heya ga shizukasugite, nemuku narimashita", "en": "The room was so quiet I got sleepy."},
        ],
        "vocab": [
            {"word": "すぎます", "reading": "すぎます", "meaning": "too much, over-"},
            {"word": "靴", "reading": "くつ", "meaning": "shoes"},
            {"word": "問題", "reading": "もんだい", "meaning": "problem; question"},
            {"word": "眠い", "reading": "ねむい", "meaning": "sleepy"},
            {"word": "少ない", "reading": "すくない", "meaning": "few, little"},
        ],
    },
    {
        "id": "n4-24",
        "title": "Easy or hard to do",
        "jp_title": "〜やすい・〜にくい",
        "goal": "Say whether something is easy or hard to do.",
        "points": [
            "**[ます-stem] + やすい** = easy to do: このペンは書きやすいです。",
            "**[ます-stem] + にくい** = hard to do: この本は字が小さくて読みにくいです。",
            "They behave like い-adjectives: 読みやすかった, 分かりにくくないです.",
            "易しい / 難しい describe a thing itself (an easy test); やすい / にくい describe how easy an action is.",
        ],
        "examples": [
            {"jp": "このペンは書きやすいです。", "kana": "このペンはかきやすいです", "romaji": "kono pen wa kakiyasui desu", "en": "This pen is easy to write with."},
            {"jp": "先生の説明は分かりやすいです。", "kana": "せんせいのせつめいはわかりやすいです", "romaji": "sensei no setsumei wa wakariyasui desu", "en": "The teacher's explanations are easy to understand."},
            {"jp": "この本は字が小さくて、読みにくいです。", "kana": "このほんはじがちいさくて よみにくいです", "romaji": "kono hon wa ji ga chiisakute, yominikui desu", "en": "The letters in this book are small, so it's hard to read."},
            {"jp": "この靴は歩きにくいです。", "kana": "このくつはあるきにくいです", "romaji": "kono kutsu wa arukinikui desu", "en": "These shoes are hard to walk in."},
        ],
        "vocab": [
            {"word": "説明", "reading": "せつめい", "meaning": "explanation"},
            {"word": "字", "reading": "じ", "meaning": "character, letter; handwriting"},
            {"word": "易しい", "reading": "やさしい", "meaning": "easy, simple"},
            {"word": "便利", "reading": "べんり", "meaning": "convenient"},
            {"word": "不便", "reading": "ふべん", "meaning": "inconvenient"},
        ],
    },
    {
        "id": "n4-25",
        "title": "And what's more: 〜し",
        "jp_title": "〜し、〜し",
        "goal": "List several reasons or points that add up to a conclusion.",
        "points": [
            "**[plain form] + し** lists reasons or points: この店は安いし、おいしいし、よく来ます。",
            "Nouns and な-adjectives take **だ**: 雨だし, 静かだし.",
            "One し on its own hints there are more reasons: 時間もないし、今日はやめます。",
            "It often pairs with **も** (\"also\"): 広いし、駅にも近いです。",
        ],
        "examples": [
            {"jp": "この店は安いし、おいしいし、よく来ます。", "kana": "このみせはやすいし おいしいし よくきます", "romaji": "kono mise wa yasui shi, oishii shi, yoku kimasu", "en": "This place is cheap and tasty, so I come here often."},
            {"jp": "今日は雨だし、寒いし、出かけたくないです。", "kana": "きょうはあめだし さむいし でかけたくないです", "romaji": "kyou wa ame da shi, samui shi, dekaketakunai desu", "en": "It's raining and cold today, so I don't want to go out."},
            {"jp": "この部屋は広いし、駅にも近いです。", "kana": "このへやはひろいし えきにもちかいです", "romaji": "kono heya wa hiroi shi, eki ni mo chikai desu", "en": "This room is spacious, and it's close to the station too."},
            {"jp": "時間もないし、今日はやめます。", "kana": "じかんもないし きょうはやめます", "romaji": "jikan mo nai shi, kyou wa yamemasu", "en": "I don't have time (among other things), so I'll skip it today."},
        ],
        "vocab": [
            {"word": "し", "reading": "し", "meaning": "and (what's more)"},
            {"word": "広い", "reading": "ひろい", "meaning": "spacious, wide"},
            {"word": "近い", "reading": "ちかい", "meaning": "near, close"},
            {"word": "遠い", "reading": "とおい", "meaning": "far"},
            {"word": "時間", "reading": "じかん", "meaning": "time"},
        ],
    },
    {
        "id": "n4-26",
        "title": "Should be: はずです",
        "jp_title": "〜はずです",
        "goal": "Say what you expect to be true, based on what you know.",
        "points": [
            "**[plain form] + はずです** = should be, is expected to: 田中さんはもう家に着いたはずです。",
            "Nouns take **の**: 休みのはずです; な-adjectives take **な**: 静かなはずです.",
            "**〜はずがありません** = there's no way that ...: そんなはずがありません。",
            "はず is about expectation, not advice. For \"you should do\" use 〜たほうがいいです.",
        ],
        "examples": [
            {"jp": "田中さんはもう家に着いたはずです。", "kana": "たなかさんはもういえについたはずです", "romaji": "tanaka san wa mou ie ni tsuita hazu desu", "en": "Mr. Tanaka should be home by now."},
            {"jp": "今日は日曜日だから、銀行は休みのはずです。", "kana": "きょうはにちようびだから ぎんこうはやすみのはずです", "romaji": "kyou wa nichiyoubi da kara, ginkou wa yasumi no hazu desu", "en": "It's Sunday, so the bank should be closed."},
            {"jp": "薬を飲んだから、すぐ治るはずです。", "kana": "くすりをのんだから すぐなおるはずです", "romaji": "kusuri o nonda kara, sugu naoru hazu desu", "en": "I took medicine, so I should get better soon."},
            {"jp": "そんなはずがありません。", "kana": "そんなはずがありません", "romaji": "sonna hazu ga arimasen", "en": "That can't be right."},
        ],
        "vocab": [
            {"word": "はず", "reading": "はず", "meaning": "should (be), expected to"},
            {"word": "家", "reading": "いえ", "meaning": "house, home"},
            {"word": "治ります", "reading": "なおります", "meaning": "to get better, heal"},
            {"word": "銀行", "reading": "ぎんこう", "meaning": "bank"},
            {"word": "すぐ", "reading": "すぐ", "meaning": "soon, right away"},
        ],
    },
    {
        "id": "n4-27",
        "title": "Seems like: ようだ, みたい, らしい",
        "jp_title": "〜ようです・〜みたい・〜らしい",
        "goal": "Say how things seem, based on what you notice or what you've heard.",
        "points": [
            "**[plain form] + ようです** = it seems (from what I notice): 誰か部屋にいるようです。 Nouns: のようです; な-adjectives: なようです.",
            "**みたいです** is the casual version: 風邪をひいたみたいです。 Nouns and な-adjectives attach directly: 子供みたい.",
            "**らしいです** = apparently (from what others say): 来週、テストがあるらしいです。",
            "みたい and ようだ also mean \"like\" (resemblance): 夢みたいです \"It's like a dream.\"",
        ],
        "examples": [
            {"jp": "誰か部屋にいるようです。", "kana": "だれかへやにいるようです", "romaji": "dareka heya ni iru you desu", "en": "It seems someone is in the room."},
            {"jp": "風邪をひいたみたいです。", "kana": "かぜをひいたみたいです", "romaji": "kaze o hiita mitai desu", "en": "I think I've caught a cold."},
            {"jp": "来週、テストがあるらしいです。", "kana": "らいしゅう テストがあるらしいです", "romaji": "raishuu, tesuto ga aru rashii desu", "en": "Apparently there's a test next week."},
            {"jp": "夢みたいです。", "kana": "ゆめみたいです", "romaji": "yume mitai desu", "en": "It's like a dream."},
        ],
        "vocab": [
            {"word": "ようです", "reading": "ようです", "meaning": "it seems"},
            {"word": "みたい", "reading": "みたい", "meaning": "seems; like (casual)"},
            {"word": "らしい", "reading": "らしい", "meaning": "apparently, I hear"},
            {"word": "夢", "reading": "ゆめ", "meaning": "dream"},
            {"word": "誰か", "reading": "だれか", "meaning": "someone"},
        ],
    },
    {
        "id": "n4-28",
        "title": "Try doing: てみる",
        "jp_title": "〜てみる",
        "goal": "Say you'll try something to see what it's like.",
        "points": [
            "**[て-form] + みます** = try doing (to see how it is): 着物を着てみたいです。",
            "Past: **〜てみました** = I tried it: 納豆を食べてみましたが、苦手でした。",
            "**〜てみてください** is a friendly suggestion: このケーキ、食べてみてください。",
            "てみる means \"do it and see\"; it doesn't mean struggling to manage something.",
        ],
        "examples": [
            {"jp": "一度着物を着てみたいです。", "kana": "いちどきものをきてみたいです", "romaji": "ichido kimono o kite mitai desu", "en": "I'd like to try wearing a kimono once."},
            {"jp": "納豆を食べてみましたが、苦手でした。", "kana": "なっとうをたべてみましたが にがてでした", "romaji": "nattou o tabete mimashita ga, nigate deshita", "en": "I tried natto, but I didn't like it."},
            {"jp": "このケーキ、食べてみてください。", "kana": "このケーキ たべてみてください", "romaji": "kono keeki, tabete mite kudasai", "en": "Try this cake."},
            {"jp": "新しいレストランに行ってみましょう。", "kana": "あたらしいレストランにいってみましょう", "romaji": "atarashii resutoran ni itte mimashou", "en": "Let's try the new restaurant."},
        ],
        "vocab": [
            {"word": "着物", "reading": "きもの", "meaning": "kimono"},
            {"word": "着ます", "reading": "きます", "meaning": "to wear (clothes on the body)"},
            {"word": "納豆", "reading": "なっとう", "meaning": "natto (fermented soybeans)"},
            {"word": "苦手", "reading": "にがて", "meaning": "weak at; not fond of"},
            {"word": "レストラン", "reading": "レストラン", "meaning": "restaurant"},
        ],
    },
    {
        "id": "n4-29",
        "title": "Verbs as nouns: の and こと",
        "jp_title": "〜の・〜こと",
        "goal": "Turn actions into nouns to talk about likes, hobbies and abilities.",
        "points": [
            "Add **の** or **こと** to a plain verb to use it as a noun: 本を読むのが好きです \"I like reading books.\"",
            "With 好き, 嫌い, 上手, 下手 and verbs like 忘れる, **の** is the usual choice: 窓を閉めるのを忘れました。",
            "**こと** is used before です and in set phrases: 趣味は写真を撮ることです; "
            "**〜ことができます** = can do (a little more formal than the potential form).",
            "For things you see or hear happening, only の works: 子供が歌うのを聞きました。",
        ],
        "examples": [
            {"jp": "本を読むのが好きです。", "kana": "ほんをよむのがすきです", "romaji": "hon o yomu no ga suki desu", "en": "I like reading books."},
            {"jp": "窓を閉めるのを忘れました。", "kana": "まどをしめるのをわすれました", "romaji": "mado o shimeru no o wasuremashita", "en": "I forgot to close the window."},
            {"jp": "私の趣味は写真を撮ることです。", "kana": "わたしのしゅみはしゃしんをとることです", "romaji": "watashi no shumi wa shashin o toru koto desu", "en": "My hobby is taking photos."},
            {"jp": "ピアノを弾くことができます。", "kana": "ピアノをひくことができます", "romaji": "piano o hiku koto ga dekimasu", "en": "I can play the piano."},
        ],
        "vocab": [
            {"word": "趣味", "reading": "しゅみ", "meaning": "hobby"},
            {"word": "嫌い", "reading": "きらい", "meaning": "disliked (to dislike)"},
            {"word": "弾きます", "reading": "ひきます", "meaning": "to play (piano, guitar)"},
            {"word": "歌います", "reading": "うたいます", "meaning": "to sing"},
            {"word": "ピアノ", "reading": "ピアノ", "meaning": "piano"},
        ],
    },
    {
        "id": "n4-30",
        "title": "Doing vs happening: 開ける and 開く",
        "jp_title": "自動詞・他動詞",
        "goal": "Choose between verb pairs like 開ける (open something) and 開く (something opens).",
        "points": [
            "Many verbs come in pairs: a **transitive** one (someone does it, the thing takes を) and an "
            "**intransitive** one (it happens, the thing takes が): ドアを開けます / ドアが開きます.",
            "Common pairs: 開ける / 開く, 閉める / 閉まる, つける / つく (light on), 消す / 消える (off), "
            "始める / 始まる, 入れる / 入る.",
            "**[intransitive] + ています** describes the resulting state: 電気がついています \"The light is on.\"",
            "**[transitive] + てあります** means someone did it deliberately and it stays that way: "
            "机の上に花が飾ってあります \"Flowers have been placed on the desk.\"",
        ],
        "examples": [
            {"jp": "ドアを開けます。", "kana": "ドアをあけます", "romaji": "doa o akemasu", "en": "I open the door."},
            {"jp": "ドアが開きます。", "kana": "ドアがあきます", "romaji": "doa ga akimasu", "en": "The door opens."},
            {"jp": "電気がついています。", "kana": "でんきがついています", "romaji": "denki ga tsuite imasu", "en": "The light is on."},
            {"jp": "授業は九時に始まります。", "kana": "じゅぎょうはくじにはじまります", "romaji": "jugyou wa kuji ni hajimarimasu", "en": "Class starts at nine."},
            {"jp": "机の上に花が飾ってあります。", "kana": "つくえのうえにはながかざってあります", "romaji": "tsukue no ue ni hana ga kazatte arimasu", "en": "Flowers have been placed on the desk."},
        ],
        "vocab": [
            {"word": "開けます", "reading": "あけます", "meaning": "to open (something)"},
            {"word": "開きます", "reading": "あきます", "meaning": "(something) opens"},
            {"word": "閉まります", "reading": "しまります", "meaning": "(something) closes"},
            {"word": "消します", "reading": "けします", "meaning": "to turn off; to erase"},
            {"word": "始まります", "reading": "はじまります", "meaning": "(something) begins"},
            {"word": "電気", "reading": "でんき", "meaning": "electricity; light"},
        ],
    },
    # ------------------------------------------------------------------ N3
    {
        "id": "n3-01",
        "title": "About to, in the middle of, just did",
        "jp_title": "〜ところです",
        "goal": "Say exactly where you are in an action: about to start, in the middle of it, or just finished.",
        "points": [
            "**[dictionary form] + ところです** = about to do it: 今から出かけるところです。 \"I'm just about to go out.\"",
            "**[て-form] + いるところです** = in the middle of doing it right now: 今、昼ご飯を食べているところです。",
            "**[た-form] + ところです** = have just done it, moments ago: 今、駅に着いたところです。",
            "These often answer 今、何をしていますか or もう〜ましたか. With friends, drop です: 出かけるところ。",
        ],
        "examples": [
            {"jp": "今から出かけるところです。", "kana": "いまからでかけるところです", "romaji": "ima kara dekakeru tokoro desu", "en": "I'm just about to go out."},
            {"jp": "今、昼ご飯を食べているところです。", "kana": "いま ひるごはんをたべているところです", "romaji": "ima, hirugohan o tabete iru tokoro desu", "en": "I'm eating lunch right now."},
            {"jp": "今、駅に着いたところです。", "kana": "いま えきについたところです", "romaji": "ima, eki ni tsuita tokoro desu", "en": "I've just arrived at the station."},
            {"jp": "ちょうど宿題が終わったところです。", "kana": "ちょうどしゅくだいがおわったところです", "romaji": "choudo shukudai ga owatta tokoro desu", "en": "I've just finished my homework."},
        ],
        "vocab": [
            {"word": "ところ", "reading": "ところ", "meaning": "point, moment (in an action)"},
            {"word": "出かけます", "reading": "でかけます", "meaning": "to go out"},
            {"word": "着きます", "reading": "つきます", "meaning": "to arrive"},
            {"word": "ちょうど", "reading": "ちょうど", "meaning": "just, exactly"},
            {"word": "昼ご飯", "reading": "ひるごはん", "meaning": "lunch"},
            {"word": "宿題", "reading": "しゅくだい", "meaning": "homework"},
        ],
    },
    {
        "id": "n3-02",
        "title": "While you still can",
        "jp_title": "〜うちに",
        "goal": "Say to do something while a situation lasts, before it changes.",
        "points": [
            "**[state] + うちに** = while it is still that way, before it changes: 若いうちに, 温かいうちに, 学生のうちに.",
            "い-adjectives attach directly (温かいうちに), な-adjectives take な (元気なうちに), nouns take の (学生のうちに). "
            "Negatives work too: 雨が降らないうちに \"before it starts raining\".",
            "Often used for advice: 温かいうちに食べてください。 \"Please eat it while it's warm.\"",
            "**[verb ている] + うちに** can mean \"while doing it, something happened without you noticing\": "
            "本を読んでいるうちに、寝てしまいました。",
        ],
        "examples": [
            {"jp": "温かいうちに食べてください。", "kana": "あたたかいうちにたべてください", "romaji": "atatakai uchi ni tabete kudasai", "en": "Please eat it while it's warm."},
            {"jp": "学生のうちに、いろいろな国に行きたいです。", "kana": "がくせいのうちに いろいろなくににいきたいです", "romaji": "gakusei no uchi ni, iroiro na kuni ni ikitai desu", "en": "I want to go to lots of countries while I'm still a student."},
            {"jp": "雨が降らないうちに帰りましょう。", "kana": "あめがふらないうちにかえりましょう", "romaji": "ame ga furanai uchi ni kaerimashou", "en": "Let's go home before it starts raining."},
            {"jp": "本を読んでいるうちに、寝てしまいました。", "kana": "ほんをよんでいるうちに ねてしまいました", "romaji": "hon o yonde iru uchi ni, nete shimaimashita", "en": "While I was reading, I fell asleep."},
        ],
        "vocab": [
            {"word": "うちに", "reading": "うちに", "meaning": "while (still), before it changes"},
            {"word": "温かい", "reading": "あたたかい", "meaning": "warm (food, drinks, feelings)"},
            {"word": "若い", "reading": "わかい", "meaning": "young"},
            {"word": "明るい", "reading": "あかるい", "meaning": "bright, light"},
            {"word": "寝ます", "reading": "ねます", "meaning": "to sleep, to go to bed"},
        ],
    },
    {
        "id": "n3-03",
        "title": "Nothing but..., just did",
        "jp_title": "〜ばかり",
        "goal": "Complain that someone does only one thing, and say something happened only recently.",
        "points": [
            "**[noun] + ばかり** = nothing but, only (often a complaint): 弟はゲームばかりしています。",
            "**[て-form] + ばかりいます** = do nothing but ...: 毎日寝てばかりいます。",
            "**[た-form] + ばかりです** = just did, recently (it still feels new): 先月日本に来たばかりです。",
            "Compare たところ: 着いたところ is exact and moments ago; 来たばかり can be weeks ago, as long as it feels recent.",
        ],
        "examples": [
            {"jp": "弟はゲームばかりしています。", "kana": "おとうとはゲームばかりしています", "romaji": "otouto wa geemu bakari shite imasu", "en": "My little brother does nothing but play games."},
            {"jp": "毎日寝てばかりいます。", "kana": "まいにちねてばかりいます", "romaji": "mainichi nete bakari imasu", "en": "I do nothing but sleep every day."},
            {"jp": "先月日本に来たばかりです。", "kana": "せんげつにほんにきたばかりです", "romaji": "sengetsu nihon ni kita bakari desu", "en": "I only came to Japan last month."},
            {"jp": "このパソコンは買ったばかりなのに、もう壊れました。", "kana": "このパソコンはかったばかりなのに もうこわれました", "romaji": "kono pasokon wa katta bakari na noni, mou kowaremashita", "en": "I only just bought this computer, and it's already broken."},
        ],
        "vocab": [
            {"word": "ばかり", "reading": "ばかり", "meaning": "only, nothing but; just (did)"},
            {"word": "弟", "reading": "おとうと", "meaning": "younger brother"},
            {"word": "先月", "reading": "せんげつ", "meaning": "last month"},
            {"word": "壊れます", "reading": "こわれます", "meaning": "to break (by itself)"},
            {"word": "パソコン", "reading": "パソコン", "meaning": "personal computer"},
        ],
    },
    {
        "id": "n3-04",
        "title": "That's why, it doesn't mean",
        "jp_title": "〜わけだ・〜わけではない",
        "goal": "Draw a conclusion, soften a statement, and say something is impossible.",
        "points": [
            "**[plain form] + わけです** = so that's why, no wonder: 十年も住んでいたんですか。上手なわけですね。",
            "**わけではありません** = it's not that ..., it doesn't necessarily mean ...: 嫌いなわけではありません。 "
            "\"It's not that I dislike it.\"",
            "**わけがない** = there's no way that ...: こんな難しい問題、できるわけがない。",
            "な-adjectives take な (上手なわけ), nouns take の or という (学生というわけではない).",
        ],
        "examples": [
            {"jp": "十年も日本に住んでいたんですか。上手なわけですね。", "kana": "じゅうねんもにほんにすんでいたんですか じょうずなわけですね", "romaji": "juunen mo nihon ni sunde ita n desu ka. jouzu na wake desu ne", "en": "You lived in Japan for ten years? No wonder you're so good."},
            {"jp": "肉が嫌いなわけではありません。", "kana": "にくがきらいなわけではありません", "romaji": "niku ga kirai na wake de wa arimasen", "en": "It's not that I dislike meat."},
            {"jp": "高い物がいつもいいわけではありません。", "kana": "たかいものがいつもいいわけではありません", "romaji": "takai mono ga itsumo ii wake de wa arimasen", "en": "Expensive things aren't always good."},
            {"jp": "こんな難しい問題、私にできるわけがない。", "kana": "こんなむずかしいもんだい わたしにできるわけがない", "romaji": "konna muzukashii mondai, watashi ni dekiru wake ga nai", "en": "There's no way I can do such a hard problem."},
        ],
        "vocab": [
            {"word": "わけ", "reading": "わけ", "meaning": "reason, meaning; conclusion"},
            {"word": "嫌い", "reading": "きらい", "meaning": "disliked"},
            {"word": "肉", "reading": "にく", "meaning": "meat"},
            {"word": "問題", "reading": "もんだい", "meaning": "problem, question"},
            {"word": "住みます", "reading": "すみます", "meaning": "to live (somewhere)"},
            {"word": "こんな", "reading": "こんな", "meaning": "this kind of, such a"},
        ],
    },
    {
        "id": "n3-05",
        "title": "About, toward, for",
        "jp_title": "〜について・〜に対して・〜にとって",
        "goal": "Name the topic, the target, and the point of view of a sentence.",
        "points": [
            "**[noun] + について** = about, concerning a topic: 日本の歴史について調べています。",
            "**[noun] + に対して** = toward, to (the person or thing your attitude or action is aimed at): "
            "子供に対して、優しく話してください。",
            "**[noun] + にとって** = for, from someone's point of view: 私にとって、家族が一番大切です。",
            "Before a noun, use **についての** and **に対する**: 日本についての本, 質問に対する答え.",
        ],
        "examples": [
            {"jp": "日本の歴史について調べています。", "kana": "にほんのれきしについてしらべています", "romaji": "nihon no rekishi ni tsuite shirabete imasu", "en": "I'm looking into Japanese history."},
            {"jp": "私にとって、家族が一番大切です。", "kana": "わたしにとって かぞくがいちばんたいせつです", "romaji": "watashi ni totte, kazoku ga ichiban taisetsu desu", "en": "For me, family is the most important thing."},
            {"jp": "子供に対して、優しく話してください。", "kana": "こどもにたいして やさしくはなしてください", "romaji": "kodomo ni taishite, yasashiku hanashite kudasai", "en": "Please speak gently to children."},
            {"jp": "質問に対する答えを書いてください。", "kana": "しつもんにたいするこたえをかいてください", "romaji": "shitsumon ni taisuru kotae o kaite kudasai", "en": "Please write the answers to the questions."},
        ],
        "vocab": [
            {"word": "歴史", "reading": "れきし", "meaning": "history"},
            {"word": "調べます", "reading": "しらべます", "meaning": "to look into, to look up"},
            {"word": "大切", "reading": "たいせつ", "meaning": "important, precious"},
            {"word": "優しい", "reading": "やさしい", "meaning": "kind, gentle"},
            {"word": "答え", "reading": "こたえ", "meaning": "answer"},
            {"word": "家族", "reading": "かぞく", "meaning": "family"},
        ],
    },
    {
        "id": "n3-06",
        "title": "By, depending on, because of",
        "jp_title": "〜によって・〜による",
        "goal": "Use によって for \"depending on\", \"by\" (who did it) and \"because of\".",
        "points": [
            "**[noun] + によって** has three common uses. 1) **depending on**: 人によって考え方が違います。",
            "2) **by**, naming who made something in a passive sentence: この本は有名な作家によって書かれました。",
            "3) **because of, due to** (formal, as on the news): 台風によって電車が止まりました。",
            "Before a noun use **による**: 台風による被害 \"damage caused by the typhoon\". "
            "**によっては** = in some cases: 国によっては…",
        ],
        "examples": [
            {"jp": "人によって考え方が違います。", "kana": "ひとによってかんがえかたがちがいます", "romaji": "hito ni yotte kangaekata ga chigaimasu", "en": "Ways of thinking differ from person to person."},
            {"jp": "この本は有名な作家によって書かれました。", "kana": "このほんはゆうめいなさっかによってかかれました", "romaji": "kono hon wa yuumei na sakka ni yotte kakaremashita", "en": "This book was written by a famous author."},
            {"jp": "台風によって電車が止まりました。", "kana": "たいふうによってでんしゃがとまりました", "romaji": "taifuu ni yotte densha ga tomarimashita", "en": "The trains stopped because of the typhoon."},
            {"jp": "季節によって、景色が変わります。", "kana": "きせつによって けしきがかわります", "romaji": "kisetsu ni yotte, keshiki ga kawarimasu", "en": "The scenery changes with the seasons."},
        ],
        "vocab": [
            {"word": "考え方", "reading": "かんがえかた", "meaning": "way of thinking"},
            {"word": "作家", "reading": "さっか", "meaning": "author, writer"},
            {"word": "台風", "reading": "たいふう", "meaning": "typhoon"},
            {"word": "季節", "reading": "きせつ", "meaning": "season"},
            {"word": "景色", "reading": "けしき", "meaning": "scenery, view"},
            {"word": "違います", "reading": "ちがいます", "meaning": "to differ; to be wrong"},
        ],
    },
    {
        "id": "n3-07",
        "title": "Thanks to, because of",
        "jp_title": "〜おかげで・〜せいで",
        "goal": "Give credit for a good result and blame the cause of a bad one.",
        "points": [
            "**おかげで** = thanks to (a good result): 先生のおかげで、試験に合格しました。",
            "**せいで** = because of, blaming the cause of a bad result: 雨のせいで、試合が中止になりました。",
            "Nouns take の, verbs and い-adjectives use the plain form, な-adjectives take な: "
            "薬を飲んだおかげで, 寝坊したせいで, 静かなおかげで.",
            "**おかげさまで** is a set polite phrase: \"I'm well, thank you.\" **〜せいか** = maybe because of.",
        ],
        "examples": [
            {"jp": "先生のおかげで、試験に合格しました。", "kana": "せんせいのおかげで しけんにごうかくしました", "romaji": "sensei no okage de, shiken ni goukaku shimashita", "en": "Thanks to my teacher, I passed the exam."},
            {"jp": "雨のせいで、試合が中止になりました。", "kana": "あめのせいで しあいがちゅうしになりました", "romaji": "ame no sei de, shiai ga chuushi ni narimashita", "en": "Because of the rain, the match was called off."},
            {"jp": "薬を飲んだおかげで、よくなりました。", "kana": "くすりをのんだおかげで よくなりました", "romaji": "kusuri o nonda okage de, yoku narimashita", "en": "Thanks to taking the medicine, I got better."},
            {"jp": "寝坊したせいで、バスに乗り遅れました。", "kana": "ねぼうしたせいで バスにのりおくれました", "romaji": "nebou shita sei de, basu ni noriokuremashita", "en": "I overslept, so I missed the bus."},
        ],
        "vocab": [
            {"word": "合格", "reading": "ごうかく", "meaning": "passing (an exam)"},
            {"word": "試合", "reading": "しあい", "meaning": "match, game"},
            {"word": "中止", "reading": "ちゅうし", "meaning": "cancellation, calling off"},
            {"word": "寝坊", "reading": "ねぼう", "meaning": "oversleeping"},
            {"word": "乗り遅れます", "reading": "のりおくれます", "meaning": "to miss (a train, bus)"},
            {"word": "薬", "reading": "くすり", "meaning": "medicine"},
        ],
    },
    {
        "id": "n3-08",
        "title": "Trying to, making a point of",
        "jp_title": "〜ようとする・〜ようにする",
        "goal": "Describe an attempt, a refusal, and an effort you make regularly.",
        "points": [
            "**[volitional form] + とする** = try to, be about to (often interrupted): "
            "出かけようとしたとき、雨が降り出しました。",
            "**[volitional form] + としない** = won't even try, refuses to: 弟は野菜を食べようとしません。",
            "**[dictionary or ない form] + ようにする** = make a point of, try to (as a habit): "
            "毎日野菜を食べるようにしています。 夜遅くまでゲームをしないようにしています。",
            "Compare ようになる (N4): a change that just happens. ようにする: something you do on purpose.",
        ],
        "examples": [
            {"jp": "出かけようとしたとき、雨が降り出しました。", "kana": "でかけようとしたとき あめがふりだしました", "romaji": "dekakeyou to shita toki, ame ga furidashimashita", "en": "Just as I was about to go out, it started to rain."},
            {"jp": "弟は野菜を食べようとしません。", "kana": "おとうとはやさいをたべようとしません", "romaji": "otouto wa yasai o tabeyou to shimasen", "en": "My little brother won't even try to eat vegetables."},
            {"jp": "毎日野菜を食べるようにしています。", "kana": "まいにちやさいをたべるようにしています", "romaji": "mainichi yasai o taberu you ni shite imasu", "en": "I make a point of eating vegetables every day."},
            {"jp": "夜遅くまでゲームをしないようにしています。", "kana": "よるおそくまでゲームをしないようにしています", "romaji": "yoru osoku made geemu o shinai you ni shite imasu", "en": "I try not to play games until late at night."},
        ],
        "vocab": [
            {"word": "野菜", "reading": "やさい", "meaning": "vegetables"},
            {"word": "降り出します", "reading": "ふりだします", "meaning": "to start to rain or snow"},
            {"word": "遅く", "reading": "おそく", "meaning": "late (adverb)"},
            {"word": "甘い", "reading": "あまい", "meaning": "sweet"},
            {"word": "健康", "reading": "けんこう", "meaning": "health"},
        ],
    },
    {
        "id": "n3-09",
        "title": "Leaving things as they are",
        "jp_title": "〜まま・〜ずに",
        "goal": "Say that something stayed the same, and that you did something without doing something else.",
        "points": [
            "**[た-form] + まま** = with something left as it is: 窓を開けたまま寝てしまいました。 "
            "\"I fell asleep with the window open.\"",
            "Nouns take の and adjectives attach as usual: 子供のまま, 若いまま, きれいなまま. "
            "**このまま / そのまま** = like this / as it is: そのままでいいです。",
            "**[ない-stem] + ずに** = without doing (a more written ないで): 朝ご飯を食べずに出かけました。",
            "する becomes **せずに**: 勉強せずに試験を受けました。",
        ],
        "examples": [
            {"jp": "窓を開けたまま寝てしまいました。", "kana": "まどをあけたまま ねてしまいました", "romaji": "mado o aketa mama nete shimaimashita", "en": "I fell asleep with the window open."},
            {"jp": "靴をはいたまま入らないでください。", "kana": "くつをはいたまま はいらないでください", "romaji": "kutsu o haita mama hairanaide kudasai", "en": "Please don't come in with your shoes on."},
            {"jp": "朝ご飯を食べずに出かけました。", "kana": "あさごはんをたべずに でかけました", "romaji": "asagohan o tabezu ni dekakemashita", "en": "I went out without eating breakfast."},
            {"jp": "勉強せずに試験を受けました。", "kana": "べんきょうせずに しけんをうけました", "romaji": "benkyou sezu ni shiken o ukemashita", "en": "I took the exam without studying."},
        ],
        "vocab": [
            {"word": "まま", "reading": "まま", "meaning": "as it is, unchanged"},
            {"word": "窓", "reading": "まど", "meaning": "window"},
            {"word": "靴", "reading": "くつ", "meaning": "shoes"},
            {"word": "はきます", "reading": "はきます", "meaning": "to put on, wear (shoes, trousers)"},
            {"word": "受けます", "reading": "うけます", "meaning": "to take (an exam)"},
            {"word": "そのまま", "reading": "そのまま", "meaning": "as it is"},
        ],
    },
    {
        "id": "n3-10",
        "title": "It's been decided",
        "jp_title": "〜ことになる・〜ことになっている",
        "goal": "Report decisions and rules without making them sound like your own choice.",
        "points": [
            "**[dictionary or ない form] + ことになりました** = it has been decided (by others, or by circumstances): "
            "来月、大阪に引っ越すことになりました。",
            "Compare ことにする (N4): **you** decide. ことになる sounds modest, so people use it even for their own plans.",
            "**ことになっています** = it's the rule, it's arranged that way: この部屋では靴を脱ぐことになっています。",
            "Negative rules use the ない form: 図書館では話さないことになっています。",
        ],
        "examples": [
            {"jp": "来月、大阪に引っ越すことになりました。", "kana": "らいげつ おおさかにひっこすことになりました", "romaji": "raigetsu, oosaka ni hikkosu koto ni narimashita", "en": "It's been decided that I'm moving to Osaka next month."},
            {"jp": "夏休みに、家族で旅行することになりました。", "kana": "なつやすみに かぞくでりょこうすることになりました", "romaji": "natsuyasumi ni, kazoku de ryokou suru koto ni narimashita", "en": "We've decided to take a family trip in the summer holidays."},
            {"jp": "この部屋では靴を脱ぐことになっています。", "kana": "このへやではくつをぬぐことになっています", "romaji": "kono heya de wa kutsu o nugu koto ni natte imasu", "en": "In this room, you take your shoes off."},
            {"jp": "図書館では話さないことになっています。", "kana": "としょかんでははなさないことになっています", "romaji": "toshokan de wa hanasanai koto ni natte imasu", "en": "You're not supposed to talk in the library."},
        ],
        "vocab": [
            {"word": "引っ越します", "reading": "ひっこします", "meaning": "to move (house)"},
            {"word": "脱ぎます", "reading": "ぬぎます", "meaning": "to take off (clothes, shoes)"},
            {"word": "決まります", "reading": "きまります", "meaning": "to be decided"},
            {"word": "規則", "reading": "きそく", "meaning": "rule"},
            {"word": "旅行", "reading": "りょこう", "meaning": "trip, travel"},
            {"word": "図書館", "reading": "としょかん", "meaning": "library"},
        ],
    },
    {
        "id": "n3-11",
        "title": "Every time",
        "jp_title": "〜たびに",
        "goal": "Say that something happens each and every time another thing happens.",
        "points": [
            "**[dictionary form] + たびに** = every time ...: この歌を聞くたびに、子供の頃を思い出します。",
            "Nouns take の: 旅行のたびに、お土産を買います。",
            "The second half is something that happens naturally or by habit, not a one-off request or plan.",
            "Compare **〜と** (N4), which can also mean \"whenever\". たびに stresses \"each and every time\", often with a feeling.",
        ],
        "examples": [
            {"jp": "この歌を聞くたびに、子供の頃を思い出します。", "kana": "このうたをきくたびに こどものころをおもいだします", "romaji": "kono uta o kiku tabi ni, kodomo no koro o omoidashimasu", "en": "Every time I hear this song, I remember my childhood."},
            {"jp": "旅行のたびに、お土産を買います。", "kana": "りょこうのたびに おみやげをかいます", "romaji": "ryokou no tabi ni, omiyage o kaimasu", "en": "I buy souvenirs every time I travel."},
            {"jp": "雨が降るたびに、この道は水でいっぱいになります。", "kana": "あめがふるたびに このみちはみずでいっぱいになります", "romaji": "ame ga furu tabi ni, kono michi wa mizu de ippai ni narimasu", "en": "Every time it rains, this road fills with water."},
            {"jp": "引っ越しのたびに、物が増えます。", "kana": "ひっこしのたびに ものがふえます", "romaji": "hikkoshi no tabi ni, mono ga fuemasu", "en": "Every time I move house, I end up with more stuff."},
        ],
        "vocab": [
            {"word": "たびに", "reading": "たびに", "meaning": "every time"},
            {"word": "思い出します", "reading": "おもいだします", "meaning": "to remember, to recall"},
            {"word": "頃", "reading": "ころ", "meaning": "(around the) time, days (子供の頃 = childhood)"},
            {"word": "お土産", "reading": "おみやげ", "meaning": "souvenir"},
            {"word": "増えます", "reading": "ふえます", "meaning": "to increase"},
            {"word": "道", "reading": "みち", "meaning": "road, way"},
        ],
    },
    {
        "id": "n3-12",
        "title": "The more..., the more",
        "jp_title": "〜ば〜ほど",
        "goal": "Say that as one thing increases, another changes with it.",
        "points": [
            "**[ば-form] + [the same word, dictionary form] + ほど** = the more ..., the more ...: "
            "練習すればするほど、上手になります。",
            "い-adjectives: 高ければ高いほど. な-adjectives: 静かなら静かなほど.",
            "The ば part can be left out: 日本語は勉強するほど面白くなります。",
            "**ほど** alone means \"not as ... as\" with a negative: 今日は昨日ほど寒くありません。",
        ],
        "examples": [
            {"jp": "練習すればするほど、上手になります。", "kana": "れんしゅうすればするほど じょうずになります", "romaji": "renshuu sureba suru hodo, jouzu ni narimasu", "en": "The more you practise, the better you get."},
            {"jp": "野菜は新しければ新しいほどおいしいです。", "kana": "やさいはあたらしければあたらしいほどおいしいです", "romaji": "yasai wa atarashikereba atarashii hodo oishii desu", "en": "The fresher vegetables are, the better they taste."},
            {"jp": "日本語は勉強するほど面白くなります。", "kana": "にほんごはべんきょうするほどおもしろくなります", "romaji": "nihongo wa benkyou suru hodo omoshiroku narimasu", "en": "The more you study Japanese, the more interesting it gets."},
            {"jp": "今日は昨日ほど寒くありません。", "kana": "きょうはきのうほどさむくありません", "romaji": "kyou wa kinou hodo samuku arimasen", "en": "Today isn't as cold as yesterday."},
        ],
        "vocab": [
            {"word": "ほど", "reading": "ほど", "meaning": "extent; (not) as ... as"},
            {"word": "練習", "reading": "れんしゅう", "meaning": "practice"},
            {"word": "新しい", "reading": "あたらしい", "meaning": "new, fresh"},
            {"word": "面白い", "reading": "おもしろい", "meaning": "interesting, funny"},
            {"word": "寒い", "reading": "さむい", "meaning": "cold (weather)"},
        ],
    },
    {
        "id": "n3-13",
        "title": "-ish, and typical of",
        "jp_title": "〜っぽい・〜らしい",
        "goal": "Describe what something seems like, and what is typical of someone or something.",
        "points": [
            "**[noun or verb stem] + っぽい** = -ish, tends to (casual): 子供っぽい \"childish\", "
            "忘れっぽい \"forgetful\", 白っぽい \"whitish\".",
            "**[noun] + らしい** = typical of, just as it should be (usually a compliment): "
            "今日は春らしい天気ですね。 彼らしい \"so like him\".",
            "This らしい is not the N4 らしい \"apparently, I hear\": 春らしい means \"very spring-like\".",
            "っぽい often sounds a little negative; らしい sounds positive: 子供っぽい \"childish\" vs 子供らしい \"nicely childlike\".",
        ],
        "examples": [
            {"jp": "兄は子供っぽいところがあります。", "kana": "あにはこどもっぽいところがあります", "romaji": "ani wa kodomoppoi tokoro ga arimasu", "en": "My older brother has a childish side."},
            {"jp": "最近、忘れっぽくなりました。", "kana": "さいきん わすれっぽくなりました", "romaji": "saikin, wasureppoku narimashita", "en": "I've become forgetful lately."},
            {"jp": "今日は春らしい天気ですね。", "kana": "きょうははるらしいてんきですね", "romaji": "kyou wa harurashii tenki desu ne", "en": "It's real spring weather today, isn't it?"},
            {"jp": "そのやり方はとても彼らしいです。", "kana": "そのやりかたはとてもかれらしいです", "romaji": "sono yarikata wa totemo karerashii desu", "en": "That way of doing it is so typical of him."},
        ],
        "vocab": [
            {"word": "子供っぽい", "reading": "こどもっぽい", "meaning": "childish"},
            {"word": "忘れっぽい", "reading": "わすれっぽい", "meaning": "forgetful"},
            {"word": "春らしい", "reading": "はるらしい", "meaning": "spring-like, typical of spring"},
            {"word": "天気", "reading": "てんき", "meaning": "weather"},
            {"word": "最近", "reading": "さいきん", "meaning": "lately, recently"},
            {"word": "やり方", "reading": "やりかた", "meaning": "way of doing something"},
        ],
    },
    {
        "id": "n3-14",
        "title": "As, in the role of",
        "jp_title": "〜として",
        "goal": "Say in what role or capacity someone does something.",
        "points": [
            "**[noun] + として** = as, in the role of: 留学生として日本に来ました。",
            "Common uses: 趣味として \"as a hobby\", プレゼントとして \"as a present\", 代表として \"as a representative\".",
            "Before a noun use **としての**: 親としての責任 \"responsibility as a parent\".",
            "**としては** = as far as ... is concerned: 私としては、反対です。 \"Personally, I'm against it.\"",
        ],
        "examples": [
            {"jp": "留学生として日本に来ました。", "kana": "りゅうがくせいとしてにほんにきました", "romaji": "ryuugakusei to shite nihon ni kimashita", "en": "I came to Japan as an exchange student."},
            {"jp": "趣味として、ギターを習っています。", "kana": "しゅみとして ギターをならっています", "romaji": "shumi to shite, gitaa o naratte imasu", "en": "I'm learning the guitar as a hobby."},
            {"jp": "誕生日のプレゼントとして、時計をもらいました。", "kana": "たんじょうびのプレゼントとして とけいをもらいました", "romaji": "tanjoubi no purezento to shite, tokei o moraimashita", "en": "I got a watch as a birthday present."},
            {"jp": "私としては、その計画に反対です。", "kana": "わたしとしては そのけいかくにはんたいです", "romaji": "watashi to shite wa, sono keikaku ni hantai desu", "en": "Personally, I'm against that plan."},
        ],
        "vocab": [
            {"word": "留学生", "reading": "りゅうがくせい", "meaning": "international student"},
            {"word": "趣味", "reading": "しゅみ", "meaning": "hobby"},
            {"word": "習います", "reading": "ならいます", "meaning": "to learn (from someone), take lessons"},
            {"word": "計画", "reading": "けいかく", "meaning": "plan"},
            {"word": "反対", "reading": "はんたい", "meaning": "opposition, being against"},
            {"word": "時計", "reading": "とけい", "meaning": "clock, watch"},
        ],
    },
    {
        "id": "n3-15",
        "title": "Instead of, in exchange for",
        "jp_title": "〜かわりに",
        "goal": "Say what you do instead of something, in someone's place, or in return.",
        "points": [
            "**[noun の / dictionary form] + かわりに** = instead of: 電車のかわりに、バスで行きました。",
            "It also means \"in someone's place\": 母のかわりに、私が晩ご飯を作りました。",
            "And \"in exchange for\": 英語を教えるかわりに、日本語を教えてもらいます。",
            "It can be written **代わりに**. At the start of a sentence, **そのかわり** = instead, in return.",
        ],
        "examples": [
            {"jp": "電車のかわりに、バスで行きました。", "kana": "でんしゃのかわりに バスでいきました", "romaji": "densha no kawari ni, basu de ikimashita", "en": "I went by bus instead of by train."},
            {"jp": "母のかわりに、私が晩ご飯を作りました。", "kana": "ははのかわりに わたしがばんごはんをつくりました", "romaji": "haha no kawari ni, watashi ga bangohan o tsukurimashita", "en": "I made dinner in my mother's place."},
            {"jp": "英語を教えるかわりに、日本語を教えてもらいます。", "kana": "えいごをおしえるかわりに にほんごをおしえてもらいます", "romaji": "eigo o oshieru kawari ni, nihongo o oshiete moraimasu", "en": "In exchange for teaching English, I get taught Japanese."},
            {"jp": "肉のかわりに、豆腐を使いました。", "kana": "にくのかわりに とうふをつかいました", "romaji": "niku no kawari ni, toufu o tsukaimashita", "en": "I used tofu instead of meat."},
        ],
        "vocab": [
            {"word": "代わり", "reading": "かわり", "meaning": "substitute, replacement"},
            {"word": "晩ご飯", "reading": "ばんごはん", "meaning": "dinner"},
            {"word": "豆腐", "reading": "とうふ", "meaning": "tofu"},
            {"word": "使います", "reading": "つかいます", "meaning": "to use"},
            {"word": "教えます", "reading": "おしえます", "meaning": "to teach, to tell"},
        ],
    },
    {
        "id": "n3-16",
        "title": "Considering, for a...",
        "jp_title": "〜わりに",
        "goal": "Say that a result is different from what you would expect.",
        "points": [
            "**[plain form] + わりに** = considering ..., for a ... (the result is not what you'd expect): "
            "この店は安いわりに、おいしいです。",
            "Nouns take の, な-adjectives take な: 年のわりに元気です。 有名なわりに…",
            "It works for good and bad surprises: たくさん勉強したわりに、点数が悪かった。",
            "Compare **のに** (N4): のに sounds frustrated; わりに compares with what you'd normally expect.",
        ],
        "examples": [
            {"jp": "この店は安いわりに、おいしいです。", "kana": "このみせはやすいわりに おいしいです", "romaji": "kono mise wa yasui wari ni, oishii desu", "en": "This restaurant is tasty for how cheap it is."},
            {"jp": "祖父は年のわりに、元気です。", "kana": "そふはとしのわりに げんきです", "romaji": "sofu wa toshi no wari ni, genki desu", "en": "My grandfather is energetic for his age."},
            {"jp": "たくさん勉強したわりに、点数が悪かったです。", "kana": "たくさんべんきょうしたわりに てんすうがわるかったです", "romaji": "takusan benkyou shita wari ni, tensuu ga warukatta desu", "en": "Considering how much I studied, my score was bad."},
            {"jp": "この映画は有名なわりに、つまらなかったです。", "kana": "このえいがはゆうめいなわりに つまらなかったです", "romaji": "kono eiga wa yuumei na wari ni, tsumaranakatta desu", "en": "For such a famous film, it was boring."},
        ],
        "vocab": [
            {"word": "わりに", "reading": "わりに", "meaning": "considering, for (a ...)"},
            {"word": "点数", "reading": "てんすう", "meaning": "score, points"},
            {"word": "祖父", "reading": "そふ", "meaning": "(my) grandfather"},
            {"word": "年", "reading": "とし", "meaning": "age; year"},
            {"word": "つまらない", "reading": "つまらない", "meaning": "boring"},
        ],
    },
    {
        "id": "n3-17",
        "title": "Just as, exactly like",
        "jp_title": "〜とおりに",
        "goal": "Say that something is done or happens exactly as said, planned or expected.",
        "points": [
            "**[dictionary or た-form] + とおりに** = (do it) just as ...: 先生が言ったとおりに、やってみました。",
            "Nouns use **のとおりに** or **どおりに**: 説明書のとおりに, 予定どおりに.",
            "**思ったとおり** = just as I thought: 思ったとおり、雨が降ってきました。",
            "**このとおり** = like this (while showing): このとおりに書いてください。",
        ],
        "examples": [
            {"jp": "先生が言ったとおりに、やってみました。", "kana": "せんせいがいったとおりに やってみました", "romaji": "sensei ga itta toori ni, yatte mimashita", "en": "I tried doing it exactly as the teacher said."},
            {"jp": "説明書のとおりに、組み立ててください。", "kana": "せつめいしょのとおりに くみたててください", "romaji": "setsumeisho no toori ni, kumitatete kudasai", "en": "Please put it together as the instructions say."},
            {"jp": "電車は予定どおりに着きました。", "kana": "でんしゃはよていどおりにつきました", "romaji": "densha wa yotei doori ni tsukimashita", "en": "The train arrived on schedule."},
            {"jp": "思ったとおり、雨が降ってきました。", "kana": "おもったとおり あめがふってきました", "romaji": "omotta toori, ame ga futte kimashita", "en": "Just as I thought, it started to rain."},
        ],
        "vocab": [
            {"word": "とおり", "reading": "とおり", "meaning": "way, manner (〜とおりに = just as)"},
            {"word": "説明書", "reading": "せつめいしょ", "meaning": "instructions, manual"},
            {"word": "組み立てます", "reading": "くみたてます", "meaning": "to assemble, put together"},
            {"word": "予定", "reading": "よてい", "meaning": "plan, schedule"},
            {"word": "説明", "reading": "せつめい", "meaning": "explanation"},
        ],
    },
    {
        "id": "n3-18",
        "title": "Please let me",
        "jp_title": "〜させてください",
        "goal": "Ask permission to do something yourself, politely.",
        "points": [
            "**[causative て-form] + ください** = please let me ...: 今日は早く帰らせてください。",
            "Causative recap (N4): 帰る → 帰らせる, 食べる → 食べさせる, する → させる, 来る → 来させる.",
            "**〜させてもらえませんか** is softer: ちょっと考えさせてもらえませんか。",
            "**〜させていただけませんか** is very polite: 写真を撮らせていただけませんか。",
        ],
        "examples": [
            {"jp": "今日は早く帰らせてください。", "kana": "きょうははやくかえらせてください", "romaji": "kyou wa hayaku kaerasete kudasai", "en": "Please let me go home early today."},
            {"jp": "私にも手伝わせてください。", "kana": "わたしにもてつだわせてください", "romaji": "watashi ni mo tetsudawasete kudasai", "en": "Please let me help too."},
            {"jp": "ちょっと考えさせてもらえませんか。", "kana": "ちょっとかんがえさせてもらえませんか", "romaji": "chotto kangaesasete moraemasen ka", "en": "Could you let me think about it a little?"},
            {"jp": "写真を撮らせていただけませんか。", "kana": "しゃしんをとらせていただけませんか", "romaji": "shashin o torasete itadakemasen ka", "en": "Would you mind if I took a photo?"},
        ],
        "vocab": [
            {"word": "手伝います", "reading": "てつだいます", "meaning": "to help"},
            {"word": "考えます", "reading": "かんがえます", "meaning": "to think about, consider"},
            {"word": "撮ります", "reading": "とります", "meaning": "to take (a photo)"},
            {"word": "写真", "reading": "しゃしん", "meaning": "photo"},
            {"word": "早く", "reading": "はやく", "meaning": "early, quickly"},
        ],
    },
    {
        "id": "n3-19",
        "title": "Called, that, they say",
        "jp_title": "〜という・〜って",
        "goal": "Name things, explain what something is about, and pass on what people said, casually.",
        "points": [
            "**[name] + という + [noun]** = a ... called ...: 「さくら」という店を知っていますか。",
            "**[sentence] + という + [noun]** gives the content of a story, news or rumour: 明日、雨が降るという話を聞きました。",
            "**〜というのは** = what ... means is: 「JLPT」というのは、日本語能力試験のことです。",
            "In casual speech **って** replaces という, と言う and とは: 田中さん、明日来ないって。 \"Tanaka-san says they aren't coming tomorrow.\"",
        ],
        "examples": [
            {"jp": "さくらという店を知っていますか。", "kana": "さくらというみせをしっていますか", "romaji": "sakura to iu mise o shitte imasu ka", "en": "Do you know a shop called Sakura?"},
            {"jp": "明日、雨が降るという話を聞きました。", "kana": "あした あめがふるというはなしをききました", "romaji": "ashita, ame ga furu to iu hanashi o kikimashita", "en": "I heard that it's going to rain tomorrow."},
            {"jp": "田中さんは明日来ないって。", "kana": "たなかさんはあしたこないって", "romaji": "tanaka san wa ashita konaitte", "en": "Tanaka-san says they aren't coming tomorrow."},
            {"jp": "これは何という意味ですか。", "kana": "これはなんといういみですか", "romaji": "kore wa nan to iu imi desu ka", "en": "What does this mean?"},
        ],
        "vocab": [
            {"word": "という", "reading": "という", "meaning": "called, named; that (content)"},
            {"word": "話", "reading": "はなし", "meaning": "story, talk"},
            {"word": "意味", "reading": "いみ", "meaning": "meaning"},
            {"word": "能力", "reading": "のうりょく", "meaning": "ability"},
            {"word": "試験", "reading": "しけん", "meaning": "exam"},
        ],
    },
    {
        "id": "n3-20",
        "title": "Even, as long as",
        "jp_title": "〜さえ・〜さえ〜ば",
        "goal": "Stress a surprising extreme, and say the one condition that is enough.",
        "points": [
            "**[noun] + さえ** = even (something surprising, usually in a negative sentence): "
            "忙しくて、水を飲む時間さえありません。",
            "With particles: で → **でさえ**, に → **にさえ**: 先生でさえ分かりませんでした。",
            "**[noun] + さえ + [ば-form]** = as long as, if only: 時間さえあれば、旅行に行きたいです。",
            "Verbs use **[ます-stem] + さえすれば**: この薬を飲みさえすれば、すぐ治ります。",
        ],
        "examples": [
            {"jp": "忙しくて、水を飲む時間さえありません。", "kana": "いそがしくて みずをのむじかんさえありません", "romaji": "isogashikute, mizu o nomu jikan sae arimasen", "en": "I'm so busy I don't even have time to drink water."},
            {"jp": "この問題は先生でさえ分かりませんでした。", "kana": "このもんだいはせんせいでさえわかりませんでした", "romaji": "kono mondai wa sensei de sae wakarimasen deshita", "en": "Even the teacher couldn't work out this problem."},
            {"jp": "時間さえあれば、旅行に行きたいです。", "kana": "じかんさえあれば りょこうにいきたいです", "romaji": "jikan sae areba, ryokou ni ikitai desu", "en": "If only I had the time, I'd like to travel."},
            {"jp": "この薬を飲みさえすれば、すぐ治ります。", "kana": "このくすりをのみさえすれば すぐなおります", "romaji": "kono kusuri o nomi sae sureba, sugu naorimasu", "en": "As long as you take this medicine, you'll get better quickly."},
        ],
        "vocab": [
            {"word": "さえ", "reading": "さえ", "meaning": "even; (さえ〜ば) as long as"},
            {"word": "忙しい", "reading": "いそがしい", "meaning": "busy"},
            {"word": "治ります", "reading": "なおります", "meaning": "to get better, heal"},
            {"word": "時間", "reading": "じかん", "meaning": "time"},
            {"word": "すぐ", "reading": "すぐ", "meaning": "soon, right away"},
        ],
    },
    {
        "id": "n3-21",
        "title": "Asking someone to, hoping that",
        "jp_title": "〜ように言う・〜ますように",
        "goal": "Report requests and instructions, and make a wish.",
        "points": [
            "**[dictionary or ない form] + ように言う / 頼む** reports a request or instruction: "
            "先生に、もっと練習するように言われました。",
            "Useful verbs: 言う (tell), 頼む (ask a favour), 注意する (warn): 子供に、道で走らないように注意しました。",
            "**[ます-stem] + ますように** = a wish or prayer: 試験に合格できますように。 \"I hope I pass the exam.\"",
            "Recap from N4: **ように** alone means \"so that\": 忘れないように、メモします。",
        ],
        "examples": [
            {"jp": "先生に、もっと練習するように言われました。", "kana": "せんせいに もっとれんしゅうするようにいわれました", "romaji": "sensei ni, motto renshuu suru you ni iwaremashita", "en": "My teacher told me to practise more."},
            {"jp": "母に、早く帰るように頼まれました。", "kana": "ははに はやくかえるようにたのまれました", "romaji": "haha ni, hayaku kaeru you ni tanomaremashita", "en": "My mother asked me to come home early."},
            {"jp": "子供に、道で走らないように注意しました。", "kana": "こどもに みちではしらないようにちゅういしました", "romaji": "kodomo ni, michi de hashiranai you ni chuui shimashita", "en": "I warned the child not to run in the street."},
            {"jp": "試験に合格できますように。", "kana": "しけんにごうかくできますように", "romaji": "shiken ni goukaku dekimasu you ni", "en": "I hope I pass the exam."},
        ],
        "vocab": [
            {"word": "頼みます", "reading": "たのみます", "meaning": "to ask (a favour), to request"},
            {"word": "注意", "reading": "ちゅうい", "meaning": "warning, caution"},
            {"word": "走ります", "reading": "はしります", "meaning": "to run"},
            {"word": "もっと", "reading": "もっと", "meaning": "more"},
            {"word": "メモ", "reading": "メモ", "meaning": "memo, note"},
        ],
    },
    {
        "id": "n3-22",
        "title": "Other people's feelings",
        "jp_title": "〜がる・〜たがる",
        "goal": "Describe what other people feel and want, as you see it.",
        "points": [
            "Feeling words like 欲しい, 怖い and 寂しい describe **your own** feelings. "
            "For someone else, add **がる**: 怖い → 怖がる, 欲しい → 欲しがる.",
            "**[ます-stem] + たがる** = someone else wants to: 弟は外で遊びたがっています。",
            "It's usually in the ている form for what's going on now: 妹は犬を欲しがっています。",
            "Also 嫌がる (show dislike) and 残念がる (be disappointed). Don't use がる for people above you; "
            "it can sound like you're describing a child.",
        ],
        "examples": [
            {"jp": "妹は犬を欲しがっています。", "kana": "いもうとはいぬをほしがっています", "romaji": "imouto wa inu o hoshigatte imasu", "en": "My little sister wants a dog."},
            {"jp": "弟は外で遊びたがっています。", "kana": "おとうとはそとであそびたがっています", "romaji": "otouto wa soto de asobitagatte imasu", "en": "My little brother wants to play outside."},
            {"jp": "子供は暗い部屋を怖がります。", "kana": "こどもはくらいへやをこわがります", "romaji": "kodomo wa kurai heya o kowagarimasu", "en": "Children are scared of dark rooms."},
            {"jp": "猫はお風呂を嫌がります。", "kana": "ねこはおふろをいやがります", "romaji": "neko wa ofuro o iyagarimasu", "en": "Cats hate baths."},
        ],
        "vocab": [
            {"word": "欲しがります", "reading": "ほしがります", "meaning": "(someone else) wants"},
            {"word": "怖い", "reading": "こわい", "meaning": "scary; scared"},
            {"word": "寂しい", "reading": "さびしい", "meaning": "lonely"},
            {"word": "嫌がります", "reading": "いやがります", "meaning": "to dislike, to not want to"},
            {"word": "暗い", "reading": "くらい", "meaning": "dark"},
            {"word": "猫", "reading": "ねこ", "meaning": "cat"},
        ],
    },
    {
        "id": "n3-23",
        "title": "Things like..., how surprising",
        "jp_title": "〜なんて",
        "goal": "Make light of something, be modest, or show surprise.",
        "points": [
            "**[noun] + なんて** = things like ..., the likes of ... (making light of it, or being modest): "
            "私なんて、まだまだです。",
            "**[plain form] + なんて** shows surprise or disbelief: 兄が結婚するなんて、びっくりしました。",
            "It can sound negative: 宿題なんて、やりたくない。 \"I don't want to do stuff like homework.\"",
            "**なんか** is a more casual version of the noun use: 私なんか…",
        ],
        "examples": [
            {"jp": "私なんて、まだまだです。", "kana": "わたしなんて まだまだです", "romaji": "watashi nante, madamada desu", "en": "Me? I've still got a long way to go."},
            {"jp": "兄が結婚するなんて、びっくりしました。", "kana": "あにがけっこんするなんて びっくりしました", "romaji": "ani ga kekkon suru nante, bikkuri shimashita", "en": "I was so surprised that my brother is getting married."},
            {"jp": "こんなに早く雪が降るなんて、信じられません。", "kana": "こんなにはやくゆきがふるなんて しんじられません", "romaji": "konna ni hayaku yuki ga furu nante, shinjiraremasen", "en": "I can't believe it's snowing this early."},
            {"jp": "宿題なんて、やりたくない。", "kana": "しゅくだいなんて やりたくない", "romaji": "shukudai nante, yaritakunai", "en": "I don't want to do stuff like homework."},
        ],
        "vocab": [
            {"word": "なんて", "reading": "なんて", "meaning": "things like; (surprise) that ..."},
            {"word": "結婚", "reading": "けっこん", "meaning": "marriage"},
            {"word": "びっくりします", "reading": "びっくりします", "meaning": "to be surprised"},
            {"word": "信じます", "reading": "しんじます", "meaning": "to believe"},
            {"word": "雪", "reading": "ゆき", "meaning": "snow"},
            {"word": "まだまだ", "reading": "まだまだ", "meaning": "still a long way to go"},
        ],
    },
    {
        "id": "n3-24",
        "title": "Right in the middle of",
        "jp_title": "〜最中に",
        "goal": "Say that something happened at the very moment you were busy with something else.",
        "points": [
            "**[noun の / ている form] + 最中に** = right in the middle of (and then something interrupted): "
            "食事の最中に、電話が鳴りました。",
            "It's stronger than 〜ているときに: it stresses \"at that very moment\".",
            "**最中です** at the end of a sentence = be in the middle of: 今、晩ご飯を作っている最中です。",
            "Compare 〜ているところ (lesson 1): ところ just says what stage you're at; 最中に usually sets up an interruption.",
        ],
        "examples": [
            {"jp": "食事の最中に、電話が鳴りました。", "kana": "しょくじのさいちゅうに でんわがなりました", "romaji": "shokuji no saichuu ni, denwa ga narimashita", "en": "The phone rang right in the middle of the meal."},
            {"jp": "試験の最中に、お腹が痛くなりました。", "kana": "しけんのさいちゅうに おなかがいたくなりました", "romaji": "shiken no saichuu ni, onaka ga itaku narimashita", "en": "My stomach started hurting in the middle of the exam."},
            {"jp": "話している最中に、電気が消えました。", "kana": "はなしているさいちゅうに でんきがきえました", "romaji": "hanashite iru saichuu ni, denki ga kiemashita", "en": "The lights went out right while we were talking."},
            {"jp": "今、晩ご飯を作っている最中です。", "kana": "いま ばんごはんをつくっているさいちゅうです", "romaji": "ima, bangohan o tsukutte iru saichuu desu", "en": "I'm in the middle of making dinner right now."},
        ],
        "vocab": [
            {"word": "最中", "reading": "さいちゅう", "meaning": "the middle of (doing something)"},
            {"word": "食事", "reading": "しょくじ", "meaning": "meal"},
            {"word": "鳴ります", "reading": "なります", "meaning": "to ring, to sound"},
            {"word": "お腹", "reading": "おなか", "meaning": "stomach, belly"},
            {"word": "痛い", "reading": "いたい", "meaning": "painful, sore"},
            {"word": "消えます", "reading": "きえます", "meaning": "to go out, to disappear"},
        ],
    },
    {
        "id": "n3-25",
        "title": "Not only..., but also",
        "jp_title": "〜だけでなく・〜はもちろん",
        "goal": "Add a second, less obvious point to a first one.",
        "points": [
            "**[noun or plain form] + だけでなく** = not only ... (but also): 姉は英語だけでなく、中国語も話せます。",
            "**だけじゃなく** is the spoken version; **ばかりでなく** is more formal.",
            "**[noun] + はもちろん** = ... of course, and also: この店は味はもちろん、値段も安いです。 "
            "The first item is the obvious one.",
            "The second half usually has **も**: 子供だけでなく、大人も楽しめます。",
        ],
        "examples": [
            {"jp": "姉は英語だけでなく、中国語も話せます。", "kana": "あねはえいごだけでなく ちゅうごくごもはなせます", "romaji": "ane wa eigo dake de naku, chuugokugo mo hanasemasu", "en": "My older sister speaks not only English but also Chinese."},
            {"jp": "この映画は子供だけでなく、大人も楽しめます。", "kana": "このえいがはこどもだけでなく おとなもたのしめます", "romaji": "kono eiga wa kodomo dake de naku, otona mo tanoshimemasu", "en": "Adults as well as children can enjoy this film."},
            {"jp": "この店は味はもちろん、値段も安いです。", "kana": "このみせはあじはもちろん ねだんもやすいです", "romaji": "kono mise wa aji wa mochiron, nedan mo yasui desu", "en": "This restaurant tastes good, of course, and it's cheap too."},
            {"jp": "週末はもちろん、平日も混んでいます。", "kana": "しゅうまつはもちろん へいじつもこんでいます", "romaji": "shuumatsu wa mochiron, heijitsu mo konde imasu", "en": "It's crowded on weekdays, never mind weekends."},
        ],
        "vocab": [
            {"word": "中国語", "reading": "ちゅうごくご", "meaning": "Chinese (language)"},
            {"word": "大人", "reading": "おとな", "meaning": "adult"},
            {"word": "味", "reading": "あじ", "meaning": "taste, flavour"},
            {"word": "値段", "reading": "ねだん", "meaning": "price"},
            {"word": "平日", "reading": "へいじつ", "meaning": "weekday"},
            {"word": "混みます", "reading": "こみます", "meaning": "to get crowded"},
        ],
    },
    {
        "id": "n3-26",
        "title": "I want you to",
        "jp_title": "〜てほしい・〜てもらいたい",
        "goal": "Say what you want someone else to do, or not do.",
        "points": [
            "**[て-form] + ほしい** = I want someone to do something. The person takes **に**: "
            "友達に引っ越しを手伝ってほしいです。",
            "Negative: **〜ないでほしい** = I don't want someone to ...: 私の部屋に勝手に入らないでほしい。",
            "**〜てもらいたい** means the same and sounds a little more polite: 先生にもう一度説明してもらいたいです。",
            "Saying ほしい straight to someone above you can sound pushy; ask with **〜ていただけませんか** instead.",
        ],
        "examples": [
            {"jp": "友達に引っ越しを手伝ってほしいです。", "kana": "ともだちにひっこしをてつだってほしいです", "romaji": "tomodachi ni hikkoshi o tetsudatte hoshii desu", "en": "I want my friends to help me move."},
            {"jp": "私の部屋に勝手に入らないでほしい。", "kana": "わたしのへやにかってにはいらないでほしい", "romaji": "watashi no heya ni katte ni hairanaide hoshii", "en": "I don't want people coming into my room without asking."},
            {"jp": "先生にもう一度説明してもらいたいです。", "kana": "せんせいにもういちどせつめいしてもらいたいです", "romaji": "sensei ni mou ichido setsumei shite moraitai desu", "en": "I'd like the teacher to explain it once more."},
            {"jp": "早く元気になってほしいです。", "kana": "はやくげんきになってほしいです", "romaji": "hayaku genki ni natte hoshii desu", "en": "I hope you get well soon."},
        ],
        "vocab": [
            {"word": "勝手に", "reading": "かってに", "meaning": "without permission, as one pleases"},
            {"word": "もう一度", "reading": "もういちど", "meaning": "once more"},
            {"word": "引っ越し", "reading": "ひっこし", "meaning": "moving (house)"},
            {"word": "友達", "reading": "ともだち", "meaning": "friend"},
            {"word": "元気", "reading": "げんき", "meaning": "well, healthy, lively"},
        ],
    },
    {
        "id": "n3-27",
        "title": "Even if",
        "jp_title": "たとえ〜ても・〜としても",
        "goal": "Say that the result won't change, whatever happens.",
        "points": [
            "**ても** (N4) = even if. **たとえ** in front makes it stronger: たとえ雨が降っても、試合はあります。",
            "Nouns and な-adjectives use **でも**: たとえ子供でも、ルールは守らなければなりません。",
            "**[plain form] + としても** = even supposing that ... (more hypothetical): "
            "今から急いだとしても、間に合わないでしょう。",
            "The second half says what stays the same.",
        ],
        "examples": [
            {"jp": "たとえ雨が降っても、試合はあります。", "kana": "たとえあめがふっても しあいはあります", "romaji": "tatoe ame ga futte mo, shiai wa arimasu", "en": "Even if it rains, the match will go ahead."},
            {"jp": "たとえ子供でも、ルールは守らなければなりません。", "kana": "たとえこどもでも ルールはまもらなければなりません", "romaji": "tatoe kodomo demo, ruuru wa mamoranakereba narimasen", "en": "Even children have to follow the rules."},
            {"jp": "今から急いだとしても、間に合わないでしょう。", "kana": "いまからいそいだとしても まにあわないでしょう", "romaji": "ima kara isoida to shite mo, maniawanai deshou", "en": "Even if we hurry now, we probably won't make it."},
            {"jp": "たとえ反対されても、留学したいです。", "kana": "たとえはんたいされても りゅうがくしたいです", "romaji": "tatoe hantai sarete mo, ryuugaku shitai desu", "en": "Even if people are against it, I want to study abroad."},
        ],
        "vocab": [
            {"word": "たとえ", "reading": "たとえ", "meaning": "even if (with 〜ても)"},
            {"word": "守ります", "reading": "まもります", "meaning": "to follow (rules), to protect"},
            {"word": "急ぎます", "reading": "いそぎます", "meaning": "to hurry"},
            {"word": "間に合います", "reading": "まにあいます", "meaning": "to be in time"},
            {"word": "留学", "reading": "りゅうがく", "meaning": "studying abroad"},
            {"word": "ルール", "reading": "ルール", "meaning": "rule"},
        ],
    },
    {
        "id": "n3-28",
        "title": "Can't very well",
        "jp_title": "〜わけにはいかない",
        "goal": "Say you can't do something because it wouldn't be right, and that you have no choice but to.",
        "points": [
            "**[dictionary form] + わけにはいかない** = can't (because of duty, common sense or feelings), "
            "even if you'd like to: 明日は試験だから、遊びに行くわけにはいきません。",
            "It isn't about ability (that's the potential form): you *could*, but it wouldn't be right.",
            "**[ない form] + わけにはいかない** = have to, can't not: 約束したから、行かないわけにはいきません。",
            "This builds on lesson 4's わけ. Polite form: わけにはいきません.",
        ],
        "examples": [
            {"jp": "明日は試験だから、遊びに行くわけにはいきません。", "kana": "あしたはしけんだから あそびにいくわけにはいきません", "romaji": "ashita wa shiken da kara, asobi ni iku wake ni wa ikimasen", "en": "I have an exam tomorrow, so I can't very well go out and play."},
            {"jp": "友達の秘密を話すわけにはいかない。", "kana": "ともだちのひみつをはなすわけにはいかない", "romaji": "tomodachi no himitsu o hanasu wake ni wa ikanai", "en": "I can't tell my friend's secret."},
            {"jp": "約束したから、行かないわけにはいきません。", "kana": "やくそくしたから いかないわけにはいきません", "romaji": "yakusoku shita kara, ikanai wake ni wa ikimasen", "en": "I promised, so I have to go."},
            {"jp": "熱があるけど、今日は休むわけにはいかない。", "kana": "ねつがあるけど きょうはやすむわけにはいかない", "romaji": "netsu ga aru kedo, kyou wa yasumu wake ni wa ikanai", "en": "I have a fever, but I can't take today off."},
        ],
        "vocab": [
            {"word": "秘密", "reading": "ひみつ", "meaning": "secret"},
            {"word": "約束", "reading": "やくそく", "meaning": "promise"},
            {"word": "熱", "reading": "ねつ", "meaning": "fever; heat"},
            {"word": "休みます", "reading": "やすみます", "meaning": "to rest, take time off"},
            {"word": "遊びます", "reading": "あそびます", "meaning": "to play, hang out"},
        ],
    },
    {
        "id": "n3-29",
        "title": "As ... changes",
        "jp_title": "〜につれて・〜にしたがって",
        "goal": "Describe two things changing together over time.",
        "points": [
            "**[dictionary form or noun] + につれて** = as one thing changes, another changes with it: "
            "時間がたつにつれて、寂しくなりました。",
            "Both halves are gradual changes, often with 〜なる or words like 増える.",
            "**にしたがって** means the same, and also \"following (rules, instructions)\": "
            "説明にしたがって、ボタンを押してください。",
            "Compare ば〜ほど (lesson 12): a similar idea, but につれて sounds more like describing a process.",
        ],
        "examples": [
            {"jp": "時間がたつにつれて、寂しくなりました。", "kana": "じかんがたつにつれて さびしくなりました", "romaji": "jikan ga tatsu ni tsurete, sabishiku narimashita", "en": "As time passed, I got lonelier."},
            {"jp": "日本語が上手になるにつれて、日本の生活が楽しくなりました。", "kana": "にほんごがじょうずになるにつれて にほんのせいかつがたのしくなりました", "romaji": "nihongo ga jouzu ni naru ni tsurete, nihon no seikatsu ga tanoshiku narimashita", "en": "As my Japanese got better, life in Japan got more fun."},
            {"jp": "山に登るにつれて、寒くなりました。", "kana": "やまにのぼるにつれて さむくなりました", "romaji": "yama ni noboru ni tsurete, samuku narimashita", "en": "As we climbed the mountain, it got colder."},
            {"jp": "説明にしたがって、ボタンを押してください。", "kana": "せつめいにしたがって ボタンをおしてください", "romaji": "setsumei ni shitagatte, botan o oshite kudasai", "en": "Please press the button as the instructions say."},
        ],
        "vocab": [
            {"word": "たちます", "reading": "たちます", "meaning": "(time) passes"},
            {"word": "生活", "reading": "せいかつ", "meaning": "life, daily life"},
            {"word": "登ります", "reading": "のぼります", "meaning": "to climb"},
            {"word": "押します", "reading": "おします", "meaning": "to press, to push"},
            {"word": "ボタン", "reading": "ボタン", "meaning": "button"},
        ],
    },
    {
        "id": "n3-30",
        "title": "I should have...",
        "jp_title": "〜ばよかった・〜のに",
        "goal": "Express regret about what you did, or didn't do.",
        "points": [
            "**[ば-form] + よかった** = I should have ... (regret): もっと勉強すればよかったです。",
            "Negative: **[ない → なければ] + よかった** = I shouldn't have ...: あんなこと、言わなければよかった。",
            "**〜たらよかった** means the same and is common in speech: 傘を持ってきたらよかった。",
            "**〜ばよかったのに** = you should have ... (regret on someone else's behalf): 早く言えばよかったのに。",
        ],
        "examples": [
            {"jp": "もっと勉強すればよかったです。", "kana": "もっとべんきょうすればよかったです", "romaji": "motto benkyou sureba yokatta desu", "en": "I should have studied more."},
            {"jp": "傘を持ってくればよかった。", "kana": "かさをもってくればよかった", "romaji": "kasa o motte kureba yokatta", "en": "I should have brought an umbrella."},
            {"jp": "あんなこと、言わなければよかった。", "kana": "あんなこと いわなければよかった", "romaji": "anna koto, iwanakereba yokatta", "en": "I shouldn't have said that."},
            {"jp": "困っていたなら、早く言えばよかったのに。", "kana": "こまっていたなら はやくいえばよかったのに", "romaji": "komatte ita nara, hayaku ieba yokatta noni", "en": "If you were having trouble, you should have said so sooner."},
        ],
        "vocab": [
            {"word": "傘", "reading": "かさ", "meaning": "umbrella"},
            {"word": "困ります", "reading": "こまります", "meaning": "to be in trouble, to be stuck"},
            {"word": "あんな", "reading": "あんな", "meaning": "that kind of"},
            {"word": "後悔", "reading": "こうかい", "meaning": "regret"},
            {"word": "持ってきます", "reading": "もってきます", "meaning": "to bring"},
        ],
    },
    # ------------------------------------------------------------------ N2
    {
        "id": "n2-01",
        "title": "Despite, even though",
        "jp_title": "〜にもかかわらず",
        "goal": "Say that something happened despite a situation that suggests otherwise.",
        "points": [
            "**[noun / plain form] + にもかかわらず** = despite, even though (formal, common in writing and the news): "
            "雨にもかかわらず、たくさんの人が集まりました。",
            "It follows nouns and plain forms directly: 雨にもかかわらず, 何度も注意したにもかかわらず. "
            "な-adjectives and nouns can also take **である**: 休日であるにもかかわらず.",
            "The result is usually surprising or disappointing. It's like のに (N4), but more formal and less emotional.",
            "Unlike のに, it can't end a sentence as a complaint: 来たのに！ works, 来たにもかかわらず！ doesn't.",
        ],
        "examples": [
            {"jp": "雨にもかかわらず、たくさんの人が集まりました。", "kana": "あめにもかかわらず たくさんのひとがあつまりました", "romaji": "ame ni mo kakawarazu, takusan no hito ga atsumarimashita", "en": "Despite the rain, lots of people gathered."},
            {"jp": "何度も注意したにもかかわらず、弟はまた遅刻した。", "kana": "なんどもちゅういしたにもかかわらず おとうとはまたちこくした", "romaji": "nando mo chuui shita ni mo kakawarazu, otouto wa mata chikoku shita", "en": "Despite being warned many times, my brother was late again."},
            {"jp": "彼女は熱があるにもかかわらず、学校に来た。", "kana": "かのじょはねつがあるにもかかわらず がっこうにきた", "romaji": "kanojo wa netsu ga aru ni mo kakawarazu, gakkou ni kita", "en": "She came to school even though she had a fever."},
            {"jp": "一生懸命練習したにもかかわらず、試合に負けてしまった。", "kana": "いっしょうけんめいれんしゅうしたにもかかわらず しあいにまけてしまった", "romaji": "isshoukenmei renshuu shita ni mo kakawarazu, shiai ni makete shimatta", "en": "We lost the match despite practising so hard."},
        ],
        "vocab": [
            {"word": "集まる", "reading": "あつまる", "meaning": "to gather"},
            {"word": "遅刻", "reading": "ちこく", "meaning": "being late"},
            {"word": "一生懸命", "reading": "いっしょうけんめい", "meaning": "with all one's might"},
            {"word": "負ける", "reading": "まける", "meaning": "to lose (a game)"},
            {"word": "彼女", "reading": "かのじょ", "meaning": "she; girlfriend"},
        ],
    },
    {
        "id": "n2-02",
        "title": "Precisely because",
        "jp_title": "〜からこそ・〜こそ",
        "goal": "Stress that a reason, or one particular thing, is exactly what matters.",
        "points": [
            "**[plain form] + からこそ** = precisely because (stressing the reason, often a surprising one): "
            "大切だからこそ、厳しく言うのです。",
            "It often explains something that seems contradictory: 忙しいからこそ、休みの日が大切だ。",
            "**[noun] + こそ** = this very one, X (and nothing else): 今年こそ、試験に合格したい。 \"This year for sure.\"",
            "Set phrases: **こちらこそ** \"likewise, the pleasure is mine\", **今度こそ** \"this time for sure\".",
        ],
        "examples": [
            {"jp": "あなたのことが大切だからこそ、厳しく言うのです。", "kana": "あなたのことがたいせつだからこそ きびしくいうのです", "romaji": "anata no koto ga taisetsu da kara koso, kibishiku iu no desu", "en": "It's precisely because you matter to me that I'm being strict."},
            {"jp": "忙しいからこそ、休みの日が大切だ。", "kana": "いそがしいからこそ やすみのひがたいせつだ", "romaji": "isogashii kara koso, yasumi no hi ga taisetsu da", "en": "It's because I'm busy that my days off matter."},
            {"jp": "今年こそ、試験に合格したい。", "kana": "ことしこそ しけんにごうかくしたい", "romaji": "kotoshi koso, shiken ni goukaku shitai", "en": "This year for sure, I want to pass the exam."},
            {"jp": "失敗したからこそ、学べたこともある。", "kana": "しっぱいしたからこそ まなべたこともある", "romaji": "shippai shita kara koso, manabeta koto mo aru", "en": "There are things I could learn only because I failed."},
        ],
        "vocab": [
            {"word": "厳しい", "reading": "きびしい", "meaning": "strict, harsh"},
            {"word": "こちらこそ", "reading": "こちらこそ", "meaning": "likewise, the pleasure is mine"},
            {"word": "今度", "reading": "こんど", "meaning": "this time; next time"},
            {"word": "学ぶ", "reading": "まなぶ", "meaning": "to learn, study"},
            {"word": "今年", "reading": "ことし", "meaning": "this year"},
        ],
    },
    {
        "id": "n2-03",
        "title": "Must be, surely",
        "jp_title": "〜に違いない・〜に決まっている",
        "goal": "Make a confident guess, and say something is obvious.",
        "points": [
            "**[plain form] + に違いない** = must be, I'm sure (a confident guess, more written): "
            "部屋の電気が消えている。もう寝たに違いない。",
            "Nouns and な-adjectives attach directly, without だ: うそに違いない, 静かに違いない.",
            "**に決まっている** = it's obvious that (conversational, sometimes pushy): そんな話、うそに決まっている。",
            "Compare **はず** (N4): はず is based on facts or reasoning; に違いない is a strong feeling of certainty.",
        ],
        "examples": [
            {"jp": "部屋の電気が消えている。もう寝たに違いない。", "kana": "へやのでんきがきえている もうねたにちがいない", "romaji": "heya no denki ga kiete iru. mou neta ni chigai nai", "en": "The light in the room is off. They must have gone to bed."},
            {"jp": "あんなに練習したのだから、合格するに違いない。", "kana": "あんなにれんしゅうしたのだから ごうかくするにちがいない", "romaji": "anna ni renshuu shita no da kara, goukaku suru ni chigai nai", "en": "After practising that much, you're sure to pass."},
            {"jp": "そんな話、うそに決まっている。", "kana": "そんなはなし うそにきまっている", "romaji": "sonna hanashi, uso ni kimatte iru", "en": "A story like that is obviously a lie."},
            {"jp": "この店はいつも混んでいるから、おいしいに違いない。", "kana": "このみせはいつもこんでいるから おいしいにちがいない", "romaji": "kono mise wa itsumo konde iru kara, oishii ni chigai nai", "en": "This restaurant is always crowded, so it must be good."},
        ],
        "vocab": [
            {"word": "違いない", "reading": "ちがいない", "meaning": "(it) must be, no doubt"},
            {"word": "決まっている", "reading": "きまっている", "meaning": "(it's) obvious, bound to be"},
            {"word": "うそ", "reading": "うそ", "meaning": "lie"},
            {"word": "あんなに", "reading": "あんなに", "meaning": "that much, so"},
            {"word": "混む", "reading": "こむ", "meaning": "to be crowded"},
        ],
    },
    {
        "id": "n2-04",
        "title": "Although, that said",
        "jp_title": "〜ものの・〜とはいえ",
        "goal": "Admit that something is true, then say the result falls short of what you'd expect.",
        "points": [
            "**[plain form] + ものの** = although (it's true that ..., but): 免許は取ったものの、まだ一度も運転していない。",
            "な-adjectives take な or である, nouns take である: 便利なものの, 学生であるものの.",
            "**とはいえ** = even so, that said: 春とはいえ、朝はまだ寒い。 It can also start a sentence: とはいえ、…",
            "Both are more formal than けど, and the second half goes against what the first half leads you to expect.",
        ],
        "examples": [
            {"jp": "免許は取ったものの、まだ一度も運転していない。", "kana": "めんきょはとったものの まだいちどもうんてんしていない", "romaji": "menkyo wa totta mono no, mada ichido mo unten shite inai", "en": "Although I got my licence, I haven't driven even once."},
            {"jp": "本を買ったものの、忙しくてまだ読んでいない。", "kana": "ほんをかったものの いそがしくてまだよんでいない", "romaji": "hon o katta mono no, isogashikute mada yonde inai", "en": "I bought the book, but I've been too busy to read it."},
            {"jp": "春とはいえ、朝はまだ寒い。", "kana": "はるとはいえ あさはまださむい", "romaji": "haru to wa ie, asa wa mada samui", "en": "It may be spring, but the mornings are still cold."},
            {"jp": "安いとはいえ、毎日外食するとお金がかかる。", "kana": "やすいとはいえ まいにちがいしょくするとおかねがかかる", "romaji": "yasui to wa ie, mainichi gaishoku suru to okane ga kakaru", "en": "It may be cheap, but eating out every day costs money."},
        ],
        "vocab": [
            {"word": "免許", "reading": "めんきょ", "meaning": "licence"},
            {"word": "運転", "reading": "うんてん", "meaning": "driving"},
            {"word": "一度も", "reading": "いちども", "meaning": "(not) even once"},
            {"word": "外食", "reading": "がいしょく", "meaning": "eating out"},
            {"word": "とはいえ", "reading": "とはいえ", "meaning": "even so, that said"},
        ],
    },
    {
        "id": "n2-05",
        "title": "Triggered by, through",
        "jp_title": "〜をきっかけに・〜を通じて",
        "goal": "Say what started a change, and through what or whom something happened.",
        "points": [
            "**[noun] + をきっかけに** = triggered by, taking the opportunity of: 留学をきっかけに、料理を始めました。",
            "With verbs, add **の**: 日本のアニメを見たのをきっかけに…",
            "**[noun] + を通じて** = through, by way of (a person or a means): 友達を通じて知り合いました。 "
            "Also \"throughout\": 一年を通じて暖かい。",
            "**を通して** means almost the same and is common in speech.",
        ],
        "examples": [
            {"jp": "留学をきっかけに、料理を始めました。", "kana": "りゅうがくをきっかけに りょうりをはじめました", "romaji": "ryuugaku o kikkake ni, ryouri o hajimemashita", "en": "Studying abroad got me started on cooking."},
            {"jp": "日本のアニメを見たのをきっかけに、日本語の勉強を始めた。", "kana": "にほんのアニメをみたのをきっかけに にほんごのべんきょうをはじめた", "romaji": "nihon no anime o mita no o kikkake ni, nihongo no benkyou o hajimeta", "en": "Watching Japanese anime got me started on studying Japanese."},
            {"jp": "友達を通じて、今の恋人と知り合いました。", "kana": "ともだちをつうじて いまのこいびととしりあいました", "romaji": "tomodachi o tsuujite, ima no koibito to shiriaimashita", "en": "I met my current partner through a friend."},
            {"jp": "この島は、一年を通じて暖かい。", "kana": "このしまは いちねんをつうじてあたたかい", "romaji": "kono shima wa, ichinen o tsuujite atatakai", "en": "This island is warm all year round."},
        ],
        "vocab": [
            {"word": "通じて", "reading": "つうじて", "meaning": "through; throughout"},
            {"word": "知り合う", "reading": "しりあう", "meaning": "to get to know, meet"},
            {"word": "恋人", "reading": "こいびと", "meaning": "boyfriend or girlfriend, partner"},
            {"word": "島", "reading": "しま", "meaning": "island"},
            {"word": "暖かい", "reading": "あたたかい", "meaning": "warm (weather)"},
        ],
    },
    {
        "id": "n2-06",
        "title": "Regarding, based on",
        "jp_title": "〜に関して・〜に基づいて",
        "goal": "Name the subject of a formal statement, and what it is based on.",
        "points": [
            "**[noun] + に関して** = regarding, about (more formal than について): この件に関して、何か質問はありますか。",
            "Before a noun use **に関する**: 日本の歴史に関する本.",
            "**[noun] + に基づいて** = based on (facts, data, rules): 調査の結果に基づいて、計画を立てた。 "
            "Before a noun: **に基づいた** or **に基づく**.",
            "Both are common in announcements, reports and the N2 reading section.",
        ],
        "examples": [
            {"jp": "この件に関して、何か質問はありますか。", "kana": "このけんにかんして なにかしつもんはありますか", "romaji": "kono ken ni kanshite, nani ka shitsumon wa arimasu ka", "en": "Are there any questions about this matter?"},
            {"jp": "日本の歴史に関する本を探しています。", "kana": "にほんのれきしにかんするほんをさがしています", "romaji": "nihon no rekishi ni kansuru hon o sagashite imasu", "en": "I'm looking for books on Japanese history."},
            {"jp": "調査の結果に基づいて、新しい計画を立てた。", "kana": "ちょうさのけっかにもとづいて あたらしいけいかくをたてた", "romaji": "chousa no kekka ni motozuite, atarashii keikaku o tateta", "en": "We drew up a new plan based on the survey results."},
            {"jp": "この映画は、本当にあった話に基づいている。", "kana": "このえいがは ほんとうにあったはなしにもとづいている", "romaji": "kono eiga wa, hontou ni atta hanashi ni motozuite iru", "en": "This film is based on a true story."},
        ],
        "vocab": [
            {"word": "件", "reading": "けん", "meaning": "matter, case"},
            {"word": "関する", "reading": "かんする", "meaning": "to concern, relate to"},
            {"word": "基づく", "reading": "もとづく", "meaning": "to be based on"},
            {"word": "調査", "reading": "ちょうさ", "meaning": "survey, investigation"},
            {"word": "結果", "reading": "けっか", "meaning": "result"},
            {"word": "計画を立てる", "reading": "けいかくをたてる", "meaning": "to make a plan"},
        ],
    },
    {
        "id": "n2-07",
        "title": "Not only..., but also",
        "jp_title": "〜ばかりか・〜うえに",
        "goal": "Pile up two points of the same kind, good or bad.",
        "points": [
            "**[plain form / noun] + ばかりか** = not only ... but even (the second part is more surprising): "
            "彼は英語ばかりか、中国語も話せる。",
            "The second half often has **も** or **まで**: 道に迷ったばかりか、財布までなくしてしまった。",
            "**[plain form] + うえに** = on top of, besides (adding a similar point): この店は安いうえに、とてもおいしい。 "
            "Nouns take の, な-adjectives take な.",
            "Both add things of the same kind: good and good, or bad and bad.",
        ],
        "examples": [
            {"jp": "彼は英語ばかりか、中国語も話せる。", "kana": "かれはえいごばかりか ちゅうごくごもはなせる", "romaji": "kare wa eigo bakari ka, chuugokugo mo hanaseru", "en": "He can speak not only English but Chinese too."},
            {"jp": "道に迷ったばかりか、財布までなくしてしまった。", "kana": "みちにまよったばかりか さいふまでなくしてしまった", "romaji": "michi ni mayotta bakari ka, saifu made nakushite shimatta", "en": "Not only did I get lost, I even lost my wallet."},
            {"jp": "この店は安いうえに、とてもおいしい。", "kana": "このみせはやすいうえに とてもおいしい", "romaji": "kono mise wa yasui ue ni, totemo oishii", "en": "This restaurant is cheap, and on top of that, very tasty."},
            {"jp": "今日は寒いうえに、雨も降っている。", "kana": "きょうはさむいうえに あめもふっている", "romaji": "kyou wa samui ue ni, ame mo futte iru", "en": "It's cold today, and it's raining as well."},
        ],
        "vocab": [
            {"word": "迷う", "reading": "まよう", "meaning": "to get lost; to hesitate"},
            {"word": "財布", "reading": "さいふ", "meaning": "wallet"},
            {"word": "なくす", "reading": "なくす", "meaning": "to lose (something)"},
            {"word": "うえに", "reading": "うえに", "meaning": "on top of, besides"},
        ],
    },
    {
        "id": "n2-08",
        "title": "Have no choice but to",
        "jp_title": "〜ざるを得ない",
        "goal": "Say you are forced to do something you'd rather not.",
        "points": [
            "**[ない-stem] + ざるを得ない** = have no choice but to, can't help but (formal): "
            "台風が来るので、旅行を中止せざるを得ない。",
            "Build it from the ない form: 帰らない → 帰らざるを得ない, 認めない → 認めざるを得ない. "
            "する becomes **せざるを得ない**.",
            "It sounds reluctant: you don't want to, but the situation forces you.",
            "In speech, **〜しかない** or **〜なければならない** (N4) are more common: 中止するしかない。",
        ],
        "examples": [
            {"jp": "台風が来るので、旅行を中止せざるを得ない。", "kana": "たいふうがくるので りょこうをちゅうしせざるをえない", "romaji": "taifuu ga kuru node, ryokou o chuushi sezaru o enai", "en": "A typhoon is coming, so we have no choice but to cancel the trip."},
            {"jp": "先生に言われたら、やらざるを得ない。", "kana": "せんせいにいわれたら やらざるをえない", "romaji": "sensei ni iwaretara, yarazaru o enai", "en": "If the teacher tells me to, I'll have to do it."},
            {"jp": "彼の言うことは正しいと認めざるを得ない。", "kana": "かれのいうことはただしいとみとめざるをえない", "romaji": "kare no iu koto wa tadashii to mitomezaru o enai", "en": "I have to admit that what he says is right."},
            {"jp": "終電がないので、タクシーで帰らざるを得なかった。", "kana": "しゅうでんがないので タクシーでかえらざるをえなかった", "romaji": "shuuden ga nai node, takushii de kaerazaru o enakatta", "en": "There was no last train, so I had no choice but to go home by taxi."},
        ],
        "vocab": [
            {"word": "得る", "reading": "える", "meaning": "to get (in ざるを得ない)"},
            {"word": "認める", "reading": "みとめる", "meaning": "to admit, accept"},
            {"word": "終電", "reading": "しゅうでん", "meaning": "the last train"},
            {"word": "中止", "reading": "ちゅうし", "meaning": "cancellation"},
            {"word": "しかない", "reading": "しかない", "meaning": "there's nothing to do but"},
        ],
    },
    {
        "id": "n2-09",
        "title": "As soon as, depending on",
        "jp_title": "〜次第・〜次第で",
        "goal": "Promise to act as soon as something happens, and say what a result depends on.",
        "points": [
            "**[ます-stem] + 次第** = as soon as (then I'll do something; polite, for future actions): 準備ができ次第、出発します。",
            "It isn't used for things that already happened; for those, use 〜とすぐ. A common polite phrase: 分かり次第、ご連絡します。",
            "**[noun] + 次第だ / 次第で** = depending on, it's up to: 合格できるかどうかは、あなたの努力次第です。",
            "天気次第で = depending on the weather: 天気次第で、予定が変わるかもしれません。",
        ],
        "examples": [
            {"jp": "準備ができ次第、出発します。", "kana": "じゅんびができしだい しゅっぱつします", "romaji": "junbi ga deki shidai, shuppatsu shimasu", "en": "We'll leave as soon as we're ready."},
            {"jp": "結果が分かり次第、ご連絡します。", "kana": "けっかがわかりしだい ごれんらくします", "romaji": "kekka ga wakari shidai, go renraku shimasu", "en": "I'll contact you as soon as I know the results."},
            {"jp": "合格できるかどうかは、あなたの努力次第です。", "kana": "ごうかくできるかどうかは あなたのどりょくしだいです", "romaji": "goukaku dekiru ka dou ka wa, anata no doryoku shidai desu", "en": "Whether you pass depends on your own effort."},
            {"jp": "明日の試合は、天気次第で中止になるかもしれない。", "kana": "あしたのしあいは てんきしだいでちゅうしになるかもしれない", "romaji": "ashita no shiai wa, tenki shidai de chuushi ni naru ka mo shirenai", "en": "Tomorrow's match may be called off, depending on the weather."},
        ],
        "vocab": [
            {"word": "次第", "reading": "しだい", "meaning": "as soon as; depending on"},
            {"word": "出発", "reading": "しゅっぱつ", "meaning": "departure"},
            {"word": "努力", "reading": "どりょく", "meaning": "effort"},
            {"word": "準備", "reading": "じゅんび", "meaning": "preparation"},
            {"word": "かどうか", "reading": "かどうか", "meaning": "whether or not"},
        ],
    },
    {
        "id": "n2-10",
        "title": "More and more, in the process of",
        "jp_title": "〜一方だ・〜つつある",
        "goal": "Describe a trend that keeps going, and a change that is happening now.",
        "points": [
            "**[dictionary form] + 一方だ** = keeps on (getting more and more ...), usually a bad trend: 最近、物価は上がる一方だ。",
            "It goes with verbs of change: 増える, 減る, 悪くなる, 高くなる.",
            "**[ます-stem] + つつある** = is in the process of (a gradual change happening now; formal): この町の人口は、減りつつある。",
            "Don't confuse it with **〜一方で** (on the other hand), from N3 reading: 便利になった一方で、問題も増えた。",
        ],
        "examples": [
            {"jp": "最近、物価は上がる一方だ。", "kana": "さいきん ぶっかはあがるいっぽうだ", "romaji": "saikin, bukka wa agaru ippou da", "en": "Prices just keep going up these days."},
            {"jp": "祖父の病気は、悪くなる一方だった。", "kana": "そふのびょうきは わるくなるいっぽうだった", "romaji": "sofu no byouki wa, waruku naru ippou datta", "en": "My grandfather's illness kept getting worse."},
            {"jp": "この町の人口は、減りつつある。", "kana": "このまちのじんこうは へりつつある", "romaji": "kono machi no jinkou wa, heri tsutsu aru", "en": "This town's population is gradually falling."},
            {"jp": "外国から来る観光客は、増えつつある。", "kana": "がいこくからくるかんこうきゃくは ふえつつある", "romaji": "gaikoku kara kuru kankoukyaku wa, fue tsutsu aru", "en": "The number of tourists from abroad is steadily rising."},
        ],
        "vocab": [
            {"word": "物価", "reading": "ぶっか", "meaning": "prices (cost of living)"},
            {"word": "人口", "reading": "じんこう", "meaning": "population"},
            {"word": "減る", "reading": "へる", "meaning": "to decrease"},
            {"word": "観光客", "reading": "かんこうきゃく", "meaning": "tourist"},
            {"word": "病気", "reading": "びょうき", "meaning": "illness"},
        ],
    },
    {
        "id": "n2-11",
        "title": "Not only, of all times",
        "jp_title": "〜に限らず・〜に限って",
        "goal": "Say that something isn't limited to one group, and complain that it happens at the worst moment.",
        "points": [
            "**[noun] + に限らず** = not only, not limited to: この店は、若い人に限らず、お年寄りにも人気がある。",
            "**[noun / plain form] + に限って** = of all (days, times or people), precisely when: 急いでいる日に限って、電車が遅れる。",
            "**に限り** = only (limited to), common on notices: 先着十名に限り、無料です。",
            "**[dictionary form] + に限る** = there's nothing better than: 疲れたときは、早く寝るに限る。",
        ],
        "examples": [
            {"jp": "この店は、若い人に限らず、お年寄りにも人気がある。", "kana": "このみせは わかいひとにかぎらず おとしよりにもにんきがある", "romaji": "kono mise wa, wakai hito ni kagirazu, otoshiyori ni mo ninki ga aru", "en": "This shop is popular not only with young people but with older people too."},
            {"jp": "急いでいる日に限って、電車が遅れる。", "kana": "いそいでいるひにかぎって でんしゃがおくれる", "romaji": "isoide iru hi ni kagitte, densha ga okureru", "en": "It's always on the days I'm in a hurry that the train is late."},
            {"jp": "傘を持っていない日に限って、雨が降る。", "kana": "かさをもっていないひにかぎって あめがふる", "romaji": "kasa o motte inai hi ni kagitte, ame ga furu", "en": "It always rains on the one day I don't have an umbrella."},
            {"jp": "疲れたときは、早く寝るに限る。", "kana": "つかれたときは はやくねるにかぎる", "romaji": "tsukareta toki wa, hayaku neru ni kagiru", "en": "When you're tired, there's nothing better than going to bed early."},
        ],
        "vocab": [
            {"word": "限る", "reading": "かぎる", "meaning": "to limit; to be best"},
            {"word": "お年寄り", "reading": "おとしより", "meaning": "elderly people"},
            {"word": "人気", "reading": "にんき", "meaning": "popularity"},
            {"word": "急ぐ", "reading": "いそぐ", "meaning": "to hurry"},
            {"word": "先着", "reading": "せんちゃく", "meaning": "first come (first served)"},
        ],
    },
    {
        "id": "n2-12",
        "title": "Merely, no more than",
        "jp_title": "〜にすぎない",
        "goal": "Play something down as small or unimportant.",
        "points": [
            "**[noun / plain form] + にすぎない** = merely, no more than: それは、ただの噂にすぎない。",
            "It makes something sound small: 私は、日本語を勉強している一人の学生にすぎません。",
            "Often with numbers: 参加者は、十人にすぎなかった。 \"There were only ten participants.\"",
            "Also written **に過ぎない**. It's more formal than だけ and stresses how little it is.",
        ],
        "examples": [
            {"jp": "それは、ただの噂にすぎない。", "kana": "それは ただのうわさにすぎない", "romaji": "sore wa, tada no uwasa ni suginai", "en": "That's nothing but a rumour."},
            {"jp": "私は、日本語を勉強している一人の学生にすぎません。", "kana": "わたしは にほんごをべんきょうしているひとりのがくせいにすぎません", "romaji": "watashi wa, nihongo o benkyou shite iru hitori no gakusei ni sugimasen", "en": "I'm just one student studying Japanese."},
            {"jp": "説明会の参加者は、十人にすぎなかった。", "kana": "せつめいかいのさんかしゃは じゅうにんにすぎなかった", "romaji": "setsumeikai no sankasha wa, juunin ni suginakatta", "en": "Only ten people came to the information session."},
            {"jp": "これは私の考えにすぎないが、もう少し待ったほうがいいと思う。", "kana": "これはわたしのかんがえにすぎないが もうすこしまったほうがいいとおもう", "romaji": "kore wa watashi no kangae ni suginai ga, mou sukoshi matta hou ga ii to omou", "en": "This is just my opinion, but I think we should wait a little longer."},
        ],
        "vocab": [
            {"word": "噂", "reading": "うわさ", "meaning": "rumour"},
            {"word": "ただの", "reading": "ただの", "meaning": "mere, just a"},
            {"word": "参加者", "reading": "さんかしゃ", "meaning": "participant"},
            {"word": "説明会", "reading": "せつめいかい", "meaning": "information session"},
            {"word": "考え", "reading": "かんがえ", "meaning": "idea, opinion"},
        ],
    },
    {
        "id": "n2-13",
        "title": "Unable to, could well",
        "jp_title": "〜かねる・〜かねない",
        "goal": "Refuse politely, and warn that something bad could happen.",
        "points": [
            "**[ます-stem] + かねる** = can't (a polite refusal: I'd like to, but it's difficult): その質問には、お答えしかねます。",
            "It's common in shops and formal replies: 分かりかねます \"I'm afraid I can't say\".",
            "**[ます-stem] + かねない** = could well, might (a bad result): スピードを出しすぎると、事故になりかねない。",
            "Careful: かねる means \"can't\", but かねない means \"it could happen\", not \"can't not\".",
        ],
        "examples": [
            {"jp": "申し訳ありませんが、その質問にはお答えしかねます。", "kana": "もうしわけありませんが そのしつもんにはおこたえしかねます", "romaji": "moushiwake arimasen ga, sono shitsumon ni wa okotae shikanemasu", "en": "I'm sorry, but I'm unable to answer that question."},
            {"jp": "この件については、私には分かりかねます。", "kana": "このけんについては わたしにはわかりかねます", "romaji": "kono ken ni tsuite wa, watashi ni wa wakarikanemasu", "en": "I'm afraid I can't say anything about this matter."},
            {"jp": "スピードを出しすぎると、事故になりかねない。", "kana": "スピードをだしすぎると じこになりかねない", "romaji": "supiido o dashisugiru to, jiko ni narikanenai", "en": "If you go too fast, you could well have an accident."},
            {"jp": "そんなことを言ったら、誤解されかねないよ。", "kana": "そんなことをいったら ごかいされかねないよ", "romaji": "sonna koto o ittara, gokai sarekanenai yo", "en": "If you say something like that, you could be misunderstood."},
        ],
        "vocab": [
            {"word": "事故", "reading": "じこ", "meaning": "accident"},
            {"word": "誤解", "reading": "ごかい", "meaning": "misunderstanding"},
            {"word": "答える", "reading": "こたえる", "meaning": "to answer"},
            {"word": "スピード", "reading": "スピード", "meaning": "speed"},
        ],
    },
    {
        "id": "n2-14",
        "title": "There is a risk that",
        "jp_title": "〜おそれがある",
        "goal": "Warn formally that something bad may happen, as news and notices do.",
        "points": [
            "**[dictionary form / noun の] + おそれがある** = there is a risk that (something bad; formal): "
            "明日の夜、台風が上陸するおそれがあります。",
            "Also written **恐れがある**. Negative: **おそれはない** = there's no risk of.",
            "It's stronger and more formal than かもしれない, and always about something bad.",
            "Typical of weather reports and warnings: 大雨のおそれ, 津波のおそれはありません.",
        ],
        "examples": [
            {"jp": "明日の夜、台風が上陸するおそれがあります。", "kana": "あしたのよる たいふうがじょうりくするおそれがあります", "romaji": "ashita no yoru, taifuu ga jouriku suru osore ga arimasu", "en": "There is a risk the typhoon will make landfall tomorrow night."},
            {"jp": "この薬は眠くなるおそれがあるので、運転の前には飲まないでください。", "kana": "このくすりはねむくなるおそれがあるので うんてんのまえにはのまないでください", "romaji": "kono kusuri wa nemuku naru osore ga aru node, unten no mae ni wa nomanaide kudasai", "en": "This medicine may make you drowsy, so don't take it before driving."},
            {"jp": "このままでは、この動物は絶滅するおそれがある。", "kana": "このままでは このどうぶつはぜつめつするおそれがある", "romaji": "kono mama de wa, kono doubutsu wa zetsumetsu suru osore ga aru", "en": "If things go on like this, this animal may die out."},
            {"jp": "この地震による津波のおそれはありません。", "kana": "このじしんによるつなみのおそれはありません", "romaji": "kono jishin ni yoru tsunami no osore wa arimasen", "en": "There is no risk of a tsunami from this earthquake."},
        ],
        "vocab": [
            {"word": "上陸", "reading": "じょうりく", "meaning": "landfall, landing"},
            {"word": "絶滅", "reading": "ぜつめつ", "meaning": "extinction"},
            {"word": "地震", "reading": "じしん", "meaning": "earthquake"},
            {"word": "津波", "reading": "つなみ", "meaning": "tsunami"},
            {"word": "眠い", "reading": "ねむい", "meaning": "sleepy"},
        ],
    },
    {
        "id": "n2-15",
        "title": "While, even though",
        "jp_title": "〜つつ・〜つつも",
        "goal": "Describe two actions at once, and admit doing something you know you shouldn't.",
        "points": [
            "**[ます-stem] + つつ** = while (two things at once; a written ながら): 景色を楽しみつつ、山道を歩いた。",
            "**[ます-stem] + つつも** = although, even while (doing something that goes against it): "
            "体に悪いと知りつつも、夜遅くまでゲームをしてしまう。",
            "つつも often goes with feelings and knowledge: 悪いと分かりつつも, 返事をしなければと思いつつ.",
            "Don't confuse it with **〜つつある** (lesson 10), which is a change in progress.",
        ],
        "examples": [
            {"jp": "景色を楽しみつつ、山道を歩いた。", "kana": "けしきをたのしみつつ やまみちをあるいた", "romaji": "keshiki o tanoshimi tsutsu, yamamichi o aruita", "en": "I walked the mountain path while enjoying the scenery."},
            {"jp": "体に悪いと知りつつも、夜遅くまでゲームをしてしまう。", "kana": "からだにわるいとしりつつも よるおそくまでゲームをしてしまう", "romaji": "karada ni warui to shiri tsutsu mo, yoru osoku made geemu o shite shimau", "en": "I know it's bad for me, yet I end up playing games until late at night."},
            {"jp": "早く返事をしなければと思いつつ、一週間もたってしまった。", "kana": "はやくへんじをしなければとおもいつつ いっしゅうかんもたってしまった", "romaji": "hayaku henji o shinakereba to omoi tsutsu, isshuukan mo tatte shimatta", "en": "I kept meaning to reply soon, but a whole week went by."},
            {"jp": "よくないと分かりつつも、つい甘い物を食べてしまう。", "kana": "よくないとわかりつつも ついあまいものをたべてしまう", "romaji": "yokunai to wakari tsutsu mo, tsui amai mono o tabete shimau", "en": "I know it's not good, but I always end up eating sweets."},
        ],
        "vocab": [
            {"word": "返事", "reading": "へんじ", "meaning": "reply"},
            {"word": "つい", "reading": "つい", "meaning": "without meaning to"},
            {"word": "山道", "reading": "やまみち", "meaning": "mountain path"},
            {"word": "知る", "reading": "しる", "meaning": "to know, find out"},
        ],
    },
    {
        "id": "n2-16",
        "title": "Now that, since",
        "jp_title": "〜からには・〜以上は",
        "goal": "Say that because of a situation, you must see something through.",
        "points": [
            "**[plain form] + からには** = now that, since (so you must or should follow through): 約束したからには、必ず守ります。",
            "The second half is a duty, decision or strong wish: 〜なければならない, 〜べきだ, 〜つもりだ, 〜たい.",
            "**[plain form] + 以上(は)** = since, as long as (the same idea, a little more formal): 試合に出る以上は、絶対に勝ちたい。",
            "Nouns take である: 学生である以上, 学生であるからには.",
        ],
        "examples": [
            {"jp": "約束したからには、必ず守ります。", "kana": "やくそくしたからには かならずまもります", "romaji": "yakusoku shita kara ni wa, kanarazu mamorimasu", "en": "Now that I've promised, I'll definitely keep my word."},
            {"jp": "日本に来たからには、日本語を話せるようになりたい。", "kana": "にほんにきたからには にほんごをはなせるようになりたい", "romaji": "nihon ni kita kara ni wa, nihongo o hanaseru you ni naritai", "en": "Since I've come to Japan, I want to become able to speak Japanese."},
            {"jp": "試合に出る以上は、絶対に勝ちたい。", "kana": "しあいにでるいじょうは ぜったいにかちたい", "romaji": "shiai ni deru ijou wa, zettai ni kachitai", "en": "Since I'm playing in the match, I absolutely want to win."},
            {"jp": "学生である以上、授業には出るべきだ。", "kana": "がくせいであるいじょう じゅぎょうにはでるべきだ", "romaji": "gakusei de aru ijou, jugyou ni wa deru beki da", "en": "As long as you're a student, you should go to your classes."},
        ],
        "vocab": [
            {"word": "必ず", "reading": "かならず", "meaning": "definitely, without fail"},
            {"word": "絶対に", "reading": "ぜったいに", "meaning": "absolutely"},
            {"word": "勝つ", "reading": "かつ", "meaning": "to win"},
            {"word": "べき", "reading": "べき", "meaning": "should (〜べきだ)"},
        ],
    },
    {
        "id": "n2-17",
        "title": "For a..., considering",
        "jp_title": "〜にしては",
        "goal": "Say that something is surprising for the standard you'd expect.",
        "points": [
            "**[noun / plain form] + にしては** = for (a ...), considering: 初めてにしては、とても上手ですね。",
            "Nouns attach directly (子供にしては, 五月にしては); verbs use the plain form (十年も住んでいるにしては).",
            "Compare **わりに** (N3): very similar, but にしては usually has a clear standard: a person, a number, a situation.",
            "It can praise or criticise: 子供が作ったにしてはよくできている / 十年住んでいるにしては話せない.",
        ],
        "examples": [
            {"jp": "初めてにしては、とても上手ですね。", "kana": "はじめてにしては とてもじょうずですね", "romaji": "hajimete ni shite wa, totemo jouzu desu ne", "en": "That's very good for a first time."},
            {"jp": "この料理は、子供が作ったにしてはよくできている。", "kana": "このりょうりは こどもがつくったにしてはよくできている", "romaji": "kono ryouri wa, kodomo ga tsukutta ni shite wa yoku dekite iru", "en": "For something a child made, this dish is really well done."},
            {"jp": "彼は十年も日本に住んでいるにしては、日本語があまり話せない。", "kana": "かれはじゅうねんもにほんにすんでいるにしては にほんごがあまりはなせない", "romaji": "kare wa juunen mo nihon ni sunde iru ni shite wa, nihongo ga amari hanasenai", "en": "For someone who's lived in Japan for ten years, he can't speak much Japanese."},
            {"jp": "五月にしては、今日は暑いですね。", "kana": "ごがつにしては きょうはあついですね", "romaji": "gogatsu ni shite wa, kyou wa atsui desu ne", "en": "It's hot today for May."},
        ],
        "vocab": [
            {"word": "初めて", "reading": "はじめて", "meaning": "for the first time"},
            {"word": "暑い", "reading": "あつい", "meaning": "hot (weather)"},
            {"word": "よくできる", "reading": "よくできる", "meaning": "to be well made, well done"},
            {"word": "五月", "reading": "ごがつ", "meaning": "May"},
        ],
    },
    {
        "id": "n2-18",
        "title": "Supposing that",
        "jp_title": "〜としたら・〜とすれば",
        "goal": "Talk about imagined situations and draw conclusions from them.",
        "points": [
            "**[plain form] + としたら / とすれば** = if (we suppose that), assuming: もし一億円あったとしたら、何をしますか。",
            "It's for imagined or uncertain situations, often with a question or a guess in the second half.",
            "**とすれば** also draws a conclusion from what you know: 彼が来ないとすれば、何か理由があるのだろう。",
            "Compare たら / ば (N4): としたら stresses that it's only a supposition.",
        ],
        "examples": [
            {"jp": "もし一億円あったとしたら、何をしますか。", "kana": "もしいちおくえんあったとしたら なにをしますか", "romaji": "moshi ichiokuen atta to shitara, nani o shimasu ka", "en": "If you had a hundred million yen, what would you do?"},
            {"jp": "生まれ変われるとしたら、何になりたいですか。", "kana": "うまれかわれるとしたら なにになりたいですか", "romaji": "umarekawareru to shitara, nani ni naritai desu ka", "en": "If you could be reborn, what would you want to be?"},
            {"jp": "彼が来ないとすれば、何か理由があるのだろう。", "kana": "かれがこないとすれば なにかりゆうがあるのだろう", "romaji": "kare ga konai to sureba, nani ka riyuu ga aru no darou", "en": "If he's not coming, there must be some reason."},
            {"jp": "今から出るとしたら、何時に着きますか。", "kana": "いまからでるとしたら なんじにつきますか", "romaji": "ima kara deru to shitara, nanji ni tsukimasu ka", "en": "If we left now, what time would we arrive?"},
        ],
        "vocab": [
            {"word": "一億", "reading": "いちおく", "meaning": "a hundred million"},
            {"word": "生まれ変わる", "reading": "うまれかわる", "meaning": "to be reborn"},
            {"word": "理由", "reading": "りゆう", "meaning": "reason"},
            {"word": "もし", "reading": "もし", "meaning": "if (supposing)"},
        ],
    },
    {
        "id": "n2-19",
        "title": "There's no way to",
        "jp_title": "〜ようがない",
        "goal": "Say that something can't be done because there is simply no means.",
        "points": [
            "**[ます-stem] + ようがない** = there's no way to, can't possibly (no method exists): "
            "連絡先が分からないので、連絡しようがない。",
            "Build it from the ます-stem: 連絡し + ようがない, 直し + ようがない, 行き + ようがない.",
            "**言いようがない** = indescribable: 言いようがないほど美しかった。 **ようもない** is a little stronger.",
            "Compare 〜ことができない: ようがない says there's no means or method at all.",
        ],
        "examples": [
            {"jp": "連絡先が分からないので、連絡しようがない。", "kana": "れんらくさきがわからないので れんらくしようがない", "romaji": "renrakusaki ga wakaranai node, renraku shiyou ga nai", "en": "I don't know their contact details, so there's no way to get in touch."},
            {"jp": "ここまで壊れていたら、もう直しようがない。", "kana": "ここまでこわれていたら もうなおしようがない", "romaji": "koko made kowarete itara, mou naoshiyou ga nai", "en": "When it's this broken, there's no way to fix it."},
            {"jp": "その景色は、言いようがないほど美しかった。", "kana": "そのけしきは いいようがないほどうつくしかった", "romaji": "sono keshiki wa, iiyou ga nai hodo utsukushikatta", "en": "The scenery was indescribably beautiful."},
            {"jp": "道が分からないので、行きようがない。", "kana": "みちがわからないので いきようがない", "romaji": "michi ga wakaranai node, ikiyou ga nai", "en": "I don't know the way, so I have no way of getting there."},
        ],
        "vocab": [
            {"word": "連絡先", "reading": "れんらくさき", "meaning": "contact details"},
            {"word": "直す", "reading": "なおす", "meaning": "to fix, repair"},
            {"word": "美しい", "reading": "うつくしい", "meaning": "beautiful"},
            {"word": "壊れる", "reading": "こわれる", "meaning": "to break"},
        ],
    },
    {
        "id": "n2-20",
        "title": "Used to, that's how it is",
        "jp_title": "〜ものだ",
        "goal": "Look back on the past, state a general truth, and give advice with ものだ.",
        "points": [
            "**[た-form] + ものだ** = used to (looking back fondly): 子供のころは、よくこの川で泳いだものだ。",
            "**[dictionary form] + ものだ** = that's how it is, naturally: 人は、だれでも間違えるものだ。",
            "It also gives advice about what's proper: 人の話は、最後まで聞くものだ。 Negative: 〜ないものだ.",
            "And exclamations: 時間がたつのは、本当に早いものだ。 \"Time really does fly.\"",
        ],
        "examples": [
            {"jp": "子供のころは、よくこの川で泳いだものだ。", "kana": "こどものころは よくこのかわでおよいだものだ", "romaji": "kodomo no koro wa, yoku kono kawa de oyoida mono da", "en": "When I was a child, I often used to swim in this river."},
            {"jp": "人は、だれでも間違えるものだ。", "kana": "ひとは だれでもまちがえるものだ", "romaji": "hito wa, dare demo machigaeru mono da", "en": "Everyone makes mistakes."},
            {"jp": "人の話は、最後まで聞くものだ。", "kana": "ひとのはなしは さいごまできくものだ", "romaji": "hito no hanashi wa, saigo made kiku mono da", "en": "You should listen to people until they've finished."},
            {"jp": "時間がたつのは、本当に早いものだ。", "kana": "じかんがたつのは ほんとうにはやいものだ", "romaji": "jikan ga tatsu no wa, hontou ni hayai mono da", "en": "Time really does fly."},
        ],
        "vocab": [
            {"word": "川", "reading": "かわ", "meaning": "river"},
            {"word": "間違える", "reading": "まちがえる", "meaning": "to make a mistake"},
            {"word": "最後", "reading": "さいご", "meaning": "the end, last"},
            {"word": "だれでも", "reading": "だれでも", "meaning": "anyone, everyone"},
        ],
    },
    {
        "id": "n2-21",
        "title": "According to, in line with",
        "jp_title": "〜に応じて・〜に沿って",
        "goal": "Say that something changes to match a situation, or follows a line, plan or wish.",
        "points": [
            "**[noun] + に応じて** = according to, in response to (changing to match): 料金は、利用する時間に応じて変わります。",
            "Before a noun use **に応じた**: レベルに応じたクラス.",
            "**[noun] + に沿って** = along, in line with (following a line, plan or wish): 川に沿って歩く。 計画に沿って進める。",
            "Before a noun use **に沿った**: 希望に沿った部屋.",
        ],
        "examples": [
            {"jp": "料金は、利用する時間に応じて変わります。", "kana": "りょうきんは りようするじかんにおうじてかわります", "romaji": "ryoukin wa, riyou suru jikan ni oujite kawarimasu", "en": "The fee changes according to how long you use it."},
            {"jp": "このスクールでは、レベルに応じたクラスを選べます。", "kana": "このスクールでは レベルにおうじたクラスをえらべます", "romaji": "kono sukuuru de wa, reberu ni oujita kurasu o erabemasu", "en": "At this school, you can choose a class that suits your level."},
            {"jp": "川に沿って、桜の木が並んでいる。", "kana": "かわにそって さくらのきがならんでいる", "romaji": "kawa ni sotte, sakura no ki ga narande iru", "en": "Cherry trees line the river."},
            {"jp": "計画に沿って、準備を進めましょう。", "kana": "けいかくにそって じゅんびをすすめましょう", "romaji": "keikaku ni sotte, junbi o susumemashou", "en": "Let's go ahead with the preparations according to the plan."},
        ],
        "vocab": [
            {"word": "応じる", "reading": "おうじる", "meaning": "to respond, to match"},
            {"word": "沿う", "reading": "そう", "meaning": "to follow (a line, plan)"},
            {"word": "利用", "reading": "りよう", "meaning": "use"},
            {"word": "並ぶ", "reading": "ならぶ", "meaning": "to line up"},
            {"word": "進める", "reading": "すすめる", "meaning": "to move forward with"},
            {"word": "桜", "reading": "さくら", "meaning": "cherry blossom"},
        ],
    },
    {
        "id": "n2-22",
        "title": "Starting with, including",
        "jp_title": "〜をはじめ",
        "goal": "Give the most typical example first, then widen to the whole group.",
        "points": [
            "**[noun] + をはじめ** = starting with, including (the most typical example first): "
            "東京をはじめ、日本の大きな町には外国人が多い。",
            "**をはじめとして / をはじめとする** are more formal: 校長先生をはじめとする先生方.",
            "The second half covers a bigger group: 〜など, たくさんの〜, いろいろな〜.",
            "It can also be written with kanji: **を始め**.",
        ],
        "examples": [
            {"jp": "東京をはじめ、日本の大きな町には外国人が多い。", "kana": "とうきょうをはじめ にほんのおおきなまちにはがいこくじんがおおい", "romaji": "toukyou o hajime, nihon no ookina machi ni wa gaikokujin ga ooi", "en": "Tokyo and Japan's other big cities have many foreign residents."},
            {"jp": "このお店には、すしをはじめ、いろいろな日本料理がある。", "kana": "このおみせには すしをはじめ いろいろなにほんりょうりがある", "romaji": "kono omise ni wa, sushi o hajime, iroiro na nihon ryouri ga aru", "en": "This restaurant has all kinds of Japanese food, starting with sushi."},
            {"jp": "両親をはじめ、たくさんの人に助けてもらいました。", "kana": "りょうしんをはじめ たくさんのひとにたすけてもらいました", "romaji": "ryoushin o hajime, takusan no hito ni tasukete moraimashita", "en": "Many people helped me, my parents first among them."},
            {"jp": "校長先生をはじめとする先生方が、会場に集まった。", "kana": "こうちょうせんせいをはじめとするせんせいがたが かいじょうにあつまった", "romaji": "kouchou sensei o hajime to suru senseigata ga, kaijou ni atsumatta", "en": "The teachers, led by the headteacher, gathered in the hall."},
        ],
        "vocab": [
            {"word": "両親", "reading": "りょうしん", "meaning": "parents"},
            {"word": "校長", "reading": "こうちょう", "meaning": "headteacher, principal"},
            {"word": "先生方", "reading": "せんせいがた", "meaning": "teachers (polite plural)"},
            {"word": "外国人", "reading": "がいこくじん", "meaning": "foreigner"},
            {"word": "助ける", "reading": "たすける", "meaning": "to help"},
        ],
    },
    {
        "id": "n2-23",
        "title": "On the other hand",
        "jp_title": "〜反面",
        "goal": "Describe the good and bad sides of the same thing.",
        "points": [
            "**[plain form] + 反面** = while, on the other hand (two opposite sides of one thing): 都会の生活は、便利な反面、物価が高い。",
            "な-adjectives take な or である, nouns take である: 便利な反面, 学生である反面.",
            "**一方(で)** is similar, but it can also compare two different things; 反面 is one thing's two sides.",
            "**その反面** can start a sentence: その反面、寂しいこともある。",
        ],
        "examples": [
            {"jp": "都会の生活は、便利な反面、物価が高い。", "kana": "とかいのせいかつは べんりなはんめん ぶっかがたかい", "romaji": "tokai no seikatsu wa, benri na hanmen, bukka ga takai", "en": "City life is convenient, but on the other hand, prices are high."},
            {"jp": "スマートフォンは便利な反面、使いすぎると目が疲れる。", "kana": "スマートフォンはべんりなはんめん つかいすぎるとめがつかれる", "romaji": "sumaatofon wa benri na hanmen, tsukaisugiru to me ga tsukareru", "en": "Smartphones are handy, but use them too much and your eyes get tired."},
            {"jp": "一人暮らしは自由な反面、寂しいこともある。", "kana": "ひとりぐらしはじゆうなはんめん さびしいこともある", "romaji": "hitorigurashi wa jiyuu na hanmen, sabishii koto mo aru", "en": "Living alone gives you freedom, but it can be lonely too."},
            {"jp": "姉は厳しい反面、とても優しいところもある。", "kana": "あねはきびしいはんめん とてもやさしいところもある", "romaji": "ane wa kibishii hanmen, totemo yasashii tokoro mo aru", "en": "My older sister is strict, but she has a very kind side too."},
        ],
        "vocab": [
            {"word": "反面", "reading": "はんめん", "meaning": "the other side, on the other hand"},
            {"word": "都会", "reading": "とかい", "meaning": "city"},
            {"word": "一人暮らし", "reading": "ひとりぐらし", "meaning": "living alone"},
            {"word": "自由", "reading": "じゆう", "meaning": "freedom; free"},
        ],
    },
    {
        "id": "n2-24",
        "title": "Together with, as",
        "jp_title": "〜とともに",
        "goal": "Say who you do something with, and that two changes happen together.",
        "points": [
            "**[noun] + とともに** = together with (a formal と一緒に): 家族とともに、日本に引っ越しました。",
            "**[dictionary form / noun] + とともに** = as (one change goes with another): 年をとるとともに、体力が落ちてきた。",
            "It also means \"at the same time as\": 卒業とともに、国へ帰った。",
            "It can be written with kanji: **と共に**.",
        ],
        "examples": [
            {"jp": "家族とともに、日本に引っ越しました。", "kana": "かぞくとともに にほんにひっこしました", "romaji": "kazoku to tomo ni, nihon ni hikkoshimashita", "en": "I moved to Japan together with my family."},
            {"jp": "年をとるとともに、体力が落ちてきた。", "kana": "としをとるとともに たいりょくがおちてきた", "romaji": "toshi o toru to tomo ni, tairyoku ga ochite kita", "en": "My stamina has been dropping as I get older."},
            {"jp": "卒業とともに、国へ帰った。", "kana": "そつぎょうとともに くにへかえった", "romaji": "sotsugyou to tomo ni, kuni e kaetta", "en": "As soon as I graduated, I went back to my country."},
            {"jp": "インターネットの発達とともに、生活が大きく変わった。", "kana": "インターネットのはったつとともに せいかつがおおきくかわった", "romaji": "intaanetto no hattatsu to tomo ni, seikatsu ga ookiku kawatta", "en": "Life has changed greatly along with the development of the internet."},
        ],
        "vocab": [
            {"word": "体力", "reading": "たいりょく", "meaning": "stamina, physical strength"},
            {"word": "卒業", "reading": "そつぎょう", "meaning": "graduation"},
            {"word": "発達", "reading": "はったつ", "meaning": "development"},
            {"word": "落ちる", "reading": "おちる", "meaning": "to fall, drop"},
            {"word": "年をとる", "reading": "としをとる", "meaning": "to get older"},
        ],
    },
    {
        "id": "n2-25",
        "title": "It's not that... not",
        "jp_title": "〜ないことはない",
        "goal": "Give a hedged yes, and tell someone there's no need to do something.",
        "points": [
            "**[ない form] + ことはない** = it's not that ... not (it's possible, but with reservations): "
            "食べられないことはないが、あまり好きではない。",
            "It's a hesitant yes: 急げば、間に合わないことはない \"We might just make it if we hurry\".",
            "**ないこともない** is a little softer: 彼の気持ちも、分からないこともない。",
            "Don't mix it up with **[dictionary form] + ことはない** = there's no need to: そんなに心配することはないよ。",
        ],
        "examples": [
            {"jp": "納豆は、食べられないことはないが、あまり好きではない。", "kana": "なっとうは たべられないことはないが あまりすきではない", "romaji": "nattou wa, taberarenai koto wa nai ga, amari suki de wa nai", "en": "It's not that I can't eat natto, but I don't really like it."},
            {"jp": "急げば、間に合わないことはない。", "kana": "いそげば まにあわないことはない", "romaji": "isogeba, maniawanai koto wa nai", "en": "If we hurry, we might just make it."},
            {"jp": "彼の気持ちも、分からないこともない。", "kana": "かれのきもちも わからないこともない", "romaji": "kare no kimochi mo, wakaranai koto mo nai", "en": "I can sort of understand how he feels."},
            {"jp": "そんなに心配することはないよ。", "kana": "そんなにしんぱいすることはないよ", "romaji": "sonna ni shinpai suru koto wa nai yo", "en": "There's no need to worry so much."},
        ],
        "vocab": [
            {"word": "納豆", "reading": "なっとう", "meaning": "natto (fermented soybeans)"},
            {"word": "間に合う", "reading": "まにあう", "meaning": "to be in time"},
            {"word": "気持ち", "reading": "きもち", "meaning": "feelings"},
            {"word": "心配", "reading": "しんぱい", "meaning": "worry"},
        ],
    },
    {
        "id": "n2-26",
        "title": "When it comes to",
        "jp_title": "〜にかけては",
        "goal": "Praise a skill that nobody can beat.",
        "points": [
            "**[noun] + にかけては** = when it comes to (praising a skill): 料理にかけては、母がいちばんだ。",
            "The second half is strongly positive: だれにも負けない, 自信がある, かなう人はいない.",
            "It's for skills and abilities. For a neutral topic use について or に関して (lesson 6).",
            "With verbs, add こと: 走ることにかけては、だれにも負けない。",
        ],
        "examples": [
            {"jp": "料理にかけては、母がいちばんだ。", "kana": "りょうりにかけては ははがいちばんだ", "romaji": "ryouri ni kakete wa, haha ga ichiban da", "en": "When it comes to cooking, my mother is the best."},
            {"jp": "走ることにかけては、だれにも負けない。", "kana": "はしることにかけては だれにもまけない", "romaji": "hashiru koto ni kakete wa, dare ni mo makenai", "en": "When it comes to running, I'm second to none."},
            {"jp": "彼は、ゲームにかけては自信があるらしい。", "kana": "かれは ゲームにかけてはじしんがあるらしい", "romaji": "kare wa, geemu ni kakete wa jishin ga aru rashii", "en": "Apparently he's very confident when it comes to games."},
            {"jp": "記憶力にかけては、弟にかなわない。", "kana": "きおくりょくにかけては おとうとにかなわない", "romaji": "kiokuryoku ni kakete wa, otouto ni kanawanai", "en": "When it comes to memory, I'm no match for my little brother."},
        ],
        "vocab": [
            {"word": "自信", "reading": "じしん", "meaning": "confidence"},
            {"word": "記憶力", "reading": "きおくりょく", "meaning": "memory (ability)"},
            {"word": "かなわない", "reading": "かなわない", "meaning": "to be no match for"},
            {"word": "負ける", "reading": "まける", "meaning": "to lose"},
        ],
    },
    {
        "id": "n2-27",
        "title": "To my surprise, sadly",
        "jp_title": "〜ことに",
        "goal": "Put your feeling about a fact first: to my surprise, sadly, luckily.",
        "points": [
            "**[feeling word] + ことに** = (I find it) ... that: 驚いたことに、彼はもう結婚していた。",
            "Common ones: 残念なことに (sadly), うれしいことに (happily), 困ったことに (annoyingly), 驚いたことに (surprisingly).",
            "な-adjectives take な (残念なことに), い-adjectives attach directly (うれしいことに), verbs use the た-form (驚いたことに).",
            "It's mostly used in writing or formal speech.",
        ],
        "examples": [
            {"jp": "驚いたことに、彼はもう結婚していた。", "kana": "おどろいたことに かれはもうけっこんしていた", "romaji": "odoroita koto ni, kare wa mou kekkon shite ita", "en": "To my surprise, he was already married."},
            {"jp": "残念なことに、雨で花火大会が中止になった。", "kana": "ざんねんなことに あめではなびたいかいがちゅうしになった", "romaji": "zannen na koto ni, ame de hanabi taikai ga chuushi ni natta", "en": "Sadly, the fireworks festival was cancelled because of the rain."},
            {"jp": "うれしいことに、試験に合格していた。", "kana": "うれしいことに しけんにごうかくしていた", "romaji": "ureshii koto ni, shiken ni goukaku shite ita", "en": "To my joy, I had passed the exam."},
            {"jp": "困ったことに、財布を家に忘れてきた。", "kana": "こまったことに さいふをいえにわすれてきた", "romaji": "komatta koto ni, saifu o ie ni wasurete kita", "en": "Annoyingly, I've left my wallet at home."},
        ],
        "vocab": [
            {"word": "残念", "reading": "ざんねん", "meaning": "disappointing, a pity"},
            {"word": "花火大会", "reading": "はなびたいかい", "meaning": "fireworks festival"},
            {"word": "驚く", "reading": "おどろく", "meaning": "to be surprised"},
            {"word": "うれしい", "reading": "うれしい", "meaning": "happy, glad"},
        ],
    },
    {
        "id": "n2-28",
        "title": "From the fact that",
        "jp_title": "〜ことから",
        "goal": "Give a fact as the reason for a name or as evidence for a conclusion.",
        "points": [
            "**[plain form] + ことから** = from the fact that, because (a fact that explains a name or a conclusion): "
            "形が星に似ていることから、この花は星の花と呼ばれている。",
            "It's common when explaining names and in reasoning: 〜ことから、〜と考えられる / 〜と分かる.",
            "な-adjectives take な or である, nouns take である: 静かなことから, 島であることから.",
            "It's more formal than から and ので, and points to a fact as evidence.",
        ],
        "examples": [
            {"jp": "形が星に似ていることから、この花は星の花と呼ばれている。", "kana": "かたちがほしににていることから このはなはほしのはなとよばれている", "romaji": "katachi ga hoshi ni nite iru koto kara, kono hana wa hoshi no hana to yobarete iru", "en": "Because its shape looks like a star, this flower is called the star flower."},
            {"jp": "道がぬれていることから、夜の間に雨が降ったと分かる。", "kana": "みちがぬれていることから よるのあいだにあめがふったとわかる", "romaji": "michi ga nurete iru koto kara, yoru no aida ni ame ga futta to wakaru", "en": "From the wet roads, you can tell it rained during the night."},
            {"jp": "窓が開いていたことから、警察は泥棒が窓から入ったと考えている。", "kana": "まどがあいていたことから けいさつはどろぼうがまどからはいったとかんがえている", "romaji": "mado ga aite ita koto kara, keisatsu wa dorobou ga mado kara haitta to kangaete iru", "en": "Since the window was open, the police think the burglar came in through it."},
            {"jp": "この鳥は、声が美しいことから、人気がある。", "kana": "このとりは こえがうつくしいことから にんきがある", "romaji": "kono tori wa, koe ga utsukushii koto kara, ninki ga aru", "en": "This bird is popular because of its beautiful song."},
        ],
        "vocab": [
            {"word": "似る", "reading": "にる", "meaning": "to look like, resemble"},
            {"word": "星", "reading": "ほし", "meaning": "star"},
            {"word": "警察", "reading": "けいさつ", "meaning": "police"},
            {"word": "泥棒", "reading": "どろぼう", "meaning": "burglar, thief"},
            {"word": "ぬれる", "reading": "ぬれる", "meaning": "to get wet"},
        ],
    },
    {
        "id": "n2-29",
        "title": "After doing, for doing",
        "jp_title": "〜上で・〜上",
        "goal": "Say that one step comes before another, and what something is needed for.",
        "points": [
            "**[た-form] + 上で** = after (doing A first, then B): よく考えた上で、決めてください。",
            "Nouns take の: 相談の上で, 確認の上.",
            "**[dictionary form] + 上で** = in (doing), for: 日本で生活する上で、日本語はとても大切だ。",
            "**[noun] + 上**, read じょう, = in terms of: 健康上の理由で \"for health reasons\".",
        ],
        "examples": [
            {"jp": "よく考えた上で、決めてください。", "kana": "よくかんがえたうえで きめてください", "romaji": "yoku kangaeta ue de, kimete kudasai", "en": "Please decide after thinking it over carefully."},
            {"jp": "両親と相談の上で、留学することにした。", "kana": "りょうしんとそうだんのうえで りゅうがくすることにした", "romaji": "ryoushin to soudan no ue de, ryuugaku suru koto ni shita", "en": "After talking it over with my parents, I decided to study abroad."},
            {"jp": "日本で生活する上で、日本語はとても大切だ。", "kana": "にほんでせいかつするうえで にほんごはとてもたいせつだ", "romaji": "nihon de seikatsu suru ue de, nihongo wa totemo taisetsu da", "en": "Japanese is very important for living in Japan."},
            {"jp": "彼は、健康上の理由で、大会に出られなかった。", "kana": "かれは けんこうじょうのりゆうで たいかいにでられなかった", "romaji": "kare wa, kenkoujou no riyuu de, taikai ni derarenakatta", "en": "He couldn't take part in the competition for health reasons."},
        ],
        "vocab": [
            {"word": "相談", "reading": "そうだん", "meaning": "talking over, consultation"},
            {"word": "決める", "reading": "きめる", "meaning": "to decide"},
            {"word": "生活", "reading": "せいかつ", "meaning": "life, living"},
            {"word": "健康上", "reading": "けんこうじょう", "meaning": "for health reasons, health-wise"},
        ],
    },
    {
        "id": "n2-30",
        "title": "Can't help doing",
        "jp_title": "〜ずにはいられない",
        "goal": "Say that a feeling or reaction is too strong to hold back.",
        "points": [
            "**[ない-stem] + ずにはいられない** = can't help (doing), can't stop yourself: その映画を見て、泣かずにはいられなかった。",
            "する becomes **せずにはいられない**: 心配せずにはいられない.",
            "In speech, **〜ないではいられない** or simply **〜てしまう** are common.",
            "It's about strong feelings and natural reactions, usually the speaker's own.",
        ],
        "examples": [
            {"jp": "その映画を見て、泣かずにはいられなかった。", "kana": "そのえいがをみて なかずにはいられなかった", "romaji": "sono eiga o mite, nakazu ni wa irarenakatta", "en": "Watching that film, I couldn't help crying."},
            {"jp": "子供が一人で旅行すると聞いて、心配せずにはいられない。", "kana": "こどもがひとりでりょこうするときいて しんぱいせずにはいられない", "romaji": "kodomo ga hitori de ryokou suru to kiite, shinpai sezu ni wa irarenai", "en": "Hearing my child is travelling alone, I can't help worrying."},
            {"jp": "あまりにおかしくて、笑わずにはいられなかった。", "kana": "あまりにおかしくて わらわずにはいられなかった", "romaji": "amari ni okashikute, warawazu ni wa irarenakatta", "en": "It was so funny I couldn't stop laughing."},
            {"jp": "おいしそうなケーキを見ると、買わずにはいられない。", "kana": "おいしそうなケーキをみると かわずにはいられない", "romaji": "oishisou na keeki o miru to, kawazu ni wa irarenai", "en": "When I see a delicious-looking cake, I can't resist buying it."},
        ],
        "vocab": [
            {"word": "泣く", "reading": "なく", "meaning": "to cry"},
            {"word": "笑う", "reading": "わらう", "meaning": "to laugh"},
            {"word": "あまりに", "reading": "あまりに", "meaning": "too, so (much)"},
            {"word": "おかしい", "reading": "おかしい", "meaning": "funny; strange"},
        ],
    },
    # ------------------------------------------------------------------ N1
    {
        "id": "n1-01",
        "title": "Unique to",
        "jp_title": "〜ならではの",
        "goal": "Praise something that only a particular place, person or season can offer.",
        "points": [
            "**[noun] + ならではの** = unique to, that only X can offer (praise): 京都ならではの景色.",
            "At the end of a sentence, **ならではだ**: この丁寧な仕上がりは、手作りならではだ。",
            "Often with people, places and seasons: 子供ならではの発想, 冬ならではの楽しみ.",
            "ならでは is always positive. For a neutral \"typical of\", use らしい (N3).",
        ],
        "examples": [
            {"jp": "これは、京都ならではの景色ですね。", "kana": "これは きょうとならではのけしきですね", "romaji": "kore wa, kyouto nara de wa no keshiki desu ne", "en": "This is scenery you can only find in Kyoto."},
            {"jp": "子供ならではの自由な発想に、驚かされた。", "kana": "こどもならではのじゆうなはっそうに おどろかされた", "romaji": "kodomo nara de wa no jiyuu na hassou ni, odorokasareta", "en": "I was amazed by the free thinking only a child could have."},
            {"jp": "雪の中で入る温泉は、冬ならではの楽しみだ。", "kana": "ゆきのなかではいるおんせんは ふゆならではのたのしみだ", "romaji": "yuki no naka de hairu onsen wa, fuyu nara de wa no tanoshimi da", "en": "Bathing in a hot spring in the snow is a pleasure only winter offers."},
            {"jp": "この丁寧な仕上がりは、手作りならではだ。", "kana": "このていねいなしあがりは てづくりならではだ", "romaji": "kono teinei na shiagari wa, tezukuri nara de wa da", "en": "This careful finish is something only handmade work has."},
        ],
        "vocab": [
            {"word": "発想", "reading": "はっそう", "meaning": "idea, way of thinking"},
            {"word": "温泉", "reading": "おんせん", "meaning": "hot spring"},
            {"word": "仕上がり", "reading": "しあがり", "meaning": "finish, result"},
            {"word": "手作り", "reading": "てづくり", "meaning": "handmade"},
            {"word": "丁寧", "reading": "ていねい", "meaning": "careful, polite"},
        ],
    },
    {
        "id": "n1-02",
        "title": "Once it comes to",
        "jp_title": "〜ともなると・〜ともなれば",
        "goal": "Say that reaching a higher stage naturally brings certain changes or expectations.",
        "points": [
            "**[noun / dictionary form] + ともなると / ともなれば** = once it comes to, when it reaches (a higher stage): "
            "大学生ともなると、自分で考えて行動しなければならない。",
            "It's used for a stage, position or time that brings natural expectations: 週末ともなると, プロともなれば, 十二月ともなれば.",
            "The second half says what is natural at that stage: 〜なければならない, 〜ものだ, 混む, にぎやかになる.",
            "Compare **になると**: ともなると stresses that it's a special or higher level.",
        ],
        "examples": [
            {"jp": "大学生ともなると、自分で考えて行動しなければならない。", "kana": "だいがくせいともなると じぶんでかんがえてこうどうしなければならない", "romaji": "daigakusei to mo naru to, jibun de kangaete koudou shinakereba naranai", "en": "Once you're a university student, you have to think and act for yourself."},
            {"jp": "週末ともなると、この公園は親子でいっぱいになる。", "kana": "しゅうまつともなると このこうえんはおやこでいっぱいになる", "romaji": "shuumatsu to mo naru to, kono kouen wa oyako de ippai ni naru", "en": "At weekends, this park fills up with parents and children."},
            {"jp": "十二月ともなれば、町はどこもにぎやかになる。", "kana": "じゅうにがつともなれば まちはどこもにぎやかになる", "romaji": "juunigatsu to mo nareba, machi wa doko mo nigiyaka ni naru", "en": "Once December comes, the whole town gets lively."},
            {"jp": "プロともなれば、練習の量も違う。", "kana": "プロともなれば れんしゅうのりょうもちがう", "romaji": "puro to mo nareba, renshuu no ryou mo chigau", "en": "At the professional level, even the amount of practice is different."},
        ],
        "vocab": [
            {"word": "行動", "reading": "こうどう", "meaning": "action, behaviour"},
            {"word": "親子", "reading": "おやこ", "meaning": "parent and child"},
            {"word": "量", "reading": "りょう", "meaning": "amount, quantity"},
            {"word": "プロ", "reading": "プロ", "meaning": "professional"},
        ],
    },
    {
        "id": "n1-03",
        "title": "Ignoring, regardless of",
        "jp_title": "〜をよそに",
        "goal": "Describe someone acting without regard for others' worries or the situation.",
        "points": [
            "**[noun] + をよそに** = ignoring, regardless of (other people's feelings or a situation): "
            "親の心配をよそに、彼は一人で旅に出た。",
            "The first part is usually something others care about: 心配, 期待, 反対, 不安.",
            "It has a nuance of not caring and is often a little critical, but it can be neutral: 住民の不安をよそに、工事が始まった。",
            "Compare **にもかかわらず** (N2): をよそに stresses ignoring something.",
        ],
        "examples": [
            {"jp": "親の心配をよそに、彼は一人で旅に出た。", "kana": "おやのしんぱいをよそに かれはひとりでたびにでた", "romaji": "oya no shinpai o yoso ni, kare wa hitori de tabi ni deta", "en": "Ignoring his parents' worries, he set off on a journey alone."},
            {"jp": "周りの反対をよそに、姉は留学を決めた。", "kana": "まわりのはんたいをよそに あねはりゅうがくをきめた", "romaji": "mawari no hantai o yoso ni, ane wa ryuugaku o kimeta", "en": "Despite everyone's opposition, my sister decided to study abroad."},
            {"jp": "試験が近いのをよそに、弟は毎日遊んでいる。", "kana": "しけんがちかいのをよそに おとうとはまいにちあそんでいる", "romaji": "shiken ga chikai no o yoso ni, otouto wa mainichi asonde iru", "en": "Paying no attention to the approaching exam, my brother plays every day."},
            {"jp": "住民の不安をよそに、工事が始まった。", "kana": "じゅうみんのふあんをよそに こうじがはじまった", "romaji": "juumin no fuan o yoso ni, kouji ga hajimatta", "en": "The construction started regardless of the residents' anxiety."},
        ],
        "vocab": [
            {"word": "よそ", "reading": "よそ", "meaning": "elsewhere; (をよそに) ignoring"},
            {"word": "周り", "reading": "まわり", "meaning": "the people around, surroundings"},
            {"word": "不安", "reading": "ふあん", "meaning": "anxiety, unease"},
            {"word": "旅に出る", "reading": "たびにでる", "meaning": "to set out on a journey"},
        ],
    },
    {
        "id": "n1-04",
        "title": "Even though, even",
        "jp_title": "〜といえども",
        "goal": "Say that even a special case doesn't change what follows, formally.",
        "points": [
            "**[noun / plain form] + といえども** = even though, even (it's X, but still ...): "
            "子供といえども、ルールは守らなければならない。",
            "It often goes with たとえ: たとえ親友といえども、言っていいことと悪いことがある。",
            "With 一 + counter it means \"not even\": 一円といえども、無駄にはできない。",
            "It's like とはいえ (N2) and ても (N4), but more formal and written.",
        ],
        "examples": [
            {"jp": "子供といえども、ルールは守らなければならない。", "kana": "こどもといえども ルールはまもらなければならない", "romaji": "kodomo to iedomo, ruuru wa mamoranakereba naranai", "en": "Even children must follow the rules."},
            {"jp": "たとえ親友といえども、言っていいことと悪いことがある。", "kana": "たとえしんゆうといえども いっていいこととわるいことがある", "romaji": "tatoe shinyuu to iedomo, itte ii koto to warui koto ga aru", "en": "Even with a best friend, there are things you can and can't say."},
            {"jp": "冬といえども、この地方はあまり寒くない。", "kana": "ふゆといえども このちほうはあまりさむくない", "romaji": "fuyu to iedomo, kono chihou wa amari samukunai", "en": "Even in winter, this region isn't very cold."},
            {"jp": "一円といえども、無駄にはできない。", "kana": "いちえんといえども むだにはできない", "romaji": "ichien to iedomo, muda ni wa dekinai", "en": "Not even a single yen can be wasted."},
        ],
        "vocab": [
            {"word": "親友", "reading": "しんゆう", "meaning": "best friend"},
            {"word": "地方", "reading": "ちほう", "meaning": "region, area"},
            {"word": "無駄", "reading": "むだ", "meaning": "waste"},
            {"word": "たとえ", "reading": "たとえ", "meaning": "even if, even"},
        ],
    },
    {
        "id": "n1-05",
        "title": "The moment, as soon as",
        "jp_title": "〜や否や・〜なり",
        "goal": "Describe something that happened the instant something else did.",
        "points": [
            "**[dictionary form] + や否や** = the moment, as soon as (written): ベルが鳴るや否や、生徒たちは教室を飛び出した。",
            "**[dictionary form] + なり** = as soon as; the subject is usually someone other than the speaker: "
            "彼は家に帰るなり、寝てしまった。",
            "The second half is something that happened, often surprising; it isn't a request or a plan.",
            "Compare **次第** (N2): 次第 is for future plans, while や否や and なり describe past events.",
        ],
        "examples": [
            {"jp": "ベルが鳴るや否や、生徒たちは教室を飛び出した。", "kana": "ベルがなるやいなや せいとたちはきょうしつをとびだした", "romaji": "beru ga naru ya ina ya, seitotachi wa kyoushitsu o tobidashita", "en": "The moment the bell rang, the students rushed out of the classroom."},
            {"jp": "彼は家に帰るなり、寝てしまった。", "kana": "かれはいえにかえるなり ねてしまった", "romaji": "kare wa ie ni kaeru nari, nete shimatta", "en": "He fell asleep as soon as he got home."},
            {"jp": "店が開くや否や、客が一斉に入ってきた。", "kana": "みせがあくやいなや きゃくがいっせいにはいってきた", "romaji": "mise ga aku ya ina ya, kyaku ga issei ni haitte kita", "en": "As soon as the shop opened, the customers all rushed in."},
            {"jp": "母は私の顔を見るなり、泣き出した。", "kana": "はははわたしのかおをみるなり なきだした", "romaji": "haha wa watashi no kao o miru nari, nakidashita", "en": "My mother burst into tears the moment she saw my face."},
        ],
        "vocab": [
            {"word": "飛び出す", "reading": "とびだす", "meaning": "to rush out"},
            {"word": "一斉に", "reading": "いっせいに", "meaning": "all at once"},
            {"word": "泣き出す", "reading": "なきだす", "meaning": "to burst into tears"},
            {"word": "生徒", "reading": "せいと", "meaning": "pupil, student"},
        ],
    },
    {
        "id": "n1-06",
        "title": "In order to",
        "jp_title": "〜べく",
        "goal": "State a purpose formally, as in writing and speeches.",
        "points": [
            "**[dictionary form] + べく** = in order to (formal, written): 夢をかなえるべく、毎日努力している。",
            "する becomes **すべく** (or するべく): 問題を解決すべく、話し合いが行われた。",
            "It's like ために, but more formal; there's usually a clear goal behind it.",
            "Don't confuse it with **べきだ** (N2, should): べく is about purpose.",
        ],
        "examples": [
            {"jp": "夢をかなえるべく、毎日努力している。", "kana": "ゆめをかなえるべく まいにちどりょくしている", "romaji": "yume o kanaeru beku, mainichi doryoku shite iru", "en": "I'm working hard every day to make my dream come true."},
            {"jp": "問題を解決すべく、話し合いが行われた。", "kana": "もんだいをかいけつすべく はなしあいがおこなわれた", "romaji": "mondai o kaiketsu subeku, hanashiai ga okonawareta", "en": "Talks were held to solve the problem."},
            {"jp": "試験に合格すべく、彼女は一年間必死に勉強した。", "kana": "しけんにごうかくすべく かのじょはいちねんかんひっしにべんきょうした", "romaji": "shiken ni goukaku subeku, kanojo wa ichinenkan hisshi ni benkyou shita", "en": "To pass the exam, she studied desperately for a whole year."},
            {"jp": "家族に会うべく、彼は十年ぶりに故郷へ帰った。", "kana": "かぞくにあうべく かれはじゅうねんぶりにこきょうへかえった", "romaji": "kazoku ni au beku, kare wa juunen buri ni kokyou e kaetta", "en": "He returned to his hometown for the first time in ten years to see his family."},
        ],
        "vocab": [
            {"word": "かなえる", "reading": "かなえる", "meaning": "to make (a dream) come true"},
            {"word": "解決", "reading": "かいけつ", "meaning": "solution, solving"},
            {"word": "話し合い", "reading": "はなしあい", "meaning": "discussion, talks"},
            {"word": "必死", "reading": "ひっし", "meaning": "desperate, frantic"},
            {"word": "故郷", "reading": "こきょう", "meaning": "hometown"},
        ],
    },
    {
        "id": "n1-07",
        "title": "Has a tendency to",
        "jp_title": "〜きらいがある",
        "goal": "Point out an undesirable habit or tendency.",
        "points": [
            "**[dictionary form / noun の] + きらいがある** = has a (bad) tendency to: 彼は、物事を悪い方に考えるきらいがある。",
            "It's for undesirable habits or tendencies of people or groups, and it's formal.",
            "Compare **〜がちだ** and **〜傾向がある**: きらいがある sounds more critical.",
            "It's usually written in hiragana, although it comes from 嫌い.",
        ],
        "examples": [
            {"jp": "彼は、物事を悪い方に考えるきらいがある。", "kana": "かれは ものごとをわるいほうにかんがえるきらいがある", "romaji": "kare wa, monogoto o warui hou ni kangaeru kirai ga aru", "en": "He has a tendency to look on the dark side of things."},
            {"jp": "最近の若者は、すぐに答えを求めるきらいがある。", "kana": "さいきんのわかものは すぐにこたえをもとめるきらいがある", "romaji": "saikin no wakamono wa, sugu ni kotae o motomeru kirai ga aru", "en": "Young people these days tend to want answers right away."},
            {"jp": "私は、何でも一人で抱え込むきらいがある。", "kana": "わたしは なんでもひとりでかかえこむきらいがある", "romaji": "watashi wa, nan demo hitori de kakaekomu kirai ga aru", "en": "I tend to take everything on by myself."},
            {"jp": "この店は、値段の割に量が少ないきらいがある。", "kana": "このみせは ねだんのわりにりょうがすくないきらいがある", "romaji": "kono mise wa, nedan no wari ni ryou ga sukunai kirai ga aru", "en": "This restaurant tends to give small portions for the price."},
        ],
        "vocab": [
            {"word": "物事", "reading": "ものごと", "meaning": "things, matters"},
            {"word": "求める", "reading": "もとめる", "meaning": "to seek, want"},
            {"word": "抱え込む", "reading": "かかえこむ", "meaning": "to take on (alone)"},
            {"word": "若者", "reading": "わかもの", "meaning": "young people"},
            {"word": "傾向", "reading": "けいこう", "meaning": "tendency"},
        ],
    },
    {
        "id": "n1-08",
        "title": "Undaunted by",
        "jp_title": "〜をものともせず",
        "goal": "Praise someone who carries on in spite of a difficulty.",
        "points": [
            "**[noun] + をものともせず(に)** = undaunted by, braving (a difficulty): "
            "彼は足のけがをものともせず、最後まで走り続けた。",
            "It praises someone who overcomes hardship; the noun is a difficulty: 困難, 危険, 激しい雪, 反対.",
            "It's about other people; you don't normally use it to praise yourself.",
            "Compare **にもかかわらず** (N2): をものともせず adds admiration for the person's courage.",
        ],
        "examples": [
            {"jp": "彼は足のけがをものともせず、最後まで走り続けた。", "kana": "かれはあしのけがをものともせず さいごまではしりつづけた", "romaji": "kare wa ashi no kega o mono to mo sezu, saigo made hashiritsuzuketa", "en": "Undaunted by his leg injury, he kept running to the end."},
            {"jp": "彼女は周囲の反対をものともせず、自分の店を開いた。", "kana": "かのじょはしゅういのはんたいをものともせず じぶんのみせをひらいた", "romaji": "kanojo wa shuui no hantai o mono to mo sezu, jibun no mise o hiraita", "en": "Brushing aside everyone's opposition, she opened her own shop."},
            {"jp": "彼らは、激しい雪をものともせず、山頂を目指した。", "kana": "かれらは はげしいゆきをものともせず さんちょうをめざした", "romaji": "karera wa, hageshii yuki o mono to mo sezu, sanchou o mezashita", "en": "Braving the heavy snow, they headed for the summit."},
            {"jp": "その選手は、年齢をものともせず、若い選手に勝った。", "kana": "そのせんしゅは ねんれいをものともせず わかいせんしゅにかった", "romaji": "sono senshu wa, nenrei o mono to mo sezu, wakai senshu ni katta", "en": "That athlete beat the younger players, undaunted by age."},
        ],
        "vocab": [
            {"word": "けが", "reading": "けが", "meaning": "injury"},
            {"word": "周囲", "reading": "しゅうい", "meaning": "the people around, surroundings"},
            {"word": "激しい", "reading": "はげしい", "meaning": "fierce, heavy"},
            {"word": "山頂", "reading": "さんちょう", "meaning": "summit"},
            {"word": "年齢", "reading": "ねんれい", "meaning": "age"},
            {"word": "選手", "reading": "せんしゅ", "meaning": "athlete, player"},
        ],
    },
    {
        "id": "n1-09",
        "title": "Not even one",
        "jp_title": "〜たりとも",
        "goal": "Stress strongly that not even the smallest amount is allowed or happened.",
        "points": [
            "**一 + counter + たりとも + negative** = not even one (strong emphasis): 一秒たりとも気を抜けない。",
            "Common pairs: 一日たりとも, 一円たりとも, 一秒たりとも, 一瞬たりとも, 一人たりとも.",
            "It's formal and dramatic. In everyday speech, 一日も〜ない says the same more plainly.",
            "The verb is always negative: 〜ない, 〜てはいけない, 〜できない.",
        ],
        "examples": [
            {"jp": "彼は三年間、一日たりとも練習を休まなかった。", "kana": "かれはさんねんかん いちにちたりともれんしゅうをやすまなかった", "romaji": "kare wa sannenkan, ichinichi taritomo renshuu o yasumanakatta", "en": "In three years, he didn't miss practice even once."},
            {"jp": "試験中は、一秒たりとも気を抜けない。", "kana": "しけんちゅうは いちびょうたりともきをぬけない", "romaji": "shikenchuu wa, ichibyou taritomo ki o nukenai", "en": "During the exam, you can't relax for even a second."},
            {"jp": "税金は、一円たりとも無駄にしてはいけない。", "kana": "ぜいきんは いちえんたりとも むだにしてはいけない", "romaji": "zeikin wa, ichien taritomo muda ni shite wa ikenai", "en": "Not a single yen of tax money should be wasted."},
            {"jp": "この試合は、一瞬たりとも目が離せない。", "kana": "このしあいは いっしゅんたりともめがはなせない", "romaji": "kono shiai wa, isshun taritomo me ga hanasenai", "en": "You can't take your eyes off this match for even a moment."},
        ],
        "vocab": [
            {"word": "秒", "reading": "びょう", "meaning": "second (of time)"},
            {"word": "気を抜く", "reading": "きをぬく", "meaning": "to let your attention slip"},
            {"word": "税金", "reading": "ぜいきん", "meaning": "tax"},
            {"word": "一瞬", "reading": "いっしゅん", "meaning": "an instant, a moment"},
            {"word": "目が離せない", "reading": "めがはなせない", "meaning": "can't take your eyes off"},
        ],
    },
    {
        "id": "n1-10",
        "title": "Can't help feeling",
        "jp_title": "〜を禁じ得ない",
        "goal": "Express a strong emotion you can't hold back, in formal language.",
        "points": [
            "**[noun] + を禁じ得ない** = can't help feeling (a strong emotion; very formal): その話を聞いて、涙を禁じ得なかった。",
            "Typical nouns: 涙, 怒り, 同情, 驚き, 失望.",
            "It's for the speaker's own feelings, mostly in speeches, the news and writing.",
            "Compare **〜ずにはいられない** (N2): を禁じ得ない takes a noun and is more formal.",
        ],
        "examples": [
            {"jp": "その話を聞いて、涙を禁じ得なかった。", "kana": "そのはなしをきいて なみだをきんじえなかった", "romaji": "sono hanashi o kiite, namida o kinjienakatta", "en": "Hearing that story, I couldn't hold back my tears."},
            {"jp": "突然の事故の知らせに、驚きを禁じ得ない。", "kana": "とつぜんのじこのしらせに おどろきをきんじえない", "romaji": "totsuzen no jiko no shirase ni, odoroki o kinjienai", "en": "I can't help being shocked by the news of the sudden accident."},
            {"jp": "子供たちの苦しい生活に、同情を禁じ得ない。", "kana": "こどもたちのくるしいせいかつに どうじょうをきんじえない", "romaji": "kodomotachi no kurushii seikatsu ni, doujou o kinjienai", "en": "I can't help feeling sympathy for the children's hard lives."},
            {"jp": "約束を何度も破る彼の態度には、怒りを禁じ得ない。", "kana": "やくそくをなんどもやぶるかれのたいどには いかりをきんじえない", "romaji": "yakusoku o nando mo yaburu kare no taido ni wa, ikari o kinjienai", "en": "I can't help feeling angry at the way he keeps breaking promises."},
        ],
        "vocab": [
            {"word": "涙", "reading": "なみだ", "meaning": "tears"},
            {"word": "突然", "reading": "とつぜん", "meaning": "sudden(ly)"},
            {"word": "同情", "reading": "どうじょう", "meaning": "sympathy"},
            {"word": "怒り", "reading": "いかり", "meaning": "anger"},
            {"word": "態度", "reading": "たいど", "meaning": "attitude"},
            {"word": "禁じる", "reading": "きんじる", "meaning": "to forbid"},
        ],
    },
    {
        "id": "n1-11",
        "title": "Whatever, whether",
        "jp_title": "〜であれ・〜であれ〜であれ",
        "goal": "Say that something holds no matter what, who, or which.",
        "points": [
            "**[noun] + であれ** = whatever / whoever it is, even if it's: 理由が何であれ、約束を破るのはよくない。",
            "**AであれBであれ** = whether A or B: 雨であれ雪であれ、試合は予定どおり行われる。",
            "With question words: 誰であれ, どこであれ, 何であれ.",
            "It's like でも, but more formal and written.",
        ],
        "examples": [
            {"jp": "理由が何であれ、約束を破るのはよくない。", "kana": "りゆうがなんであれ やくそくをやぶるのはよくない", "romaji": "riyuu ga nan de are, yakusoku o yaburu no wa yokunai", "en": "Whatever the reason, breaking a promise is wrong."},
            {"jp": "雨であれ雪であれ、試合は予定どおり行われる。", "kana": "あめであれゆきであれ しあいはよていどおりおこなわれる", "romaji": "ame de are yuki de are, shiai wa yotei doori okonawareru", "en": "Rain or snow, the match will go ahead as planned."},
            {"jp": "誰であれ、ここに入るには許可が必要だ。", "kana": "だれであれ ここにはいるにはきょかがひつようだ", "romaji": "dare de are, koko ni hairu ni wa kyoka ga hitsuyou da", "en": "Whoever you are, you need permission to enter here."},
            {"jp": "小さな役割であれ、責任を持ってやるべきだ。", "kana": "ちいさなやくわりであれ せきにんをもってやるべきだ", "romaji": "chiisa na yakuwari de are, sekinin o motte yaru beki da", "en": "Even if it's a small role, you should take it seriously."},
        ],
        "vocab": [
            {"word": "許可", "reading": "きょか", "meaning": "permission"},
            {"word": "責任", "reading": "せきにん", "meaning": "responsibility"},
            {"word": "役割", "reading": "やくわり", "meaning": "role"},
            {"word": "破る", "reading": "やぶる", "meaning": "to break (a promise, rule)"},
        ],
    },
    {
        "id": "n1-12",
        "title": "Since it's (a special occasion)",
        "jp_title": "〜とあって",
        "goal": "Explain a natural result of a special or unusual situation.",
        "points": [
            "**[noun / plain form] + とあって** = because it's (a special situation), naturally ...: "
            "連休とあって、観光地はどこも人でいっぱいだった。",
            "The first part is special or unusual; the second describes what naturally happened, not a wish or a request.",
            "Common: 連休とあって, 人気の店とあって, 初めての海外旅行とあって, 年に一度のお祭りとあって.",
            "It's common in news reports.",
        ],
        "examples": [
            {"jp": "連休とあって、観光地はどこも人でいっぱいだった。", "kana": "れんきゅうとあって かんこうちはどこもひとでいっぱいだった", "romaji": "renkyuu to atte, kankouchi wa doko mo hito de ippai datta", "en": "With it being a long weekend, every tourist spot was packed."},
            {"jp": "人気の店とあって、開店前から長い行列ができていた。", "kana": "にんきのみせとあって かいてんまえからながいぎょうれつができていた", "romaji": "ninki no mise to atte, kaiten mae kara nagai gyouretsu ga dekite ita", "en": "It being a popular shop, a long queue had formed before it opened."},
            {"jp": "初めての海外旅行とあって、娘はとても興奮している。", "kana": "はじめてのかいがいりょこうとあって むすめはとてもこうふんしている", "romaji": "hajimete no kaigai ryokou to atte, musume wa totemo koufun shite iru", "en": "As it's her first trip abroad, my daughter is very excited."},
            {"jp": "年に一度のお祭りとあって、通りは大勢の人でにぎわっていた。", "kana": "ねんにいちどのおまつりとあって とおりはおおぜいのひとでにぎわっていた", "romaji": "nen ni ichido no omatsuri to atte, toori wa oozei no hito de nigiwatte ita", "en": "With it being the once-a-year festival, the streets were bustling with people."},
        ],
        "vocab": [
            {"word": "連休", "reading": "れんきゅう", "meaning": "consecutive holidays, long weekend"},
            {"word": "観光地", "reading": "かんこうち", "meaning": "tourist spot"},
            {"word": "行列", "reading": "ぎょうれつ", "meaning": "queue, line"},
            {"word": "興奮", "reading": "こうふん", "meaning": "excitement"},
            {"word": "にぎわう", "reading": "にぎわう", "meaning": "to be lively, bustling"},
        ],
    },
    {
        "id": "n1-13",
        "title": "Can't fail to, can't get away without",
        "jp_title": "〜ずにはおかない・〜ずにはすまない",
        "goal": "Say that something is bound to have an effect, and that you can't avoid a duty.",
        "points": [
            "**[ない-stem] + ずにはおかない** = can't fail to, is bound to (cause a feeling or effect): "
            "この映画は、見る人を感動させずにはおかない。",
            "**[ない-stem] + ずにはすまない** = can't get away without (doing), must (because of social obligation): "
            "人の物を壊したのだから、謝らずにはすまない。",
            "する becomes **せずには**: 弁償せずにはすまない.",
            "Both are formal. おかない is about a strong effect, すまない about what you owe others.",
        ],
        "examples": [
            {"jp": "この映画は、見る人を感動させずにはおかない。", "kana": "このえいがは みるひとをかんどうさせずにはおかない", "romaji": "kono eiga wa, miru hito o kandou sasezu ni wa okanai", "en": "This film can't fail to move those who see it."},
            {"jp": "彼の言葉は、聞く人の心を動かさずにはおかない。", "kana": "かれのことばは きくひとのこころをうごかさずにはおかない", "romaji": "kare no kotoba wa, kiku hito no kokoro o ugokasazu ni wa okanai", "en": "His words never fail to move people's hearts."},
            {"jp": "人の物を壊したのだから、謝らずにはすまない。", "kana": "ひとのものをこわしたのだから あやまらずにはすまない", "romaji": "hito no mono o kowashita no da kara, ayamarazu ni wa sumanai", "en": "You broke someone else's thing, so you can't get away without apologising."},
            {"jp": "借りた本をなくしたので、弁償せずにはすまないだろう。", "kana": "かりたほんをなくしたので べんしょうせずにはすまないだろう", "romaji": "karita hon o nakushita node, benshou sezu ni wa sumanai darou", "en": "I lost the book I borrowed, so I'll probably have to pay for it."},
        ],
        "vocab": [
            {"word": "感動", "reading": "かんどう", "meaning": "being moved, deep emotion"},
            {"word": "動かす", "reading": "うごかす", "meaning": "to move"},
            {"word": "謝る", "reading": "あやまる", "meaning": "to apologise"},
            {"word": "弁償", "reading": "べんしょう", "meaning": "paying compensation"},
        ],
    },
    {
        "id": "n1-14",
        "title": "Unbecoming of, should never",
        "jp_title": "〜まじき",
        "goal": "Criticise behaviour that someone in a certain position must never show.",
        "points": [
            "**[dictionary form] + まじき + noun** = (an act) unbecoming of, that should never be done: 教師にあるまじき行為.",
            "The typical pattern is **[person] + として / にあるまじき + [noun]**: 医者としてあるまじきこと.",
            "Other verbs work too: 許すまじき行為 = an unforgivable act.",
            "It's very formal and strongly critical, and appears in news reports and editorials.",
        ],
        "examples": [
            {"jp": "生徒をたたくなど、教師にあるまじき行為だ。", "kana": "せいとをたたくなど きょうしにあるまじきこういだ", "romaji": "seito o tataku nado, kyoushi ni aru majiki koui da", "en": "Hitting a student is behaviour unworthy of a teacher."},
            {"jp": "患者の秘密を話すのは、医者としてあるまじきことだ。", "kana": "かんじゃのひみつをはなすのは いしゃとしてあるまじきことだ", "romaji": "kanja no himitsu o hanasu no wa, isha to shite aru majiki koto da", "en": "Revealing a patient's secrets is something a doctor must never do."},
            {"jp": "弱い人をいじめるなんて、許すまじき行為だ。", "kana": "よわいひとをいじめるなんて ゆるすまじきこういだ", "romaji": "yowai hito o ijimeru nante, yurusu majiki koui da", "en": "Bullying the weak is an unforgivable act."},
            {"jp": "試合中に審判を批判するのは、選手としてあるまじき態度だ。", "kana": "しあいちゅうにしんぱんをひはんするのは せんしゅとしてあるまじきたいどだ", "romaji": "shiaichuu ni shinpan o hihan suru no wa, senshu to shite aru majiki taido da", "en": "Criticising the referee during a match is an attitude unbecoming of an athlete."},
        ],
        "vocab": [
            {"word": "教師", "reading": "きょうし", "meaning": "teacher"},
            {"word": "行為", "reading": "こうい", "meaning": "act, behaviour"},
            {"word": "患者", "reading": "かんじゃ", "meaning": "patient"},
            {"word": "審判", "reading": "しんぱん", "meaning": "referee, umpire"},
            {"word": "批判", "reading": "ひはん", "meaning": "criticism"},
        ],
    },
    {
        "id": "n1-15",
        "title": "By means of, as of",
        "jp_title": "〜をもって",
        "goal": "Use the formal をもって for the means of doing something and for a cut-off point.",
        "points": [
            "**[noun] + をもって** = by means of, with (formal): 結果は、後日書面をもってお知らせします。",
            "It also marks a point in time, \"as of\": 本日をもって、受付を終了いたします。",
            "In speeches and announcements: **これをもちまして** = with this (we end ...).",
            "**身をもって** = from personal experience: 失敗の大切さを、身をもって知った。",
        ],
        "examples": [
            {"jp": "結果は、後日書面をもってお知らせします。", "kana": "けっかは ごじつしょめんをもっておしらせします", "romaji": "kekka wa, gojitsu shomen o motte oshirase shimasu", "en": "We will inform you of the results in writing at a later date."},
            {"jp": "本日をもって、申し込みの受付を終了いたします。", "kana": "ほんじつをもって もうしこみのうけつけをしゅうりょういたします", "romaji": "honjitsu o motte, moushikomi no uketsuke o shuuryou itashimasu", "en": "Applications close as of today."},
            {"jp": "これをもちまして、本日の会を終わります。", "kana": "これをもちまして ほんじつのかいをおわります", "romaji": "kore o mochimashite, honjitsu no kai o owarimasu", "en": "With this, we conclude today's meeting."},
            {"jp": "失敗の大切さを、身をもって知った。", "kana": "しっぱいのたいせつさを みをもってしった", "romaji": "shippai no taisetsusa o, mi o motte shitta", "en": "I learned the value of failure first-hand."},
        ],
        "vocab": [
            {"word": "書面", "reading": "しょめん", "meaning": "writing, written document"},
            {"word": "後日", "reading": "ごじつ", "meaning": "at a later date"},
            {"word": "終了", "reading": "しゅうりょう", "meaning": "end, closing"},
            {"word": "身", "reading": "み", "meaning": "body, oneself"},
            {"word": "本日", "reading": "ほんじつ", "meaning": "today (formal)"},
        ],
    },
    {
        "id": "n1-16",
        "title": "Although, while",
        "jp_title": "〜ながらも",
        "goal": "Join two facts that seem to contradict each other, calmly and formally.",
        "points": [
            "**[ます-stem / adjective / noun] + ながらも** = although, while: 狭いながらも、ここは楽しい我が家だ。",
            "It attaches to verb stems (知りながらも), い-adjectives (狭いながらも), and nouns (子供ながらも).",
            "It's more formal and less emotional than のに or けど.",
            "Compare **〜つつも** (N2): very similar, but ながらも also attaches to adjectives and nouns.",
        ],
        "examples": [
            {"jp": "狭いながらも、ここは楽しい我が家だ。", "kana": "せまいながらも ここはたのしいわがやだ", "romaji": "semai nagara mo, koko wa tanoshii wagaya da", "en": "Small as it is, this is our happy home."},
            {"jp": "彼は、悪いと知りながらも、うそをついてしまった。", "kana": "かれは わるいとしりながらも うそをついてしまった", "romaji": "kare wa, warui to shiri nagara mo, uso o tsuite shimatta", "en": "Even though he knew it was wrong, he told a lie."},
            {"jp": "子供ながらも、その考えはしっかりしている。", "kana": "こどもながらも そのかんがえはしっかりしている", "romaji": "kodomo nagara mo, sono kangae wa shikkari shite iru", "en": "Though only a child, their ideas are well thought out."},
            {"jp": "少しずつながらも、日本語が上達している。", "kana": "すこしずつながらも にほんごがじょうたつしている", "romaji": "sukoshi zutsu nagara mo, nihongo ga joutatsu shite iru", "en": "Slowly though it may be, my Japanese is improving."},
        ],
        "vocab": [
            {"word": "我が家", "reading": "わがや", "meaning": "our home, my home"},
            {"word": "うそをつく", "reading": "うそをつく", "meaning": "to tell a lie"},
            {"word": "上達", "reading": "じょうたつ", "meaning": "improvement (in a skill)"},
            {"word": "しっかり", "reading": "しっかり", "meaning": "solid, well thought out"},
        ],
    },
    {
        "id": "n1-17",
        "title": "While (also doing)",
        "jp_title": "〜がてら・〜かたがた",
        "goal": "Say you did something extra while doing something else.",
        "points": [
            "**[noun / ます-stem] + がてら** = while (doing A, also doing B): 散歩がてら、パンを買ってきた。",
            "The second half is something done on the way or at the same time: 買い物がてら, 駅まで送りがてら.",
            "**かたがた** is similar but very formal, often in letters or polite visits: お礼かたがた、ご挨拶に伺いました。",
            "Compare **〜ついでに** (N3): very close in meaning; がてら sounds more literary.",
        ],
        "examples": [
            {"jp": "散歩がてら、パンを買ってきた。", "kana": "さんぽがてら パンをかってきた", "romaji": "sanpo gatera, pan o katte kita", "en": "I went for a walk and bought some bread on the way."},
            {"jp": "買い物がてら、新しくできたカフェに寄ってみた。", "kana": "かいものがてら あたらしくできたカフェによってみた", "romaji": "kaimono gatera, atarashiku dekita kafe ni yotte mita", "en": "While out shopping, I dropped in at the new café."},
            {"jp": "友達を駅まで送りがてら、本屋に寄った。", "kana": "ともだちをえきまでおくりがてら ほんやによった", "romaji": "tomodachi o eki made okuri gatera, honya ni yotta", "en": "While walking my friend to the station, I stopped at a bookshop."},
            {"jp": "先日のお礼かたがた、ご挨拶に伺いました。", "kana": "せんじつのおれいかたがた ごあいさつにうかがいました", "romaji": "senjitsu no orei katagata, go aisatsu ni ukagaimashita", "en": "I've come to pay my respects and to thank you for the other day."},
        ],
        "vocab": [
            {"word": "散歩", "reading": "さんぽ", "meaning": "walk, stroll"},
            {"word": "寄る", "reading": "よる", "meaning": "to drop in"},
            {"word": "挨拶", "reading": "あいさつ", "meaning": "greeting"},
            {"word": "伺う", "reading": "うかがう", "meaning": "to visit (humble)"},
            {"word": "お礼", "reading": "おれい", "meaning": "thanks"},
        ],
    },
    {
        "id": "n1-18",
        "title": "Nothing but, all in",
        "jp_title": "〜ずくめ",
        "goal": "Say that everything around is the same kind of thing.",
        "points": [
            "**[noun] + ずくめ** = nothing but, full of: 今年は、いいことずくめの一年だった。",
            "It goes with a limited set of nouns: いいことずくめ, 黒ずくめ, ごちそうずくめ, 規則ずくめ.",
            "**黒ずくめ** = dressed all in black: 黒ずくめの男.",
            "Compare **〜だらけ** (covered in bad things like ごみ, 傷) and **〜ばかり**: ずくめ is about everything being X.",
        ],
        "examples": [
            {"jp": "今年は、合格に結婚にと、いいことずくめの一年だった。", "kana": "ことしは ごうかくにけっこんにと いいことずくめのいちねんだった", "romaji": "kotoshi wa, goukaku ni kekkon ni to, ii koto zukume no ichinen datta", "en": "This year was full of good things, from passing an exam to getting married."},
            {"jp": "黒ずくめの男が、店の前に立っていた。", "kana": "くろずくめのおとこが みせのまえにたっていた", "romaji": "kurozukume no otoko ga, mise no mae ni tatte ita", "en": "A man dressed all in black was standing in front of the shop."},
            {"jp": "この学校は、規則ずくめで息が詰まる。", "kana": "このがっこうは きそくずくめでいきがつまる", "romaji": "kono gakkou wa, kisoku zukume de iki ga tsumaru", "en": "This school is so full of rules it's suffocating."},
            {"jp": "お正月は、ごちそうずくめで少し太ってしまった。", "kana": "おしょうがつは ごちそうずくめですこしふとってしまった", "romaji": "oshougatsu wa, gochisou zukume de sukoshi futotte shimatta", "en": "With nothing but feasting over New Year, I put on a little weight."},
        ],
        "vocab": [
            {"word": "規則", "reading": "きそく", "meaning": "rule"},
            {"word": "息が詰まる", "reading": "いきがつまる", "meaning": "to feel suffocated"},
            {"word": "ごちそう", "reading": "ごちそう", "meaning": "feast, treat"},
            {"word": "お正月", "reading": "おしょうがつ", "meaning": "New Year"},
            {"word": "太る", "reading": "ふとる", "meaning": "to put on weight"},
        ],
    },
    {
        "id": "n1-19",
        "title": "Even down to, as for",
        "jp_title": "〜に至るまで・〜に至っては",
        "goal": "Cover everything up to the extreme, single out the most extreme case, and state an end result.",
        "points": [
            "**[noun] + に至るまで** = (even) down to, all the way to: 子供からお年寄りに至るまで、みんなこの歌を知っている。",
            "**[noun] + に至っては** = as for (the most extreme example): 兄も姉も料理が苦手だが、父に至っては、お湯も沸かせない。",
            "**[noun / dictionary form] + に至った** = finally came to (a result): 長い話し合いの結果、計画は中止に至った。",
            "All are formal; 至る means \"to reach\".",
        ],
        "examples": [
            {"jp": "子供からお年寄りに至るまで、みんなこの歌を知っている。", "kana": "こどもからおとしよりにいたるまで みんなこのうたをしっている", "romaji": "kodomo kara otoshiyori ni itaru made, minna kono uta o shitte iru", "en": "Everyone, from children to the elderly, knows this song."},
            {"jp": "この店は、食器から家具に至るまで、すべて手作りだ。", "kana": "このみせは しょっきからかぐにいたるまで すべててづくりだ", "romaji": "kono mise wa, shokki kara kagu ni itaru made, subete tezukuri da", "en": "Everything in this shop, from the tableware to the furniture, is handmade."},
            {"jp": "兄も姉も料理が苦手だが、父に至っては、お湯も沸かせない。", "kana": "あにもあねもりょうりがにがてだが ちちにいたっては おゆもわかせない", "romaji": "ani mo ane mo ryouri ga nigate da ga, chichi ni itatte wa, oyu mo wakasenai", "en": "My brother and sister are bad at cooking, and as for my father, he can't even boil water."},
            {"jp": "長い話し合いの結果、計画は中止に至った。", "kana": "ながいはなしあいのけっか けいかくはちゅうしにいたった", "romaji": "nagai hanashiai no kekka, keikaku wa chuushi ni itatta", "en": "After long discussions, the plan was finally cancelled."},
        ],
        "vocab": [
            {"word": "至る", "reading": "いたる", "meaning": "to reach, lead to"},
            {"word": "家具", "reading": "かぐ", "meaning": "furniture"},
            {"word": "お湯", "reading": "おゆ", "meaning": "hot water"},
            {"word": "沸かす", "reading": "わかす", "meaning": "to boil"},
        ],
    },
    {
        "id": "n1-20",
        "title": "No need to, needless to say",
        "jp_title": "〜までもない",
        "goal": "Say that something is too obvious or simple to bother doing.",
        "points": [
            "**[dictionary form] + までもない** = there's no need to (it's obvious or too simple): そんな簡単なことは、説明するまでもない。",
            "**言うまでもなく** = needless to say: 言うまでもなく、健康は何より大切だ。",
            "**〜までもなく** can start a clause: 調べるまでもなく、答えは明らかだ。",
            "Compare **〜ことはない** (N2, no need to): までもない adds that it's too obvious to bother with.",
        ],
        "examples": [
            {"jp": "そんな簡単なことは、説明するまでもない。", "kana": "そんなかんたんなことは せつめいするまでもない", "romaji": "sonna kantan na koto wa, setsumei suru made mo nai", "en": "Something that simple doesn't need explaining."},
            {"jp": "言うまでもなく、健康は何より大切だ。", "kana": "いうまでもなく けんこうはなによりたいせつだ", "romaji": "iu made mo naku, kenkou wa nani yori taisetsu da", "en": "Needless to say, health matters more than anything."},
            {"jp": "調べるまでもなく、答えは明らかだ。", "kana": "しらべるまでもなく こたえはあきらかだ", "romaji": "shiraberu made mo naku, kotae wa akiraka da", "en": "The answer is obvious without even checking."},
            {"jp": "これくらいの距離なら、タクシーに乗るまでもない。", "kana": "これくらいのきょりなら タクシーにのるまでもない", "romaji": "kore kurai no kyori nara, takushii ni noru made mo nai", "en": "For a distance like this, there's no need to take a taxi."},
        ],
        "vocab": [
            {"word": "明らか", "reading": "あきらか", "meaning": "clear, obvious"},
            {"word": "距離", "reading": "きょり", "meaning": "distance"},
            {"word": "何より", "reading": "なにより", "meaning": "more than anything"},
            {"word": "説明", "reading": "せつめい", "meaning": "explanation"},
        ],
    },
    {
        "id": "n1-21",
        "title": "Combined with",
        "jp_title": "〜と相まって",
        "goal": "Say that two factors worked together to produce a result.",
        "points": [
            "**[noun] + と相まって** = combined with (two factors working together): "
            "美しい景色と相まって、その音楽は心に深く響いた。",
            "Two patterns: **AとBが相まって** or **Aと相まって、B**.",
            "It describes a combined effect, good or bad: 円安と物価の上昇が相まって、生活は苦しくなる一方だ。",
            "It's formal and common in reports, reviews and the news.",
        ],
        "examples": [
            {"jp": "美しい景色と相まって、その音楽は心に深く響いた。", "kana": "うつくしいけしきとあいまって そのおんがくはこころにふかくひびいた", "romaji": "utsukushii keshiki to aimatte, sono ongaku wa kokoro ni fukaku hibiita", "en": "Together with the beautiful scenery, the music moved me deeply."},
            {"jp": "好天と連休が相まって、観光地は大変な人出だった。", "kana": "こうてんとれんきゅうがあいまって かんこうちはたいへんなひとでだった", "romaji": "kouten to renkyuu ga aimatte, kankouchi wa taihen na hitode datta", "en": "With fine weather and a long weekend combined, the tourist spots were packed."},
            {"jp": "彼女の努力と才能が相まって、大きな成功を収めた。", "kana": "かのじょのどりょくとさいのうがあいまって おおきなせいこうをおさめた", "romaji": "kanojo no doryoku to sainou ga aimatte, ookina seikou o osameta", "en": "Her effort and talent together brought her great success."},
            {"jp": "円安と物価の上昇が相まって、生活は苦しくなる一方だ。", "kana": "えんやすとぶっかのじょうしょうがあいまって せいかつはくるしくなるいっぽうだ", "romaji": "enyasu to bukka no joushou ga aimatte, seikatsu wa kurushiku naru ippou da", "en": "The weak yen and rising prices together keep making life harder."},
        ],
        "vocab": [
            {"word": "相まって", "reading": "あいまって", "meaning": "combined with, together with"},
            {"word": "響く", "reading": "ひびく", "meaning": "to resonate, echo"},
            {"word": "人出", "reading": "ひとで", "meaning": "turnout, crowds"},
            {"word": "才能", "reading": "さいのう", "meaning": "talent"},
            {"word": "収める", "reading": "おさめる", "meaning": "to achieve (success)"},
            {"word": "上昇", "reading": "じょうしょう", "meaning": "rise"},
        ],
    },
    {
        "id": "n1-22",
        "title": "If only, and yet",
        "jp_title": "〜ものを",
        "goal": "Express regret or reproach that something easy didn't happen.",
        "points": [
            "**[plain form] + ものを** = if only, and yet (regret or reproach): 言ってくれれば手伝ったものを。",
            "It usually follows a condition: 〜ば…ものを, 〜たら…ものを. The speaker feels sorry or annoyed.",
            "At the end of a sentence it works like のに (N4), but sounds more literary.",
            "It often criticises someone else: 早く医者に行けば治ったものを、彼は我慢してしまった。",
        ],
        "examples": [
            {"jp": "言ってくれれば手伝ったものを。", "kana": "いってくれればてつだったものを", "romaji": "itte kurereba tetsudatta mono o", "en": "If only you'd told me, I'd have helped."},
            {"jp": "早く医者に行けば治ったものを、彼は我慢してしまった。", "kana": "はやくいしゃにいけばなおったものを かれはがまんしてしまった", "romaji": "hayaku isha ni ikeba naotta mono o, kare wa gaman shite shimatta", "en": "If he'd gone to the doctor early it would have healed, but he just put up with it."},
            {"jp": "一言謝ればすむものを、彼女は意地を張っている。", "kana": "ひとことあやまればすむものを かのじょはいじをはっている", "romaji": "hitokoto ayamareba sumu mono o, kanojo wa iji o hatte iru", "en": "One word of apology would settle it, and yet she's being stubborn."},
            {"jp": "もう少し待っていれば会えたものを、先に帰ってしまった。", "kana": "もうすこしまっていればあえたものを さきにかえってしまった", "romaji": "mou sukoshi matte ireba aeta mono o, saki ni kaette shimatta", "en": "If I'd waited a little longer I could have seen them, but I went home first."},
        ],
        "vocab": [
            {"word": "我慢", "reading": "がまん", "meaning": "putting up with, enduring"},
            {"word": "一言", "reading": "ひとこと", "meaning": "a single word"},
            {"word": "意地を張る", "reading": "いじをはる", "meaning": "to be stubborn"},
            {"word": "すむ", "reading": "すむ", "meaning": "to be settled, be enough"},
        ],
    },
    {
        "id": "n1-23",
        "title": "In order to (determined)",
        "jp_title": "〜んがため",
        "goal": "Recognise a very literary way of stating a determined purpose.",
        "points": [
            "**[ない-form stem] + んがため(に)** = in order to (strong determination; very literary): "
            "夢を実現せんがため、彼は全てを捨てて海外へ渡った。",
            "Form: 勝た + んがため, 生き + んがため; する becomes **せんがため**.",
            "It's much stiffer than ために or べく; you'll meet it in novels, speeches and older writing.",
            "Before a noun: **んがための**: 夢を実現せんがための努力.",
        ],
        "examples": [
            {"jp": "夢を実現せんがため、彼は全てを捨てて海外へ渡った。", "kana": "ゆめをじつげんせんがため かれはすべてをすててかいがいへわたった", "romaji": "yume o jitsugen sen ga tame, kare wa subete o sutete kaigai e watatta", "en": "To realise his dream, he gave up everything and went abroad."},
            {"jp": "試合に勝たんがため、選手たちは厳しい練習に耐えた。", "kana": "しあいにかたんがため せんしゅたちはきびしいれんしゅうにたえた", "romaji": "shiai ni katan ga tame, senshutachi wa kibishii renshuu ni taeta", "en": "Determined to win the match, the players endured hard training."},
            {"jp": "生きんがために、人々は必死に働いた。", "kana": "いきんがために ひとびとはひっしにはたらいた", "romaji": "ikin ga tame ni, hitobito wa hisshi ni hataraita", "en": "To survive, people worked desperately."},
            {"jp": "真実を明らかにせんがため、記者は取材を続けた。", "kana": "しんじつをあきらかにせんがため きしゃはしゅざいをつづけた", "romaji": "shinjitsu o akiraka ni sen ga tame, kisha wa shuzai o tsuzuketa", "en": "Determined to bring the truth to light, the reporter kept investigating."},
        ],
        "vocab": [
            {"word": "実現", "reading": "じつげん", "meaning": "realisation, making real"},
            {"word": "渡る", "reading": "わたる", "meaning": "to cross over, go over"},
            {"word": "耐える", "reading": "たえる", "meaning": "to endure"},
            {"word": "真実", "reading": "しんじつ", "meaning": "truth"},
            {"word": "取材", "reading": "しゅざい", "meaning": "news gathering, investigation"},
        ],
    },
    {
        "id": "n1-24",
        "title": "Never stop wishing",
        "jp_title": "〜てやまない",
        "goal": "Express a strong, lasting wish or feeling, as in speeches and letters.",
        "points": [
            "**[て-form] + やまない** = never stop (wishing, hoping, loving): 皆様のご健康とご活躍を願ってやみません。",
            "It goes with feeling verbs: 願う, 祈る, 期待する, 尊敬する, 愛する.",
            "It's for the speaker's own strong, lasting feelings; it's formal and common in speeches and letters.",
            "The polite form is **〜てやみません**.",
        ],
        "examples": [
            {"jp": "皆様のご健康とご活躍を願ってやみません。", "kana": "みなさまのごけんこうとごかつやくをねがってやみません", "romaji": "minasama no go kenkou to go katsuyaku o negatte yamimasen", "en": "I sincerely wish you all good health and every success."},
            {"jp": "私は、恩師を今も尊敬してやまない。", "kana": "わたしは おんしをいまもそんけいしてやまない", "romaji": "watashi wa, onshi o ima mo sonkei shite yamanai", "en": "I still deeply respect my former teacher."},
            {"jp": "彼の成功を、心から期待してやまない。", "kana": "かれのせいこうを こころからきたいしてやまない", "romaji": "kare no seikou o, kokoro kara kitai shite yamanai", "en": "I truly hope for his success."},
            {"jp": "子供たちの未来が明るいものであることを祈ってやまない。", "kana": "こどもたちのみらいがあかるいものであることをいのってやまない", "romaji": "kodomotachi no mirai ga akarui mono de aru koto o inotte yamanai", "en": "I pray with all my heart that the children's future will be bright."},
        ],
        "vocab": [
            {"word": "活躍", "reading": "かつやく", "meaning": "being active, success"},
            {"word": "恩師", "reading": "おんし", "meaning": "one's former teacher"},
            {"word": "尊敬", "reading": "そんけい", "meaning": "respect"},
            {"word": "祈る", "reading": "いのる", "meaning": "to pray, wish"},
            {"word": "未来", "reading": "みらい", "meaning": "future"},
        ],
    },
    {
        "id": "n1-25",
        "title": "No one but",
        "jp_title": "〜をおいて",
        "goal": "Say that one person, place or time is the only possible choice.",
        "points": [
            "**[noun] + をおいて(ほかに)〜ない** = no one / nothing but X: "
            "チームのキャプテンにふさわしいのは、彼をおいてほかにいない。",
            "It praises X as the only real choice; the sentence ends with ない or いない.",
            "Common: 彼をおいて, 京都をおいて, 今をおいて.",
            "**今をおいてほかにない** = now is the only chance, there's no better time.",
        ],
        "examples": [
            {"jp": "チームのキャプテンにふさわしいのは、彼をおいてほかにいない。", "kana": "チームのキャプテンにふさわしいのは かれをおいてほかにいない", "romaji": "chiimu no kyaputen ni fusawashii no wa, kare o oite hoka ni inai", "en": "There's no one but him who's fit to be team captain."},
            {"jp": "日本の秋を楽しむなら、京都をおいてほかにない。", "kana": "にほんのあきをたのしむなら きょうとをおいてほかにない", "romaji": "nihon no aki o tanoshimu nara, kyouto o oite hoka ni nai", "en": "If you want to enjoy autumn in Japan, there's nowhere like Kyoto."},
            {"jp": "留学するなら、今をおいてほかにチャンスはない。", "kana": "りゅうがくするなら いまをおいてほかにチャンスはない", "romaji": "ryuugaku suru nara, ima o oite hoka ni chansu wa nai", "en": "If you're going to study abroad, there's no better chance than now."},
            {"jp": "この問題を解決できるのは、あの先生をおいてほかにいないだろう。", "kana": "このもんだいをかいけつできるのは あのせんせいをおいてほかにいないだろう", "romaji": "kono mondai o kaiketsu dekiru no wa, ano sensei o oite hoka ni inai darou", "en": "No one but that teacher could solve this problem."},
        ],
        "vocab": [
            {"word": "ふさわしい", "reading": "ふさわしい", "meaning": "suitable, fit for"},
            {"word": "キャプテン", "reading": "キャプテン", "meaning": "captain"},
            {"word": "チャンス", "reading": "チャンス", "meaning": "chance, opportunity"},
            {"word": "ほかに", "reading": "ほかに", "meaning": "other than, besides"},
        ],
    },
    {
        "id": "n1-26",
        "title": "Using as an excuse",
        "jp_title": "〜にかこつけて",
        "goal": "Say that someone used one thing as a pretext for another.",
        "points": [
            "**[noun] + にかこつけて** = using (something) as an excuse: 弟は、勉強にかこつけて、友達の家に遊びに行った。",
            "The real purpose is different from the stated reason; it's often a little critical or humorous.",
            "Common excuses: 雨, 用事, 勉強, 誕生日祝い, 病気.",
            "**〜を口実に** means almost the same.",
        ],
        "examples": [
            {"jp": "弟は、勉強にかこつけて、友達の家に遊びに行った。", "kana": "おとうとは べんきょうにかこつけて ともだちのいえにあそびにいった", "romaji": "otouto wa, benkyou ni kakotsukete, tomodachi no ie ni asobi ni itta", "en": "Using studying as an excuse, my brother went off to play at his friend's house."},
            {"jp": "雨にかこつけて、ジョギングをさぼってしまった。", "kana": "あめにかこつけて ジョギングをさぼってしまった", "romaji": "ame ni kakotsukete, jogingu o sabotte shimatta", "en": "I used the rain as an excuse to skip my jog."},
            {"jp": "誕生日祝いにかこつけて、みんなでおいしいものを食べに行った。", "kana": "たんじょうびいわいにかこつけて みんなでおいしいものをたべにいった", "romaji": "tanjoubi iwai ni kakotsukete, minna de oishii mono o tabe ni itta", "en": "Using a birthday as an excuse, we all went out for something delicious."},
            {"jp": "用事にかこつけて、集まりを早めに抜け出した。", "kana": "ようじにかこつけて あつまりをはやめにぬけだした", "romaji": "youji ni kakotsukete, atsumari o hayame ni nukedashita", "en": "Using an errand as an excuse, I slipped out of the get-together early."},
        ],
        "vocab": [
            {"word": "さぼる", "reading": "さぼる", "meaning": "to skip (out of laziness)"},
            {"word": "用事", "reading": "ようじ", "meaning": "errand, something to do"},
            {"word": "抜け出す", "reading": "ぬけだす", "meaning": "to slip out"},
            {"word": "口実", "reading": "こうじつ", "meaning": "pretext, excuse"},
            {"word": "祝い", "reading": "いわい", "meaning": "celebration"},
        ],
    },
    {
        "id": "n1-27",
        "title": "Without meaning to",
        "jp_title": "〜ともなく・〜ともなしに",
        "goal": "Describe something done idly, or something from an unclear source.",
        "points": [
            "**[dictionary form] + ともなく / ともなしに** = without meaning to, idly: 見るともなく窓の外を見ていた。",
            "It goes with verbs of perception, and the verb is often repeated: 見るともなく見る, 聞くともなく聞く.",
            "**question word + ともなく** = from no one / nowhere in particular: どこからともなく、いい匂いがしてきた。",
            "It's literary and common in novels.",
        ],
        "examples": [
            {"jp": "見るともなく窓の外を見ていると、雪が降り始めた。", "kana": "みるともなくまどのそとをみていると ゆきがふりはじめた", "romaji": "miru to mo naku mado no soto o mite iru to, yuki ga furihajimeta", "en": "As I was idly gazing out of the window, it started to snow."},
            {"jp": "ラジオを聞くともなく聞いていたら、懐かしい曲が流れてきた。", "kana": "ラジオをきくともなくきいていたら なつかしいきょくがながれてきた", "romaji": "rajio o kiku to mo naku kiite itara, natsukashii kyoku ga nagarete kita", "en": "While I was half-listening to the radio, an old favourite song came on."},
            {"jp": "どこからともなく、いい匂いがしてきた。", "kana": "どこからともなく いいにおいがしてきた", "romaji": "doko kara to mo naku, ii nioi ga shite kita", "en": "A lovely smell drifted in from somewhere."},
            {"jp": "誰からともなく、拍手が起こった。", "kana": "だれからともなく はくしゅがおこった", "romaji": "dare kara to mo naku, hakushu ga okotta", "en": "Applause broke out, started by no one in particular."},
        ],
        "vocab": [
            {"word": "懐かしい", "reading": "なつかしい", "meaning": "nostalgic, dearly remembered"},
            {"word": "匂い", "reading": "におい", "meaning": "smell"},
            {"word": "拍手", "reading": "はくしゅ", "meaning": "applause"},
            {"word": "曲", "reading": "きょく", "meaning": "song, piece of music"},
        ],
    },
    {
        "id": "n1-28",
        "title": "Precisely because (formal)",
        "jp_title": "〜ばこそ",
        "goal": "Stress a positive reason behind something, formally.",
        "points": [
            "**[ば-form] + こそ** = precisely because (stressing a positive, often hidden reason): 子供のことを思えばこそ、厳しく言うのだ。",
            "The sentence often ends with **のだ / のです**.",
            "It's like からこそ (N2), but more formal and literary.",
            "It often explains a good intention behind something that looks harsh.",
        ],
        "examples": [
            {"jp": "子供のことを思えばこそ、厳しく言うのだ。", "kana": "こどものことをおもえばこそ きびしくいうのだ", "romaji": "kodomo no koto o omoeba koso, kibishiku iu no da", "en": "It's precisely because I care about my child that I'm strict."},
            {"jp": "健康であればこそ、好きなことができる。", "kana": "けんこうであればこそ すきなことができる", "romaji": "kenkou de areba koso, suki na koto ga dekiru", "en": "It's only because you're healthy that you can do what you love."},
            {"jp": "あなたを信じていればこそ、本当のことを話したのです。", "kana": "あなたをしんじていればこそ ほんとうのことをはなしたのです", "romaji": "anata o shinjite ireba koso, hontou no koto o hanashita no desu", "en": "It's because I trust you that I told you the truth."},
            {"jp": "毎日練習を続ければこそ、上手になるのだ。", "kana": "まいにちれんしゅうをつづければこそ じょうずになるのだ", "romaji": "mainichi renshuu o tsuzukereba koso, jouzu ni naru no da", "en": "It's precisely by practising every day that you get better."},
        ],
        "vocab": [
            {"word": "思う", "reading": "おもう", "meaning": "to think; to care about"},
            {"word": "信じる", "reading": "しんじる", "meaning": "to believe, trust"},
            {"word": "健康", "reading": "けんこう", "meaning": "health; healthy"},
            {"word": "上手", "reading": "じょうず", "meaning": "skilled, good at"},
        ],
    },
    {
        "id": "n1-29",
        "title": "In contrast to",
        "jp_title": "〜にひきかえ",
        "goal": "Contrast two opposite things, showing how you feel about them.",
        "points": [
            "**[noun] + にひきかえ** = in contrast to, unlike (with the speaker's judgement): "
            "遊んでばかりいる兄にひきかえ、弟はとてもまじめだ。",
            "It's subjective: the speaker sets a good side against a bad side.",
            "Verbs and adjectives take の: 去年の夏が暑かったのにひきかえ、今年は涼しい。",
            "Compare **に対して** (N3): に対して is neutral, にひきかえ adds the speaker's feelings.",
        ],
        "examples": [
            {"jp": "遊んでばかりいる兄にひきかえ、弟はとてもまじめだ。", "kana": "あそんでばかりいるあににひきかえ おとうとはとてもまじめだ", "romaji": "asonde bakari iru ani ni hikikae, otouto wa totemo majime da", "en": "Unlike their older brother, who does nothing but play, the younger one is very serious."},
            {"jp": "去年の夏が暑かったのにひきかえ、今年は涼しい。", "kana": "きょねんのなつがあつかったのにひきかえ ことしはすずしい", "romaji": "kyonen no natsu ga atsukatta no ni hikikae, kotoshi wa suzushii", "en": "In contrast to last summer, which was hot, this year is cool."},
            {"jp": "前の部屋にひきかえ、今度の部屋は日当たりがいい。", "kana": "まえのへやにひきかえ こんどのへやはひあたりがいい", "romaji": "mae no heya ni hikikae, kondo no heya wa hiatari ga ii", "en": "Unlike my old room, the new one gets plenty of sun."},
            {"jp": "にぎやかな姉にひきかえ、妹はおとなしい性格だ。", "kana": "にぎやかなあねにひきかえ いもうとはおとなしいせいかくだ", "romaji": "nigiyaka na ane ni hikikae, imouto wa otonashii seikaku da", "en": "In contrast to her lively older sister, the younger one is quiet."},
        ],
        "vocab": [
            {"word": "まじめ", "reading": "まじめ", "meaning": "serious, diligent"},
            {"word": "涼しい", "reading": "すずしい", "meaning": "cool (weather)"},
            {"word": "おとなしい", "reading": "おとなしい", "meaning": "quiet, gentle"},
            {"word": "性格", "reading": "せいかく", "meaning": "personality"},
        ],
    },
    {
        "id": "n1-30",
        "title": "Starting with",
        "jp_title": "〜を皮切りに",
        "goal": "Name the first event in a series that then spreads.",
        "points": [
            "**[noun] + を皮切りに(して)** = starting with (the first of a series of similar events): "
            "東京での公演を皮切りに、全国ツアーが始まる。",
            "The second half is a series that spreads: 全国で, 次々と, 各地で.",
            "**を皮切りとして** means the same and is a little stiffer.",
            "It's common in news about tours, openings, sales and events.",
        ],
        "examples": [
            {"jp": "東京での公演を皮切りに、全国ツアーが始まる。", "kana": "とうきょうでのこうえんをかわきりに ぜんこくツアーがはじまる", "romaji": "toukyou de no kouen o kawakiri ni, zenkoku tsuaa ga hajimaru", "en": "Starting with a performance in Tokyo, a nationwide tour will begin."},
            {"jp": "最初の店の成功を皮切りに、その会社は次々と店を増やした。", "kana": "さいしょのみせのせいこうをかわきりに そのかいしゃはつぎつぎとみせをふやした", "romaji": "saisho no mise no seikou o kawakiri ni, sono kaisha wa tsugitsugi to mise o fuyashita", "en": "Starting with the success of its first shop, the company opened one shop after another."},
            {"jp": "彼の発言を皮切りに、参加者が次々と意見を述べ始めた。", "kana": "かれのはつげんをかわきりに さんかしゃがつぎつぎといけんをのべはじめた", "romaji": "kare no hatsugen o kawakiri ni, sankasha ga tsugitsugi to iken o nobehajimeta", "en": "Starting with his remark, the participants began voicing their opinions one after another."},
            {"jp": "九州を皮切りに、各地で桜が咲き始めた。", "kana": "きゅうしゅうをかわきりに かくちでさくらがさきはじめた", "romaji": "kyuushuu o kawakiri ni, kakuchi de sakura ga sakihajimeta", "en": "Starting with Kyushu, cherry blossoms began blooming around the country."},
        ],
        "vocab": [
            {"word": "皮切り", "reading": "かわきり", "meaning": "start, beginning"},
            {"word": "公演", "reading": "こうえん", "meaning": "performance"},
            {"word": "全国", "reading": "ぜんこく", "meaning": "nationwide"},
            {"word": "発言", "reading": "はつげん", "meaning": "remark, statement"},
            {"word": "各地", "reading": "かくち", "meaning": "various places, every region"},
        ],
    },
]

_BY_ID = {lesson["id"]: lesson for lesson in LESSONS}
LEVELS = ("N5", "N4", "N3", "N2", "N1")


def get(lesson_id: str) -> dict | None:
    return _BY_ID.get(lesson_id)


def level(lesson: dict) -> str:
    """The JLPT level from the id prefix: n5-03 -> "N5", n2-01 -> "N2"."""
    return lesson["id"].split("-")[0].upper()


def number(lesson: dict) -> int:
    """Position within its own level: n4-01 is N4 lesson 1."""
    same = [les for les in LESSONS if level(les) == level(lesson)]
    return same.index(lesson) + 1


def label(lesson: dict) -> str:
    return f"{level(lesson)} lesson {number(lesson)}"


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
fill in a blank, answer a question in Japanese, or pick the right word (like a JLPT question).
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
            clean = lambda s: "".join(c for c in s if c not in " 、。！？…")  # noqa: E731
            to_hira = lambda s: "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)  # noqa: E731
            if to_hira(clean(reading)) != to_hira(clean(ex["kana"])):
                print(f"{lesson['id']} furigana differs: {ex['jp']} -> {clean(reading)} vs {clean(ex['kana'])}")
                problems += 1
        for v in lesson["vocab"]:
            if checks.kana_to_romaji(v["reading"]) is None:
                print(f"{lesson['id']} vocab reading isn't pure kana: {v['reading']}")
                problems += 1
    print(f"{len(LESSONS)} lessons checked, {problems} problem(s)")
