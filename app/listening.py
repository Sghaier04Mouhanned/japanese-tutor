"""JLPT-style listening practice (聴解), written by hand so the content is reliable.

Each item is a short dialogue or talk with a narrator, like the real test:
- task    課題理解      what will someone do next? (choices printed)
- point   ポイント理解  why / what exactly? (choices printed)
- summary 概要理解      what is the speaker's main point? (choices only heard)
- quick   即時応答      pick the best reply to one line (replies only heard)
- integrated 統合理解   (N2) compare options someone explains with what two people then say

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
}  # kind -> (English, Japanese, choices printed on the page)

ITEMS: list[dict] = [
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
        # Quick replies are spoken by the other person; summary choices by the narrator.
        replier = "N" if item["kind"] == "summary" else ("F" if item["lines"][-1][0] == "M" else "M")
        out += [{"who": replier, "text": f"{n}。{c}", "en": f"{n}. {en}"}
                for n, (c, en) in enumerate(zip(item["choices"], item["choices_en"]), 1)]
    return out


if __name__ == "__main__":
    import sys

    from . import checks, furigana

    problems = 0
    for item in ITEMS:
        expected = 4 if item["kind"] != "quick" else 3
        if len(item["choices"]) != expected or len(set(item["choices"])) != expected:
            print(f"{item['id']}: needs {expected} different choices")
            problems += 1
        if not 0 <= item["answer"] < len(item["choices"]):
            print(f"{item['id']}: answer index out of range")
            problems += 1
        if item["kind"] not in KINDS or any(who not in VOICES for who, _jp, _en in item["lines"]):
            print(f"{item['id']}: unknown kind or role")
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
