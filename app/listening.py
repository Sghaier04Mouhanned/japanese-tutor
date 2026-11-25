"""JLPT-style listening practice (聴解), written by hand so the content is reliable.

Each item is a short dialogue or talk with a narrator, like the real test:
- task    課題理解      what will someone do next? (choices printed)
- point   ポイント理解  why / what exactly? (choices printed)
- summary 概要理解      what is the speaker's main point? (choices only heard)
- quick   即時応答      pick the best reply to one line (replies only heard)
- integrated 統合理解   (N2) compare options someone explains with what two people then say
- utterance 発話表現    (N5, N4) what would you say in this situation? (replies only heard)

The audio is made with VOICEVOX, one voice per role (N narrator, F woman,
M man, S staff member). `python -m app.listening` checks the items; `--readings` prints the
automatic furigana of the transcripts for proofreading.
"""

from __future__ import annotations

# Role -> (VOICEVOX speaker name, style). Missing voices fall back to the default one.
VOICES = {"N": ("九州そら", "ノーマル"), "F": ("春日部つむぎ", "ノーマル"), "M": ("玄野武宏", "ノーマル"),
          "S": ("青山龍星", "ノーマル")}
ROLE_LABELS = {"N": "Narrator", "F": "Woman", "M": "Man", "S": "Staff"}

KINDS = {
    "task": ("Task-based", "課題理解", True),
    "point": ("Key point", "ポイント理解", True),
    "summary": ("Summary", "概要理解", False),
    "quick": ("Quick response", "即時応答", False),
    "integrated": ("Integrated", "統合理解", True),
    "utterance": ("Utterance", "発話表現", False),
}  # kind -> (English, Japanese, choices printed on the page)

ITEMS: list[dict] = [
    # ------------------------------------------------------------------ N5
    {
        "id": "n5-l01",
        "title": "Drawing in the park",
        "kind": "task",
        "intro": "学校で、先生が話しています。学生は、あした何を持っていきますか。",
        "lines": [
            ("F", "みなさん、あしたは、公園で絵をかきます。", "Everyone, tomorrow we're going to draw pictures in the park."),
            ("F", "えんぴつと紙は、学校にありますから、持ってこなくてもいいです。",
             "There are pencils and paper at school, so you don't need to bring them."),
            ("F", "おべんとうを持ってきてください。飲み物は、公園の前の店で買うことができます。",
             "Please bring a packed lunch. You can buy drinks at the shop in front of the park."),
        ],
        "question": "学生は、あした何を持っていきますか。",
        "intro_en": "At school, the teacher is speaking. What will the students take tomorrow?",
        "question_en": "What will the students take tomorrow?",
        "choices": ["えんぴつ", "紙", "おべんとう", "飲み物"],
        "answer": 2,
        "why": "Pencils and paper are at school (持ってこなくてもいい), and drinks can be bought at the park. "
               "Only the lunch: おべんとうを持ってきてください.",
        "vocab": [
            {"word": "公園", "reading": "こうえん", "meaning": "park"},
            {"word": "絵", "reading": "え", "meaning": "picture"},
            {"word": "えんぴつ", "reading": "えんぴつ", "meaning": "pencil"},
            {"word": "おべんとう", "reading": "おべんとう", "meaning": "packed lunch"},
        ],
    },
    {
        "id": "n5-l02",
        "title": "Lunch break",
        "kind": "task",
        "intro": "会社で、男の人と女の人が話しています。男の人は、このあと、まず何をしますか。",
        "lines": [
            ("M", "あ、もう12時ですね。昼ごはんを食べに行きませんか。", "Oh, it's already twelve. Shall we go and get lunch?"),
            ("F", "いいですね。でも、わたしは、このメールを書いてから行きます。", "Good idea. But I'll go after I've written this email."),
            ("M", "じゃあ、ぼくは、先にこの手紙を出してきます。", "Then I'll go and post this letter first."),
            ("F", "はい。じゃあ、10分後に、エレベーターの前で会いましょう。", "OK. Then let's meet in front of the lift in ten minutes."),
        ],
        "question": "男の人は、このあと、まず何をしますか。",
        "intro_en": "At an office, a man and a woman are talking. What will the man do first after this?",
        "question_en": "What will the man do first after this?",
        "choices": ["昼ごはんを食べる", "メールを書く", "手紙を出しに行く", "エレベーターの前で待つ"],
        "answer": 2,
        "why": "The woman writes the email. He says 先にこの手紙を出してきます (I'll post this letter first); "
               "they meet and eat after that.",
        "vocab": [
            {"word": "昼ごはん", "reading": "ひるごはん", "meaning": "lunch"},
            {"word": "先に", "reading": "さきに", "meaning": "first, ahead"},
            {"word": "手紙を出す", "reading": "てがみをだす", "meaning": "to post a letter"},
            {"word": "エレベーター", "reading": "エレベーター", "meaning": "lift, elevator"},
        ],
    },
    {
        "id": "n5-l03",
        "title": "Buying fruit",
        "kind": "task",
        "intro": "店で、女の人と店の人が話しています。女の人は、何を買いますか。",
        "lines": [
            ("F", "すみません、このりんご、一ついくらですか。", "Excuse me, how much is one of these apples?"),
            ("S", "一つ150円です。三つで400円ですよ。", "150 yen each. Three for 400 yen."),
            ("F", "じゃあ、三つください。あ、それから、このみかんも。", "Then three, please. Oh, and these mandarins too."),
            ("S", "みかんは、五つで300円です。", "The mandarins are five for 300 yen."),
            ("F", "うーん、みかんは、やめます。りんごだけください。", "Hmm, I'll leave the mandarins. Just the apples, please."),
        ],
        "question": "女の人は、何を買いますか。",
        "intro_en": "In a shop, a woman and a shop assistant are talking. What will the woman buy?",
        "question_en": "What will the woman buy?",
        "choices": ["りんご一つ", "りんご三つ", "りんご三つとみかん五つ", "みかん五つ"],
        "answer": 1,
        "why": "She asks for three apples (三つください), thinks about mandarins, then drops them: みかんは、やめます。りんごだけください.",
        "vocab": [
            {"word": "いくら", "reading": "いくら", "meaning": "how much"},
            {"word": "みかん", "reading": "みかん", "meaning": "mandarin orange"},
            {"word": "やめる", "reading": "やめる", "meaning": "to give up on, not do"},
            {"word": "だけ", "reading": "だけ", "meaning": "only, just"},
        ],
    },
    {
        "id": "n5-l04",
        "title": "A rainy Sunday",
        "kind": "point",
        "intro": "男の人と女の人が話しています。女の人は、きのう、どこへ行きましたか。",
        "lines": [
            ("M", "きのうは日曜日でしたね。どこかへ行きましたか。", "Yesterday was Sunday. Did you go anywhere?"),
            ("F", "ええ。友だちと山へ行きたかったんですが、雨でしたから、デパートへ行きました。",
             "Yes. I wanted to go to the mountains with a friend, but it was raining, so we went to a department store."),
            ("M", "そうですか。何か買いましたか。", "Really? Did you buy anything?"),
            ("F", "いいえ、何も買いませんでした。デパートの中のレストランで、ごはんを食べました。",
             "No, I didn't buy anything. We ate at a restaurant inside the department store."),
        ],
        "question": "女の人は、きのう、どこへ行きましたか。",
        "intro_en": "A man and a woman are talking. Where did the woman go yesterday?",
        "question_en": "Where did the woman go yesterday?",
        "choices": ["山", "友だちの家", "デパート", "公園"],
        "answer": 2,
        "why": "She WANTED to go to the mountains (行きたかったんですが), but it rained, so デパートへ行きました.",
        "vocab": [
            {"word": "どこか", "reading": "どこか", "meaning": "somewhere, anywhere"},
            {"word": "デパート", "reading": "デパート", "meaning": "department store"},
            {"word": "何か", "reading": "なにか", "meaning": "something, anything"},
        ],
    },
    {
        "id": "n5-l05",
        "title": "Tanaka's family",
        "kind": "point",
        "intro": "女の人と男の人が話しています。男の人の家族は、何人ですか。",
        "lines": [
            ("F", "田中さんは、何人家族ですか。", "How many people are in your family, Tanaka?"),
            ("M", "5人です。父と母と、姉が一人と、弟が一人います。",
             "Five. My father, my mother, an older sister and a younger brother."),
            ("F", "そうですか。みんないっしょに住んでいますか。", "I see. Do you all live together?"),
            ("M", "いいえ。姉は東京で仕事をしていますから、今は4人で住んでいます。",
             "No. My sister works in Tokyo, so there are four of us living together now."),
        ],
        "question": "男の人の家族は、何人ですか。",
        "intro_en": "A woman and a man are talking. How many people are in the man's family?",
        "question_en": "How many people are in the man's family?",
        "choices": ["3人", "4人", "5人", "6人"],
        "answer": 2,
        "why": "5人です: father, mother, sister, brother and him. Four is how many live at home now, because his sister "
               "works in Tokyo.",
        "vocab": [
            {"word": "家族", "reading": "かぞく", "meaning": "family"},
            {"word": "姉", "reading": "あね", "meaning": "(my) older sister"},
            {"word": "弟", "reading": "おとうと", "meaning": "(my) younger brother"},
            {"word": "住む", "reading": "すむ", "meaning": "to live (somewhere)"},
        ],
    },
    {
        "id": "n5-l06",
        "title": "Meeting before the film",
        "kind": "point",
        "intro": "男の人と女の人が、電話で話しています。二人は、何時に会いますか。",
        "lines": [
            ("M", "もしもし。あしたの映画は、何時に始まりますか。", "Hello. What time does tomorrow's film start?"),
            ("F", "2時半です。", "Half past two."),
            ("M", "じゃあ、2時に駅で会いましょうか。", "Then shall we meet at the station at two?"),
            ("F", "映画の前に、いっしょに昼ごはんを食べませんか。12時半はどうですか。",
             "How about having lunch together before the film? What about half past twelve?"),
            ("M", "すみません、午前中は仕事がありますから、1時でもいいですか。",
             "Sorry, I'm working in the morning, so is one o'clock all right?"),
            ("F", "いいですよ。じゃあ、1時に駅で。", "Sure. One o'clock at the station, then."),
        ],
        "question": "二人は、何時に会いますか。",
        "intro_en": "A man and a woman are talking on the phone. What time will they meet?",
        "question_en": "What time will they meet?",
        "choices": ["12時半", "1時", "2時", "2時半"],
        "answer": 1,
        "why": "The film is at 2:30 and he suggests 2, but she wants lunch first at 12:30. He works in the morning, so they "
               "settle on 1時に駅で.",
        "vocab": [
            {"word": "もしもし", "reading": "もしもし", "meaning": "hello (on the phone)"},
            {"word": "始まる", "reading": "はじまる", "meaning": "to start"},
            {"word": "午前中", "reading": "ごぜんちゅう", "meaning": "in the morning"},
        ],
    },
    {
        "id": "n5-l07",
        "title": "Asking for water",
        "kind": "utterance",
        "voice": "M",
        "intro": "レストランで、水がほしいです。店の人に、何と言いますか。",
        "lines": [],
        "question": "",
        "intro_en": "You're in a restaurant and you'd like some water. What do you say to the staff?",
        "question_en": "",
        "choices_en": ["Water, please.", "Here's some water.", "I'll give you water."],
        "choices": ["水をください。", "水をどうぞ。", "水をあげます。"],
        "answer": 0,
        "why": "〜をください asks for something. 〜をどうぞ offers it, and あげます means you give it: both are the "
               "staff's side.",
        "vocab": [
            {"word": "ほしい", "reading": "ほしい", "meaning": "to want (a thing)"},
            {"word": "ください", "reading": "ください", "meaning": "please give me"},
        ],
    },
    {
        "id": "n5-l08",
        "title": "Meeting the teacher",
        "kind": "utterance",
        "voice": "F",
        "intro": "朝、学校で先生に会いました。何と言いますか。",
        "lines": [],
        "question": "",
        "intro_en": "In the morning, you meet your teacher at school. What do you say?",
        "question_en": "",
        "choices_en": ["Good evening.", "Good morning.", "Good night."],
        "choices": ["こんばんは。", "おはようございます。", "おやすみなさい。"],
        "answer": 1,
        "why": "In the morning it's おはようございます (polite, for a teacher). こんばんは is for the evening, and "
               "おやすみなさい is said before going to bed.",
        "vocab": [
            {"word": "おはようございます", "reading": "おはようございます", "meaning": "good morning (polite)"},
            {"word": "おやすみなさい", "reading": "おやすみなさい", "meaning": "good night"},
        ],
    },
    {
        "id": "n5-l09",
        "title": "Whose umbrella?",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "これは、だれのかさですか。", "Whose umbrella is this?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": ["It's mine.", "It's over there.", "It's 1,000 yen."],
        "choices": ["わたしのです。", "あそこにあります。", "1,000円です。"],
        "answer": 0,
        "why": "だれの asks whose, so the reply names the owner: わたしのです (it's mine). The others answer where and how much.",
        "vocab": [
            {"word": "だれの", "reading": "だれの", "meaning": "whose"},
            {"word": "かさ", "reading": "かさ", "meaning": "umbrella"},
        ],
    },
    {
        "id": "n5-l10",
        "title": "Shall we have tea?",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "いっしょに、お茶を飲みませんか。", "Would you like to have some tea together?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": ["Yes, I didn't drink any.", "Yes, let's.", "No, it's tea."],
        "choices": ["はい、飲みませんでした。", "ええ、飲みましょう。", "いいえ、お茶です。"],
        "answer": 1,
        "why": "〜ませんか is an invitation, and 〜ましょう accepts it. 飲みませんでした is a past answer to a different "
               "question.",
        "vocab": [
            {"word": "いっしょに", "reading": "いっしょに", "meaning": "together"},
            {"word": "お茶", "reading": "おちゃ", "meaning": "(green) tea"},
        ],
    },
    # ------------------------------------------------------------------ N4
    {
        "id": "n4-l01",
        "title": "Shopping for the party",
        "kind": "task",
        "intro": "女の人と男の人が話しています。男の人は、これから何を買いに行きますか。",
        "lines": [
            ("F", "明日のパーティーの準備、もうできた？", "Are you ready for tomorrow's party?"),
            ("M", "うん、飲み物はもう買ってあるよ。ケーキも予約した。", "Yeah, I've already bought the drinks. And I've ordered the cake."),
            ("F", "よかった。お皿とコップは？", "Great. What about plates and cups?"),
            ("M", "お皿は家にあるのを使うつもり。コップは足りないかもしれない。",
             "I'm going to use the plates we have at home. We might not have enough cups."),
            ("F", "コップなら、私が持っていくよ。あ、でも、果物がないね。", "I'll bring cups. Oh, but there's no fruit."),
            ("M", "あ、そうだ。じゃあ、今から買ってくるよ。", "Oh, right. I'll go and buy some now, then."),
        ],
        "question": "男の人は、これから何を買いに行きますか。",
        "intro_en": "A woman and a man are talking. What is the man going to buy now?",
        "question_en": "What is the man going to buy now?",
        "choices": ["飲み物", "ケーキ", "コップ", "果物"],
        "answer": 3,
        "why": "The drinks are bought (買ってある), the cake is ordered, and she'll bring cups. Only the fruit is missing: "
               "今から買ってくるよ.",
        "vocab": [
            {"word": "準備", "reading": "じゅんび", "meaning": "preparation"},
            {"word": "予約する", "reading": "よやくする", "meaning": "to book, order in advance"},
            {"word": "足りない", "reading": "たりない", "meaning": "not enough"},
            {"word": "果物", "reading": "くだもの", "meaning": "fruit"},
        ],
    },
    {
        "id": "n4-l02",
        "title": "First visit to a clinic",
        "kind": "task",
        "intro": "病院で、受付の女の人と男の人が話しています。男の人は、このあとまず何をしますか。",
        "lines": [
            ("M", "すみません、この病院は初めてなんですが。", "Excuse me, this is my first time at this clinic."),
            ("F", "では、保険証を見せてください。……はい、ありがとうございます。", "Then please show me your health insurance card... Yes, thank you."),
            ("F", "それから、この紙に名前と住所を書いてください。", "Next, please write your name and address on this form."),
            ("M", "はい。", "OK."),
            ("F", "書いたら、熱を測ってから、こちらに持ってきてください。",
             "When you've written them, take your temperature and then bring it here."),
            ("M", "分かりました。体温計はどこですか。", "I see. Where is the thermometer?"),
            ("F", "あちらの机の上にあります。", "It's on that desk over there."),
        ],
        "question": "男の人は、このあとまず何をしますか。",
        "intro_en": "At a clinic, a woman at reception and a man are talking. What will the man do first after this?",
        "question_en": "What will the man do first after this?",
        "choices": ["保険証を見せる", "紙に名前と住所を書く", "熱を測る", "紙を受付に持っていく"],
        "answer": 1,
        "why": "He has already shown his card. The order is: write the form (書いたら), then take his temperature, then bring "
               "the form back. So first he writes.",
        "vocab": [
            {"word": "受付", "reading": "うけつけ", "meaning": "reception"},
            {"word": "保険証", "reading": "ほけんしょう", "meaning": "health insurance card"},
            {"word": "住所", "reading": "じゅうしょ", "meaning": "address"},
            {"word": "熱を測る", "reading": "ねつをはかる", "meaning": "to take one's temperature"},
            {"word": "体温計", "reading": "たいおんけい", "meaning": "thermometer"},
        ],
    },
    {
        "id": "n4-l03",
        "title": "Next week's class",
        "kind": "task",
        "intro": "教室で、先生が話しています。学生は、来週の授業までに何をしなければなりませんか。",
        "lines": [
            ("F", "皆さん、今日の授業はここまでです。", "Everyone, that's all for today's class."),
            ("F", "来週はテストの予定でしたが、再来週になりました。", "We were going to have a test next week, but it's moved to the week after."),
            ("F", "来週の授業では、作文を書きます。テーマは「私の好きな場所」です。",
             "In next week's class you'll write an essay. The theme is \"My favourite place\"."),
            ("F", "教科書の三十ページの言葉を使いますから、来週までに覚えてきてください。",
             "You'll use the words on page thirty of the textbook, so please learn them by next week."),
            ("F", "作文は授業中に書きますから、家で書かなくてもいいですよ。",
             "You'll write the essay during class, so you don't need to write it at home."),
        ],
        "question": "学生は、来週の授業までに何をしなければなりませんか。",
        "intro_en": "In a classroom, the teacher is speaking. What must the students do before next week's class?",
        "question_en": "What must the students do before next week's class?",
        "choices": ["テストの勉強をする", "作文を書く", "教科書の言葉を覚える", "好きな場所に行く"],
        "answer": 2,
        "why": "The test moved to the week after next, and the essay is written in class (家で書かなくてもいい). "
               "The homework is the words on page 30: 来週までに覚えてきてください.",
        "vocab": [
            {"word": "授業", "reading": "じゅぎょう", "meaning": "class, lesson"},
            {"word": "予定", "reading": "よてい", "meaning": "plan, schedule"},
            {"word": "再来週", "reading": "さらいしゅう", "meaning": "the week after next"},
            {"word": "作文", "reading": "さくぶん", "meaning": "essay, composition"},
            {"word": "教科書", "reading": "きょうかしょ", "meaning": "textbook"},
        ],
    },
    {
        "id": "n4-l04",
        "title": "Why were you late?",
        "kind": "point",
        "intro": "会社で、男の人と女の人が話しています。男の人は、どうして遅れましたか。",
        "lines": [
            ("M", "すみません、遅くなりました。", "Sorry I'm late."),
            ("F", "大丈夫ですよ。電車が遅れたんですか。", "That's all right. Was the train late?"),
            ("M", "いいえ、電車はいつもどおりでした。でも、家を出るとき、かぎが見つからなくて。",
             "No, the train was on time. But when I was leaving the house, I couldn't find my key."),
            ("F", "ああ、それは困りましたね。", "Oh, that's annoying."),
            ("M", "ええ。結局、かばんの中にあったんですけど。", "Yes. In the end it was in my bag."),
        ],
        "question": "男の人は、どうして遅れましたか。",
        "intro_en": "At an office, a man and a woman are talking. Why was the man late?",
        "question_en": "Why was the man late?",
        "choices": ["電車が遅れたから", "朝、起きられなかったから", "かぎを探していたから", "かばんを忘れたから"],
        "answer": 2,
        "why": "The train was on time (いつもどおり). He couldn't find his key when leaving: かぎが見つからなくて. "
               "The bag is where the key turned up, not something he forgot.",
        "vocab": [
            {"word": "遅れる", "reading": "おくれる", "meaning": "to be late"},
            {"word": "いつもどおり", "reading": "いつもどおり", "meaning": "as usual"},
            {"word": "見つかる", "reading": "みつかる", "meaning": "to be found"},
            {"word": "結局", "reading": "けっきょく", "meaning": "in the end"},
        ],
    },
    {
        "id": "n4-l05",
        "title": "When shall we see a film?",
        "kind": "point",
        "intro": "男の人と女の人が話しています。二人は、いつ映画を見に行きますか。",
        "lines": [
            ("M", "今度の土曜日、映画を見に行かない？", "Do you want to go and see a film this Saturday?"),
            ("F", "土曜日はアルバイトがあるの。日曜日はどう？", "I've got my part-time job on Saturday. How about Sunday?"),
            ("M", "日曜日は弟の誕生日だから、家族で食事をするんだ。", "Sunday is my little brother's birthday, so we're having a family meal."),
            ("F", "そうか。じゃあ、来週の金曜日の夜は？", "I see. Then how about next Friday evening?"),
            ("M", "金曜日は、仕事が遅くまであるかもしれないな。あ、でも、木曜日なら大丈夫だよ。",
             "I might be working late on Friday. Oh, but Thursday is fine."),
            ("F", "木曜日は私も早く終わるから、いいよ。", "I finish early on Thursday too, so that works."),
        ],
        "question": "二人は、いつ映画を見に行きますか。",
        "intro_en": "A man and a woman are talking. When will they go to see a film?",
        "question_en": "When will they go to see a film?",
        "choices": ["木曜日", "金曜日", "土曜日", "日曜日"],
        "answer": 0,
        "why": "Saturday she works, Sunday is his brother's birthday, Friday he may work late. He offers Thursday and she "
               "agrees: いいよ.",
        "vocab": [
            {"word": "今度", "reading": "こんど", "meaning": "this coming, next"},
            {"word": "アルバイト", "reading": "アルバイト", "meaning": "part-time job"},
            {"word": "誕生日", "reading": "たんじょうび", "meaning": "birthday"},
            {"word": "遅くまで", "reading": "おそくまで", "meaning": "until late"},
        ],
    },
    {
        "id": "n4-l06",
        "title": "Where are the umbrellas?",
        "kind": "point",
        "intro": "デパートで、女の人と店の人が話しています。女の人は、まず何階に行きますか。",
        "lines": [
            ("F", "すみません、傘を売っているところはどこですか。", "Excuse me, where do you sell umbrellas?"),
            ("S", "傘は三階です。", "Umbrellas are on the third floor."),
            ("S", "でも、今日は二階の入り口の近くでも、安く売っていますよ。",
             "But today they're also on sale cheaply near the entrance on the second floor."),
            ("F", "そうですか。じゃあ、先にそちらを見てみます。", "Really? Then I'll have a look there first."),
            ("S", "エスカレーターはあちらです。", "The escalator is over there."),
        ],
        "question": "女の人は、まず何階に行きますか。",
        "intro_en": "In a department store, a woman and a staff member are talking. Which floor will the woman go to first?",
        "question_en": "Which floor will the woman go to first?",
        "choices": ["一階", "二階", "三階", "四階"],
        "answer": 1,
        "why": "Umbrellas are usually on the 3rd floor, but there's a cheap sale near the 2nd-floor entrance, and she says "
               "先にそちらを見てみます (I'll look there first).",
        "vocab": [
            {"word": "傘", "reading": "かさ", "meaning": "umbrella"},
            {"word": "売る", "reading": "うる", "meaning": "to sell"},
            {"word": "入り口", "reading": "いりぐち", "meaning": "entrance"},
            {"word": "先に", "reading": "さきに", "meaning": "first, before that"},
        ],
    },
    {
        "id": "n4-l07",
        "title": "Borrowing a pen",
        "kind": "utterance",
        "voice": "F",
        "intro": "友達のペンを使いたいです。何と言いますか。",
        "lines": [],
        "question": "",
        "intro_en": "You want to use your friend's pen. What do you say?",
        "question_en": "",
        "choices_en": ["Can I lend you a pen?", "Can I borrow your pen?", "Shall I borrow a pen for you?"],
        "choices": ["ペン、貸してもいい？", "ペン、借りてもいい？", "ペン、借りてあげようか。"],
        "answer": 1,
        "why": "借りる is to borrow, 貸す is to lend. 借りてもいい？ asks permission to borrow. 貸してもいい？ offers to lend "
               "your own pen, and 〜てあげようか offers to do something for the other person.",
        "vocab": [
            {"word": "借りる", "reading": "かりる", "meaning": "to borrow"},
            {"word": "貸す", "reading": "かす", "meaning": "to lend"},
        ],
    },
    {
        "id": "n4-l08",
        "title": "Leaving work first",
        "kind": "utterance",
        "voice": "M",
        "intro": "仕事が終わりました。会社の人より先に帰ります。何と言いますか。",
        "lines": [],
        "question": "",
        "intro_en": "Work is over. You're going home before your colleagues. What do you say?",
        "question_en": "",
        "choices_en": ["I'm off now (and coming back).", "Excuse me for leaving first.", "Sorry to intrude."],
        "choices": ["いってきます。", "お先に失礼します。", "おじゃまします。"],
        "answer": 1,
        "why": "お先に失礼します is the set phrase for leaving work before others. いってきます means you'll come back "
               "(leaving home), and おじゃまします is said when entering someone's home.",
        "vocab": [
            {"word": "お先に失礼します", "reading": "おさきにしつれいします", "meaning": "excuse me for leaving first"},
            {"word": "おじゃまします", "reading": "おじゃまします", "meaning": "sorry to intrude (entering a home)"},
        ],
    },
    {
        "id": "n4-l09",
        "title": "Is there a post office?",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "すみません、この近くに郵便局はありますか。", "Excuse me, is there a post office near here?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": ["Yes, it's next to that bank.", "Yes, I'm going to the post office.", "No, I sent a letter."],
        "choices": ["ええ、あの銀行の隣にありますよ。", "はい、郵便局へ行きます。", "いいえ、手紙を出しました。"],
        "answer": 0,
        "why": "He asks where a post office is, so the reply says where: あの銀行の隣. The other two talk about "
               "the speaker's own plans.",
        "vocab": [
            {"word": "郵便局", "reading": "ゆうびんきょく", "meaning": "post office"},
            {"word": "隣", "reading": "となり", "meaning": "next to"},
        ],
    },
    {
        "id": "n4-l10",
        "title": "Tea or coffee?",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "お茶とコーヒーと、どちらがいいですか。", "Which would you like, tea or coffee?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": ["Yes, that's fine.", "Then coffee, please.", "There's neither."],
        "choices": ["はい、いいです。", "じゃあ、コーヒーをお願いします。", "どちらもありません。"],
        "answer": 1,
        "why": "どちらがいいですか asks you to choose, so you name one: コーヒーをお願いします. はい doesn't answer a "
               "which-question, and どちらもありません would be the host's line.",
        "vocab": [
            {"word": "どちら", "reading": "どちら", "meaning": "which (of two)"},
            {"word": "お願いします", "reading": "おねがいします", "meaning": "please"},
        ],
    },
    # ------------------------------------------------------------------ N3
    {
        "id": "n3-l01",
        "title": "Preparing a presentation",
        "kind": "task",
        "intro": "大学で、女の学生と男の学生が話しています。男の学生は、このあとまず何をしますか。",
        "lines": [
            ("F", "田中くん、来週の発表の準備、もう始めた？", "Tanaka, have you started preparing for next week's presentation?"),
            ("M", "うん、資料はだいたい集めたんだけど、まだまとめてないんだ。", "Yeah, I've collected most of the material, but I haven't put it together yet."),
            ("F", "そうなんだ。先生が、発表の前に一度原稿を見せてほしいって言ってたよ。", "I see. The teacher said they'd like to see the script once before the presentation."),
            ("M", "え、そうなの？知らなかった。じゃあ、すぐ原稿を書かないと。", "Really? I didn't know. Then I'd better write the script right away."),
            ("F", "あ、でも、その前に、いつ見せればいいか、先生にメールで聞いたほうがいいんじゃない？先生、来週はお休みらしいから。",
             "Oh, but before that, shouldn't you email the teacher and ask when to show it? Apparently the teacher is off next week."),
            ("M", "そうか。じゃあ、まずそうするよ。", "I see. Then I'll do that first."),
        ],
        "question": "男の学生は、このあとまず何をしますか。",
        "intro_en": "At a university, a female student and a male student are talking. What will the male student do first after this?",
        "question_en": "What will the male student do first after this?",
        "choices": ["資料を集める", "原稿を書く", "先生にメールを送る", "先生に原稿を見せる"],
        "answer": 2,
        "why": "He was going to write the script, but she suggests emailing the teacher first (その前に…メールで聞いたほうが), "
               "and he agrees: まずそうするよ.",
        "vocab": [
            {"word": "発表", "reading": "はっぴょう", "meaning": "presentation"},
            {"word": "資料", "reading": "しりょう", "meaning": "materials, data"},
            {"word": "原稿", "reading": "げんこう", "meaning": "script, manuscript"},
            {"word": "まとめる", "reading": "まとめる", "meaning": "to put together, summarize"},
        ],
    },
    {
        "id": "n3-l02",
        "title": "A shirt in the wrong size",
        "kind": "task",
        "intro": "店で、女の人と店員が話しています。女の人は、このあとどこへ行きますか。",
        "lines": [
            ("F", "すみません、このシャツの、もう少し大きいサイズはありますか。", "Excuse me, do you have this shirt in a slightly bigger size?"),
            ("M", "申し訳ございません。こちらの店には、今このサイズしかないんです。駅前の店にはあるかもしれませんので、お調べしましょうか。",
             "I'm very sorry. This shop only has this size at the moment. The shop by the station might have it. Shall I check?"),
            ("F", "お願いします。", "Yes, please."),
            ("M", "お待たせしました。駅前の店にも、ないそうです。ただ、インターネットで注文していただければ、三日ほどで届きます。",
             "Thank you for waiting. They don't have it either. But if you order online, it'll arrive in about three days."),
            ("F", "そうですか。じゃあ、家に帰ってから注文します。今日は、ほかの店も見てみたいので。",
             "I see. Then I'll order it when I get home. Today I'd like to look at some other shops too."),
            ("M", "かしこまりました。", "Certainly."),
        ],
        "question": "女の人は、このあとどこへ行きますか。",
        "intro_en": "In a shop, a woman and a shop assistant are talking. Where will the woman go after this?",
        "question_en": "Where will the woman go after this?",
        "choices": ["駅前の店", "ほかの店", "自分の家", "この店のレジ"],
        "answer": 1,
        "why": "The station shop doesn't have it either. She'll order online after getting home, but today she wants to look "
               "at other shops first (今日は、ほかの店も見てみたい).",
        "vocab": [
            {"word": "店員", "reading": "てんいん", "meaning": "shop assistant"},
            {"word": "駅前", "reading": "えきまえ", "meaning": "in front of the station"},
            {"word": "注文", "reading": "ちゅうもん", "meaning": "order"},
            {"word": "届く", "reading": "とどく", "meaning": "to arrive, be delivered"},
        ],
    },
    {
        "id": "n3-l03",
        "title": "A trip to the supermarket",
        "kind": "task",
        "intro": "家で、女の人と男の人が話しています。男の人は、何を買ってきますか。",
        "lines": [
            ("F", "ねえ、スーパーに行くなら、牛乳と卵を買ってきてくれる？", "Hey, if you're going to the supermarket, could you get milk and eggs?"),
            ("M", "いいよ。ほかには？", "Sure. Anything else?"),
            ("F", "えっと、パンはまだあるし……あ、卵はやっぱりいいや。昨日買ったの、忘れてた。",
             "Um, we still have bread... oh, never mind the eggs. I forgot I bought some yesterday."),
            ("M", "じゃあ、牛乳だけ？", "So just milk?"),
            ("F", "うん。あ、それから、トイレットペーパーもお願い。", "Yes. Oh, and toilet paper too, please."),
            ("M", "分かった。", "Got it."),
        ],
        "question": "男の人は、何を買ってきますか。",
        "intro_en": "At home, a woman and a man are talking. What will the man buy?",
        "question_en": "What will the man buy?",
        "choices": ["牛乳と卵", "牛乳とトイレットペーパー", "卵とパン", "牛乳とパンとトイレットペーパー"],
        "answer": 1,
        "why": "The eggs are cancelled (やっぱりいいや), there's still bread, and toilet paper is added at the end.",
        "vocab": [
            {"word": "牛乳", "reading": "ぎゅうにゅう", "meaning": "milk"},
            {"word": "やっぱり", "reading": "やっぱり", "meaning": "after all (changing your mind)"},
            {"word": "いいや", "reading": "いいや", "meaning": "never mind, it's fine (casual)"},
        ],
    },
    {
        "id": "n3-l04",
        "title": "Why he was late",
        "kind": "point",
        "intro": "男の人と女の人が話しています。男の人は、どうして遅れましたか。",
        "lines": [
            ("F", "遅かったね。電車、遅れてたの？", "You're late. Was the train delayed?"),
            ("M", "いや、電車は時間どおりだったんだけど、家を出るとき、かぎが見つからなくて。",
             "No, the train was on time, but when I was leaving home, I couldn't find my keys."),
            ("F", "また？", "Again?"),
            ("M", "いつもの所に置いたと思ってたんだけど、かばんの中に入ってたんだ。", "I thought I'd put them in the usual place, but they were in my bag."),
            ("F", "次からは、玄関にかけておいたら？", "From now on, why not hang them by the front door?"),
        ],
        "question": "男の人は、どうして遅れましたか。",
        "intro_en": "A man and a woman are talking. Why was the man late?",
        "question_en": "Why was the man late?",
        "choices": ["電車が遅れたから", "かぎを探していたから", "かばんを忘れたから", "道を間違えたから"],
        "answer": 1,
        "why": "The train was on time (時間どおり); he couldn't find his keys (かぎが見つからなくて), which turned out to be in his bag.",
        "vocab": [
            {"word": "かぎ", "reading": "かぎ", "meaning": "key"},
            {"word": "見つかる", "reading": "みつかる", "meaning": "to be found"},
            {"word": "玄関", "reading": "げんかん", "meaning": "entrance, front door"},
        ],
    },
    {
        "id": "n3-l05",
        "title": "Quitting the cooking class",
        "kind": "point",
        "intro": "男の人と女の人が話しています。女の人が料理教室をやめたいちばんの理由は何ですか。",
        "lines": [
            ("M", "料理教室、やめたんだって？楽しそうだったのに。", "I heard you quit your cooking class? It seemed like fun."),
            ("F", "うん、楽しかったよ。先生も優しかったし。", "Yes, it was fun. And the teacher was kind."),
            ("M", "じゃあ、どうして？お金がかかるから？", "Then why? Because it cost money?"),
            ("F", "ううん、それは大丈夫だったんだけど、引っ越してから、教室まで一時間以上かかるようになっちゃって。",
             "No, that was fine, but since I moved, it takes over an hour to get to the class."),
            ("M", "ああ、それは大変だね。", "Ah, that's tough."),
            ("F", "うん。近くにいい教室があったら、また習いたいんだけどね。", "Yeah. If there were a good class nearby, I'd like to learn again."),
        ],
        "question": "女の人が料理教室をやめたいちばんの理由は何ですか。",
        "intro_en": "A man and a woman are talking. What is the main reason the woman quit her cooking class?",
        "question_en": "What is the main reason the woman quit her cooking class?",
        "choices": ["先生が厳しかったから", "お金がかかるから", "教室が遠くなったから", "料理が上手になったから"],
        "answer": 2,
        "why": "The teacher was kind and money was fine (それは大丈夫だった); after moving, the class is over an hour away.",
        "vocab": [
            {"word": "教室", "reading": "きょうしつ", "meaning": "class, classroom"},
            {"word": "理由", "reading": "りゆう", "meaning": "reason"},
            {"word": "以上", "reading": "いじょう", "meaning": "more than"},
        ],
    },
    {
        "id": "n3-l06",
        "title": "What time to meet",
        "kind": "point",
        "intro": "男の学生と女の学生が、電話で話しています。二人は、何時に会いますか。",
        "lines": [
            ("M", "もしもし。明日の買い物、十時に駅で会う約束だったよね。", "Hello. We said we'd meet at the station at ten tomorrow to go shopping, right?"),
            ("F", "うん。", "Yes."),
            ("M", "ごめん、午前中に病院に行かなきゃいけなくなって。十二時でもいい？", "Sorry, I have to go to the hospital in the morning. Is twelve OK?"),
            ("F", "十二時か……。じゃあ、先にお昼ご飯を食べてから行かない？一時に、駅前のレストランはどう？",
             "Twelve, hmm... Then why don't we have lunch first? How about one o'clock at the restaurant by the station?"),
            ("M", "いいね。そうしよう。", "Sounds good. Let's do that."),
        ],
        "question": "二人は、何時に会いますか。",
        "intro_en": "A male student and a female student are talking on the phone. What time will they meet?",
        "question_en": "What time will they meet?",
        "choices": ["10時", "12時", "1時", "2時"],
        "answer": 2,
        "why": "Ten is cancelled, he suggests twelve, and she counters with lunch at one (一時に、駅前のレストラン), which he accepts.",
        "vocab": [
            {"word": "午前中", "reading": "ごぜんちゅう", "meaning": "during the morning"},
            {"word": "病院", "reading": "びょういん", "meaning": "hospital"},
            {"word": "先に", "reading": "さきに", "meaning": "first, beforehand"},
        ],
    },
    {
        "id": "n3-l07",
        "title": "Breakfast on the radio",
        "kind": "summary",
        "intro": "ラジオで、女の人が話しています。",
        "lines": [
            ("F", "皆さんは、朝ご飯を毎日食べていますか。忙しくて、朝は何も食べないという人も多いと思います。",
             "Do you all eat breakfast every day? I think many people are too busy and don't eat anything in the morning."),
            ("F", "でも、朝ご飯を食べないと、午前中、頭が働きにくくなると言われています。",
             "But it's said that if you skip breakfast, your brain works less well in the morning."),
            ("F", "時間がない人は、バナナ一本や牛乳一杯だけでもかまいません。少しでも何かを食べるようにしましょう。",
             "If you have no time, just one banana or one glass of milk is fine. Let's try to eat at least a little."),
        ],
        "question": "女の人が、いちばん言いたいことは何ですか。",
        "intro_en": "A woman is talking on the radio.",
        "question_en": "What does the woman most want to say?",
        "choices_en": [
            "You should take your time over breakfast.",
            "You should eat breakfast, even just a little.",
            "Bananas are the best breakfast.",
            "Busy people don't need to eat breakfast.",
        ],
        "choices": [
            "朝ご飯は、ゆっくり時間をかけて食べたほうがいい。",
            "朝ご飯は、少しでもいいから食べたほうがいい。",
            "朝ご飯には、バナナがいちばんいい。",
            "忙しい人は、朝ご飯を食べなくてもいい。",
        ],
        "answer": 1,
        "why": "The talk ends with the main point: even a banana or a glass of milk is fine, so eat at least a little "
               "(少しでも何かを食べるようにしましょう).",
        "vocab": [
            {"word": "皆さん", "reading": "みなさん", "meaning": "everyone"},
            {"word": "頭が働く", "reading": "あたまがはたらく", "meaning": "the brain works, think clearly"},
            {"word": "かまわない", "reading": "かまわない", "meaning": "it's fine, doesn't matter"},
        ],
    },
    {
        "id": "n3-l08",
        "title": "Is this seat free?",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "すみません、この席、空いていますか。", "Excuse me, is this seat free?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": ["Yes, I kept it free for you.", "Yes, go ahead.", "No, you're welcome."],
        "choices": ["ええ、空けておきました。", "ええ、どうぞ。", "いいえ、どういたしまして。"],
        "answer": 1,
        "why": "ええ、どうぞ (yes, go ahead) answers the question. 空けておきました means you kept it free on purpose, "
               "and どういたしまして answers a thank-you.",
        "vocab": [
            {"word": "席", "reading": "せき", "meaning": "seat"},
            {"word": "空く", "reading": "あく", "meaning": "to be free, empty"},
        ],
    },
    {
        "id": "n3-l09",
        "title": "Handing out worksheets",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "このプリント、クラスのみんなに配っておいてくれる？", "Could you hand these worksheets out to everyone in the class?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": [
            "Yes, I'll hand them out.",
            "Yes, I'll get someone to hand them out.",
            "No, I didn't hand them out.",
        ],
        "choices": ["はい、配っておきます。", "はい、配ってもらいます。", "いいえ、配りませんでした。"],
        "answer": 0,
        "why": "〜ておいてくれる？ is a request, so 配っておきます (I'll hand them out) is the reply. 配ってもらいます would mean "
               "getting someone else to do it.",
        "vocab": [
            {"word": "プリント", "reading": "プリント", "meaning": "handout, worksheet"},
            {"word": "配る", "reading": "くばる", "meaning": "to hand out"},
        ],
    },
    {
        "id": "n3-l10",
        "title": "Has Tanaka gone home?",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "あれ、田中さん、もう帰っちゃったの？", "Huh, has Tanaka already gone home?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices_en": [
            "Yeah, they left a moment ago.",
            "Yeah, they'll be back soon.",
            "No, you don't have to go home.",
        ],
        "choices": ["うん、さっき帰ったよ。", "うん、もうすぐ帰ってくるよ。", "ううん、帰らなくてもいいよ。"],
        "answer": 0,
        "why": "帰っちゃった asks whether Tanaka has already left. さっき帰ったよ (left a moment ago) answers it; "
               "the others are about coming back or not needing to leave.",
        "vocab": [
            {"word": "さっき", "reading": "さっき", "meaning": "a moment ago"},
            {"word": "もうすぐ", "reading": "もうすぐ", "meaning": "soon"},
        ],
    },
    {
        "id": "n3-l11",
        "title": "A library card",
        "kind": "task",
        "intro": "図書館で、男の人と係の人が話しています。男の人は、このあと何をしなければなりませんか。",
        "lines": [
            ("M", "すみません、この本を借りたいんですが。", "Excuse me, I'd like to borrow this book."),
            ("F", "はい。図書館のカードはお持ちですか。", "Certainly. Do you have a library card?"),
            ("M", "いえ、今日初めて来たので、持っていないんです。", "No, it's my first time here, so I don't have one."),
            ("F", "では、カードを作りましょう。住所が分かるもの、たとえば免許証か保険証はありますか。",
             "Then let's make you a card. Do you have something that shows your address, such as a driving licence or a health insurance card?"),
            ("M", "学生証しかないんですが……。", "I only have my student ID..."),
            ("F", "学生証には住所が書いてありませんので、申し訳ありませんが、住所が分かるものを持って、もう一度来ていただけますか。",
             "A student ID doesn't show your address, so I'm sorry, but could you come back with something that does?"),
            ("M", "分かりました。", "I understand."),
        ],
        "question": "男の人は、このあと何をしなければなりませんか。",
        "intro_en": "At a library, a man and a staff member are talking. What does the man have to do after this?",
        "question_en": "What does the man have to do after this?",
        "choices": ["図書館のカードを作る", "住所が分かるものを持ってくる", "学生証を見せる", "借りた本を返す"],
        "answer": 1,
        "why": "He can't make a card today: his student ID has no address. He's asked to come back with something that shows "
               "his address (住所が分かるものを持って、もう一度来て).",
        "vocab": [
            {"word": "係の人", "reading": "かかりのひと", "meaning": "staff member in charge"},
            {"word": "住所", "reading": "じゅうしょ", "meaning": "address"},
            {"word": "免許証", "reading": "めんきょしょう", "meaning": "driving licence"},
            {"word": "保険証", "reading": "ほけんしょう", "meaning": "health insurance card"},
            {"word": "学生証", "reading": "がくせいしょう", "meaning": "student ID"},
        ],
    },
    {
        "id": "n3-l12",
        "title": "Getting ready for a party",
        "kind": "task",
        "intro": "女の学生と男の学生が、パーティーの準備について話しています。男の学生は、このあと何を買いに行きますか。",
        "lines": [
            ("F", "飲み物は、もう買ってあるよね。", "We've already bought the drinks, right?"),
            ("M", "うん、ジュースとお茶は昨日買っておいた。", "Yes, I bought juice and tea yesterday."),
            ("F", "じゃあ、あとは食べ物だね。ケーキは私が予約してあるから、帰りに取ってくる。",
             "Then all that's left is food. I've reserved the cake, so I'll pick it up on the way back."),
            ("M", "ありがとう。じゃあ、僕はお菓子を買ってくるよ。", "Thanks. Then I'll go and buy some snacks."),
            ("F", "あ、お菓子は、さっき山田さんが持ってきてくれたの。それより、紙のお皿とコップが足りないかもしれない。",
             "Oh, Yamada brought snacks a little while ago. More importantly, we might not have enough paper plates and cups."),
            ("M", "分かった。じゃあ、それを買ってくる。", "Got it. Then I'll go and buy those."),
        ],
        "question": "男の学生は、このあと何を買いに行きますか。",
        "intro_en": "A female student and a male student are talking about preparing for a party. What will the male student go to buy?",
        "question_en": "What will the male student go to buy?",
        "choices": ["ジュースとお茶", "ケーキ", "お菓子", "紙のお皿とコップ"],
        "answer": 3,
        "why": "The drinks are bought, she'll collect the cake, and Yamada already brought snacks. What's missing is paper plates "
               "and cups (紙のお皿とコップが足りない), and he says he'll buy those.",
        "vocab": [
            {"word": "予約", "reading": "よやく", "meaning": "reservation, booking"},
            {"word": "お菓子", "reading": "おかし", "meaning": "sweets, snacks"},
            {"word": "足りない", "reading": "たりない", "meaning": "not enough"},
            {"word": "それより", "reading": "それより", "meaning": "more importantly, rather than that"},
        ],
    },
    {
        "id": "n3-l13",
        "title": "Doctor's advice",
        "kind": "task",
        "intro": "病院で、医者と女の人が話しています。女の人は、今晩どうしますか。",
        "lines": [
            ("M", "熱は少し下がりましたね。薬はちゃんと飲んでいますか。", "Your fever has gone down a little. Are you taking your medicine properly?"),
            ("F", "はい、朝と晩に飲んでいます。", "Yes, I take it in the morning and the evening."),
            ("M", "いいですね。今晩はお風呂に入ってもいいですが、長く入らないでください。シャワーだけのほうがいいでしょう。",
             "Good. You can have a bath tonight, but don't stay in long. A shower alone would probably be better."),
            ("F", "分かりました。運動は、まだだめですか。", "I see. Is exercise still not allowed?"),
            ("M", "そうですね、ジョギングは来週まで待ってください。", "Well, please wait until next week for jogging."),
        ],
        "question": "女の人は、今晩どうしますか。",
        "intro_en": "At a hospital, a doctor and a woman are talking. What will the woman do tonight?",
        "question_en": "What will the woman do tonight?",
        "choices": ["お風呂に長く入る", "シャワーを浴びる", "ジョギングをする", "薬を飲まないで寝る"],
        "answer": 1,
        "why": "A bath is allowed but not a long one, and the doctor says a shower would be better (シャワーだけのほうがいい). "
               "Jogging must wait until next week, and she takes her medicine every evening.",
        "vocab": [
            {"word": "熱", "reading": "ねつ", "meaning": "fever"},
            {"word": "下がる", "reading": "さがる", "meaning": "to go down"},
            {"word": "今晩", "reading": "こんばん", "meaning": "tonight"},
            {"word": "浴びる", "reading": "あびる", "meaning": "to take (a shower)"},
        ],
    },
    {
        "id": "n3-l14",
        "title": "The new apartment",
        "kind": "point",
        "intro": "男の人と女の人が、女の人の新しいアパートについて話しています。女の人がいちばん気に入っているのは、どんなところですか。",
        "lines": [
            ("M", "新しいアパート、どう？", "How's the new apartment?"),
            ("F", "うん、すごく気に入ってる。駅からは少し遠いんだけどね。", "I really like it. It's a bit far from the station, though."),
            ("M", "部屋は広いの？", "Is the room big?"),
            ("F", "前の部屋とあまり変わらないかな。でも、窓が大きくて、朝、日がたくさん入るの。それがいちばんうれしい。",
             "Not much different from my old room. But the windows are big, and lots of sunlight comes in in the morning. That's what makes me happiest."),
            ("M", "へえ、いいね。", "Oh, nice."),
        ],
        "question": "女の人がいちばん気に入っているのは、どんなところですか。",
        "intro_en": "A man and a woman are talking about the woman's new apartment. What does the woman like most about it?",
        "question_en": "What does the woman like most about it?",
        "choices": ["駅から近いところ", "部屋が広いところ", "日当たりがいいところ", "家賃が安いところ"],
        "answer": 2,
        "why": "It's far from the station and the room is about the same size, but lots of morning sun comes in, and "
               "それがいちばんうれしい (that's what makes her happiest).",
        "vocab": [
            {"word": "気に入る", "reading": "きにいる", "meaning": "to like, be pleased with"},
            {"word": "日当たり", "reading": "ひあたり", "meaning": "sunlight (a room gets)"},
            {"word": "家賃", "reading": "やちん", "meaning": "rent"},
        ],
    },
    {
        "id": "n3-l15",
        "title": "A problem with a new phone",
        "kind": "point",
        "intro": "店で、男の人と店員が話しています。男の人のスマートフォンは、どこが問題ですか。",
        "lines": [
            ("M", "すみません、このスマートフォン、先週買ったばかりなんですが、ちょっと見てもらえますか。",
             "Excuse me, I only bought this smartphone last week. Could you have a look at it?"),
            ("F", "はい。どうなさいましたか。", "Of course. What seems to be the problem?"),
            ("M", "電話もメールも普通に使えるんですけど、写真を撮ろうとすると、画面が暗くなって止まってしまうんです。",
             "Calls and email work normally, but whenever I try to take a photo, the screen goes dark and freezes."),
            ("F", "そうですか。電池は、すぐなくなりますか。", "I see. Does the battery run out quickly?"),
            ("M", "いえ、電池は大丈夫です。", "No, the battery's fine."),
        ],
        "question": "男の人のスマートフォンは、どこが問題ですか。",
        "intro_en": "In a shop, a man and a shop assistant are talking. What is wrong with the man's smartphone?",
        "question_en": "What is wrong with the man's smartphone?",
        "choices": ["電話がかけられない", "メールが送れない", "カメラが使えない", "電池がすぐなくなる"],
        "answer": 2,
        "why": "Calls, email and the battery are fine; the screen freezes when he tries to take a photo "
               "(写真を撮ろうとすると…止まってしまう), so the camera can't be used.",
        "vocab": [
            {"word": "画面", "reading": "がめん", "meaning": "screen"},
            {"word": "電池", "reading": "でんち", "meaning": "battery"},
            {"word": "止まる", "reading": "とまる", "meaning": "to stop, freeze"},
        ],
    },
    {
        "id": "n3-l16",
        "title": "Sports day is moved",
        "kind": "point",
        "intro": "学校で、先生が話しています。運動会は、どうして来週になりましたか。",
        "lines": [
            ("F", "皆さん、明日の運動会のことですが、来週の土曜日に変更することになりました。",
             "Everyone, about tomorrow's sports day: it has been moved to next Saturday."),
            ("F", "天気予報では、明日は晴れるそうなんですが、グラウンドが昨日の雨で、まだ使えない状態なんです。",
             "The forecast says it will be sunny tomorrow, but the sports ground still can't be used because of yesterday's rain."),
            ("F", "来週の土曜日は、明日と同じ時間に始めます。お弁当を忘れないようにしてください。",
             "Next Saturday we'll start at the same time as planned for tomorrow. Please don't forget your packed lunch."),
        ],
        "question": "運動会は、どうして来週になりましたか。",
        "intro_en": "At a school, a teacher is speaking. Why has sports day been moved to next week?",
        "question_en": "Why has sports day been moved to next week?",
        "choices": ["明日は雨が降るから", "グラウンドが使えないから", "先生が忙しいから", "お弁当が準備できないから"],
        "answer": 1,
        "why": "Tomorrow will be sunny (晴れるそう), but the ground is still unusable after yesterday's rain "
               "(グラウンドが…まだ使えない状態).",
        "vocab": [
            {"word": "運動会", "reading": "うんどうかい", "meaning": "sports day"},
            {"word": "変更", "reading": "へんこう", "meaning": "change (of plans)"},
            {"word": "天気予報", "reading": "てんきよほう", "meaning": "weather forecast"},
            {"word": "状態", "reading": "じょうたい", "meaning": "condition, state"},
        ],
    },
    {
        "id": "n3-l17",
        "title": "At the art museum",
        "kind": "summary",
        "intro": "美術館で、係の人が話しています。",
        "lines": [
            ("F", "本日は、さくら美術館にお越しいただき、ありがとうございます。",
             "Thank you for visiting the Sakura Art Museum today."),
            ("F", "館内では、写真を撮ってもかまいませんが、フラッシュは使わないでください。また、作品には手を触れないようにお願いします。",
             "You may take photos inside the museum, but please don't use a flash. Also, please don't touch the works."),
            ("F", "なお、二階のカフェは、本日は午後三時までとなっております。",
             "Please note that the café on the second floor is open until 3 p.m. today."),
        ],
        "question": "係の人は、何について話していますか。",
        "intro_en": "At an art museum, a staff member is speaking.",
        "question_en": "What is the staff member talking about?",
        "choices": ["美術館の歴史", "美術館で守ってほしいこと", "新しい作品の紹介", "カフェのメニュー"],
        "choices_en": ["The museum's history", "Rules visitors should follow in the museum",
                       "Introducing new works", "The café menu"],
        "answer": 1,
        "why": "Most of the talk is about rules: no flash, don't touch the works. The café hours are only an added note (なお).",
        "vocab": [
            {"word": "美術館", "reading": "びじゅつかん", "meaning": "art museum"},
            {"word": "作品", "reading": "さくひん", "meaning": "work (of art)"},
            {"word": "触れる", "reading": "ふれる", "meaning": "to touch"},
            {"word": "館内", "reading": "かんない", "meaning": "inside the building"},
        ],
    },
    {
        "id": "n3-l18",
        "title": "Why he runs",
        "kind": "summary",
        "intro": "男の人が、自分の趣味について話しています。",
        "lines": [
            ("M", "私は三年前から、毎週末に走っています。始めたのは、健康のためでした。",
             "I've been running every weekend for three years. I started for my health."),
            ("M", "最初は五分走るだけで疲れてしまいましたが、少しずつ距離を伸ばして、去年は初めてマラソン大会に出ました。",
             "At first I was tired after running for just five minutes, but I gradually increased the distance, and last year I ran in a marathon for the first time."),
            ("M", "でも、今は記録よりも、走りながら町の景色を見るのが楽しみなんです。",
             "But these days, rather than my time, what I enjoy is looking at the town as I run."),
        ],
        "question": "男の人は、今、どんな気持ちで走っていますか。",
        "intro_en": "A man is talking about his hobby.",
        "question_en": "How does the man feel about running now?",
        "choices": [
            "健康のために、しかたなく走っている。",
            "マラソン大会で、いい記録を出したい。",
            "景色を楽しみながら走りたい。",
            "疲れるので、もうやめたい。",
        ],
        "choices_en": ["He runs for his health because he has to.", "He wants a good time in a marathon.",
                       "He wants to enjoy the scenery while running.", "He wants to stop because it's tiring."],
        "answer": 2,
        "why": "He started for his health, but 今は記録よりも…景色を見るのが楽しみ: now he enjoys the scenery more than his time.",
        "vocab": [
            {"word": "距離", "reading": "きょり", "meaning": "distance"},
            {"word": "伸ばす", "reading": "のばす", "meaning": "to extend, increase"},
            {"word": "大会", "reading": "たいかい", "meaning": "competition, tournament"},
            {"word": "記録", "reading": "きろく", "meaning": "record, (race) time"},
        ],
    },
    {
        "id": "n3-l19",
        "title": "Borrowing a pen",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "すみません、ちょっとペンを貸してもらえませんか。", "Excuse me, could you lend me a pen for a moment?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["ええ、どうぞ使ってください。", "いいえ、借りてもいいですよ。", "はい、貸してもらいました。"],
        "choices_en": ["Sure, please use it.", "No, you may borrow it.", "Yes, I was lent one."],
        "answer": 0,
        "why": "〜てもらえませんか asks a favour, so ええ、どうぞ使ってください agrees to lend it. The other replies mix up "
               "lending and borrowing (貸す / 借りる).",
        "vocab": [
            {"word": "貸す", "reading": "かす", "meaning": "to lend"},
            {"word": "借りる", "reading": "かりる", "meaning": "to borrow"},
        ],
    },
    {
        "id": "n3-l20",
        "title": "A heavy bag",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "その荷物、重そうだね。持とうか。", "That bag looks heavy. Shall I carry it?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["ありがとう。じゃあ、お願い。", "うん、重くないみたいだね。", "ううん、持ってもらおうか。"],
        "choices_en": ["Thanks. Then, please.", "Yeah, it doesn't seem heavy.", "No, shall I have it carried?"],
        "answer": 0,
        "why": "持とうか offers help, so ありがとう。じゃあ、お願い accepts it. The second reply comments on someone else's bag, "
               "and the third makes no sense as an answer to an offer.",
        "vocab": [
            {"word": "荷物", "reading": "にもつ", "meaning": "luggage, bag"},
            {"word": "重そう", "reading": "おもそう", "meaning": "looks heavy"},
        ],
    },
    # ------------------------------------------------------------------ N2
    {
        "id": "n2-l01",
        "title": "A scholarship application",
        "kind": "task",
        "intro": "大学の事務室で、男の学生と職員が話しています。男の学生は、このあとまず何をしなければなりませんか。",
        "lines": [
            ("M", "すみません、奨学金の申請書を出しに来たんですが。", "Excuse me, I've come to hand in my scholarship application."),
            ("F", "はい、拝見します。……あ、推薦書がまだ入っていませんね。", "Certainly, let me see... Ah, the letter of recommendation isn't included yet."),
            ("M", "推薦書は指導教員の先生に頼んであるんですが、まだいただいていなくて。締め切りは金曜日でしたよね。",
             "I've asked my supervisor for it, but I haven't received it yet. The deadline was Friday, wasn't it?"),
            ("F", "ええ。推薦書は、先生から直接こちらに送っていただくこともできますので、それは大丈夫です。ただ、こちらの申請書、署名が抜けていますね。",
             "Yes. The teacher can also send the recommendation directly to us, so that's fine. But this application form is missing your signature."),
            ("M", "あ、本当だ。", "Oh, you're right."),
            ("F", "それと、成績証明書は、二階の窓口で発行してもらってください。こちらは今日中にお願いします。",
             "Also, please get your transcript issued at the counter on the second floor. We need that today."),
            ("M", "分かりました。じゃあ、ここで署名してから、すぐ行ってきます。", "I see. Then I'll sign here and go right away."),
        ],
        "question": "男の学生は、このあとまず何をしなければなりませんか。",
        "intro_en": "In a university office, a male student and a staff member are talking. What must the student do first after this?",
        "question_en": "What must the student do first after this?",
        "choices": ["先生に推薦書を頼む", "申請書に署名する", "成績証明書をもらいに行く", "推薦書を事務室に送る"],
        "answer": 1,
        "why": "He'll sign first and then go for the transcript (ここで署名してから、すぐ行ってきます). The recommendation is "
               "already requested, and the teacher can send it directly.",
        "vocab": [
            {"word": "奨学金", "reading": "しょうがくきん", "meaning": "scholarship"},
            {"word": "申請書", "reading": "しんせいしょ", "meaning": "application form"},
            {"word": "推薦書", "reading": "すいせんしょ", "meaning": "letter of recommendation"},
            {"word": "署名", "reading": "しょめい", "meaning": "signature"},
            {"word": "成績証明書", "reading": "せいせきしょうめいしょ", "meaning": "transcript (of grades)"},
            {"word": "窓口", "reading": "まどぐち", "meaning": "counter, window"},
        ],
    },
    {
        "id": "n2-l02",
        "title": "A farewell present",
        "kind": "task",
        "intro": "女の人と男の人が、友達へのプレゼントについて話しています。二人は、何をプレゼントすることにしましたか。",
        "lines": [
            ("F", "来月、佐藤さんが国に帰っちゃうでしょう。みんなで何かプレゼントしようよ。",
             "Sato is going back home next month, right? Let's all give something as a present."),
            ("M", "いいね。何がいいかな。日本らしい物がいいよね。扇子とか。", "Good idea. What would be good? Something very Japanese. A folding fan, maybe."),
            ("F", "扇子もいいけど、佐藤さん、荷物が多くて困ってるって言ってたよ。大きい物や重い物は、避けたほうがいいかも。",
             "A fan's nice, but Sato said they're struggling with too much luggage. Maybe we should avoid anything big or heavy."),
            ("M", "そうか。じゃあ、食べ物は？日本のお菓子とか。", "I see. Then what about food? Japanese sweets or something."),
            ("F", "うーん、すぐなくなっちゃうし、残る物のほうがいいんじゃない？みんなで書いたメッセージカードと、写真を入れた小さいアルバムはどう？",
             "Hmm, they'd be gone in no time. Wouldn't something that lasts be better? How about a message card we all write, and a small photo album?"),
            ("M", "それなら軽いし、いいね。そうしよう。", "That's light too. Great, let's do that."),
        ],
        "question": "二人は、何をプレゼントすることにしましたか。",
        "intro_en": "A woman and a man are talking about a present for a friend. What have they decided to give?",
        "question_en": "What have they decided to give?",
        "choices": ["扇子", "日本のお菓子", "メッセージカードとアルバム", "大きい置物"],
        "answer": 2,
        "why": "The fan is ruled out (avoid luggage), sweets don't last (すぐなくなっちゃう), and he agrees to the card and "
               "small album: そうしよう.",
        "vocab": [
            {"word": "扇子", "reading": "せんす", "meaning": "folding fan"},
            {"word": "避ける", "reading": "さける", "meaning": "to avoid"},
            {"word": "残る", "reading": "のこる", "meaning": "to remain, last"},
            {"word": "日本らしい", "reading": "にほんらしい", "meaning": "typically Japanese"},
        ],
    },
    {
        "id": "n2-l03",
        "title": "Why she's moving",
        "kind": "point",
        "intro": "男の人と女の人が話しています。女の人が引っ越すことにした一番の理由は何ですか。",
        "lines": [
            ("M", "引っ越すんだって？今のマンション、駅から近くて便利だって言ってたじゃない。",
             "I hear you're moving? You said your flat was handy, close to the station."),
            ("F", "うん、便利なのは確かなんだけどね。", "Yes, it's definitely convenient."),
            ("M", "家賃が上がったとか？", "Did the rent go up or something?"),
            ("F", "それもちょっとはあるけど、それより、隣の部屋の人が夜遅くまで音楽をかけてて、全然眠れないの。"
                  "管理会社にも何度か相談したんだけど、なかなか改善されなくて。",
             "That's a small part of it, but more than that, the person next door plays music late at night and I can't sleep at all. "
             "I've talked to the management company several times, but nothing really improves."),
            ("M", "それはつらいね。", "That sounds tough."),
            ("F", "次の部屋は、駅から少し遠くなるけど、静かな所を選んだんだ。", "My next place is a bit further from the station, but I chose somewhere quiet."),
        ],
        "question": "女の人が引っ越すことにした一番の理由は何ですか。",
        "intro_en": "A man and a woman are talking. What is the main reason the woman decided to move?",
        "question_en": "What is the main reason the woman decided to move?",
        "choices": ["駅から遠いから", "家賃が上がったから", "隣の部屋がうるさいから", "管理会社が親切じゃないから"],
        "answer": 2,
        "why": "The rent is only a small part (ちょっとはある); それより (more than that) the neighbour's late-night music keeps "
               "her awake.",
        "vocab": [
            {"word": "改善", "reading": "かいぜん", "meaning": "improvement"},
            {"word": "管理会社", "reading": "かんりがいしゃ", "meaning": "property management company"},
            {"word": "つらい", "reading": "つらい", "meaning": "hard, painful"},
            {"word": "それより", "reading": "それより", "meaning": "more than that"},
        ],
    },
    {
        "id": "n2-l04",
        "title": "Worried about the presentation",
        "kind": "point",
        "intro": "男の学生と女の学生が、発表について話しています。男の学生が一番心配していることは何ですか。",
        "lines": [
            ("F", "明日の発表、準備はどう？", "How's the preparation for tomorrow's presentation?"),
            ("M", "資料はもうできてるし、練習も何回もしたんだ。", "The materials are done, and I've practised lots of times."),
            ("F", "じゃあ、大丈夫じゃない。", "Then you'll be fine, won't you?"),
            ("M", "うん、発表自体は何とかなると思う。ただ、そのあとの質問の時間がね。先生たち、けっこう厳しい質問をするらしいから、"
                  "うまく答えられるか自信がなくて。",
             "Yeah, I think the presentation itself will be OK. It's the question time afterwards. Apparently the teachers ask pretty "
             "tough questions, so I'm not confident I can answer well."),
            ("F", "そっか。じゃあ、聞かれそうな質問を、一緒に考えてみようか。", "I see. Then shall we think up some likely questions together?"),
            ("M", "本当？助かるよ。", "Really? That'd be a big help."),
        ],
        "question": "男の学生が一番心配していることは何ですか。",
        "intro_en": "A male student and a female student are talking about a presentation. What is the male student most worried about?",
        "question_en": "What is the male student most worried about?",
        "choices": ["資料がまだできていないこと", "発表の練習が足りないこと", "質問にうまく答えられるかどうか", "発表の時間が短いこと"],
        "answer": 2,
        "why": "The materials and practice are done, and the presentation itself will be fine (何とかなる); ただ (but) the "
               "question time worries him.",
        "vocab": [
            {"word": "自体", "reading": "じたい", "meaning": "itself"},
            {"word": "何とかなる", "reading": "なんとかなる", "meaning": "to work out somehow"},
            {"word": "自信", "reading": "じしん", "meaning": "confidence"},
            {"word": "けっこう", "reading": "けっこう", "meaning": "quite, fairly"},
        ],
    },
    {
        "id": "n2-l05",
        "title": "The baker's secret",
        "kind": "point",
        "intro": "ラジオで、アナウンサーとパン屋の主人が話しています。パン屋の主人が、パン作りで一番大切にしていることは何ですか。",
        "lines": [
            ("F", "このお店のパンは、毎朝すぐに売り切れてしまうそうですね。人気の秘密は何でしょうか。",
             "I hear the bread here sells out quickly every morning. What's the secret of its popularity?"),
            ("M", "そうですね、材料にはこだわっています。小麦粉は、近くの農家から直接買っているんです。",
             "Well, I'm particular about ingredients. I buy flour directly from a nearby farm."),
            ("F", "なるほど。", "I see."),
            ("M", "でも、一番大切にしているのは、毎日同じ味を出すことなんです。その日の気温や湿度によって生地の状態が変わりますから、"
                  "毎朝確かめながら、水の量や焼く時間を少しずつ変えているんですよ。",
             "But what I value most is making it taste the same every day. The dough changes with the day's temperature and humidity, "
             "so every morning I check it and adjust the amount of water and the baking time a little."),
            ("F", "毎日同じ味にするために、毎日やり方を変えているんですね。", "So you change your method every day in order to keep the taste the same every day."),
        ],
        "question": "パン屋の主人が、パン作りで一番大切にしていることは何ですか。",
        "intro_en": "On the radio, an announcer and a baker are talking. What does the baker value most in making bread?",
        "question_en": "What does the baker value most in making bread?",
        "choices": ["近くの農家から材料を買うこと", "毎日同じ味のパンを作ること", "毎朝早く店を開けること", "新しいパンを次々に作ること"],
        "answer": 1,
        "why": "Ingredients matter, but でも、一番大切にしているのは、毎日同じ味を出すこと.",
        "vocab": [
            {"word": "売り切れる", "reading": "うりきれる", "meaning": "to sell out"},
            {"word": "こだわる", "reading": "こだわる", "meaning": "to be particular about"},
            {"word": "小麦粉", "reading": "こむぎこ", "meaning": "flour"},
            {"word": "湿度", "reading": "しつど", "meaning": "humidity"},
            {"word": "生地", "reading": "きじ", "meaning": "dough"},
            {"word": "確かめる", "reading": "たしかめる", "meaning": "to check, make sure"},
        ],
    },
    {
        "id": "n2-l06",
        "title": "Paper books and e-books",
        "kind": "summary",
        "intro": "テレビで、専門家が話しています。",
        "lines": [
            ("M", "最近は、電子書籍で本を読む人が増えています。たくさんの本を持ち歩けますし、夜でも明かりなしで読めるので、とても便利です。",
             "More and more people read e-books these days. You can carry lots of books around and read at night without a light, "
             "so they're very convenient."),
            ("M", "一方で、紙の本には、ページをめくりながら、どのくらい読んだかが目で分かるという良さがあります。内容を覚えやすいという研究もあるんです。",
             "On the other hand, paper books have the advantage that as you turn the pages, you can see how far you've read. Some "
             "research even says the content is easier to remember."),
            ("M", "ですから、どちらが優れているかではなく、目的に合わせて選ぶことが大切だと思います。たとえば、移動中は電子書籍、"
                  "じっくり勉強したいときは紙の本、というようにです。",
             "So I think the important thing isn't which is better, but choosing to suit your purpose. For example, e-books while "
             "travelling, and paper books when you want to study properly."),
        ],
        "question": "専門家が、一番言いたいことは何ですか。",
        "intro_en": "On TV, an expert is speaking.",
        "question_en": "What does the expert most want to say?",
        "choices": [
            "電子書籍のほうが、紙の本より便利だ。",
            "紙の本のほうが、内容を覚えやすい。",
            "目的に合わせて、電子書籍と紙の本を使い分けるといい。",
            "移動中は、本を読まないほうがいい。",
        ],
        "choices_en": [
            "E-books are more convenient than paper books.",
            "Content is easier to remember from paper books.",
            "It's good to choose between e-books and paper books to suit your purpose.",
            "You shouldn't read while travelling.",
        ],
        "answer": 2,
        "why": "ですから introduces the conclusion: どちらが優れているかではなく、目的に合わせて選ぶことが大切. "
               "Choices 1 and 2 are only one side each.",
        "vocab": [
            {"word": "専門家", "reading": "せんもんか", "meaning": "expert"},
            {"word": "電子書籍", "reading": "でんししょせき", "meaning": "e-book"},
            {"word": "持ち歩く", "reading": "もちあるく", "meaning": "to carry around"},
            {"word": "めくる", "reading": "めくる", "meaning": "to turn (pages)"},
            {"word": "優れる", "reading": "すぐれる", "meaning": "to be excellent, superior"},
            {"word": "じっくり", "reading": "じっくり", "meaning": "carefully, taking one's time"},
        ],
    },
    {
        "id": "n2-l07",
        "title": "Bringing the shopping street back",
        "kind": "summary",
        "intro": "町の集まりで、女の人が話しています。",
        "lines": [
            ("F", "駅前の商店街は、十年ほど前から、閉まったままの店が増えてきました。大きなショッピングセンターができて、お客さんがそちらに行ってしまったからです。",
             "For about ten years, more and more shops on the shopping street by the station have stayed closed. A big shopping "
             "centre opened, and customers went there instead."),
            ("F", "そこで、私たちは去年から、空いている店を若い人に安く貸すことにしました。すると、カフェや雑貨の店が次々に開いて、"
                  "今では週末になると、町の外からも人が来るようになりました。",
             "So from last year, we decided to rent the empty shops cheaply to young people. Then cafés and gift shops opened one "
             "after another, and now people come from outside the town at weekends."),
            ("F", "まだ課題はありますが、町の人と新しい人が協力すれば、商店街はもう一度にぎやかになると信じています。",
             "There are still problems, but I believe that if the townspeople and the newcomers work together, the shopping street "
             "will be lively again."),
        ],
        "question": "女の人は、何について話していますか。",
        "intro_en": "At a town meeting, a woman is speaking.",
        "question_en": "What is the woman talking about?",
        "choices": [
            "ショッピングセンターの便利さ",
            "商店街を元気にするための取り組み",
            "カフェの開き方",
            "町の外から来る人の問題",
        ],
        "choices_en": [
            "How convenient the shopping centre is",
            "The effort to bring the shopping street back to life",
            "How to open a café",
            "Problems with people from outside the town",
        ],
        "answer": 1,
        "why": "The whole talk is about reviving the street: the problem, renting shops to young people, the results, and her hopes.",
        "vocab": [
            {"word": "商店街", "reading": "しょうてんがい", "meaning": "shopping street"},
            {"word": "雑貨", "reading": "ざっか", "meaning": "miscellaneous goods, gifts"},
            {"word": "課題", "reading": "かだい", "meaning": "issue, challenge"},
            {"word": "取り組み", "reading": "とりくみ", "meaning": "effort, initiative"},
            {"word": "にぎやか", "reading": "にぎやか", "meaning": "lively, busy"},
        ],
    },
    {
        "id": "n2-l08",
        "title": "Out when you came",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "せっかく来てくれたのに、留守にしててごめんね。", "Sorry I was out when you went to the trouble of coming.")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": [
            "ううん、こっちこそ、連絡しないで来ちゃってごめん。",
            "うん、留守にしてくれてありがとう。",
            "せっかくだから、留守にしようか。",
        ],
        "choices_en": [
            "No, I'm the one who should apologise for turning up without calling.",
            "Yes, thanks for being out.",
            "Since we have the chance, shall we go out?",
        ],
        "answer": 0,
        "why": "She apologises for being out, so the natural reply apologises back: こっちこそ…ごめん (I'm the one who's sorry).",
        "vocab": [
            {"word": "せっかく", "reading": "せっかく", "meaning": "going to the trouble; rare chance"},
            {"word": "留守", "reading": "るす", "meaning": "being out, away from home"},
            {"word": "こっちこそ", "reading": "こっちこそ", "meaning": "I'm the one (who should...)"},
        ],
    },
    {
        "id": "n2-l09",
        "title": "Looking over the materials",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "この資料、明日まででいいから、目を通しておいてくれる？", "Could you look over these materials? Tomorrow is fine.")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["はい、明日までに読んでおきます。", "はい、明日、目を通してもらいます。", "いいえ、まだ読んでもらっていません。"],
        "choices_en": ["Sure, I'll read them by tomorrow.", "Sure, I'll have someone look them over tomorrow.",
                       "No, nobody has read them for me yet."],
        "answer": 0,
        "why": "目を通す means to look over, and 〜ておいてくれる？ asks the listener to do it, so 読んでおきます. "
               "The other two replies have someone else doing the reading (〜てもらう).",
        "vocab": [
            {"word": "目を通す", "reading": "めをとおす", "meaning": "to look over, skim"},
            {"word": "資料", "reading": "しりょう", "meaning": "materials, documents"},
        ],
    },
    {
        "id": "n2-l10",
        "title": "Choosing a cooking course",
        "kind": "integrated",
        "intro": "料理教室の受付で、係の人が説明しています。それから、女の人と男の人が話します。",
        "lines": [
            ("S", "当教室には、三つのコースがございます。", "Our school offers three courses."),
            ("S", "まず、Aコースは「和食の基本」です。だしの取り方から始めて、毎回一品ずつ家庭料理を作ります。土曜日の午前中です。",
             "First, Course A is Japanese cooking basics. We start with making dashi stock and cook one home-style dish each time. "
             "It's on Saturday mornings."),
            ("S", "Bコースは「パン作り」です。少人数のクラスで、焼きたてのパンを持って帰れます。平日の夜七時からです。",
             "Course B is bread making. It's a small class, and you can take home freshly baked bread. It's on weekday evenings from 7."),
            ("S", "Cコースは「世界の料理」です。毎月、違う国の料理を作ります。日曜日の午後です。",
             "Course C is world cuisine. Each month we cook food from a different country. It's on Sunday afternoons."),
            ("F", "どれもおもしろそうだね。私、平日の夜はアルバイトがあるから、週末がいいな。",
             "They all sound fun. I have my part-time job on weekday evenings, so the weekend would be best."),
            ("M", "じゃあ、AかCだね。", "Then it's A or C."),
            ("F", "うん。いろいろな国の料理も楽しそうだけど、まずは基本からちゃんと覚えたいんだよね。毎日のご飯を、自分で作れるようになりたいから。",
             "Yes. Food from different countries sounds fun too, but I want to learn the basics properly first. I want to be able to "
             "cook my everyday meals myself."),
            ("M", "それなら、決まりだね。僕は、焼きたてのパンを持って帰れるのがいいな。夜なら行けるし。",
             "Then that settles it. For me, taking home freshly baked bread sounds good. I can go in the evenings, too."),
        ],
        "question": "女の人は、どのコースに申し込みますか。",
        "intro_en": "At the reception of a cooking school, a staff member is explaining. Then a woman and a man talk.",
        "question_en": "Which course will the woman sign up for?",
        "choices": ["Aコース", "Bコース", "Cコース", "どのコースにも申し込まない"],
        "answer": 0,
        "why": "She can only do weekends (A or C), and wants the basics first (まずは基本からちゃんと覚えたい): Course A. "
               "Course B is the man's choice.",
        "vocab": [
            {"word": "和食", "reading": "わしょく", "meaning": "Japanese cuisine"},
            {"word": "一品", "reading": "いっぴん", "meaning": "one dish"},
            {"word": "少人数", "reading": "しょうにんずう", "meaning": "small number of people"},
            {"word": "焼きたて", "reading": "やきたて", "meaning": "freshly baked"},
            {"word": "基本", "reading": "きほん", "meaning": "basics"},
            {"word": "決まり", "reading": "きまり", "meaning": "settled, decided"},
        ],
    },
    {
        "id": "n2-l11",
        "title": "An umbrella left on the train",
        "kind": "task",
        "intro": "駅で、女の人と駅員が話しています。女の人は、このあとまず何をしますか。",
        "lines": [
            ("F", "すみません、さっき乗った電車に、傘を忘れてしまったんですが。", "Excuse me, I left my umbrella on the train I was just on."),
            ("M", "何時ごろの、どちら行きの電車ですか。", "What time was it, and where was it going?"),
            ("F", "十時十五分発の、みなみ駅行きです。前から三両目に乗っていました。",
             "The 10:15 to Minami Station. I was in the third car from the front."),
            ("M", "少々お待ちください。……終点のみなみ駅で、青い傘が見つかったそうです。お客様のものでしょうか。",
             "One moment, please... A blue umbrella has been found at Minami Station, the last stop. Could it be yours?"),
            ("F", "あ、たぶんそれです。", "Oh, that's probably it."),
            ("M", "では、みなみ駅の窓口で受け取れます。その際、こちらの用紙に名前と連絡先を書いていただく必要があります。"
                  "先にここで書いていかれますか。そのほうが、向こうでの手続きが早く済みますよ。",
             "Then you can collect it at the Minami Station counter. You'll need to write your name and contact details on this "
             "form. Would you like to fill it in here first? That way the procedure there will be quicker."),
            ("F", "じゃあ、今書きます。", "Then I'll write it now."),
        ],
        "question": "女の人は、このあとまず何をしますか。",
        "intro_en": "At a station, a woman and a station attendant are talking. What will the woman do first after this?",
        "question_en": "What will the woman do first after this?",
        "choices": ["みなみ駅へ行く", "用紙に名前と連絡先を書く", "電車に乗って傘を探す", "窓口で傘を受け取る"],
        "answer": 1,
        "why": "She'll fill in the form here first (じゃあ、今書きます), then go to Minami Station to collect the umbrella.",
        "vocab": [
            {"word": "終点", "reading": "しゅうてん", "meaning": "last stop, terminus"},
            {"word": "受け取る", "reading": "うけとる", "meaning": "to receive, collect"},
            {"word": "用紙", "reading": "ようし", "meaning": "form (to fill in)"},
            {"word": "手続き", "reading": "てつづき", "meaning": "procedure, formalities"},
            {"word": "済む", "reading": "すむ", "meaning": "to be finished, done"},
            {"word": "少々", "reading": "しょうしょう", "meaning": "a little (polite)"},
        ],
    },
    {
        "id": "n2-l12",
        "title": "Tidying up before a visit",
        "kind": "task",
        "intro": "家で、男の人と女の人が話しています。男の人は、このあと何をしますか。",
        "lines": [
            ("F", "明日、両親が来るから、今日中に部屋を片付けないと。", "My parents are coming tomorrow, so we need to tidy up today."),
            ("M", "そうだね。僕は何をすればいい？掃除機をかけようか。", "Right. What should I do? Shall I vacuum?"),
            ("F", "掃除機は、さっき私がかけたからいいよ。それより、玄関に置いてある段ボールを外に出してくれる？",
             "I already vacuumed, so that's fine. More importantly, could you take the cardboard boxes in the entrance outside?"),
            ("M", "いいよ。あ、でも、段ボールのごみの日って、明日の朝じゃなかった？", "Sure. Oh, but isn't cardboard collection tomorrow morning?"),
            ("F", "そうだった。じゃあ、それは明日の朝にして、今日は台所の食器を洗ってくれる？",
             "That's right. Then leave that for tomorrow morning, and could you wash the dishes in the kitchen today?"),
            ("M", "分かった。", "Got it."),
        ],
        "question": "男の人は、このあと何をしますか。",
        "intro_en": "At home, a man and a woman are talking. What will the man do after this?",
        "question_en": "What will the man do after this?",
        "choices": ["掃除機をかける", "段ボールを外に出す", "食器を洗う", "ごみを捨てに行く"],
        "answer": 2,
        "why": "The vacuuming is done, and the cardboard waits for collection day tomorrow. Today he'll wash the dishes "
               "(今日は台所の食器を洗ってくれる？ / 分かった).",
        "vocab": [
            {"word": "片付ける", "reading": "かたづける", "meaning": "to tidy up"},
            {"word": "掃除機", "reading": "そうじき", "meaning": "vacuum cleaner"},
            {"word": "段ボール", "reading": "だんボール", "meaning": "cardboard (box)"},
            {"word": "食器", "reading": "しょっき", "meaning": "dishes, tableware"},
        ],
    },
    {
        "id": "n2-l13",
        "title": "Learning the piano again",
        "kind": "point",
        "intro": "女の人と男の人が話しています。男の人がピアノを習い始めた一番の理由は何ですか。",
        "lines": [
            ("F", "最近、ピアノを習い始めたんだって？", "I hear you've started piano lessons recently?"),
            ("M", "うん。子供のころ少しやってたんだけど、すぐにやめちゃって。", "Yeah. I did a bit as a kid, but I quit quickly."),
            ("F", "昔から、やりたかったの？", "Have you always wanted to?"),
            ("M", "それもあるけど、きっかけは娘なんだ。娘が保育園で歌を習ってきて、家でも毎日歌うんだよ。"
                  "それに合わせて弾いてあげたら、喜ぶかなと思って。",
             "That's part of it, but my daughter was what started it. She learns songs at nursery and sings them at home every day. "
             "I thought she'd be happy if I played along with her."),
            ("F", "すてきなお父さんだね。", "What a lovely dad."),
            ("M", "まだ全然弾けないけどね。", "I can't play at all yet, though."),
        ],
        "question": "男の人がピアノを習い始めた一番の理由は何ですか。",
        "intro_en": "A woman and a man are talking. What is the main reason the man started learning the piano?",
        "question_en": "What is the main reason the man started learning the piano?",
        "choices": ["子供のころの夢だったから", "娘の歌に合わせて弾きたいから", "保育園の先生に頼まれたから", "健康にいいと聞いたから"],
        "answer": 1,
        "why": "Wanting to play is only part of it (それもあるけど); きっかけは娘: he wants to play along with his daughter's songs.",
        "vocab": [
            {"word": "娘", "reading": "むすめ", "meaning": "daughter"},
            {"word": "保育園", "reading": "ほいくえん", "meaning": "nursery school"},
            {"word": "合わせる", "reading": "あわせる", "meaning": "to match, go along with"},
            {"word": "弾く", "reading": "ひく", "meaning": "to play (piano, guitar)"},
        ],
    },
    {
        "id": "n2-l14",
        "title": "Autumn in Kyoto",
        "kind": "point",
        "intro": "男の人と女の人が、旅行について話しています。女の人が一番残念だったことは何ですか。",
        "lines": [
            ("M", "京都の旅行、どうだった？", "How was your trip to Kyoto?"),
            ("F", "楽しかったよ。お寺もきれいだったし、料理もおいしかった。", "It was fun. The temples were beautiful, and the food was delicious."),
            ("M", "人が多かったんじゃない？", "Wasn't it crowded?"),
            ("F", "うん、どこも混んでたけど、それは覚悟してたから。ただ、楽しみにしてた紅葉が、今年は暖かかったせいで、まだほとんど色づいてなかったの。",
             "Yes, it was crowded everywhere, but I'd expected that. The thing is, the autumn leaves I'd been looking forward to had "
             "barely changed colour, because it's been warm this year."),
            ("M", "ああ、それは残念だったね。", "Ah, that's a shame."),
            ("F", "来年、もう一度行こうと思ってる。", "I'm thinking of going again next year."),
        ],
        "question": "女の人が一番残念だったことは何ですか。",
        "intro_en": "A man and a woman are talking about a trip. What was the woman most disappointed about?",
        "question_en": "What was the woman most disappointed about?",
        "choices": ["人が多かったこと", "料理がおいしくなかったこと", "紅葉がまだ色づいていなかったこと", "お寺が工事中だったこと"],
        "answer": 2,
        "why": "The crowds were expected (覚悟してた); ただ (but) the autumn leaves hadn't changed colour yet because of the warm weather.",
        "vocab": [
            {"word": "覚悟", "reading": "かくご", "meaning": "being prepared (for something bad)"},
            {"word": "紅葉", "reading": "こうよう", "meaning": "autumn leaves"},
            {"word": "色づく", "reading": "いろづく", "meaning": "to change colour"},
            {"word": "寺", "reading": "てら", "meaning": "temple"},
        ],
    },
    {
        "id": "n2-l15",
        "title": "What time does the bus leave?",
        "kind": "point",
        "intro": "旅行会社の人が、ツアーの参加者に話しています。バスは何時に出発しますか。",
        "lines": [
            ("F", "皆さん、お疲れさまでした。これから一時間、自由時間です。ただ今十一時ですので、十二時にこの駐車場に戻ってきてください。",
             "Thank you, everyone. You now have an hour of free time. It's eleven o'clock now, so please come back to this car park at twelve."),
            ("F", "あ、失礼しました。先ほど連絡があって、この先の道が工事で混んでいるそうです。予定より十五分早く出発したいので、"
                  "集合は十一時四十五分にお願いします。",
             "Oh, I'm sorry. I've just heard that the road ahead is congested because of roadworks. We'd like to leave fifteen "
             "minutes earlier than planned, so please gather at 11:45."),
            ("F", "出発は、集合の五分後です。遅れないようにお願いします。", "We'll leave five minutes after we gather. Please don't be late."),
        ],
        "question": "バスは何時に出発しますか。",
        "intro_en": "A tour guide is speaking to the people on a tour. What time will the bus leave?",
        "question_en": "What time will the bus leave?",
        "choices": ["11時45分", "11時50分", "12時", "12時15分"],
        "answer": 1,
        "why": "Twelve becomes a 11:45 gathering time, and 出発は、集合の五分後: departure at 11:50.",
        "vocab": [
            {"word": "自由時間", "reading": "じゆうじかん", "meaning": "free time"},
            {"word": "集合", "reading": "しゅうごう", "meaning": "gathering, meeting up"},
            {"word": "先ほど", "reading": "さきほど", "meaning": "a little while ago"},
            {"word": "駐車場", "reading": "ちゅうしゃじょう", "meaning": "car park"},
        ],
    },
    {
        "id": "n2-l16",
        "title": "Letting go of things",
        "kind": "summary",
        "intro": "ラジオで、男の人が話しています。",
        "lines": [
            ("M", "部屋が片付かないという悩みを、よく聞きます。片付けられない人の多くは、物を捨てるのが苦手です。「いつか使うかもしれない」と思ってしまうんですね。",
             "I often hear people worry that their room is never tidy. Many people who can't tidy up are bad at throwing things "
             "away. They think, \"I might use it someday.\""),
            ("M", "そこでおすすめしたいのが、「一年使わなかった物は、これからも使わない」と考えることです。迷ったら箱に入れておいて、"
                  "一年後にもう一度見てみてください。ほとんどの物は、なくても困らなかったと気づくはずです。",
             "So what I recommend is thinking, \"If I haven't used it for a year, I won't use it in future either.\" If you're unsure, "
             "put it in a box and look again a year later. You'll probably find you didn't miss most of the things at all."),
            ("M", "物が減ると、掃除も楽になり、本当に大切な物が何なのか見えてきますよ。",
             "With fewer things, cleaning gets easier, and you start to see what really matters to you."),
        ],
        "question": "男の人は、何について話していますか。",
        "intro_en": "On the radio, a man is speaking.",
        "question_en": "What is the man talking about?",
        "choices": ["掃除が楽になる道具", "物を上手に減らす方法", "箱の上手な使い方", "大切な物の買い方"],
        "choices_en": ["Tools that make cleaning easier", "How to cut down on your things well",
                       "Clever ways to use boxes", "How to buy things that matter"],
        "answer": 1,
        "why": "The whole talk is a method for throwing things away (the one-year rule). The box is just one step of it.",
        "vocab": [
            {"word": "悩み", "reading": "なやみ", "meaning": "worry, problem"},
            {"word": "片付く", "reading": "かたづく", "meaning": "to be tidy, sorted"},
            {"word": "おすすめ", "reading": "おすすめ", "meaning": "recommendation"},
            {"word": "気づく", "reading": "きづく", "meaning": "to notice, realise"},
        ],
    },
    {
        "id": "n2-l17",
        "title": "Welcome to university",
        "kind": "summary",
        "intro": "大学の入学式で、先生が新入生に話しています。",
        "lines": [
            ("F", "皆さん、ご入学おめでとうございます。大学では、高校までと違って、何を学ぶかを自分で決めなければなりません。時間割も、自分で作ります。",
             "Congratulations on starting university. Unlike up to high school, at university you have to decide for yourselves "
             "what to study. You even make your own timetable."),
            ("F", "自由な分、何もしなければ、何も身につかないまま四年間が過ぎてしまうこともあります。",
             "Because you're free, if you do nothing, four years can go by without you learning anything."),
            ("F", "興味のあることがあれば、授業以外でも、どんどん挑戦してください。分からないことがあれば、遠慮しないで先生や先輩に聞いてください。",
             "If something interests you, take it on, even outside your classes. And if there's anything you don't understand, "
             "don't hesitate to ask your teachers or older students."),
        ],
        "question": "先生が、一番伝えたいことは何ですか。",
        "intro_en": "At a university entrance ceremony, a teacher is speaking to the new students.",
        "question_en": "What does the teacher most want to convey?",
        "choices": [
            "大学の時間割の作り方",
            "大学では、自分から積極的に学ぶことが大切だ。",
            "先輩と仲良くしたほうがいい。",
            "四年間で卒業するのは難しい。",
        ],
        "choices_en": ["How to make a university timetable", "At university, it's important to learn actively on your own initiative.",
                       "You should get on well with older students.", "It's hard to graduate in four years."],
        "answer": 1,
        "why": "Freedom means nothing happens unless you act, so take things on and ask questions: learn actively.",
        "vocab": [
            {"word": "入学式", "reading": "にゅうがくしき", "meaning": "entrance ceremony"},
            {"word": "新入生", "reading": "しんにゅうせい", "meaning": "new student"},
            {"word": "時間割", "reading": "じかんわり", "meaning": "timetable"},
            {"word": "遠慮", "reading": "えんりょ", "meaning": "holding back, hesitation"},
            {"word": "先輩", "reading": "せんぱい", "meaning": "senior (older student)"},
            {"word": "積極的", "reading": "せっきょくてき", "meaning": "active, proactive"},
        ],
    },
    {
        "id": "n2-l18",
        "title": "Sorry for missing practice",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "この前は、急に休んでしまって、すみませんでした。", "I'm sorry I suddenly missed it last time.")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["いいえ、体はもう大丈夫ですか。", "はい、休んでもかまいませんよ。", "いいえ、急がなくてもいいですよ。"],
        "choices_en": ["Not at all. Are you feeling better now?", "Yes, it's fine to take the day off.",
                       "No, you don't need to hurry."],
        "answer": 0,
        "why": "She apologises for an absence that already happened, so the kind reply waves it off and asks after her health. "
               "The second reply gives permission for the future; the third mixes up 急に (suddenly) with 急ぐ (hurry).",
        "vocab": [
            {"word": "急に", "reading": "きゅうに", "meaning": "suddenly"},
            {"word": "この前", "reading": "このまえ", "meaning": "the other day, last time"},
        ],
    },
    {
        "id": "n2-l19",
        "title": "Watching someone's bag",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "悪いけど、この荷物、ちょっと見ててもらえる？すぐ戻るから。", "Sorry, could you keep an eye on this bag for a moment? I'll be right back.")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["うん、いいよ。ここで待ってるね。", "うん、見せてくれてありがとう。", "ううん、すぐには戻らないよ。"],
        "choices_en": ["Sure. I'll wait here.", "Yeah, thanks for showing me.", "No, I won't be back soon."],
        "answer": 0,
        "why": "見ててもらえる？ asks the listener to watch the bag. The second reply confuses 見る with 見せる (show), "
               "and the third answers as if the listener were leaving.",
        "vocab": [
            {"word": "悪いけど", "reading": "わるいけど", "meaning": "sorry, but (asking a favour)"},
            {"word": "戻る", "reading": "もどる", "meaning": "to come back"},
        ],
    },
    {
        "id": "n2-l20",
        "title": "Choosing a gym plan",
        "kind": "integrated",
        "intro": "スポーツクラブで、係の人が料金プランについて説明しています。それから、男の人と女の人が話します。",
        "lines": [
            ("S", "当クラブには、三つのプランがございます。", "Our club has three plans."),
            ("S", "「いつでもプラン」は、毎日、営業時間中いつでもご利用いただけます。月一万円です。",
             "The Anytime plan lets you use the club whenever it's open, every day. It's 10,000 yen a month."),
            ("S", "「平日昼プラン」は、平日の午前十時から午後五時までご利用いただけます。月六千円です。",
             "The Weekday Daytime plan covers weekdays from 10 a.m. to 5 p.m. It's 6,000 yen a month."),
            ("S", "「週末プラン」は、土曜日と日曜日のみ、一日中ご利用いただけます。月七千円です。",
             "The Weekend plan covers all day on Saturdays and Sundays only. It's 7,000 yen a month."),
            ("F", "私は、平日は学校があって、夜しか空いていないんだよね。", "On weekdays I have school, so I'm only free in the evenings."),
            ("M", "じゃあ、「いつでもプラン」しかないね。", "Then it has to be the Anytime plan."),
            ("F", "うーん、ちょっと高いなあ。週末も行けるけど、土日だけじゃ足りないし……。やっぱり平日の夜も行きたいから、高くてもそれにする。",
             "Hmm, it's a bit expensive. I can go at weekends too, but Saturdays and Sundays alone aren't enough... I want to go on "
             "weekday evenings as well, so I'll take it even though it's pricey."),
            ("M", "僕は平日の昼間が空いてるから、一番安いのにしようかな。", "I'm free on weekday daytimes, so I think I'll go for the cheapest one."),
        ],
        "question": "女の人は、どのプランに申し込みますか。",
        "intro_en": "At a sports club, a staff member is explaining the price plans. Then a man and a woman talk.",
        "question_en": "Which plan will the woman sign up for?",
        "choices": ["いつでもプラン", "平日昼プラン", "週末プラン", "どのプランにも申し込まない"],
        "answer": 0,
        "why": "She's only free on weekday evenings, which only the Anytime plan covers, and weekends alone aren't enough: "
               "高くてもそれにする. The cheapest (Weekday Daytime) is the man's choice.",
        "vocab": [
            {"word": "営業時間", "reading": "えいぎょうじかん", "meaning": "opening hours"},
            {"word": "昼間", "reading": "ひるま", "meaning": "daytime"},
            {"word": "のみ", "reading": "のみ", "meaning": "only (formal)"},
            {"word": "一日中", "reading": "いちにちじゅう", "meaning": "all day"},
        ],
    },
    # ------------------------------------------------------------------ N1
    {
        "id": "n1-l01",
        "title": "Revising a thesis chapter",
        "kind": "task",
        "intro": "大学で、男の学生と先生が卒業論文について話しています。男の学生は、このあとまず何をしなければなりませんか。",
        "lines": [
            ("M", "先生、論文の第三章を書き直してきました。見ていただけますか。", "Professor, I've rewritten chapter three of my thesis. Could you take a look?"),
            ("F", "ありがとう。……うん、前よりずっと読みやすくなったね。ただ、ここで使っているデータ、出典が書いていないよね。",
             "Thank you... Yes, it's much easier to read than before. But the data you use here doesn't say where it's from, does it?"),
            ("M", "あ、すみません。後で参考文献の一覧にまとめて載せようと思っていたんですが。",
             "Oh, sorry. I was planning to put it all in the list of references later."),
            ("F", "一覧も必要だけど、本文の中にも、どこから引用したのかをその都度示しておかないと。それがないと、読む人が確かめられないからね。",
             "You need the list too, but you also have to show in the text, each time, where you quoted from. Without that, readers can't check it."),
            ("M", "分かりました。", "I understand."),
            ("F", "それから、結論の部分はもう少し短くしてもいいけど、それは全体ができてからでいいよ。まずは今言ったところを直して、来週もう一度持ってきて。",
             "Also, the conclusion could be a bit shorter, but that can wait until the whole thing is done. First fix what I just mentioned and bring it again next week."),
            ("M", "はい、そうします。", "Yes, I'll do that."),
        ],
        "question": "男の学生は、このあとまず何をしなければなりませんか。",
        "intro_en": "At a university, a male student and his professor are talking about his graduation thesis. What must the student do first after this?",
        "question_en": "What must the student do first after this?",
        "choices": ["参考文献の一覧を作る", "本文に、データの出典を書き加える", "結論を短くする", "第三章を全部書き直す"],
        "answer": 1,
        "why": "まずは今言ったところを直して: first, show the sources in the text itself (本文の中にも…その都度示して). "
               "The reference list matters too, and the conclusion can wait until the whole thesis is done.",
        "vocab": [
            {"word": "論文", "reading": "ろんぶん", "meaning": "thesis, paper"},
            {"word": "出典", "reading": "しゅってん", "meaning": "source (of a quotation or data)"},
            {"word": "参考文献", "reading": "さんこうぶんけん", "meaning": "references, bibliography"},
            {"word": "引用", "reading": "いんよう", "meaning": "quotation, citing"},
            {"word": "その都度", "reading": "そのつど", "meaning": "each time"},
            {"word": "結論", "reading": "けつろん", "meaning": "conclusion"},
        ],
    },
    {
        "id": "n1-l02",
        "title": "Registering a move at city hall",
        "kind": "task",
        "intro": "市役所で、女の人と係の人が話しています。女の人は、このあとどこへ行きますか。",
        "lines": [
            ("F", "すみません、先週引っ越してきたので、住所の変更をしたいんですが。", "Excuse me, I moved here last week, so I'd like to change my address."),
            ("M", "転入の手続きですね。前にお住まいだった市で、転出の届けはお済みですか。",
             "That's registering your move in. Have you already filed the moving-out notice with the city where you lived before?"),
            ("F", "はい、こちらに証明書があります。", "Yes, I have the certificate here."),
            ("M", "拝見します。……はい、大丈夫です。では、こちらの用紙にご記入のうえ、三番の窓口にお出しください。"
                  "それから、お子さんがいらっしゃる場合は、学校の手続きもございますが。",
             "Let me see... Yes, that's fine. Then please fill in this form and hand it in at counter three. Also, if you have "
             "children, there are school procedures as well."),
            ("F", "小学生の息子が一人います。", "I have a son at primary school."),
            ("M", "でしたら、転入の手続きが終わりましたら、二階の教育委員会で転校の手続きをなさってください。三番の窓口で書類をお渡ししますので、それをお持ちになって。",
             "In that case, once you've finished registering, please do the school transfer at the Board of Education on the second "
             "floor. Counter three will give you a document, so please take that with you."),
            ("F", "分かりました。じゃあ、まずこれを書いて出します。", "I see. Then I'll fill this in and hand it in first."),
        ],
        "question": "女の人は、このあとどこへ行きますか。",
        "intro_en": "At city hall, a woman and a staff member are talking. Where will the woman go after this?",
        "question_en": "Where will the woman go after this?",
        "choices": ["前に住んでいた市の市役所", "三番の窓口", "二階の教育委員会", "息子の学校"],
        "answer": 1,
        "why": "She'll fill in the form and hand it in at counter three first (まずこれを書いて出します). The Board of Education "
               "comes after, with the document counter three gives her.",
        "vocab": [
            {"word": "転入", "reading": "てんにゅう", "meaning": "moving in (registering)"},
            {"word": "転出", "reading": "てんしゅつ", "meaning": "moving out"},
            {"word": "届け", "reading": "とどけ", "meaning": "notification (filed at an office)"},
            {"word": "教育委員会", "reading": "きょういくいいんかい", "meaning": "Board of Education"},
            {"word": "転校", "reading": "てんこう", "meaning": "changing schools"},
        ],
    },
    {
        "id": "n1-l03",
        "title": "Not going on to graduate school",
        "kind": "point",
        "intro": "女の学生と男の学生が話しています。女の学生が大学院に進まないことにした一番の理由は何ですか。",
        "lines": [
            ("M", "大学院、受けないんだって？先生も期待してたのに。", "I hear you're not applying to grad school? Your professor had high hopes for you."),
            ("F", "うん。研究は好きなんだけどね。", "Yeah. I do love research, though."),
            ("M", "学費のこと？", "Is it the tuition?"),
            ("F", "それは奨学金でなんとかなりそうだったの。そうじゃなくて、研究を続けるうちに、本当に知りたいのは、理論よりも、"
                  "実際の現場で何が起きているかだって気づいて。それなら、まずは現場に出て経験を積むべきだと思ったんだ。",
             "A scholarship would probably have covered that. It's not that. As I kept researching, I realised that what I really "
             "want to know isn't theory but what actually happens on the ground. So I thought I should get out there and gain experience first."),
            ("M", "なるほどね。", "I see."),
            ("F", "いつか、また学びたくなったら、戻ってくるかもしれないけど。", "If I want to study again someday, I might come back, though."),
        ],
        "question": "女の学生が大学院に進まないことにした一番の理由は何ですか。",
        "intro_en": "A female student and a male student are talking. What is the main reason she decided not to go on to graduate school?",
        "question_en": "What is the main reason she decided not to go on to graduate school?",
        "choices": ["学費が払えないから", "研究が好きではないから", "現場で経験を積みたいから", "先生に反対されたから"],
        "answer": 2,
        "why": "Tuition was manageable with a scholarship, and she likes research. そうじゃなくて: she wants to gain experience "
               "where things actually happen (まずは現場に出て経験を積むべき).",
        "vocab": [
            {"word": "大学院", "reading": "だいがくいん", "meaning": "graduate school"},
            {"word": "学費", "reading": "がくひ", "meaning": "tuition fees"},
            {"word": "理論", "reading": "りろん", "meaning": "theory"},
            {"word": "現場", "reading": "げんば", "meaning": "the actual place, on the ground"},
            {"word": "積む", "reading": "つむ", "meaning": "to accumulate, build up"},
        ],
    },
    {
        "id": "n1-l04",
        "title": "A critic on a new film",
        "kind": "point",
        "intro": "ラジオで、映画評論家が新しい映画について話しています。評論家は、この映画の一番の魅力は何だと言っていますか。",
        "lines": [
            ("M", "今回の作品は、豪華な俳優陣や迫力のある映像が話題になっていますが、私が最も心を打たれたのは、そこではありません。",
             "This film has been talked about for its star-studded cast and powerful visuals, but that's not what moved me most."),
            ("M", "主人公と年老いた父親が、ほとんど言葉を交わさないまま、一緒に食卓を囲む場面があります。せりふはないのに、"
                  "二人の長い時間や、互いへの思いが、表情や沈黙からひしひしと伝わってくるのです。",
             "There's a scene where the main character and his elderly father sit at the table together, barely exchanging a word. "
             "There's no dialogue, yet their long history and their feelings for each other come through intensely in their "
             "expressions and silence."),
            ("M", "派手な場面よりも、こうした静かな場面にこそ、監督の力量が表れていると言えるでしょう。",
             "I'd say the director's skill shows precisely in quiet scenes like this, rather than in the flashy ones."),
        ],
        "question": "評論家は、この映画の一番の魅力は何だと言っていますか。",
        "intro_en": "On the radio, a film critic is talking about a new film. What does the critic say is the film's greatest appeal?",
        "question_en": "What does the critic say is the film's greatest appeal?",
        "choices": [
            "有名な俳優がたくさん出ていること",
            "映像に迫力があること",
            "言葉を使わずに気持ちを伝える静かな場面",
            "主人公と父親の会話が面白いこと",
        ],
        "answer": 2,
        "why": "The cast and visuals are what others talk about, but そこではありません. The quiet, wordless scene (せりふはないのに…"
               "沈黙から伝わってくる) is what moved the critic; there's almost no conversation in it.",
        "vocab": [
            {"word": "評論家", "reading": "ひょうろんか", "meaning": "critic"},
            {"word": "迫力", "reading": "はくりょく", "meaning": "power, impact"},
            {"word": "沈黙", "reading": "ちんもく", "meaning": "silence"},
            {"word": "ひしひしと", "reading": "ひしひしと", "meaning": "keenly, intensely"},
            {"word": "監督", "reading": "かんとく", "meaning": "(film) director"},
            {"word": "力量", "reading": "りきりょう", "meaning": "ability, skill"},
        ],
    },
    {
        "id": "n1-l05",
        "title": "Renovating the park",
        "kind": "point",
        "intro": "町の集会で、男の人と女の人が、公園の改修計画について話しています。女の人が最も心配していることは何ですか。",
        "lines": [
            ("M", "今度の改修で、公園に新しい遊具やカフェができるそうですね。", "I hear the renovation will bring new play equipment and a café to the park."),
            ("F", "ええ、きれいになるのはいいことだと思います。費用も、市が全部出すそうですし。",
             "Yes, I think it's good that it'll be nicer. And apparently the city is covering all the costs."),
            ("M", "何か気になることでも？", "Is something bothering you?"),
            ("F", "計画では、今ある大きな木を何本も切ることになっているんです。夏は、あの木陰で休むお年寄りが多いでしょう。"
                  "日陰がなくなったら、暑くて誰も来なくなるんじゃないかと思って。",
             "The plan involves cutting down several of the big trees. In summer, lots of older people rest in their shade, don't "
             "they? I worry that without shade it'll be too hot and nobody will come."),
            ("M", "なるほど。それは確かに問題ですね。", "I see. That's certainly a problem."),
        ],
        "question": "女の人が最も心配していることは何ですか。",
        "intro_en": "At a town meeting, a man and a woman are talking about plans to renovate a park. What is the woman most worried about?",
        "question_en": "What is the woman most worried about?",
        "choices": ["改修の費用がかかること", "新しい遊具が危ないこと", "木を切ると日陰がなくなること", "カフェができてうるさくなること"],
        "answer": 2,
        "why": "She welcomes the renovation and the city pays, but cutting the big trees would remove the shade older people use "
               "(日陰がなくなったら…誰も来なくなる).",
        "vocab": [
            {"word": "改修", "reading": "かいしゅう", "meaning": "renovation, repair"},
            {"word": "遊具", "reading": "ゆうぐ", "meaning": "play equipment"},
            {"word": "木陰", "reading": "こかげ", "meaning": "shade of a tree"},
            {"word": "日陰", "reading": "ひかげ", "meaning": "shade"},
            {"word": "集会", "reading": "しゅうかい", "meaning": "meeting, gathering"},
        ],
    },
    {
        "id": "n1-l06",
        "title": "A lecture on dialects",
        "kind": "summary",
        "intro": "大学の講義で、先生が方言について話しています。",
        "lines": [
            ("F", "皆さんの中には、方言は標準語より劣っていると考える人がいるかもしれません。かつては、方言を使うことが恥ずかしいとされた時代もありました。",
             "Some of you may think dialects are inferior to standard Japanese. There was even a time when speaking dialect was "
             "considered embarrassing."),
            ("F", "しかし、方言には、その土地の暮らしや歴史が刻まれています。例えば、雪の多い地方には、雪の状態を細かく言い分ける言葉がたくさんあります。"
                  "標準語では一言で済ませてしまうものを、そこでは何通りにも表現するのです。",
             "But dialects carry the life and history of their regions. For example, snowy regions have many words that "
             "distinguish the state of the snow in detail. What standard Japanese covers with one word is expressed there in many ways."),
            ("F", "つまり、方言は単なる言葉の違いではなく、その地域の人々が世界をどのように見てきたかを映し出す、貴重な文化だと言えるでしょう。",
             "In other words, a dialect isn't just a difference in words; it's a precious culture that reflects how the people of "
             "a region have seen the world."),
        ],
        "question": "先生は、方言についてどのように考えていますか。",
        "intro_en": "In a university lecture, a professor is talking about dialects.",
        "question_en": "What does the professor think about dialects?",
        "choices": [
            "標準語より劣っているので、使わないほうがいい。",
            "雪の多い地方でしか使われていない。",
            "その地域の人々のものの見方を表す、大切な文化だ。",
            "標準語と、ほとんど違いがない。",
        ],
        "choices_en": [
            "They're inferior to standard Japanese, so it's better not to use them.",
            "They're only used in snowy regions.",
            "They're a valuable culture that shows how people in a region see things.",
            "They hardly differ from standard Japanese.",
        ],
        "answer": 2,
        "why": "つまり introduces the conclusion: 世界をどのように見てきたかを映し出す、貴重な文化. The snow words are only an example, "
               "and \"inferior\" is the view the professor argues against.",
        "vocab": [
            {"word": "方言", "reading": "ほうげん", "meaning": "dialect"},
            {"word": "標準語", "reading": "ひょうじゅんご", "meaning": "standard language"},
            {"word": "劣る", "reading": "おとる", "meaning": "to be inferior"},
            {"word": "刻む", "reading": "きざむ", "meaning": "to engrave, carve"},
            {"word": "貴重", "reading": "きちょう", "meaning": "precious, valuable"},
            {"word": "映し出す", "reading": "うつしだす", "meaning": "to reflect, show"},
        ],
    },
    {
        "id": "n1-l07",
        "title": "How we spend our time",
        "kind": "summary",
        "intro": "ラジオで、男の人が話しています。",
        "lines": [
            ("M", "時間がない、とよく言いますが、本当に時間が足りないのでしょうか。", "We often say we have no time, but do we really lack time?"),
            ("M", "ある調査によると、一日のうち、何となくスマートフォンを眺めている時間は、平均で二時間を超えるそうです。もちろん、休むことも大切です。"
                  "ただ、それが自分で選んだ休息なのか、ただ流されているだけなのかで、意味は大きく変わります。",
             "According to one survey, the time we spend idly looking at our smartphones exceeds two hours a day on average. Of "
             "course, rest matters too. But it makes a big difference whether that's rest you chose or you're just drifting along."),
            ("M", "時間を増やすことはできません。できるのは、何に時間を使うかを、自分で決めることだけなのです。",
             "You can't make more time. All you can do is decide for yourself what to spend it on."),
        ],
        "question": "男の人が、一番言いたいことは何ですか。",
        "intro_en": "On the radio, a man is speaking.",
        "question_en": "What does the man most want to say?",
        "choices": [
            "スマートフォンを使うのは、やめるべきだ。",
            "休む時間を、もっと増やしたほうがいい。",
            "何に時間を使うかを、自分で意識して選ぶことが大切だ。",
            "調査の結果は、あまり信用できない。",
        ],
        "choices_en": [
            "We should stop using smartphones.",
            "We should take more time to rest.",
            "It's important to choose consciously what we spend our time on.",
            "The survey results can't really be trusted.",
        ],
        "answer": 2,
        "why": "The talk ends with the point: 何に時間を使うかを、自分で決めること. Smartphones are just the example, and he says "
               "rest is important as long as it's chosen.",
        "vocab": [
            {"word": "何となく", "reading": "なんとなく", "meaning": "idly, without particular reason"},
            {"word": "眺める", "reading": "ながめる", "meaning": "to gaze at, look at"},
            {"word": "平均", "reading": "へいきん", "meaning": "average"},
            {"word": "休息", "reading": "きゅうそく", "meaning": "rest"},
            {"word": "流される", "reading": "ながされる", "meaning": "to drift along, be swept along"},
        ],
    },
    {
        "id": "n1-l08",
        "title": "A borrowed book",
        "kind": "quick",
        "intro": "",
        "lines": [("F", "先日お貸しした本、もうお読みになったようでしたら、お返しいただけますか。",
                   "The book I lent you the other day: if you've finished it, could you return it?")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["あ、すみません。明日必ずお持ちします。", "はい、ぜひお貸しください。", "いいえ、お返しになるには及びません。"],
        "choices_en": ["Oh, I'm sorry. I'll definitely bring it tomorrow.", "Yes, please do lend it to me.",
                       "No, there's no need for you to return it."],
        "answer": 0,
        "why": "She politely asks for her book back, so the borrower apologises and promises to bring it. The second reply asks to "
               "borrow it, and the third is what the lender would say.",
        "vocab": [
            {"word": "先日", "reading": "せんじつ", "meaning": "the other day"},
            {"word": "〜には及びません", "reading": "にはおよびません", "meaning": "there's no need to"},
        ],
    },
    {
        "id": "n1-l09",
        "title": "Trusted with the festival",
        "kind": "quick",
        "intro": "",
        "lines": [("M", "今回の文化祭の準備、君に任せたからには、最後まで責任を持ってやってもらうよ。",
                   "Now that I've put you in charge of preparing the school festival, I expect you to see it through to the end.")],
        "question": "",
        "intro_en": "",
        "question_en": "",
        "choices": ["はい、精一杯やらせていただきます。", "では、先輩にお任せしてもよろしいですか。", "責任を持っていただけて、助かります。"],
        "choices_en": ["Yes, I'll do my very best.", "Then may I leave it to you?", "Thank you for taking responsibility."],
        "answer": 0,
        "why": "〜からには: since you've been given the job, see it through. The reply accepts: 精一杯やらせていただきます. "
               "The other two hand the job back or thank the wrong person.",
        "vocab": [
            {"word": "文化祭", "reading": "ぶんかさい", "meaning": "school festival"},
            {"word": "任せる", "reading": "まかせる", "meaning": "to leave to, entrust"},
            {"word": "精一杯", "reading": "せいいっぱい", "meaning": "with all one's might"},
        ],
    },
    {
        "id": "n1-l10",
        "title": "Choosing a hot-spring trip",
        "kind": "integrated",
        "intro": "旅行会社で、係の人が温泉旅行のプランについて説明しています。それから、男の人と女の人が話します。",
        "lines": [
            ("S", "当社おすすめの温泉旅行には、四つのプランがございます。", "We have four recommended hot-spring trip plans."),
            ("S", "一つ目は「山の湯プラン」です。山奥の静かな旅館で、露天風呂から紅葉が楽しめます。駅からバスで一時間半かかります。",
             "The first is the Mountain Spring plan: a quiet inn deep in the mountains, where you can enjoy the autumn leaves from the "
             "outdoor bath. It's an hour and a half by bus from the station."),
            ("S", "二つ目は「海辺プラン」です。駅から歩いて五分の旅館で、新鮮な海の幸が自慢です。",
             "The second is the Seaside plan: an inn five minutes' walk from the station, famous for its fresh seafood."),
            ("S", "三つ目は「街なかプラン」です。温泉街の中心にあり、食べ歩きや買い物が楽しめます。",
             "The third is the Town Centre plan: in the heart of the hot-spring town, where you can enjoy street food and shopping."),
            ("S", "四つ目は「森の宿プラン」です。全室に露天風呂が付いていて、ほかのお客様と顔を合わせずに過ごせます。駅から車で二十分です。",
             "The fourth is the Forest Inn plan: every room has its own outdoor bath, so you can stay without running into other "
             "guests. It's twenty minutes by car from the station."),
            ("F", "静かなところがいいね。人が多いところは疲れちゃうし。", "Somewhere quiet would be nice. Crowded places wear me out."),
            ("M", "うん。でも、母も一緒だから、長くバスに乗るのはきついかな。", "Yeah. But my mother's coming too, so a long bus ride might be hard on her."),
            ("F", "そうだね。それに、お母さん、大きなお風呂でほかの人と一緒になるのは苦手だって言ってたよ。",
             "True. And your mother said she doesn't like sharing a big bath with other people."),
            ("M", "じゃあ、決まりだね。", "Then that settles it."),
        ],
        "question": "二人は、どのプランを選びますか。",
        "intro_en": "At a travel agency, a staff member is explaining hot-spring trip plans. Then a man and a woman talk.",
        "question_en": "Which plan will they choose?",
        "choices": ["山の湯プラン", "海辺プラン", "街なかプラン", "森の宿プラン"],
        "answer": 3,
        "why": "Quiet rules out the busy town centre; the 90-minute bus rules out the mountain plan; and the mother doesn't like "
               "sharing a bath, so a room with its own outdoor bath fits: the Forest Inn.",
        "vocab": [
            {"word": "露天風呂", "reading": "ろてんぶろ", "meaning": "outdoor bath"},
            {"word": "山奥", "reading": "やまおく", "meaning": "deep in the mountains"},
            {"word": "海の幸", "reading": "うみのさち", "meaning": "seafood"},
            {"word": "自慢", "reading": "じまん", "meaning": "pride, speciality"},
            {"word": "顔を合わせる", "reading": "かおをあわせる", "meaning": "to meet, run into"},
            {"word": "きつい", "reading": "きつい", "meaning": "hard, tough"},
        ],
    },
]

_BY_ID = {item["id"]: item for item in ITEMS}


def get(item_id: str) -> dict | None:
    return _BY_ID.get(item_id)


def level(item: dict) -> str:
    return item["id"].split("-")[0].upper()


def number(item: dict) -> int:
    same = [i for i in ITEMS if level(i) == level(item)]
    return same.index(item) + 1


def script(item: dict) -> list[dict]:
    """What is heard, in order, as on the test: the narrator sets the scene (and asks
    the question first for task and point items), then the dialogue, then the
    question again; summary and quick items also read out the numbered choices."""
    out = []
    if item["intro"]:
        out.append({"who": "N", "text": item["intro"], "en": item["intro_en"]})
    out += [{"who": who, "text": jp, "en": en} for who, jp, en in item["lines"]]
    if item["question"]:
        out.append({"who": "N", "text": item["question"], "en": item["question_en"]})
    if not KINDS[item["kind"]][2]:
        # Quick replies are spoken by the other person, summary choices by the narrator and
        # utterance choices by the person in the situation (the arrow in the test's picture).
        if item["kind"] == "summary":
            replier = "N"
        elif item["kind"] == "utterance":
            replier = item["voice"]
        else:
            replier = "F" if item["lines"][-1][0] == "M" else "M"
        out += [{"who": replier, "text": f"{n}。{c}", "en": f"{n}. {en}"}
                for n, (c, en) in enumerate(zip(item["choices"], item["choices_en"]), 1)]
    return out


if __name__ == "__main__":
    import sys

    from . import checks, furigana

    problems = 0
    for item in ITEMS:
        expected = 3 if item["kind"] in ("quick", "utterance") else 4
        if len(item["choices"]) != expected or len(set(item["choices"])) != expected:
            print(f"{item['id']}: needs {expected} different choices")
            problems += 1
        if not 0 <= item["answer"] < len(item["choices"]):
            print(f"{item['id']}: answer index out of range")
            problems += 1
        if item["kind"] not in KINDS or any(who not in VOICES for who, _jp, _en in item["lines"]):
            print(f"{item['id']}: unknown kind or role")
            problems += 1
        if item["kind"] == "utterance" and item.get("voice") not in VOICES:
            print(f"{item['id']}: utterance items need a voice for the choices")
            problems += 1
        if not KINDS[item["kind"]][2] and len(item.get("choices_en", [])) != len(item["choices"]):
            print(f"{item['id']}: spoken choices need translations (choices_en)")
            problems += 1
        if any(len(s["text"]) > 300 for s in script(item)):
            print(f"{item['id']}: a line is too long for the voice engine (300 characters)")
            problems += 1
        for v in item["vocab"]:
            if checks.kana_to_romaji(v["reading"]) is None:
                print(f"{item['id']} vocab reading isn't pure kana: {v['reading']}")
                problems += 1
    print(f"{len(ITEMS)} listening items checked, {problems} problem(s)")

    if "--readings" in sys.argv:
        for item in ITEMS:
            print(f"\n== {item['id']} {item['title']}")
            for s in script(item):
                out = []
                for seg in furigana.annotate(s["text"]):
                    if seg.get("parts"):
                        out.append("".join(f"{x['t']}({x['r']})" if x.get("r") else x["t"] for x in seg["parts"]))
                    else:
                        out.append(seg["t"])
                print(f"{s['who']}: {''.join(out)}")
