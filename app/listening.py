"""JLPT-style listening practice (聴解), written by hand so the content is reliable.

Each item is a short dialogue or talk with a narrator, like the real test:
- task    課題理解      what will someone do next? (choices printed)
- point   ポイント理解  why / what exactly? (choices printed)
- summary 概要理解      what is the speaker's main point? (choices only heard)
- quick   即時応答      pick the best reply to one line (replies only heard)

The audio is made with VOICEVOX, one voice per role (N narrator, F woman,
M man). `python -m app.listening` checks the items; `--readings` prints the
automatic furigana of the transcripts for proofreading.
"""

from __future__ import annotations

# Role -> (VOICEVOX speaker name, style). Missing voices fall back to the default one.
VOICES = {"N": ("九州そら", "ノーマル"), "F": ("春日部つむぎ", "ノーマル"), "M": ("玄野武宏", "ノーマル")}
ROLE_LABELS = {"N": "Narrator", "F": "Woman", "M": "Man"}

KINDS = {
    "task": ("Task-based", "課題理解", True),
    "point": ("Key point", "ポイント理解", True),
    "summary": ("Summary", "概要理解", False),
    "quick": ("Quick response", "即時応答", False),
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
