"""The JLPT lesson path (N5, N4, N3), written by hand so the core content is reliable.

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
]

_BY_ID = {lesson["id"]: lesson for lesson in LESSONS}
LEVELS = ("N5", "N4", "N3")


def get(lesson_id: str) -> dict | None:
    return _BY_ID.get(lesson_id)


def level(lesson: dict) -> str:
    """"N5", "N4" or "N3", from the id prefix (n5-03, n4-01, n3-02)."""
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
