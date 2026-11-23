"""JLPT-style reading practice (読解), written by hand so the content is reliable.

Each passage has the Japanese text (paragraphs), an English translation,
multiple-choice questions in Japanese with an English explanation, and a few
key words. `python -m app.reading` checks the answers and choices, and prints
the automatic furigana so the readings can be proofread.
"""

from __future__ import annotations

PASSAGES: list[dict] = [
    {
        "id": "n3-r01",
        "title": "A note on the table",
        "jp_title": "テーブルの上のメモ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "お母さんへ",
            "今日は部活の練習が長くなるので、帰りは8時ごろになると思います。晩ご飯は先に食べていてください。"
            "それから、昨日頼まれた手紙は、出すのを忘れていたので、今朝ポストに入れておきました。遅くなってごめんなさい。",
            "ゆうき",
        ],
        "en": [
            "To Mum,",
            "Club practice will run long today, so I think I'll be home around 8. Please go ahead and eat dinner without me. "
            "Also, I forgot to send the letter you asked me to post yesterday, so I put it in the postbox this morning. "
            "Sorry it was late.",
            "Yuuki",
        ],
        "questions": [
            {
                "q": "このメモを書いた人が今日することは何か。",
                "choices": [
                    "晩ご飯を作ってから、練習に行く。",
                    "練習のあと、8時ごろ家に帰る。",
                    "帰りに手紙をポストに入れる。",
                    "お母さんと一緒に晩ご飯を食べる。",
                ],
                "answer": 1,
                "why": "Practice runs long, so Yuuki will be home around 8 (帰りは8時ごろになる). The letter was already "
                       "posted this morning (入れておきました), and Mum is asked to eat first.",
            },
        ],
        "vocab": [
            {"word": "部活", "reading": "ぶかつ", "meaning": "school club activities"},
            {"word": "先に", "reading": "さきに", "meaning": "ahead, first"},
            {"word": "頼まれる", "reading": "たのまれる", "meaning": "to be asked (a favour)"},
            {"word": "今朝", "reading": "けさ", "meaning": "this morning"},
        ],
    },
    {
        "id": "n3-r02",
        "title": "An email from a friend",
        "jp_title": "友達からのメール",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "件名：日曜日のこと",
            "リンさん",
            "日曜日の映画、楽しみにしていたんだけど、急に親戚が来ることになって、行けなくなってしまいました。本当にごめんね。"
            "チケットはもう買ってあるから、よかったら、ほかの友達と行ってください。お金はいらないよ。"
            "来週の土曜日なら空いているので、また誘ってね。",
            "さき",
        ],
        "en": [
            "Subject: About Sunday",
            "Dear Lin,",
            "I was looking forward to the film on Sunday, but some relatives are suddenly coming over, so I can't go. "
            "I'm really sorry. I've already bought the tickets, so if you like, please go with another friend. "
            "You don't need to pay me. I'm free next Saturday, so invite me again!",
            "Saki",
        ],
        "questions": [
            {
                "q": "さきさんがリンさんにいちばん伝えたいことは何か。",
                "choices": [
                    "日曜日の映画のチケットを買ってほしい。",
                    "日曜日は行けないので、チケットを使ってほしい。",
                    "日曜日に親戚と一緒に映画を見てほしい。",
                    "来週の土曜日に映画のお金を返してほしい。",
                ],
                "answer": 1,
                "why": "Saki can't go (行けなくなってしまいました), has already bought the tickets (買ってある), "
                       "and asks Lin to go with another friend, free of charge.",
            },
        ],
        "vocab": [
            {"word": "件名", "reading": "けんめい", "meaning": "subject (of an email)"},
            {"word": "親戚", "reading": "しんせき", "meaning": "relative(s)"},
            {"word": "急に", "reading": "きゅうに", "meaning": "suddenly"},
            {"word": "誘う", "reading": "さそう", "meaning": "to invite"},
            {"word": "空く", "reading": "あく", "meaning": "to be free (time), to be empty"},
        ],
    },
    {
        "id": "n3-r03",
        "title": "Rubbish collection notice",
        "jp_title": "ごみの出し方のお知らせ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "マンションにお住まいの皆様へ",
            "4月から、ごみを出す曜日が変わります。燃えるごみは月曜日と木曜日、プラスチックは水曜日です。"
            "瓶と缶は、これまでどおり第2・第4金曜日に出してください。",
            "ごみは、収集日の朝8時までに出すことになっています。前の日の夜には出さないようにお願いします。",
            "管理人",
        ],
        "en": [
            "To all residents of the building,",
            "From April, the days for putting out rubbish will change. Burnable rubbish is on Mondays and Thursdays, "
            "and plastic is on Wednesdays. Please put out bottles and cans on the 2nd and 4th Fridays, as before.",
            "Rubbish must be put out by 8 a.m. on the collection day. Please don't put it out the night before.",
            "The building manager",
        ],
        "questions": [
            {
                "q": "4月から変わることは何か。",
                "choices": [
                    "瓶と缶を出す日",
                    "ごみを出す時間",
                    "燃えるごみとプラスチックを出す曜日",
                    "前の日の夜にごみを出してもいいこと",
                ],
                "answer": 2,
                "why": "The days change for burnable rubbish and plastic. Bottles and cans stay the same "
                       "(これまでどおり = as before), the 8 a.m. rule is the existing rule, and the night before is not allowed.",
            },
        ],
        "vocab": [
            {"word": "皆様", "reading": "みなさま", "meaning": "everyone (polite)"},
            {"word": "燃える", "reading": "もえる", "meaning": "to burn"},
            {"word": "瓶", "reading": "びん", "meaning": "bottle (glass)"},
            {"word": "缶", "reading": "かん", "meaning": "can, tin"},
            {"word": "収集日", "reading": "しゅうしゅうび", "meaning": "collection day"},
            {"word": "管理人", "reading": "かんりにん", "meaning": "building manager, caretaker"},
        ],
    },
    {
        "id": "n3-r04",
        "title": "Walking",
        "jp_title": "歩くこと",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "私は毎朝、駅まで20分歩いている。以前はバスを使っていたが、運動のために歩くようにしたのだ。"
            "最初は大変だったが、続けているうちに、体が軽くなってきた。",
            "それだけではない。季節によって変わる花や空の色に気がつくようになった。"
            "バスの窓から見ていたときには、気がつかなかったことばかりだ。",
        ],
        "en": [
            "Every morning I walk for 20 minutes to the station. I used to take the bus, but I started walking "
            "for the exercise. It was hard at first, but as I kept it up, my body started to feel lighter.",
            "And that's not all. I've started to notice the flowers and the colour of the sky, which change with the "
            "seasons. These are all things I never noticed when I was looking out of the bus window.",
        ],
        "questions": [
            {
                "q": "この文章で筆者がいちばん言いたいことは何か。",
                "choices": [
                    "バスより歩くほうが早く駅に着く。",
                    "歩くようになって、健康以外にもいいことがあった。",
                    "毎朝歩くのは大変なので、やめたい。",
                    "バスの窓から見る景色はきれいだ。",
                ],
                "answer": 1,
                "why": "Walking made the writer's body lighter, and それだけではない (that's not all) introduces a second "
                       "benefit: noticing the seasons. The main point is the benefits beyond health.",
            },
        ],
        "vocab": [
            {"word": "以前", "reading": "いぜん", "meaning": "before, previously"},
            {"word": "運動", "reading": "うんどう", "meaning": "exercise"},
            {"word": "続ける", "reading": "つづける", "meaning": "to continue, keep up"},
            {"word": "気がつく", "reading": "きがつく", "meaning": "to notice"},
            {"word": "筆者", "reading": "ひっしゃ", "meaning": "the writer (of a text)"},
        ],
    },
    {
        "id": "n3-r05",
        "title": "Smartphones and reading",
        "jp_title": "スマートフォンと読書",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "最近、電車の中で本を読んでいる人をあまり見なくなった。ほとんどの人がスマートフォンを見ている。"
            "私も以前は、時間さえあればスマートフォンでニュースや動画を見ていた。",
            "ところが、去年の夏、旅行先でスマートフォンが壊れてしまった。最初は不便で困ったが、"
            "仕方がないので、ホテルにあった古い小説を読んでみた。すると、時間がたつのを忘れるほど面白かった。",
            "それ以来、寝る前の一時間はスマートフォンを使わずに、本を読むようにしている。"
            "スマートフォンが悪いと言いたいわけではない。ただ、一つのことにゆっくり向き合う時間も大切だと思うようになったのだ。",
        ],
        "en": [
            "These days I rarely see people reading books on the train. Almost everyone is looking at a smartphone. "
            "I used to be the same: whenever I had a moment, I watched news and videos on my phone.",
            "But last summer, my smartphone broke while I was travelling. At first it was inconvenient and I didn't "
            "know what to do, but since there was no other choice, I tried reading an old novel that was in the hotel. "
            "It was so interesting that I forgot about the time.",
            "Since then, I read a book for the hour before bed, without using my phone. I'm not saying smartphones "
            "are bad. I've just come to think that time spent slowly focusing on one thing matters too.",
        ],
        "questions": [
            {
                "q": "筆者が旅行先で小説を読んだのはなぜか。",
                "choices": [
                    "スマートフォンが使えなかったから",
                    "ホテルの人に勧められたから",
                    "ニュースを見るのに飽きたから",
                    "前から読みたかった本だったから",
                ],
                "answer": 0,
                "why": "The phone broke (壊れてしまった), and with no other choice (仕方がないので) the writer read the "
                       "novel that happened to be in the hotel.",
            },
            {
                "q": "「時間がたつのを忘れるほど」とあるが、どういう意味か。",
                "choices": [
                    "時間がなくて、急いで読んだ。",
                    "とても面白くて、夢中になった。",
                    "読むのに長い時間がかかった。",
                    "時計がなくて、時間が分からなかった。",
                ],
                "answer": 1,
                "why": "〜ほど shows the extent: the book was so interesting that the writer lost track of time, "
                       "i.e. was completely absorbed (夢中になった).",
            },
            {
                "q": "筆者の考えに合うものはどれか。",
                "choices": [
                    "スマートフォンは使わないほうがいい。",
                    "電車の中では本を読むべきだ。",
                    "一つのことにゆっくり集中する時間も必要だ。",
                    "旅行にはスマートフォンを持っていかないほうがいい。",
                ],
                "answer": 2,
                "why": "The writer says smartphones aren't bad (悪いと言いたいわけではない) but that time spent slowly "
                       "on one thing is important too (一つのことにゆっくり向き合う時間も大切だ).",
            },
        ],
        "vocab": [
            {"word": "動画", "reading": "どうが", "meaning": "video"},
            {"word": "旅行先", "reading": "りょこうさき", "meaning": "travel destination"},
            {"word": "仕方がない", "reading": "しかたがない", "meaning": "it can't be helped"},
            {"word": "小説", "reading": "しょうせつ", "meaning": "novel"},
            {"word": "それ以来", "reading": "それいらい", "meaning": "since then"},
            {"word": "向き合う", "reading": "むきあう", "meaning": "to face, to engage with"},
        ],
    },
    {
        "id": "n3-r06",
        "title": "Grandmother's cooking",
        "jp_title": "祖母の味",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "子供のころ、夏休みになると、いなかの祖母の家に遊びに行った。祖母はいつも、私の好きな卵焼きを作ってくれた。"
            "少し甘くて、やわらかい卵焼きだった。",
            "大学生になって一人で暮らし始めてから、何度もあの卵焼きを作ってみた。"
            "しかし、レシピのとおりに作っても、どうしても同じ味にならない。",
            "先月、久しぶりに祖母に会ったとき、そのことを話すと、祖母は笑って「特別なことは何もしていないよ。"
            "食べる人のことを考えながら作るだけ」と言った。その日、祖母の隣で一緒に作ってみて、やっと分かった。"
            "祖母は火を弱くして、時間をかけてゆっくり焼いていたのだ。",
        ],
        "en": [
            "When I was a child, I used to visit my grandmother's house in the countryside every summer holiday. "
            "She always made me my favourite rolled omelette. It was slightly sweet and soft.",
            "After I started living alone as a university student, I tried making that omelette many times. "
            "But even when I followed the recipe, it just never tasted the same.",
            "Last month, when I saw my grandmother for the first time in a long while, I told her about it. "
            "She laughed and said, \"I don't do anything special. I just cook while thinking about the person who'll eat it.\" "
            "That day, I cooked next to her, and I finally understood: she turned the heat down low and cooked it slowly, "
            "taking her time.",
        ],
        "questions": [
            {
                "q": "筆者が作った卵焼きが祖母の味にならなかったのはなぜか。",
                "choices": [
                    "レシピを見ないで作っていたから",
                    "祖母とは違う卵を使っていたから",
                    "弱い火でゆっくり焼いていなかったから",
                    "砂糖を入れるのを忘れていたから",
                ],
                "answer": 2,
                "why": "Cooking beside her, the writer finally understood (やっと分かった): she used low heat and took her time "
                       "(火を弱くして、時間をかけてゆっくり焼いていた). The writer did follow the recipe (レシピのとおりに).",
            },
            {
                "q": "祖母が言った「特別なことは何もしていない」とは、どういうことか。",
                "choices": [
                    "珍しい材料や方法は使っていない。",
                    "筆者のために作ったことはない。",
                    "料理はあまり好きではない。",
                    "卵焼きはいつも失敗している。",
                ],
                "answer": 0,
                "why": "She means there's no special trick or ingredient: she just cooks thinking of the person who will eat it.",
            },
            {
                "q": "この文章の内容と合うものはどれか。",
                "choices": [
                    "筆者は今も祖母と一緒に住んでいる。",
                    "筆者は先月、祖母と一緒に卵焼きを作った。",
                    "祖母の卵焼きはとても辛かった。",
                    "筆者は子供のころから料理が上手だった。",
                ],
                "answer": 1,
                "why": "Last month (先月) the writer met her and cooked beside her (祖母の隣で一緒に作ってみて). "
                       "The writer lives alone, and the omelette was sweet (甘くて).",
            },
        ],
        "vocab": [
            {"word": "いなか", "reading": "いなか", "meaning": "the countryside, one's home town"},
            {"word": "卵焼き", "reading": "たまごやき", "meaning": "rolled omelette"},
            {"word": "暮らす", "reading": "くらす", "meaning": "to live"},
            {"word": "久しぶり", "reading": "ひさしぶり", "meaning": "for the first time in a long while"},
            {"word": "隣", "reading": "となり", "meaning": "next to"},
            {"word": "焼く", "reading": "やく", "meaning": "to cook (in a pan), to grill, to bake"},
        ],
    },
    {
        "id": "n3-r07",
        "title": "The city pool",
        "jp_title": "市民プールの案内",
        "kind": "Information search",
        "minutes": 5,
        "text": [
            "みどり市民プール　ご利用案内",
            "◆営業時間\n"
            "・平日：午前10時〜午後9時\n"
            "・土曜日・日曜日・祝日：午前9時〜午後6時\n"
            "・休館日：毎週月曜日（月曜日が祝日の場合は、次の日）",
            "◆料金（2時間まで）\n"
            "・大人：400円\n"
            "・中学生以下：200円\n"
            "・65歳以上：200円\n"
            "※2時間を過ぎると、1時間ごとに100円かかります。",
            "◆注意\n"
            "・水泳帽をかぶってください。（受付で200円で売っています）\n"
            "・食べ物は、休憩室でお願いします。",
        ],
        "en": [
            "Midori City Pool: information for visitors",
            "Opening hours\n"
            "- Weekdays: 10 a.m. to 9 p.m.\n"
            "- Saturdays, Sundays and public holidays: 9 a.m. to 6 p.m.\n"
            "- Closed: every Monday (if Monday is a public holiday, the following day)",
            "Prices (up to 2 hours)\n"
            "- Adults: 400 yen\n"
            "- Junior high school students and younger: 200 yen\n"
            "- 65 and over: 200 yen\n"
            "* After 2 hours, each extra hour costs 100 yen.",
            "Please note\n"
            "- Please wear a swimming cap (sold at reception for 200 yen).\n"
            "- Please eat only in the rest room.",
        ],
        "questions": [
            {
                "q": "中学生のゆいさんは、日曜日の午後3時から3時間泳ぎたいと思っている。料金はいくらか。",
                "choices": ["200円", "300円", "400円", "500円"],
                "answer": 1,
                "why": "A junior high school student pays 200 yen for the first 2 hours, plus 100 yen for the third hour. "
                       "Sunday closes at 6 p.m., so 3 p.m. to 6 p.m. fits.",
            },
            {
                "q": "大人のマリアさんは、祝日の月曜日に、水泳帽を持たずにプールへ行くつもりだ。正しいものはどれか。",
                "choices": [
                    "月曜日は休館日なので、プールは使えない。",
                    "午後8時まで泳ぐことができる。",
                    "受付で水泳帽を買えば、泳ぐことができる。",
                    "水泳帽がなくても、泳ぐことができる。",
                ],
                "answer": 2,
                "why": "When Monday is a holiday the pool opens (it closes the next day instead), with holiday hours "
                       "until 6 p.m. A cap is required, but reception sells them.",
            },
        ],
        "vocab": [
            {"word": "営業時間", "reading": "えいぎょうじかん", "meaning": "opening hours"},
            {"word": "祝日", "reading": "しゅくじつ", "meaning": "public holiday"},
            {"word": "休館日", "reading": "きゅうかんび", "meaning": "closing day (of a facility)"},
            {"word": "料金", "reading": "りょうきん", "meaning": "fee, charge"},
            {"word": "受付", "reading": "うけつけ", "meaning": "reception (desk)"},
            {"word": "水泳帽", "reading": "すいえいぼう", "meaning": "swimming cap"},
        ],
    },
    {
        "id": "n3-r08",
        "title": "Being on time",
        "jp_title": "時間を守るということ",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "日本に来て驚いたことの一つは、電車が時間どおりに来ることだ。一分でも遅れると、"
            "駅で「申し訳ございません」という放送が流れる。私の国では、十分ぐらいの遅れは普通なので、最初はとても不思議に感じた。",
            "友達と会うときも同じだ。日本人の友達は、約束の時間の五分前には必ず来ている。"
            "私が二、三分遅れただけで、「何かあったの？」と心配されたこともある。",
            "正直に言うと、最初は少し窮屈だと思った。しかし、慣れてくると、それは相手の時間を大切にするということなのだと分かってきた。"
            "今では私も、約束の時間より早く着くように家を出ている。",
        ],
        "en": [
            "One of the things that surprised me when I came to Japan is that trains arrive on time. If a train is even "
            "one minute late, an announcement says \"We are very sorry\" at the station. In my country, a delay of about "
            "ten minutes is normal, so at first it felt very strange.",
            "It's the same when I meet friends. My Japanese friends are always there five minutes before the time we agreed. "
            "Once, when I was only two or three minutes late, they worried and asked, \"Did something happen?\"",
            "To be honest, at first I found it a bit stifling. But as I got used to it, I came to understand that it means "
            "respecting the other person's time. Now I too leave home so that I arrive before the agreed time.",
        ],
        "questions": [
            {
                "q": "筆者が日本に来て不思議に感じたことは何か。",
                "choices": [
                    "電車が少し遅れただけで、謝る放送があること",
                    "電車がよく十分ぐらい遅れること",
                    "駅の放送の日本語が難しいこと",
                    "友達がいつも約束に遅れること",
                ],
                "answer": 0,
                "why": "Even a one-minute delay brings an apology (申し訳ございません), which felt strange because "
                       "ten-minute delays are normal in the writer's country.",
            },
            {
                "q": "「窮屈だ」とあるが、筆者はなぜそう思ったのか。",
                "choices": [
                    "時間をきちんと守らなければならないのが大変だったから",
                    "友達がなかなか約束を守らなかったから",
                    "電車がいつも混んでいたから",
                    "日本の家が狭かったから",
                ],
                "answer": 0,
                "why": "窮屈 (stifling, restrictive) refers to the strict punctuality described before it: friends arrive five "
                       "minutes early and worry about a two-minute delay.",
            },
            {
                "q": "筆者は今、どうしているか。",
                "choices": [
                    "約束の時間ちょうどに着くようにしている。",
                    "約束の時間より前に着くようにしている。",
                    "遅れたときは、友達に心配してもらう。",
                    "電車が遅れたときは、駅員に謝ってもらう。",
                ],
                "answer": 1,
                "why": "今では私も、約束の時間より早く着くように家を出ている: the writer now leaves home so as to arrive early.",
            },
        ],
        "vocab": [
            {"word": "驚く", "reading": "おどろく", "meaning": "to be surprised"},
            {"word": "放送", "reading": "ほうそう", "meaning": "announcement, broadcast"},
            {"word": "不思議", "reading": "ふしぎ", "meaning": "strange, mysterious"},
            {"word": "正直", "reading": "しょうじき", "meaning": "honest(ly)"},
            {"word": "窮屈", "reading": "きゅうくつ", "meaning": "cramped, stifling, restrictive"},
            {"word": "慣れる", "reading": "なれる", "meaning": "to get used to"},
        ],
    },
    {
        "id": "n3-r09",
        "title": "Life in the countryside",
        "jp_title": "いなかでの生活",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "三年前、私は家族と一緒に、東京から山の近くの小さな町に引っ越した。"
            "子供が生まれたのをきっかけに、自然の中で育てたいと思ったからだ。",
            "引っ越す前は、不便な生活になるのではないかと心配していた。確かに、近くに大きな店はないし、"
            "バスも一時間に一本しかない。しかし、その代わりに、近所の人たちがとても親切で、"
            "野菜を分けてくれたり、子供の面倒を見てくれたりする。",
            "もちろん、いなかの生活がだれにでも合うわけではないと思う。ただ、私たち家族にとっては、"
            "ここに来てよかったと心から思っている。",
        ],
        "en": [
            "Three years ago, my family and I moved from Tokyo to a small town near the mountains. When our child was born, "
            "it made us want to raise them surrounded by nature.",
            "Before moving, I worried that life would be inconvenient. It's true that there are no big shops nearby, and "
            "there's only one bus an hour. But in exchange, the neighbours are very kind: they share vegetables with us "
            "and look after our child.",
            "Of course, I don't think country life suits everyone. But for our family, I'm truly glad we came here.",
        ],
        "questions": [
            {
                "q": "筆者が引っ越したのはなぜか。",
                "choices": [
                    "東京の家賃が高くなったから",
                    "子供を自然の多い所で育てたかったから",
                    "近所の人に誘われたから",
                    "山に登るのが趣味だったから",
                ],
                "answer": 1,
                "why": "子供が生まれたのをきっかけに、自然の中で育てたいと思ったから: the birth of their child made them "
                       "want to raise the child in nature.",
            },
            {
                "q": "町の生活について、筆者が書いていることはどれか。",
                "choices": [
                    "バスが多くて便利だ。",
                    "近くに大きな店がたくさんある。",
                    "不便なこともあるが、近所の人が助けてくれる。",
                    "近所の人とはあまり話さない。",
                ],
                "answer": 2,
                "why": "No big shops and one bus an hour (inconvenient), but その代わりに (in exchange) the neighbours "
                       "share vegetables and look after the child.",
            },
            {
                "q": "筆者の考えに合うものはどれか。",
                "choices": [
                    "いなかの生活はだれにでも合う。",
                    "いなかの生活が合わない人もいるが、自分たちには合っている。",
                    "いつか東京に戻りたいと思っている。",
                    "子供が大きくなったら、また引っ越すつもりだ。",
                ],
                "answer": 1,
                "why": "だれにでも合うわけではない (it doesn't suit everyone), but for their family (私たち家族にとっては) "
                       "they are glad they came.",
            },
        ],
        "vocab": [
            {"word": "きっかけ", "reading": "きっかけ", "meaning": "trigger, occasion (for a change)"},
            {"word": "自然", "reading": "しぜん", "meaning": "nature"},
            {"word": "育てる", "reading": "そだてる", "meaning": "to raise, bring up"},
            {"word": "確かに", "reading": "たしかに", "meaning": "certainly, it's true that"},
            {"word": "近所", "reading": "きんじょ", "meaning": "neighbourhood"},
            {"word": "面倒を見る", "reading": "めんどうをみる", "meaning": "to look after"},
        ],
    },
    {
        "id": "n3-r10",
        "title": "School closed for a typhoon",
        "jp_title": "台風による休校のお知らせ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "保護者の皆様",
            "明日9月5日は、台風が近づいているため、休校とします。授業は9月8日（月）から通常どおり行います。"
            "なお、5日に予定していた英語のテストは、8日に行います。",
            "台風の情報によっては予定が変わることもありますので、学校のホームページを確認してください。",
            "さくら中学校",
        ],
        "en": [
            "To all parents and guardians,",
            "Because a typhoon is approaching, the school will be closed tomorrow, 5 September. Classes will run as usual "
            "from Monday 8 September. The English test planned for the 5th will be held on the 8th.",
            "Depending on the typhoon forecast, plans may change, so please check the school website.",
            "Sakura Junior High School",
        ],
        "questions": [
            {
                "q": "このお知らせから分かることは何か。",
                "choices": [
                    "9月5日に英語のテストがある。",
                    "9月8日は休校になる。",
                    "英語のテストは9月8日に行われる。",
                    "予定が変わったら、学校から電話がある。",
                ],
                "answer": 2,
                "why": "The test planned for the 5th moves to the 8th (8日に行います). The 5th is the closed day, "
                       "and changes will be posted on the website, not phoned through.",
            },
        ],
        "vocab": [
            {"word": "保護者", "reading": "ほごしゃ", "meaning": "parent, guardian"},
            {"word": "休校", "reading": "きゅうこう", "meaning": "school closure"},
            {"word": "通常", "reading": "つうじょう", "meaning": "usual, normal"},
            {"word": "なお", "reading": "なお", "meaning": "in addition, note that"},
            {"word": "確認", "reading": "かくにん", "meaning": "checking, confirmation"},
        ],
    },
    {
        "id": "n3-r11",
        "title": "Bicycle parking notice",
        "jp_title": "駐輪場のお知らせ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "みなみ駅前駐輪場をご利用の皆様へ",
            "工事のため、5月10日から6月30日まで、駐輪場の東側が使えなくなります。この間は、西側の駐輪場をご利用ください。"
            "西側は駅から少し遠くなりますが、料金は同じです。",
            "なお、期間中に東側に置いてある自転車は、市が別の場所へ移動しますので、ご注意ください。",
            "みなみ市役所",
        ],
        "en": [
            "To everyone who uses the Minami Station bicycle parking,",
            "Because of construction work, the east side of the bicycle parking cannot be used from 10 May to 30 June. "
            "During this time, please use the west side. The west side is a little further from the station, but the price is the same.",
            "Please note that bicycles left on the east side during this period will be moved elsewhere by the city.",
            "Minami City Hall",
        ],
        "questions": [
            {
                "q": "このお知らせで、いちばん伝えたいことは何か。",
                "choices": [
                    "5月10日から、駐輪場の料金が変わる。",
                    "工事の間は、西側の駐輪場を使ってほしい。",
                    "西側の駐輪場は、駅に近くて便利だ。",
                    "東側に自転車を置くと、料金が高くなる。",
                ],
                "answer": 1,
                "why": "The east side is closed for construction, so the notice asks people to use the west side "
                       "(西側の駐輪場をご利用ください). The price stays the same and the west side is further away.",
            },
        ],
        "vocab": [
            {"word": "駐輪場", "reading": "ちゅうりんじょう", "meaning": "bicycle parking"},
            {"word": "工事", "reading": "こうじ", "meaning": "construction work"},
            {"word": "期間", "reading": "きかん", "meaning": "period (of time)"},
            {"word": "移動", "reading": "いどう", "meaning": "moving, relocation"},
        ],
    },
    {
        "id": "n3-r12",
        "title": "A new deadline",
        "jp_title": "レポートの締め切り",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "件名：レポートについて",
            "2年B組の皆さん",
            "来週の月曜日までに出すことになっていたレポートですが、図書館が工事で使えないため、締め切りを一週間延ばすことにしました。"
            "新しい締め切りは、再来週の月曜日です。",
            "ただし、テーマは変わりませんので、もう書き終わった人は、そのまま出してもかまいません。",
            "山本",
        ],
        "en": [
            "Subject: About the report",
            "To everyone in class 2B,",
            "About the report that was due next Monday: because the library can't be used due to construction work, "
            "I've decided to extend the deadline by one week. The new deadline is Monday the week after next.",
            "However, the topic hasn't changed, so if you've already finished writing, you may hand it in as it is.",
            "Yamamoto",
        ],
        "questions": [
            {
                "q": "このメールの内容と合うものはどれか。",
                "choices": [
                    "レポートのテーマが変わった。",
                    "レポートは、来週の月曜日までに出さなければならない。",
                    "もう書き終わったレポートは、今出してもいい。",
                    "レポートは、図書館で書かなければならない。",
                ],
                "answer": 2,
                "why": "The topic is unchanged (テーマは変わりません), so finished reports can be handed in as they are "
                       "(そのまま出してもかまいません). The deadline moved to the week after next.",
            },
        ],
        "vocab": [
            {"word": "締め切り", "reading": "しめきり", "meaning": "deadline"},
            {"word": "延ばす", "reading": "のばす", "meaning": "to extend, postpone"},
            {"word": "再来週", "reading": "さらいしゅう", "meaning": "the week after next"},
            {"word": "ただし", "reading": "ただし", "meaning": "however, but"},
        ],
    },
    {
        "id": "n3-r13",
        "title": "A handwritten letter",
        "jp_title": "手書きの手紙",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "最近は、メールやSNSで簡単に連絡ができるようになった。私も、ふだんはメールばかり使っている。"
            "ところが先日、祖母から手書きの手紙が届いた。字は少し読みにくかったが、一字一字ていねいに書かれていて、"
            "読んでいるうちに温かい気持ちになった。",
            "メールは便利だが、手紙には、書いた人の気持ちを伝える力があるのだと思う。今度は私も、祖母に手紙を書いてみようと思っている。",
        ],
        "en": [
            "These days it has become easy to keep in touch by email and social media. I usually use nothing but email myself. "
            "But the other day, a handwritten letter arrived from my grandmother. The writing was a little hard to read, but each "
            "character had been written carefully, and as I read it, I felt warm inside.",
            "Email is convenient, but I think letters have the power to convey the writer's feelings. Next time, I'm going to try "
            "writing a letter to my grandmother too.",
        ],
        "questions": [
            {
                "q": "筆者は、手紙についてどう考えているか。",
                "choices": [
                    "字が読みにくいので、メールのほうがいい。",
                    "書いた人の気持ちが伝わる。",
                    "メールより早く連絡できる。",
                    "家族にしか書かないほうがいい。",
                ],
                "answer": 1,
                "why": "手紙には、書いた人の気持ちを伝える力がある: letters carry the writer's feelings. The writing was hard to "
                       "read, but that isn't the writer's conclusion.",
            },
        ],
        "vocab": [
            {"word": "連絡", "reading": "れんらく", "meaning": "contact, getting in touch"},
            {"word": "ふだん", "reading": "ふだん", "meaning": "usually, normally"},
            {"word": "先日", "reading": "せんじつ", "meaning": "the other day"},
            {"word": "手書き", "reading": "てがき", "meaning": "handwritten"},
            {"word": "伝える", "reading": "つたえる", "meaning": "to convey, pass on"},
        ],
    },
    {
        "id": "n3-r14",
        "title": "A note from my sister",
        "jp_title": "姉からのメモ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "はるかへ",
            "冷蔵庫のケーキは、明日友達が来たときに出すつもりなので、食べないでね。その代わり、テーブルの上のクッキーは食べてもいいよ。"
            "それから、今晩は遅くなるから、洗濯物を取り込んでおいてくれると助かります。雨が降るかもしれないそうなので。",
            "姉より",
        ],
        "en": [
            "To Haruka,",
            "I'm planning to serve the cake in the fridge when my friend comes tomorrow, so please don't eat it. Instead, you can eat "
            "the cookies on the table. Also, I'll be late tonight, so it would be a big help if you could bring the washing in. "
            "Apparently it might rain.",
            "From your sister",
        ],
        "questions": [
            {
                "q": "姉が、はるかさんに頼んでいることは何か。",
                "choices": [
                    "ケーキを冷蔵庫に入れておくこと",
                    "クッキーを買っておくこと",
                    "洗濯物を家の中に入れておくこと",
                    "明日、友達にケーキを出すこと",
                ],
                "answer": 2,
                "why": "洗濯物を取り込んでおいてくれると助かります asks Haruka to bring the washing in before the rain. "
                       "The cake and cookies are things she may or may not eat, not requests.",
            },
        ],
        "vocab": [
            {"word": "冷蔵庫", "reading": "れいぞうこ", "meaning": "fridge"},
            {"word": "洗濯物", "reading": "せんたくもの", "meaning": "laundry, the washing"},
            {"word": "取り込む", "reading": "とりこむ", "meaning": "to bring in (laundry)"},
            {"word": "助かる", "reading": "たすかる", "meaning": "to be a help, be saved"},
        ],
    },
    {
        "id": "n3-r15",
        "title": "Afraid of failing",
        "jp_title": "失敗すること",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "子供のころ、私は失敗するのがとても怖かった。テストで悪い点を取ると、何日も落ち込んだ。"
            "しかし、高校で出会った先生に「失敗しない人は、何も新しいことをしていない人だ」と言われてから、考え方が変わった。",
            "失敗は、新しいことに挑戦したしるしなのだ。今でも失敗すれば悔しいが、前ほど怖くはなくなった。",
        ],
        "en": [
            "As a child, I was very afraid of failing. If I got a bad mark on a test, I'd feel down for days. But my way of thinking "
            "changed after a teacher I met in high school told me, \"People who never fail are people who never do anything new.\"",
            "Failure is a sign that you tried something new. Even now I feel frustrated when I fail, but it doesn't scare me as much as before.",
        ],
        "questions": [
            {
                "q": "筆者は今、失敗についてどう思っているか。",
                "choices": [
                    "失敗しないように、新しいことはしない。",
                    "失敗は、挑戦したしるしだと思っている。",
                    "失敗しても、まったく悔しくない。",
                    "失敗すると、何日も落ち込んでしまう。",
                ],
                "answer": 1,
                "why": "失敗は、新しいことに挑戦したしるし: failure shows you tried something new. The writer still feels "
                       "frustrated (悔しい), and the days of feeling down were in childhood.",
            },
        ],
        "vocab": [
            {"word": "失敗", "reading": "しっぱい", "meaning": "failure, mistake"},
            {"word": "落ち込む", "reading": "おちこむ", "meaning": "to feel down"},
            {"word": "挑戦", "reading": "ちょうせん", "meaning": "challenge, attempt"},
            {"word": "しるし", "reading": "しるし", "meaning": "sign, mark"},
            {"word": "悔しい", "reading": "くやしい", "meaning": "frustrating, annoying (when you lose)"},
        ],
    },
    {
        "id": "n3-r16",
        "title": "Vending machines",
        "jp_title": "自動販売機",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "日本に来て驚いたことの一つに、自動販売機の多さがある。駅や道はもちろん、山の上や、いなかの小さな道にまで置いてある。"
            "飲み物だけでなく、アイスクリームや温かいスープ、中には野菜を売っている機械もある。",
            "私の国では、自動販売機を外に置くと、すぐに壊されたり、お金を盗まれたりしてしまう。"
            "だから、これほど多くの機械が外に置かれているのは、日本が安全な国だからだろう。",
            "一方で、夜中でも明るく光っている自動販売機を見ると、電気がもったいないと感じることもある。"
            "便利さと環境のどちらを大切にするか、考えてみる必要があるかもしれない。",
        ],
        "en": [
            "One of the things that surprised me in Japan is the number of vending machines. They're not only at stations and on "
            "streets, but even on mountaintops and small country roads. Besides drinks, they sell ice cream and hot soup, and some "
            "machines even sell vegetables.",
            "In my country, if you put a vending machine outside, it soon gets broken or has its money stolen. So I think the reason "
            "so many machines can be left outside is that Japan is a safe country.",
            "On the other hand, when I see vending machines glowing brightly even in the middle of the night, I sometimes feel it's "
            "a waste of electricity. We might need to think about which matters more: convenience or the environment.",
        ],
        "questions": [
            {
                "q": "筆者が日本に来て驚いたことは何か。",
                "choices": [
                    "自動販売機が多くて、いろいろな物を売っていること",
                    "自動販売機の飲み物が安いこと",
                    "自動販売機がよく壊れていること",
                    "自動販売機で野菜しか売っていないこと",
                ],
                "answer": 0,
                "why": "自動販売機の多さ (how many there are), in all kinds of places, selling drinks, ice cream, soup and even vegetables.",
            },
            {
                "q": "筆者は、日本に自動販売機が多い理由は何だと考えているか。",
                "choices": ["日本人は買い物が好きだから", "店が少ないから", "安全な国だから", "電気が安いから"],
                "answer": 2,
                "why": "これほど多くの機械が外に置かれているのは、日本が安全な国だからだろう: machines can stay outside "
                       "because Japan is safe.",
            },
            {
                "q": "筆者は、自動販売機についてどう感じているか。",
                "choices": [
                    "便利なので、もっと増やしたほうがいい。",
                    "便利だが、電気の使い方を考える必要もある。",
                    "環境に悪いので、すぐになくしたほうがいい。",
                    "夜は使えないので、不便だ。",
                ],
                "answer": 1,
                "why": "一方で (on the other hand), the writer feels the electricity is wasted and says we may need to weigh "
                       "convenience against the environment, without calling for them to be removed.",
            },
        ],
        "vocab": [
            {"word": "自動販売機", "reading": "じどうはんばいき", "meaning": "vending machine"},
            {"word": "機械", "reading": "きかい", "meaning": "machine"},
            {"word": "盗む", "reading": "ぬすむ", "meaning": "to steal"},
            {"word": "一方で", "reading": "いっぽうで", "meaning": "on the other hand"},
            {"word": "もったいない", "reading": "もったいない", "meaning": "wasteful, a waste"},
            {"word": "環境", "reading": "かんきょう", "meaning": "environment"},
        ],
    },
    {
        "id": "n3-r17",
        "title": "Making friends abroad",
        "jp_title": "留学生活",
        "kind": "Medium passage",
        "minutes": 6,
        "text": [
            "私が日本の大学に留学して、半年がたった。来る前は、日本語の授業さえ分かれば大丈夫だと思っていた。"
            "ところが、実際に困ったのは、授業よりも友達を作ることだった。",
            "日本人の学生はみんな親切だが、授業が終わると、すぐに帰ってしまう。話しかけても、なかなか話が続かなかった。"
            "そこで、思い切ってサッカーのサークルに入ってみた。サッカーは子供のころから好きだったし、言葉が上手でなくても、"
            "一緒に楽しめると思ったからだ。",
            "これが大成功だった。練習のあとにみんなで食事に行くようになり、今では週末に一緒に旅行する友達もできた。"
            "日本語も、教科書では習わない表現をたくさん覚えた。",
        ],
        "en": [
            "Six months have passed since I came to study at a Japanese university. Before coming, I thought I'd be fine as long as "
            "I could follow my Japanese classes. But what actually gave me trouble wasn't the classes; it was making friends.",
            "The Japanese students are all kind, but as soon as class ends, they go home. Even when I spoke to them, the conversation "
            "never seemed to last. So I took the plunge and joined a football club. I'd loved football since I was a child, and I "
            "thought we could enjoy it together even if my Japanese wasn't good.",
            "It was a great success. We started going out to eat together after practice, and now I even have friends I travel with "
            "at weekends. I've also learned lots of expressions that textbooks don't teach.",
        ],
        "questions": [
            {
                "q": "筆者が留学して困ったことは何か。",
                "choices": [
                    "授業がまったく分からなかったこと",
                    "友達がなかなかできなかったこと",
                    "サッカーをする場所がなかったこと",
                    "日本人の学生が親切ではなかったこと",
                ],
                "answer": 1,
                "why": "実際に困ったのは、授業よりも友達を作ることだった: making friends was the real problem. "
                       "The students were kind (みんな親切).",
            },
            {
                "q": "筆者がサッカーのサークルに入ったのはなぜか。",
                "choices": [
                    "日本語が上手になりたかったから",
                    "授業で先生に勧められたから",
                    "言葉が上手でなくても、楽しめると思ったから",
                    "子供のころから、サークルに入りたかったから",
                ],
                "answer": 2,
                "why": "言葉が上手でなくても、一緒に楽しめると思ったから: the writer thought football could be enjoyed together "
                       "even without good Japanese. Learning new expressions was a result, not the reason.",
            },
            {
                "q": "サークルに入って、どうなったか。",
                "choices": [
                    "授業を休むことが多くなった。",
                    "一緒に出かける友達ができた。",
                    "教科書の日本語が分かるようになった。",
                    "サッカーが上手になって、試合に出た。",
                ],
                "answer": 1,
                "why": "They eat together after practice, and now there are friends to travel with at weekends "
                       "(週末に一緒に旅行する友達もできた).",
            },
        ],
        "vocab": [
            {"word": "半年", "reading": "はんとし", "meaning": "half a year"},
            {"word": "実際に", "reading": "じっさいに", "meaning": "actually, in reality"},
            {"word": "話しかける", "reading": "はなしかける", "meaning": "to start talking to"},
            {"word": "思い切って", "reading": "おもいきって", "meaning": "boldly, taking the plunge"},
            {"word": "表現", "reading": "ひょうげん", "meaning": "expression"},
        ],
    },
    {
        "id": "n3-r18",
        "title": "Taking a nap",
        "jp_title": "昼寝の効果",
        "kind": "Medium passage",
        "minutes": 5,
        "text": [
            "昼ご飯のあと、眠くなって勉強に集中できないという経験は、だれにでもあるだろう。最近、そんなときに短い昼寝をすることが勧められている。",
            "ある研究によると、十五分から二十分ほど昼寝をすると、頭がすっきりして、午後の作業の効率が上がるそうだ。"
            "ただし、三十分以上寝てしまうと、かえって起きたあとに体がだるくなり、夜も眠れなくなることがあるという。",
            "大切なのは、長く寝すぎないことだ。昼寝をするときは、目覚まし時計をかけておくといいだろう。",
        ],
        "en": [
            "Everyone has probably had the experience of getting sleepy after lunch and being unable to focus on studying. Recently, "
            "taking a short nap at times like that has been recommended.",
            "According to one study, napping for about fifteen to twenty minutes clears your head and makes your afternoon work more "
            "efficient. However, if you sleep for thirty minutes or more, you may actually feel sluggish after waking, and even be "
            "unable to sleep at night.",
            "The important thing is not to sleep too long. When you nap, it's a good idea to set an alarm clock.",
        ],
        "questions": [
            {
                "q": "この文章によると、昼寝はどのくらいがいいか。",
                "choices": ["5分ぐらい", "15分から20分ぐらい", "30分以上", "1時間ぐらい"],
                "answer": 1,
                "why": "十五分から二十分ほど昼寝をすると…効率が上がる; thirty minutes or more has the opposite effect.",
            },
            {
                "q": "筆者がいちばん言いたいことは何か。",
                "choices": [
                    "昼ご飯のあとは、必ず昼寝をするべきだ。",
                    "昼寝をすると夜眠れなくなるので、しないほうがいい。",
                    "昼寝は、短い時間なら、いい効果がある。",
                    "目覚まし時計は、夜だけ使うほうがいい。",
                ],
                "answer": 2,
                "why": "A short nap helps, a long one backfires, and 大切なのは、長く寝すぎないことだ (don't sleep too long).",
            },
        ],
        "vocab": [
            {"word": "昼寝", "reading": "ひるね", "meaning": "nap"},
            {"word": "研究", "reading": "けんきゅう", "meaning": "research, study"},
            {"word": "すっきり", "reading": "すっきり", "meaning": "refreshed, clear"},
            {"word": "効率", "reading": "こうりつ", "meaning": "efficiency"},
            {"word": "かえって", "reading": "かえって", "meaning": "on the contrary, instead"},
            {"word": "目覚まし時計", "reading": "めざましどけい", "meaning": "alarm clock"},
        ],
    },
    {
        "id": "n3-r19",
        "title": "Spring classes at the community centre",
        "jp_title": "市民センターの教室",
        "kind": "Information search",
        "minutes": 5,
        "text": [
            "さくら市民センター　春の教室のご案内",
            "①はじめての料理教室\n"
            "・毎週土曜日　午前10時〜12時（全4回）\n"
            "・料金：4,000円（材料費を含む）",
            "②英会話（初級）\n"
            "・毎週水曜日　午後7時〜8時半（全8回）\n"
            "・料金：6,000円",
            "③写真教室\n"
            "・第1・第3日曜日　午後1時〜3時（全4回）\n"
            "・料金：3,000円　※カメラは各自でお持ちください。",
            "④親子ヨガ\n"
            "・毎週金曜日　午前10時〜11時（全6回）\n"
            "・料金：親子で5,000円",
            "お申し込み：3月20日までに、センターの受付か電話でお申し込みください。",
        ],
        "en": [
            "Sakura Community Centre: spring classes",
            "1. Cooking for beginners\n"
            "- Every Saturday, 10 a.m. to 12 noon (4 sessions)\n"
            "- Fee: 4,000 yen (ingredients included)",
            "2. English conversation (beginner)\n"
            "- Every Wednesday, 7 to 8:30 p.m. (8 sessions)\n"
            "- Fee: 6,000 yen",
            "3. Photography\n"
            "- 1st and 3rd Sundays, 1 to 3 p.m. (4 sessions)\n"
            "- Fee: 3,000 yen. Please bring your own camera.",
            "4. Parent-and-child yoga\n"
            "- Every Friday, 10 to 11 a.m. (6 sessions)\n"
            "- Fee: 5,000 yen per parent and child",
            "How to apply: by 20 March, at the centre's reception desk or by phone.",
        ],
        "questions": [
            {
                "q": "大学生のキムさんは、平日は毎日夜9時までアルバイトがあるので、週末の教室に参加したい。"
                     "カメラは持っていない。キムさんが参加できる教室はどれか。",
                "choices": ["①はじめての料理教室", "②英会話（初級）", "③写真教室", "④親子ヨガ"],
                "answer": 0,
                "why": "Weekends only rules out English (Wednesday) and yoga (Friday). Photography is on Sundays but needs your own "
                       "camera (各自でお持ちください). Cooking is on Saturdays with ingredients included.",
            },
            {
                "q": "申し込みについて、正しいものはどれか。",
                "choices": [
                    "3月20日までに、受付か電話で申し込む。",
                    "インターネットで申し込む。",
                    "教室の初日に、受付で申し込む。",
                    "3月20日から、申し込みが始まる。",
                ],
                "answer": 0,
                "why": "3月20日までに、センターの受付か電話で: by 20 March, at reception or by phone. までに means \"by\", "
                       "not \"from\".",
            },
        ],
        "vocab": [
            {"word": "材料費", "reading": "ざいりょうひ", "meaning": "cost of ingredients"},
            {"word": "含む", "reading": "ふくむ", "meaning": "to include"},
            {"word": "初級", "reading": "しょきゅう", "meaning": "beginner level"},
            {"word": "各自", "reading": "かくじ", "meaning": "each person, individually"},
            {"word": "親子", "reading": "おやこ", "meaning": "parent and child"},
            {"word": "申し込み", "reading": "もうしこみ", "meaning": "application, signing up"},
        ],
    },
    {
        "id": "n3-r20",
        "title": "Volunteering at the festival",
        "jp_title": "お祭りのボランティア",
        "kind": "Medium passage",
        "minutes": 5,
        "text": [
            "去年の夏、町のお祭りでボランティアをした。会場の掃除や道案内など、地味な仕事ばかりだったが、思っていた以上に楽しかった。",
            "いちばんうれしかったのは、道を教えたおばあさんが、帰りにわざわざ「ありがとう」と言いに来てくれたことだ。"
            "だれかの役に立てたと感じた瞬間だった。",
            "ボランティアというと、特別な人がするものだと思っていたが、そうではない。少しの時間があれば、だれにでもできることがある。"
            "今年も参加するつもりだ。",
        ],
        "en": [
            "Last summer I volunteered at our town's festival. It was all unglamorous work, like cleaning the venue and giving "
            "directions, but it was more fun than I'd expected.",
            "What made me happiest was when an elderly woman I'd given directions to went out of her way to come and say "
            "\"thank you\" on her way home. It was a moment when I felt I'd been useful to someone.",
            "I used to think volunteering was something special people do, but that's not true. If you have a little time, there's "
            "something anyone can do. I'm planning to take part again this year.",
        ],
        "questions": [
            {
                "q": "筆者がいちばんうれしかったのは、どんなことか。",
                "choices": [
                    "お祭りで働いて、お金をもらったこと",
                    "おばあさんが、お礼を言いに来てくれたこと",
                    "会場の掃除が早く終わったこと",
                    "お祭りで、友達がたくさんできたこと",
                ],
                "answer": 1,
                "why": "いちばんうれしかったのは…おばあさんが…「ありがとう」と言いに来てくれたこと.",
            },
            {
                "q": "筆者は、ボランティアについてどう考えているか。",
                "choices": [
                    "特別な人しかできない。",
                    "時間がたくさんある人がするものだ。",
                    "少しの時間でも、だれにでもできることがある。",
                    "楽しくないので、今年は参加しない。",
                ],
                "answer": 2,
                "why": "The writer used to think it was for special people, but そうではない: 少しの時間があれば、"
                       "だれにでもできることがある. And they plan to take part again.",
            },
        ],
        "vocab": [
            {"word": "会場", "reading": "かいじょう", "meaning": "venue"},
            {"word": "地味", "reading": "じみ", "meaning": "plain, unglamorous"},
            {"word": "わざわざ", "reading": "わざわざ", "meaning": "going out of one's way"},
            {"word": "役に立つ", "reading": "やくにたつ", "meaning": "to be useful"},
            {"word": "瞬間", "reading": "しゅんかん", "meaning": "moment"},
        ],
    },
]

_BY_ID = {p["id"]: p for p in PASSAGES}


def get(passage_id: str) -> dict | None:
    return _BY_ID.get(passage_id)


def level(passage: dict) -> str:
    """"N3" from the id prefix (n3-r01)."""
    return passage["id"].split("-")[0].upper()


def number(passage: dict) -> int:
    same = [p for p in PASSAGES if level(p) == level(passage)]
    return same.index(passage) + 1


if __name__ == "__main__":
    # Consistency check, plus the automatic readings for proofreading.
    import sys

    from . import checks, furigana

    problems = 0
    for p in PASSAGES:
        text = "".join(p["text"])
        if len(p["text"]) != len(p["en"]):
            print(f"{p['id']}: {len(p['text'])} paragraphs but {len(p['en'])} translated")
            problems += 1
        for i, q in enumerate(p["questions"], 1):
            if len(q["choices"]) != 4 or len(set(q["choices"])) != 4:
                print(f"{p['id']} q{i}: needs 4 different choices")
                problems += 1
            if not 0 <= q["answer"] < len(q["choices"]):
                print(f"{p['id']} q{i}: answer index out of range")
                problems += 1
        for v in p["vocab"]:
            if checks.kana_to_romaji(v["reading"]) is None:
                print(f"{p['id']} vocab reading isn't pure kana: {v['reading']}")
                problems += 1
            # The words should appear in the passage or its questions (conjugated forms aside).
            stem = v["word"][:-1] if len(v["word"]) > 1 and v["word"][-1] in "うくすつぬぶむるいる" else v["word"]
            haystack = text + "".join(q["q"] + "".join(q["choices"]) for q in p["questions"])
            if stem not in haystack:
                print(f"{p['id']} vocab word not in the passage: {v['word']}")
                problems += 1
    print(f"{len(PASSAGES)} passages checked, {problems} problem(s)")

    if "--readings" in sys.argv:
        for p in PASSAGES:
            print(f"\n== {p['id']} {p['jp_title']}")
            for line in p["text"] + [q["q"] for q in p["questions"]] + [c for q in p["questions"] for c in q["choices"]]:
                out = []
                for s in furigana.annotate(line):
                    if s.get("parts"):
                        out.append("".join(f"{x['t']}({x['r']})" if x.get("r") else x["t"] for x in s["parts"]))
                    else:
                        out.append(s["t"])
                print("".join(out))
