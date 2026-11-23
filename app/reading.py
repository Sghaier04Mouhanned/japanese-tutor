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
