"""The JLPT N5 lesson path, written by hand so the core content is reliable.

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
