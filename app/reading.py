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
    # ------------------------------------------------------------------ N2
    {
        "id": "n2-r01",
        "title": "Water cut notice",
        "jp_title": "断水のお知らせ",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "さくらハイツにお住まいの皆様へ",
            "水道管の点検工事のため、下記の日時に断水いたします。ご不便をおかけしますが、ご理解とご協力をお願いいたします。",
            "日時：6月12日（水）午前9時〜午後3時\n※工事の状況によっては、終了時間が遅れる場合があります。",
            "断水中は、トイレも使用できません。必要な水は、前日までにご用意くださいますようお願いいたします。"
            "なお、工事終了後しばらくの間、水が濁ることがありますが、少し流していただければ問題ありません。",
            "さくらハイツ管理事務所",
        ],
        "en": [
            "To all residents of Sakura Heights,",
            "Because of inspection work on the water pipes, the water will be cut off at the time below. We apologise for the "
            "inconvenience and ask for your understanding and cooperation.",
            "When: Wednesday 12 June, 9 a.m. to 3 p.m.\n* Depending on how the work goes, it may finish later.",
            "The toilets cannot be used while the water is off. Please prepare any water you need by the day before. "
            "After the work, the water may be cloudy for a while, but it will be fine once you let it run a little.",
            "Sakura Heights management office",
        ],
        "questions": [
            {
                "q": "このお知らせの内容と合っているものはどれか。",
                "choices": [
                    "断水は、午後3時に必ず終わる。",
                    "断水中でも、トイレは使える。",
                    "断水の前に、使う水を準備しておく必要がある。",
                    "工事のあと水が濁ったら、管理事務所に連絡しなければならない。",
                ],
                "answer": 2,
                "why": "必要な水は、前日までにご用意ください: prepare water the day before. The end time may be later, the toilets "
                       "can't be used, and cloudy water just needs to run a little.",
            },
        ],
        "vocab": [
            {"word": "断水", "reading": "だんすい", "meaning": "water cut-off"},
            {"word": "水道管", "reading": "すいどうかん", "meaning": "water pipe"},
            {"word": "点検", "reading": "てんけん", "meaning": "inspection"},
            {"word": "下記", "reading": "かき", "meaning": "the following, below"},
            {"word": "協力", "reading": "きょうりょく", "meaning": "cooperation"},
            {"word": "濁る", "reading": "にごる", "meaning": "to become cloudy, muddy"},
        ],
    },
    {
        "id": "n2-r02",
        "title": "A delayed order",
        "jp_title": "ご注文の商品について",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "件名：ご注文の商品について",
            "山田様",
            "このたびは当店をご利用いただき、誠にありがとうございます。ご注文いただいた本棚ですが、メーカーでの生産が遅れているため、"
            "お届けが予定より一週間ほど遅れる見込みです。",
            "お急ぎの場合は、ご注文を取り消していただくことも可能です。その際は、お手数ですが、今月20日までにこのメールにご返信ください。"
            "ご返信がない場合は、このまま商品をお送りいたします。",
            "家具のミドリ　お客様係",
        ],
        "en": [
            "Subject: About your order",
            "Dear Mr./Ms. Yamada,",
            "Thank you very much for shopping with us. Regarding the bookshelf you ordered: because production at the manufacturer "
            "is behind schedule, delivery is expected to be about a week later than planned.",
            "If you're in a hurry, you can also cancel your order. In that case, we're sorry for the trouble, but please reply to "
            "this email by the 20th of this month. If we don't hear from you, we'll send the item as planned.",
            "Midori Furniture, customer service",
        ],
        "questions": [
            {
                "q": "山田さんが注文を取り消したい場合、どうすればいいか。",
                "choices": [
                    "何もしなくていい。",
                    "20日までに、このメールに返信する。",
                    "メーカーに電話する。",
                    "商品が届いてから返品する。",
                ],
                "answer": 1,
                "why": "その際は…今月20日までにこのメールにご返信ください. Doing nothing means the item is sent as planned.",
            },
        ],
        "vocab": [
            {"word": "当店", "reading": "とうてん", "meaning": "this shop, our shop"},
            {"word": "誠に", "reading": "まことに", "meaning": "truly, sincerely"},
            {"word": "本棚", "reading": "ほんだな", "meaning": "bookshelf"},
            {"word": "見込み", "reading": "みこみ", "meaning": "expectation, estimate"},
            {"word": "取り消す", "reading": "とりけす", "meaning": "to cancel"},
            {"word": "お手数", "reading": "おてすう", "meaning": "trouble (お手数ですが = sorry to trouble you)"},
        ],
    },
    {
        "id": "n2-r03",
        "title": "The price of convenience",
        "jp_title": "便利さと引きかえに",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "コンビニやインターネットのおかげで、私たちの生活はずいぶん便利になった。夜中でも買い物ができるし、"
            "家から一歩も出ずに、ほしい物を手に入れることもできる。しかし、便利になればなるほど、"
            "私たちは待つことが苦手になってきたのではないだろうか。",
            "かつては、手紙の返事を何日も待つのが当たり前だった。待つ時間があったからこそ、相手のことをゆっくり考えることができたのだ。"
            "便利さと引きかえに、私たちはそうした時間を失いつつあるのかもしれない。",
        ],
        "en": [
            "Thanks to convenience stores and the internet, our lives have become much more convenient. We can shop in the middle "
            "of the night and get what we want without taking a single step outside. But isn't it true that the more convenient "
            "life becomes, the worse we get at waiting?",
            "In the past, waiting days for a reply to a letter was normal. It was precisely because we had that time to wait that "
            "we could think slowly about the other person. In exchange for convenience, we may be losing that kind of time.",
        ],
        "questions": [
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "生活は、もっと便利になるべきだ。",
                    "便利になったことで、待つ時間の価値が失われつつある。",
                    "手紙はメールより早く届くので、便利だ。",
                    "夜中に買い物をするのは、よくない。",
                ],
                "answer": 1,
                "why": "便利さと引きかえに、私たちはそうした時間を失いつつある: in exchange for convenience we're losing the time "
                       "that waiting gave us to think about others.",
            },
        ],
        "vocab": [
            {"word": "引きかえ", "reading": "ひきかえ", "meaning": "exchange (〜と引きかえに = in exchange for)"},
            {"word": "手に入れる", "reading": "てにいれる", "meaning": "to get, obtain"},
            {"word": "苦手", "reading": "にがて", "meaning": "bad at, not good with"},
            {"word": "かつて", "reading": "かつて", "meaning": "once, in the past"},
            {"word": "当たり前", "reading": "あたりまえ", "meaning": "natural, normal"},
            {"word": "失う", "reading": "うしなう", "meaning": "to lose"},
        ],
    },
    {
        "id": "n2-r04",
        "title": "How to praise children",
        "jp_title": "ほめること",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "子供を育てるうえで、ほめることが大切だとよく言われる。確かに、ほめられれば子供はやる気になる。"
            "しかし、何でも「すごいね」とほめればいいというものではない。",
            "結果だけをほめていると、子供は失敗を恐れて、難しいことに挑戦しなくなるおそれがある。大切なのは、結果ではなく、"
            "努力した過程をほめることだ。そうすれば、子供はうまくいかなかったときでも、もう一度頑張ろうと思えるようになる。",
        ],
        "en": [
            "It's often said that praise is important in raising children. It's true that children feel motivated when they're "
            "praised. But that doesn't mean you should say \"amazing!\" about everything.",
            "If you only praise results, children may become afraid of failing and stop taking on difficult things. What matters "
            "is to praise the effort they put in, not the result. Then, even when things don't go well, children can feel like "
            "trying again.",
        ],
        "questions": [
            {
                "q": "筆者が最も言いたいことは何か。",
                "choices": [
                    "子供は、できるだけたくさんほめたほうがいい。",
                    "子供をほめると、やる気がなくなる。",
                    "結果より、努力した過程をほめるべきだ。",
                    "失敗した子供は、ほめないほうがいい。",
                ],
                "answer": 2,
                "why": "大切なのは、結果ではなく、努力した過程をほめることだ. Praise isn't bad, but praising everything or only "
                       "results is.",
            },
        ],
        "vocab": [
            {"word": "やる気", "reading": "やるき", "meaning": "motivation"},
            {"word": "恐れる", "reading": "おそれる", "meaning": "to fear"},
            {"word": "過程", "reading": "かてい", "meaning": "process"},
            {"word": "頑張る", "reading": "がんばる", "meaning": "to try hard"},
            {"word": "ほめる", "reading": "ほめる", "meaning": "to praise"},
        ],
    },
    {
        "id": "n2-r05",
        "title": "Language changes",
        "jp_title": "言葉の変化",
        "kind": "Medium passage",
        "minutes": 8,
        "text": [
            "「最近の若者の言葉は乱れている」という意見を、よく耳にする。たとえば、「全然いい」のように、本来は否定の言葉と一緒に使う"
            "「全然」を、肯定の意味で使う人が増えている。こうした使い方に、違和感を覚える人も少なくないだろう。",
            "しかし、言葉は時代とともに変化するものだ。実は、明治時代の小説には、「全然」を肯定の意味で使った例がいくつもあるという。"
            "つまり、今「正しい」とされている使い方も、昔から決まっていたわけではないのである。",
            "もちろん、改まった場面では、相手に合わせた言葉づかいをする必要がある。だが、新しい表現をすぐに「間違いだ」と"
            "決めつけるのではなく、言葉が変わっていく様子を楽しむくらいの余裕を持ちたいものだ。",
        ],
        "en": [
            "We often hear the opinion that \"young people's language is a mess these days\". For example, more and more people "
            "use 全然 (\"not at all\"), which is originally used with negative words, in a positive sense, as in 全然いい "
            "(\"totally fine\"). Quite a few people probably feel this usage sounds wrong.",
            "But language changes with the times. In fact, it's said that novels from the Meiji era contain several examples of "
            "全然 used positively. In other words, even the usage considered \"correct\" today wasn't fixed from the start.",
            "Of course, in formal situations we need to choose our words to suit the other person. But rather than immediately "
            "labelling new expressions \"wrong\", I'd like us to be relaxed enough to enjoy watching language change.",
        ],
        "questions": [
            {
                "q": "「全然」について、筆者はどのように述べているか。",
                "choices": [
                    "昔から、否定の言葉と一緒にしか使われなかった。",
                    "昔の小説にも、肯定の意味で使った例がある。",
                    "若者だけが、間違った使い方をしている。",
                    "明治時代に、初めて使われるようになった。",
                ],
                "answer": 1,
                "why": "明治時代の小説には、「全然」を肯定の意味で使った例がいくつもある: Meiji-era novels already used it positively.",
            },
            {
                "q": "「余裕を持ちたい」とあるが、どういうことか。",
                "choices": [
                    "新しい表現を、使わないようにしたい。",
                    "言葉の変化を、広い心で受け入れたい。",
                    "改まった場面でも、若者の言葉を使いたい。",
                    "言葉を勉強する時間を、もっと作りたい。",
                ],
                "answer": 1,
                "why": "余裕 here means having the composure to enjoy change instead of calling new usage wrong at once "
                       "(すぐに「間違いだ」と決めつけるのではなく).",
            },
            {
                "q": "筆者の考えに合うものはどれか。",
                "choices": [
                    "言葉は、変化しないほうがいい。",
                    "場面に合わせた言葉づかいは、必要ない。",
                    "新しい言葉の使い方を、すぐに間違いだと決めつけるべきではない。",
                    "若者の言葉は乱れているので、直すべきだ。",
                ],
                "answer": 2,
                "why": "The writer accepts change, still values suiting words to formal situations, and argues against immediately "
                       "calling new usage wrong.",
            },
        ],
        "vocab": [
            {"word": "乱れる", "reading": "みだれる", "meaning": "to be in disorder"},
            {"word": "本来", "reading": "ほんらい", "meaning": "originally, by nature"},
            {"word": "否定", "reading": "ひてい", "meaning": "negation, denial"},
            {"word": "肯定", "reading": "こうてい", "meaning": "affirmation"},
            {"word": "違和感", "reading": "いわかん", "meaning": "sense that something is off"},
            {"word": "決めつける", "reading": "きめつける", "meaning": "to jump to a conclusion, label"},
            {"word": "余裕", "reading": "よゆう", "meaning": "room; composure"},
        ],
    },
    {
        "id": "n2-r06",
        "title": "Eating alone",
        "jp_title": "一人で食事をすること",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "以前は、一人で外食をすると「友達がいないのか」と思われるのではないかと、気にする人が多かった。"
            "しかし最近は、一人用の席を用意するレストランが増え、一人で食事を楽しむ人の姿も珍しくなくなった。",
            "一人で食事をする良さは、何といっても自由なことだ。食べたい物を、食べたいときに、自分のペースで食べられる。"
            "だれかに気をつかう必要もない。忙しい毎日の中で、一人の時間を大切にしたいと考える人が増えているのだろう。",
            "一方で、家族や友人と食卓を囲む時間には、一人では得られない楽しさがある。大切なのは、どちらか一方だけを選ぶのではなく、"
            "その日の気分や状況に応じて、上手に使い分けることではないだろうか。",
        ],
        "en": [
            "In the past, many people worried that if they ate out alone, others would think \"Doesn't this person have any "
            "friends?\". But recently more restaurants have seats for one, and people enjoying a meal alone are no longer unusual.",
            "The great thing about eating alone is, above all, the freedom. You can eat what you want, when you want, at your own "
            "pace, and you don't need to worry about anyone else. More people probably want to value time alone in their busy days.",
            "On the other hand, sitting around the table with family or friends brings a kind of enjoyment you can't get alone. "
            "Isn't the important thing not to choose only one, but to switch between them depending on your mood and the situation?",
        ],
        "questions": [
            {
                "q": "最近の変化として、本文に書かれていることはどれか。",
                "choices": [
                    "一人で食事をする人が減っている。",
                    "一人用の席を用意する店が増えている。",
                    "友達と外食する人がいなくなった。",
                    "レストランの数が減っている。",
                ],
                "answer": 1,
                "why": "一人用の席を用意するレストランが増え: more restaurants offer seats for one.",
            },
            {
                "q": "筆者は、一人で食事をする良さは何だと言っているか。",
                "choices": [
                    "料金が安いこと",
                    "新しい友達ができること",
                    "自分の好きなように食べられること",
                    "早く食べ終わること",
                ],
                "answer": 2,
                "why": "何といっても自由なこと: you can eat what you like, when you like, at your own pace.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "食事は、いつも家族と一緒にするべきだ。",
                    "一人の食事と大勢での食事を、状況に応じて使い分けるのがいい。",
                    "一人で食事をするのは寂しいので、やめたほうがいい。",
                    "忙しい人は、一人で食事をするしかない。",
                ],
                "answer": 1,
                "why": "どちらか一方だけを選ぶのではなく…状況に応じて、上手に使い分ける: switch between the two as the situation suits.",
            },
        ],
        "vocab": [
            {"word": "姿", "reading": "すがた", "meaning": "figure, sight (of someone)"},
            {"word": "何といっても", "reading": "なんといっても", "meaning": "above all, after all"},
            {"word": "気をつかう", "reading": "きをつかう", "meaning": "to be considerate, worry about others"},
            {"word": "食卓", "reading": "しょくたく", "meaning": "dining table"},
            {"word": "囲む", "reading": "かこむ", "meaning": "to surround, sit around"},
            {"word": "使い分ける", "reading": "つかいわける", "meaning": "to use each appropriately"},
        ],
    },
    {
        "id": "n2-r07",
        "title": "English in primary school",
        "jp_title": "小学校の英語教育",
        "kind": "Comparison (A/B)",
        "minutes": 6,
        "text": [
            "A\n小学校から英語を学ぶことには、大きな意味があると思う。子供は耳がいいので、小さいうちから英語の音に慣れておけば、"
            "自然な発音が身につきやすい。また、早い時期に外国の文化に触れることは、世界に目を向けるきっかけにもなるだろう。",
            "B\n小学校で英語を教えることには、慎重であるべきだ。まずは母語である日本語で、しっかり考え、表現する力を育てることが"
            "大切である。それに、英語を教えられる先生が十分にいないまま授業を増やしても、効果は期待できないのではないか。",
        ],
        "en": [
            "A\nI think learning English from primary school is very worthwhile. Children have good ears, so if they get used to the "
            "sounds of English while they're young, they pick up natural pronunciation more easily. Coming into contact with "
            "foreign cultures early can also be a first step towards looking out at the world.",
            "B\nWe should be careful about teaching English in primary school. First, it's important to develop the ability to think "
            "and express oneself properly in Japanese, the mother tongue. Besides, if we add more lessons without enough teachers "
            "who can teach English, can we really expect results?",
        ],
        "questions": [
            {
                "q": "AとBは、小学校での英語教育について、どのように述べているか。",
                "choices": [
                    "AもBも、早く始めたほうがいいと述べている。",
                    "Aは良い点を挙げて賛成し、Bは問題点を挙げて慎重な考えを示している。",
                    "AもBも、先生が足りないことを問題にしている。",
                    "Aは発音より文化が大切だと述べ、Bは文化より発音が大切だと述べている。",
                ],
                "answer": 1,
                "why": "A lists benefits (pronunciation, culture) and is in favour; B raises problems (mother tongue first, too few "
                       "teachers) and urges caution (慎重であるべきだ). Only B mentions the teacher shortage.",
            },
            {
                "q": "Bの筆者が、まず大切だと考えていることは何か。",
                "choices": [
                    "英語の発音を身につけること",
                    "外国の文化に触れること",
                    "日本語で考え、表現する力を育てること",
                    "英語の授業を増やすこと",
                ],
                "answer": 2,
                "why": "まずは母語である日本語で、しっかり考え、表現する力を育てることが大切である.",
            },
        ],
        "vocab": [
            {"word": "発音", "reading": "はつおん", "meaning": "pronunciation"},
            {"word": "身につく", "reading": "みにつく", "meaning": "to be acquired, learned"},
            {"word": "触れる", "reading": "ふれる", "meaning": "to come into contact with"},
            {"word": "慎重", "reading": "しんちょう", "meaning": "careful, cautious"},
            {"word": "母語", "reading": "ぼご", "meaning": "mother tongue"},
            {"word": "期待", "reading": "きたい", "meaning": "expectation"},
        ],
    },
    {
        "id": "n2-r08",
        "title": "How to enjoy a trip",
        "jp_title": "旅の楽しみ方",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "旅行に行く前に、細かく計画を立てる人がいる。どの電車に乗り、何時にどこを見て、どの店で食事をするか、すべて決めておくのだ。"
            "こうすれば、時間を無駄にせずに、見たい所を全部回ることができる。",
            "私も以前はそうだった。しかし、ある旅行で、乗る予定の電車が止まってしまい、計画がすべてだめになったことがある。"
            "仕方なく駅の近くを歩いていると、観光客がほとんど来ない小さな町を見つけた。地元の人が勧めてくれた食堂の料理は、"
            "ガイドブックに載っているどの店よりもおいしかった。",
            "それ以来、私は旅の計画に、あえて何も決めない時間を作るようにしている。予定どおりに進む旅は安心だが、"
            "思いがけない出会いこそが、旅を忘れられないものにしてくれると思うからだ。",
        ],
        "en": [
            "Some people plan their trips in detail before they go. Which trains to take, what to see when, which restaurants to eat "
            "at: they decide everything in advance. That way, they can see everything they want without wasting time.",
            "I used to be like that too. But once, on a trip, the train I'd planned to take stopped running, and my whole plan fell "
            "apart. With nothing else to do, I walked around near the station and found a small town that tourists hardly ever "
            "visit. The food at a little diner a local recommended was better than any restaurant in the guidebook.",
            "Since then, I deliberately leave time with nothing planned on my trips. A trip that goes to plan is reassuring, but I "
            "think it's the unexpected encounters that make a trip unforgettable.",
        ],
        "questions": [
            {
                "q": "筆者の計画が「すべてだめになった」のは、なぜか。",
                "choices": [
                    "乗る予定の電車が止まってしまったから",
                    "天気が悪かったから",
                    "計画を立てるのを忘れたから",
                    "町が観光客でいっぱいだったから",
                ],
                "answer": 0,
                "why": "乗る予定の電車が止まってしまい、計画がすべてだめになった.",
            },
            {
                "q": "筆者は、小さな町でどんな経験をしたか。",
                "choices": [
                    "ガイドブックに載っている店で食事をした。",
                    "地元の人に勧められた店の料理が、とてもおいしかった。",
                    "観光客と友達になった。",
                    "電車が動くまで、駅で待っていた。",
                ],
                "answer": 1,
                "why": "地元の人が勧めてくれた食堂の料理は、ガイドブックに載っているどの店よりもおいしかった.",
            },
            {
                "q": "筆者は今、旅行についてどう考えているか。",
                "choices": [
                    "時間を無駄にしないように、細かく計画を立てるべきだ。",
                    "計画は立てずに、すべて自由に行動するべきだ。",
                    "計画の中に、何も決めない時間を作るといい。",
                    "有名な観光地だけを回るのがいい。",
                ],
                "answer": 2,
                "why": "旅の計画に、あえて何も決めない時間を作るようにしている: the writer still plans, but leaves some time free. "
                       "Choice 2 goes too far (no plan at all).",
            },
        ],
        "vocab": [
            {"word": "無駄", "reading": "むだ", "meaning": "waste"},
            {"word": "地元", "reading": "じもと", "meaning": "local"},
            {"word": "食堂", "reading": "しょくどう", "meaning": "diner, canteen"},
            {"word": "載る", "reading": "のる", "meaning": "to appear (in print)"},
            {"word": "あえて", "reading": "あえて", "meaning": "deliberately, on purpose"},
            {"word": "思いがけない", "reading": "おもいがけない", "meaning": "unexpected"},
        ],
    },
    {
        "id": "n2-r09",
        "title": "Summer events at the library",
        "jp_title": "図書館の夏休みイベント",
        "kind": "Information search",
        "minutes": 6,
        "text": [
            "みどり市立図書館　夏休みイベントのご案内",
            "①おはなし会（対象：3歳〜小学2年生）\n"
            "・7月27日（土）、8月10日（土）　午前10時30分〜11時\n"
            "・申し込み不要。当日、直接2階の子どもコーナーへお越しください。",
            "②自由研究お助け講座（対象：小学3年生〜6年生）\n"
            "・8月3日（土）　午後1時〜3時\n"
            "・定員20名（先着順）。7月20日から、図書館のカウンターまたは電話でお申し込みください。",
            "③英語の絵本を読もう（対象：小学生とその保護者）\n"
            "・8月17日（土）　午後2時〜3時\n"
            "・定員15組（申し込みが多い場合は抽選）。7月31日までに、図書館のホームページからお申し込みください。",
            "※いずれも参加費は無料です。駐車場には限りがありますので、できるだけ公共交通機関をご利用ください。",
        ],
        "en": [
            "Midori City Library: summer holiday events",
            "1. Storytime (ages 3 to year 2 of primary school)\n"
            "- Saturday 27 July and Saturday 10 August, 10:30 to 11 a.m.\n"
            "- No sign-up needed. On the day, come straight to the children's corner on the 2nd floor.",
            "2. Help with your summer research project (years 3 to 6 of primary school)\n"
            "- Saturday 3 August, 1 to 3 p.m.\n"
            "- 20 places (first come, first served). Sign up from 20 July at the library counter or by phone.",
            "3. Let's read English picture books (primary school children and their parents)\n"
            "- Saturday 17 August, 2 to 3 p.m.\n"
            "- 15 pairs (a lottery if there are many applications). Sign up on the library website by 31 July.",
            "* All events are free. Parking is limited, so please use public transport where possible.",
        ],
        "questions": [
            {
                "q": "小学4年生のけんたくんは、夏休みの宿題の自由研究について相談できるイベントに参加したい。どうすればいいか。",
                "choices": [
                    "当日、直接2階の子どもコーナーへ行く。",
                    "7月20日以降に、カウンターか電話で申し込む。",
                    "7月31日までに、ホームページから申し込む。",
                    "申し込みをして、抽選の結果を待つ。",
                ],
                "answer": 1,
                "why": "The research-project event (②) is for years 3 to 6, and sign-up opens on 20 July at the counter or by "
                       "phone (7月20日から). The other methods belong to events ① and ③.",
            },
            {
                "q": "このお知らせの内容と合っているものはどれか。",
                "choices": [
                    "イベントによっては、参加費がかかる。",
                    "③のイベントは、申し込んだ人が全員参加できる。",
                    "①のイベントは、申し込みをしなくても参加できる。",
                    "図書館の駐車場は、いつでも十分に空いている。",
                ],
                "answer": 2,
                "why": "① says 申し込み不要 (no sign-up needed). All events are free, ③ may hold a lottery, and parking is limited.",
            },
        ],
        "vocab": [
            {"word": "対象", "reading": "たいしょう", "meaning": "intended for, target group"},
            {"word": "不要", "reading": "ふよう", "meaning": "not needed"},
            {"word": "定員", "reading": "ていいん", "meaning": "capacity, number of places"},
            {"word": "先着順", "reading": "せんちゃくじゅん", "meaning": "first come, first served"},
            {"word": "抽選", "reading": "ちゅうせん", "meaning": "lottery, draw"},
            {"word": "公共交通機関", "reading": "こうきょうこうつうきかん", "meaning": "public transport"},
        ],
    },
    {
        "id": "n2-r10",
        "title": "Machine translation and learning languages",
        "jp_title": "機械翻訳と語学学習",
        "kind": "Medium passage",
        "minutes": 8,
        "text": [
            "最近の機械翻訳は、驚くほど性能が上がった。スマートフォンに話しかけるだけで、外国語に訳してくれるアプリもある。"
            "そのため、「もう外国語を勉強する必要はない」と考える人もいるようだ。",
            "確かに、旅行先で道を聞いたり、買い物をしたりする程度なら、機械翻訳で十分かもしれない。しかし、言葉には、"
            "その国の文化や考え方が深く結びついている。冗談の面白さや、遠回しな言い方に込められた気持ちまで、"
            "機械が正確に伝えられるとは限らない。",
            "外国語を学ぶことは、単に言葉を覚えることではなく、別の文化を持つ人の見方を知ることでもある。機械翻訳は便利な道具として"
            "上手に使いつつも、自分の言葉で相手と向き合う努力を続けたいものだ。",
        ],
        "en": [
            "Machine translation has improved surprisingly in recent years. There are even apps that translate into a foreign "
            "language just by speaking to your smartphone. Because of this, some people seem to think there's no need to study "
            "foreign languages any more.",
            "It's true that for asking the way or shopping while travelling, machine translation may be enough. But language is "
            "deeply tied to a country's culture and way of thinking. A machine can't always convey exactly what makes a joke "
            "funny, or the feelings packed into an indirect way of saying something.",
            "Learning a foreign language isn't simply memorising words; it's also learning how people from another culture see "
            "things. While making good use of machine translation as a handy tool, I want to keep making the effort to engage "
            "with others in my own words.",
        ],
        "questions": [
            {
                "q": "筆者によると、機械翻訳で十分なのはどんな場合か。",
                "choices": [
                    "冗談を言うとき",
                    "旅行先で、簡単な会話をするとき",
                    "外国の文化を学ぶとき",
                    "遠回しな言い方を理解するとき",
                ],
                "answer": 1,
                "why": "旅行先で道を聞いたり、買い物をしたりする程度なら、機械翻訳で十分かもしれない.",
            },
            {
                "q": "「機械が正確に伝えられるとは限らない」とあるが、なぜか。",
                "choices": [
                    "機械翻訳の性能が、まだ低いから",
                    "スマートフォンでしか使えないから",
                    "言葉には、文化や考え方が深く結びついているから",
                    "外国語を話す人が少ないから",
                ],
                "answer": 2,
                "why": "The sentence before gives the reason: 言葉には、その国の文化や考え方が深く結びついている. "
                       "The writer actually says performance has improved a lot.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "機械翻訳があれば、外国語を勉強する必要はない。",
                    "機械翻訳は、使わないほうがいい。",
                    "機械翻訳を上手に使いながらも、外国語を学ぶ努力を続けたい。",
                    "外国語は、旅行に行く人だけが学べばいい。",
                ],
                "answer": 2,
                "why": "機械翻訳は便利な道具として上手に使いつつも、自分の言葉で相手と向き合う努力を続けたい.",
            },
        ],
        "vocab": [
            {"word": "翻訳", "reading": "ほんやく", "meaning": "translation"},
            {"word": "性能", "reading": "せいのう", "meaning": "performance (of a machine)"},
            {"word": "訳す", "reading": "やくす", "meaning": "to translate"},
            {"word": "結びつく", "reading": "むすびつく", "meaning": "to be tied to, connected"},
            {"word": "冗談", "reading": "じょうだん", "meaning": "joke"},
            {"word": "遠回し", "reading": "とおまわし", "meaning": "roundabout, indirect"},
            {"word": "単に", "reading": "たんに", "meaning": "simply, merely"},
        ],
    },
    {
        "id": "n2-r11",
        "title": "Clearing the bicycle shed",
        "jp_title": "自転車置き場の整理について",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "住民の皆様へ",
            "自転車置き場に、長い間使われていないと思われる自転車が増えております。そこで、下記のとおり整理を行うことになりました。",
            "引き続きご利用になる自転車には、管理事務所でお配りしている黄色いシールを、5月20日までに貼ってください。"
            "シールが貼られていない自転車は、5月末に処分させていただきます。",
            "なお、シールは一つの世帯につき二枚までとさせていただきます。",
            "管理事務所",
        ],
        "en": [
            "To all residents,",
            "There are more and more bicycles in the bicycle shed that seem not to have been used for a long time. We have therefore "
            "decided to clear the shed as set out below.",
            "If you will continue using your bicycle, please put one of the yellow stickers handed out at the management office on it "
            "by 20 May. Bicycles without a sticker will be disposed of at the end of May.",
            "Please note that each household may have up to two stickers.",
            "Management office",
        ],
        "questions": [
            {
                "q": "自転車置き場を使い続けたい人は、どうしなければならないか。",
                "choices": [
                    "5月末までに、自転車を別の場所に移す。",
                    "5月20日までに、自転車にシールを貼る。",
                    "管理事務所に、使っている自転車の数を知らせる。",
                    "新しい自転車を買って、登録する。",
                ],
                "answer": 1,
                "why": "引き続きご利用になる自転車には…5月20日までに貼ってください. The end of May is when unmarked bikes are removed.",
            },
        ],
        "vocab": [
            {"word": "住民", "reading": "じゅうみん", "meaning": "resident"},
            {"word": "整理", "reading": "せいり", "meaning": "sorting out, clearing"},
            {"word": "引き続き", "reading": "ひきつづき", "meaning": "continuing, still"},
            {"word": "貼る", "reading": "はる", "meaning": "to stick (on)"},
            {"word": "処分", "reading": "しょぶん", "meaning": "disposal"},
            {"word": "世帯", "reading": "せたい", "meaning": "household"},
        ],
    },
    {
        "id": "n2-r12",
        "title": "Changing a hotel booking",
        "jp_title": "ご予約内容の変更について",
        "kind": "Short passage",
        "minutes": 3,
        "text": [
            "件名：ご予約内容の変更について",
            "田中様",
            "このたびは、ホテルみどりをご予約いただき、ありがとうございます。お問い合わせいただいた、ご宿泊日の変更についてご連絡いたします。",
            "ご希望の7月15日は、あいにく和室が満室となっております。洋室でしたらご用意できますが、料金が一泊につき二千円高くなります。"
            "洋室でよろしければ、7月5日までにお電話にてお知らせください。期日までにご連絡がない場合は、元のご予約のままとさせていただきます。",
            "ホテルみどり　予約係",
        ],
        "en": [
            "Subject: About changing your booking",
            "Dear Mr./Ms. Tanaka,",
            "Thank you for booking with Hotel Midori. We are writing about your inquiry on changing the date of your stay.",
            "Unfortunately, the Japanese-style rooms are fully booked on 15 July, the date you requested. We can offer a Western-style "
            "room, but it costs 2,000 yen more per night. If a Western-style room is acceptable, please let us know by phone by 5 July. "
            "If we don't hear from you by then, your original booking will stay as it is.",
            "Hotel Midori, reservations",
        ],
        "questions": [
            {
                "q": "このメールの内容と合っているものはどれか。",
                "choices": [
                    "7月15日は、和室に泊まることができる。",
                    "洋室に変更すると、料金が安くなる。",
                    "連絡をしなければ、予約は元の日のままになる。",
                    "洋室への変更は、メールで申し込む。",
                ],
                "answer": 2,
                "why": "期日までにご連絡がない場合は、元のご予約のまま. The Japanese rooms are full, the Western room costs more, "
                       "and the change must be made by phone (お電話にて).",
            },
        ],
        "vocab": [
            {"word": "問い合わせ", "reading": "といあわせ", "meaning": "inquiry"},
            {"word": "宿泊", "reading": "しゅくはく", "meaning": "staying (at a hotel)"},
            {"word": "あいにく", "reading": "あいにく", "meaning": "unfortunately"},
            {"word": "満室", "reading": "まんしつ", "meaning": "fully booked (rooms)"},
            {"word": "洋室", "reading": "ようしつ", "meaning": "Western-style room"},
            {"word": "期日", "reading": "きじつ", "meaning": "set date, deadline"},
        ],
    },
    {
        "id": "n2-r13",
        "title": "Comparing yourself with others",
        "jp_title": "人と比べること",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "私たちはつい、自分を他人と比べてしまう。友人が自分より良い成績を取ったり、楽しそうな旅行の写真を投稿したりしているのを見ると、"
            "自分だけが取り残されたような気持ちになる。",
            "しかし、比べる相手は他人ではなく、過去の自分であるべきではないだろうか。一年前にはできなかったことが、今はできるようになっている。"
            "そうした小さな成長に目を向けることが、自信につながるのだと思う。",
        ],
        "en": [
            "We can't help comparing ourselves with others. When we see a friend get better grades than us, or post photos of a fun "
            "trip, we feel as if we alone have been left behind.",
            "But shouldn't the person we compare ourselves with be our past self, not other people? Things we couldn't do a year ago, "
            "we can do now. I think paying attention to that kind of small growth is what builds confidence.",
        ],
        "questions": [
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "友人と比べることで、もっと頑張れる。",
                    "自分の成長は、過去の自分と比べて考えたほうがいい。",
                    "旅行の写真は、投稿しないほうがいい。",
                    "他人より良い成績を取ることが、自信につながる。",
                ],
                "answer": 1,
                "why": "比べる相手は他人ではなく、過去の自分であるべき, and small growth is what builds confidence.",
            },
        ],
        "vocab": [
            {"word": "他人", "reading": "たにん", "meaning": "other people"},
            {"word": "投稿", "reading": "とうこう", "meaning": "posting (online)"},
            {"word": "取り残す", "reading": "とりのこす", "meaning": "to leave behind"},
            {"word": "過去", "reading": "かこ", "meaning": "the past"},
            {"word": "成長", "reading": "せいちょう", "meaning": "growth"},
            {"word": "つながる", "reading": "つながる", "meaning": "to lead to, be connected"},
        ],
    },
    {
        "id": "n2-r14",
        "title": "Saying hello",
        "jp_title": "あいさつ",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "引っ越してきたばかりのころ、近所の人にあいさつをしても、返事が返ってこないことがあった。都会では、"
            "人と関わりたくない人も多いのだろうと、少し寂しく思った。",
            "それでも、毎朝あいさつを続けていると、半年ほどたったころから、向こうから声をかけてくれる人が増えてきた。"
            "今では、旅行のお土産を交換するほどの仲になった人もいる。人間関係は、一度で築けるものではない。小さな積み重ねが大切なのだ。",
        ],
        "en": [
            "When I had just moved here, sometimes I'd say hello to my neighbours and get no reply. I felt a little lonely, thinking "
            "that in the city many people probably don't want to get involved with others.",
            "Even so, I kept saying hello every morning, and after about six months more and more people started greeting me first. "
            "Now there are even people I'm close enough to that we swap souvenirs from our trips. Relationships can't be built in one "
            "go. It's the small things, added up, that matter.",
        ],
        "questions": [
            {
                "q": "筆者が最も言いたいことは何か。",
                "choices": [
                    "都会の人は、あいさつをしない。",
                    "人間関係は、少しずつ作っていくものだ。",
                    "近所の人とは、関わらないほうがいい。",
                    "お土産を渡せば、すぐに仲良くなれる。",
                ],
                "answer": 1,
                "why": "人間関係は、一度で築けるものではない。小さな積み重ねが大切: relationships are built bit by bit.",
            },
        ],
        "vocab": [
            {"word": "関わる", "reading": "かかわる", "meaning": "to get involved with"},
            {"word": "声をかける", "reading": "こえをかける", "meaning": "to speak to, greet"},
            {"word": "交換", "reading": "こうかん", "meaning": "exchange"},
            {"word": "人間関係", "reading": "にんげんかんけい", "meaning": "relationships"},
            {"word": "築く", "reading": "きずく", "meaning": "to build"},
            {"word": "積み重ね", "reading": "つみかさね", "meaning": "accumulation, building up"},
        ],
    },
    {
        "id": "n2-r15",
        "title": "Morning people and night people",
        "jp_title": "朝型と夜型",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "「早起きは三文の徳」ということわざがあるように、日本では昔から、朝早く起きることが良いこととされてきた。"
            "最近も、朝の時間を勉強や運動に使う「朝活」が人気を集めている。",
            "しかし、だれもが朝型の生活に向いているわけではない。人によって、体のリズムには違いがあることが分かってきた。"
            "夜になると頭がよく働く人が無理に早起きをしても、かえって一日中眠くて、集中できないということもあるそうだ。",
            "大切なのは、世間で良いとされている方法をそのまま取り入れることではなく、自分の体に合った生活のリズムを見つけることだろう。"
            "朝型でも夜型でも、自分が最も力を発揮できる時間を知っておくことが大切なのである。",
        ],
        "en": [
            "As the proverb \"the early riser gains three coins\" suggests, getting up early has long been considered a good thing in "
            "Japan. Recently, \"asakatsu\", using the morning for study or exercise, has also become popular.",
            "But not everyone is suited to a morning lifestyle. It has become clear that body rhythms differ from person to person. "
            "Apparently, when people whose minds work best at night force themselves to get up early, they can end up sleepy all day "
            "and unable to concentrate.",
            "What matters is probably not adopting whatever method society considers good, but finding a daily rhythm that suits your "
            "own body. Whether you're a morning or a night person, the important thing is to know when you can perform at your best.",
        ],
        "questions": [
            {
                "q": "「朝活」とは、どのようなことか。",
                "choices": [
                    "朝早く起きて、勉強や運動をすること",
                    "朝ご飯をしっかり食べること",
                    "夜遅くまで勉強すること",
                    "朝早く出かけて、買い物をすること",
                ],
                "answer": 0,
                "why": "朝の時間を勉強や運動に使う「朝活」: using the morning for study or exercise.",
            },
            {
                "q": "筆者によると、夜型の人が無理に早起きすると、どうなることがあるか。",
                "choices": [
                    "体のリズムが、朝型に変わる。",
                    "一日中眠くて、集中できない。",
                    "夜、早く眠れるようになる。",
                    "朝の時間を、有効に使える。",
                ],
                "answer": 1,
                "why": "かえって一日中眠くて、集中できないということもある.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "だれでも、朝型の生活をするべきだ。",
                    "夜型の生活のほうが、効率がいい。",
                    "自分の体に合った生活のリズムを見つけることが大切だ。",
                    "ことわざに従って、生活するべきだ。",
                ],
                "answer": 2,
                "why": "大切なのは…自分の体に合った生活のリズムを見つけること. The writer doesn't favour either type.",
            },
        ],
        "vocab": [
            {"word": "ことわざ", "reading": "ことわざ", "meaning": "proverb"},
            {"word": "朝活", "reading": "あさかつ", "meaning": "morning activities (study, exercise)"},
            {"word": "向く", "reading": "むく", "meaning": "to be suited to"},
            {"word": "世間", "reading": "せけん", "meaning": "society, the world"},
            {"word": "取り入れる", "reading": "とりいれる", "meaning": "to adopt, take in"},
            {"word": "発揮", "reading": "はっき", "meaning": "showing (one's ability)"},
        ],
    },
    {
        "id": "n2-r16",
        "title": "Saving the local railway",
        "jp_title": "町の鉄道を守る",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "私が住んでいる町には、一時間に一本しか電車が来ない小さな鉄道がある。利用者は年々減り続け、数年前には廃止の話も出た。",
            "そこで、町の人たちが立ち上がった。駅に花を植えたり、電車の中で地元の野菜を売る「マルシェ列車」を走らせたりしたのだ。"
            "すると、そうした取り組みがテレビで紹介され、休日には遠くから観光客が訪れるようになった。",
            "もちろん、観光客だけで鉄道を支えるのは難しい。ふだんから地元の人が利用しなければ、いずれまた同じ問題が起きるだろう。"
            "鉄道を守るということは、結局、自分たちの町の暮らしを考えることなのだと思う。",
        ],
        "en": [
            "My town has a small railway with only one train an hour. The number of passengers fell year after year, and a few years "
            "ago there was even talk of closing it.",
            "So the townspeople took action. They planted flowers at the stations and ran a \"market train\" selling local vegetables "
            "on board. These efforts were then featured on TV, and now tourists come from far away on holidays.",
            "Of course, it's hard to keep a railway going on tourists alone. If local people don't use it in everyday life, the same "
            "problem will come back sooner or later. In the end, I think protecting the railway means thinking about life in our own town.",
        ],
        "questions": [
            {
                "q": "町の人たちは、なぜ取り組みを始めたのか。",
                "choices": [
                    "テレビで紹介されたかったから",
                    "鉄道がなくなるかもしれなかったから",
                    "野菜がたくさん取れたから",
                    "観光客が多すぎたから",
                ],
                "answer": 1,
                "why": "Passengers kept falling and there was talk of closure (廃止の話も出た). そこで (so) they took action.",
            },
            {
                "q": "取り組みの結果、どうなったか。",
                "choices": [
                    "電車の本数が増えた。",
                    "地元の人が毎日電車を使うようになった。",
                    "休日に、遠くから人が来るようになった。",
                    "鉄道の廃止が決まった。",
                ],
                "answer": 2,
                "why": "休日には遠くから観光客が訪れるようになった. The writer actually worries that locals don't use it enough.",
            },
            {
                "q": "筆者は、鉄道を守るために何が必要だと考えているか。",
                "choices": [
                    "もっと観光客を増やすこと",
                    "テレビでたくさん紹介してもらうこと",
                    "地元の人が、ふだんから鉄道を利用すること",
                    "電車の中で、野菜を売り続けること",
                ],
                "answer": 2,
                "why": "観光客だけで鉄道を支えるのは難しい; ふだんから地元の人が利用しなければ the problem will return.",
            },
        ],
        "vocab": [
            {"word": "廃止", "reading": "はいし", "meaning": "abolition, closing down"},
            {"word": "立ち上がる", "reading": "たちあがる", "meaning": "to stand up; take action"},
            {"word": "植える", "reading": "うえる", "meaning": "to plant"},
            {"word": "訪れる", "reading": "おとずれる", "meaning": "to visit"},
            {"word": "支える", "reading": "ささえる", "meaning": "to support"},
            {"word": "結局", "reading": "けっきょく", "meaning": "in the end, after all"},
        ],
    },
    {
        "id": "n2-r17",
        "title": "Aiming for 80 percent",
        "jp_title": "まず八割",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "何事も完璧にやらないと気がすまない人がいる。私もその一人で、学生時代は、レポートの文章を何度も書き直し、"
            "締め切りぎりぎりまで提出できないことがよくあった。",
            "ある時、先生に「八割できたら、一度出してみなさい」と言われた。半信半疑で試してみると、意外なことに、評価はほとんど変わらなかった。"
            "それどころか、早めに出したことで先生から意見をもらえ、かえって良いものに仕上げることができたのだ。",
            "完璧を目指すこと自体は悪くない。だが、一人で百点を目指して時間をかけるより、早い段階で人の意見を聞いたほうが、"
            "結果的に良いものができることもある。それ以来、私は「まず八割」を心がけている。",
        ],
        "en": [
            "Some people aren't satisfied unless everything is perfect. I'm one of them: as a student, I'd rewrite my reports again "
            "and again and often couldn't hand them in until the very last minute.",
            "Once, a teacher told me, \"When it's 80 percent done, try handing it in.\" I tried it, half doubting, and to my surprise "
            "my grade hardly changed. What's more, handing it in early meant I got the teacher's comments, so I could actually make "
            "it better.",
            "Aiming for perfection isn't bad in itself. But rather than spending a long time alone aiming for full marks, asking for "
            "others' opinions at an early stage can lead to a better result. Since then, I've kept \"80 percent first\" in mind.",
        ],
        "questions": [
            {
                "q": "筆者は学生時代、どんな問題を抱えていたか。",
                "choices": [
                    "レポートの書き方が分からなかった。",
                    "完璧にしようとして、なかなか提出できなかった。",
                    "締め切りを忘れることが多かった。",
                    "先生の意見を聞かなかった。",
                ],
                "answer": 1,
                "why": "何度も書き直し、締め切りぎりぎりまで提出できない: rewriting for perfection kept the writer from handing in.",
            },
            {
                "q": "「八割できたら、一度出してみなさい」と言われて、筆者はどうなったか。",
                "choices": [
                    "評価が大きく下がった。",
                    "先生から意見をもらい、より良いものにできた。",
                    "完璧主義を、すぐにやめた。",
                    "半分しか書かないで、提出した。",
                ],
                "answer": 1,
                "why": "評価はほとんど変わらなかった, and 早めに出したことで先生から意見をもらえ、かえって良いものに仕上げることができた.",
            },
            {
                "q": "筆者の考えに合うものはどれか。",
                "choices": [
                    "完璧を目指すのは、悪いことだ。",
                    "一人で百点を目指すべきだ。",
                    "早めに人の意見を聞くと、良いものができることがある。",
                    "レポートは、締め切りぎりぎりに出したほうがいい。",
                ],
                "answer": 2,
                "why": "早い段階で人の意見を聞いたほうが、結果的に良いものができることもある. Aiming for perfection 自体は悪くない.",
            },
        ],
        "vocab": [
            {"word": "完璧", "reading": "かんぺき", "meaning": "perfect"},
            {"word": "気がすまない", "reading": "きがすまない", "meaning": "not satisfied (until)"},
            {"word": "提出", "reading": "ていしゅつ", "meaning": "handing in"},
            {"word": "半信半疑", "reading": "はんしんはんぎ", "meaning": "half doubting"},
            {"word": "評価", "reading": "ひょうか", "meaning": "evaluation, grade"},
            {"word": "心がける", "reading": "こころがける", "meaning": "to keep in mind, aim to"},
        ],
    },
    {
        "id": "n2-r18",
        "title": "School uniforms",
        "jp_title": "制服は必要か",
        "kind": "Comparison (A/B)",
        "minutes": 6,
        "text": [
            "A\n中学校や高校の制服には、良い点が多いと思う。毎朝、何を着ていくか悩む必要がないし、家庭の経済的な差も目立ちにくい。"
            "また、制服を着ることで、学校の一員であるという意識も生まれるだろう。",
            "B\n制服は、もう必要ないのではないか。決められた服を全員が着ることは、生徒一人一人の個性を大切にする考え方に合わない。"
            "それに、制服は値段が高く、成長の早い子供の場合、何度も買い直さなければならないという家庭の負担もある。",
        ],
        "en": [
            "A\nI think school uniforms at junior high and high school have many good points. Students don't have to worry every "
            "morning about what to wear, and differences in families' finances are less noticeable. Wearing a uniform also gives a "
            "sense of being part of the school.",
            "B\nAren't uniforms unnecessary now? Making everyone wear set clothes doesn't fit with valuing each student's "
            "individuality. Besides, uniforms are expensive, and children who grow fast need new ones again and again, which is a "
            "burden on families.",
        ],
        "questions": [
            {
                "q": "AとBのどちらも触れている点は何か。",
                "choices": [
                    "制服を着ると、学校への意識が高まること",
                    "制服と、家庭のお金の問題",
                    "毎朝、着る服を選ぶ楽しさ",
                    "生徒の個性を大切にすること",
                ],
                "answer": 1,
                "why": "A says uniforms hide differences in family finances (経済的な差); B says they are expensive to keep buying "
                       "(家庭の負担). Both mention money; the other points appear in only one text.",
            },
            {
                "q": "AとBは、制服について、どのように考えているか。",
                "choices": [
                    "AもBも、制服は必要だと考えている。",
                    "Aは制服に賛成で、Bは制服は必要ないと考えている。",
                    "Aは制服に反対で、Bは制服に賛成している。",
                    "AもBも、制服の値段を下げるべきだと考えている。",
                ],
                "answer": 1,
                "why": "A: 良い点が多い. B: もう必要ないのではないか.",
            },
        ],
        "vocab": [
            {"word": "制服", "reading": "せいふく", "meaning": "school uniform"},
            {"word": "悩む", "reading": "なやむ", "meaning": "to worry, agonise"},
            {"word": "経済的", "reading": "けいざいてき", "meaning": "economic, financial"},
            {"word": "目立つ", "reading": "めだつ", "meaning": "to stand out"},
            {"word": "個性", "reading": "こせい", "meaning": "individuality"},
            {"word": "負担", "reading": "ふたん", "meaning": "burden"},
        ],
    },
    {
        "id": "n2-r19",
        "title": "City marathon entry",
        "jp_title": "市民マラソン大会のご案内",
        "kind": "Information search",
        "minutes": 6,
        "text": [
            "第10回　さくら市民マラソン大会　参加者募集",
            "◆開催日：10月20日（日）　※雨天決行",
            "◆種目と参加費\n"
            "・10キロの部（高校生以上）：3,000円\n"
            "・5キロの部（中学生以上）：2,000円\n"
            "・親子ペアの部（2キロ・小学生とその保護者）：1組2,500円",
            "◆申し込み方法\n"
            "・インターネット：9月1日〜9月30日\n"
            "・郵便：9月1日〜9月20日（必着）\n"
            "※定員になり次第、締め切ります。",
            "◆注意\n"
            "・大会当日の申し込みはできません。\n"
            "・一度お支払いいただいた参加費は、どのような理由があってもお返しできません。",
        ],
        "en": [
            "10th Sakura City Marathon: entries wanted",
            "Date: Sunday 20 October. Held rain or shine.",
            "Races and entry fees\n"
            "- 10 km (high school students and over): 3,000 yen\n"
            "- 5 km (junior high school students and over): 2,000 yen\n"
            "- Parent-and-child pairs (2 km, a primary school child and their parent): 2,500 yen per pair",
            "How to enter\n"
            "- Online: 1 to 30 September\n"
            "- By post: 1 to 20 September (must arrive by then)\n"
            "* Entries close as soon as places are full.",
            "Please note\n"
            "- You cannot enter on the day.\n"
            "- Entry fees cannot be refunded for any reason once paid.",
        ],
        "questions": [
            {
                "q": "中学2年生のさきさんは、大学生の姉と同じ種目に出たいと思っている。二人が一緒に出られる種目と、二人分の参加費の合計は、どれか。",
                "choices": ["10キロの部・6,000円", "5キロの部・4,000円", "親子ペアの部・2,500円", "5キロの部・2,000円"],
                "answer": 1,
                "why": "A junior high student can't run 10 km (high school and over), and the pair race is for a primary school child "
                       "and a parent. So 5 km at 2,000 yen each: 4,000 yen.",
            },
            {
                "q": "申し込みについて、正しいものはどれか。",
                "choices": [
                    "郵便なら、9月30日まで申し込める。",
                    "大会当日に、会場で申し込める。",
                    "定員になると、期間中でも締め切られることがある。",
                    "雨で大会が中止になったら、参加費が返ってくる。",
                ],
                "answer": 2,
                "why": "定員になり次第、締め切ります. Post closes on 20 September, there's no entry on the day, and the race is held "
                       "rain or shine (雨天決行) with no refunds.",
            },
        ],
        "vocab": [
            {"word": "募集", "reading": "ぼしゅう", "meaning": "recruiting, call for entries"},
            {"word": "開催", "reading": "かいさい", "meaning": "holding (an event)"},
            {"word": "雨天決行", "reading": "うてんけっこう", "meaning": "held rain or shine"},
            {"word": "種目", "reading": "しゅもく", "meaning": "event, race category"},
            {"word": "必着", "reading": "ひっちゃく", "meaning": "must arrive by (a date)"},
            {"word": "定員", "reading": "ていいん", "meaning": "capacity, number of places"},
        ],
    },
    {
        "id": "n2-r20",
        "title": "Maps and getting lost",
        "jp_title": "地図アプリと道に迷うこと",
        "kind": "Medium passage",
        "minutes": 7,
        "text": [
            "スマートフォンの地図アプリのおかげで、知らない町でも道に迷うことはほとんどなくなった。目的地を入力すれば、"
            "最短の道を教えてくれるし、到着する時間まで分かる。",
            "ただ、最近ふと気がついた。アプリに頼るようになってから、町の様子をほとんど覚えていないのだ。画面の矢印ばかり見て歩いているので、"
            "どんな店があったか、どんな景色だったかが記憶に残らない。昔、紙の地図を見ながら迷った町のほうが、今でもはっきり思い出せるのは"
            "不思議なことだ。",
            "迷うことは、時間の無駄だと思われがちだ。しかし、迷いながら歩くからこそ、周りをよく見て、町を自分の体で覚えるのではないだろうか。"
            "急がない日には、あえてアプリを閉じて歩いてみるのも悪くない。",
        ],
        "en": [
            "Thanks to map apps on smartphones, I hardly ever get lost now, even in unfamiliar towns. Enter a destination and the app "
            "shows you the shortest route, and even when you'll arrive.",
            "But recently it suddenly struck me: since I started relying on the app, I barely remember what towns are like. Because I "
            "walk looking only at the arrow on the screen, I don't remember what shops there were or what the scenery was like. It's "
            "strange that I can still clearly remember towns where I got lost with a paper map long ago.",
            "Getting lost tends to be seen as a waste of time. But isn't it precisely because we wander while lost that we look "
            "around carefully and learn a town with our own bodies? On days when you're not in a hurry, it's not a bad idea to close "
            "the app on purpose and just walk.",
        ],
        "questions": [
            {
                "q": "筆者が「ふと気がついた」のは、どんなことか。",
                "choices": [
                    "地図アプリが、間違った道を教えること",
                    "アプリを使うと、町の様子を覚えていないこと",
                    "紙の地図のほうが、見やすいこと",
                    "最短の道が、一番いい道ではないこと",
                ],
                "answer": 1,
                "why": "アプリに頼るようになってから、町の様子をほとんど覚えていない.",
            },
            {
                "q": "筆者によると、迷いながら歩くと、どんな良さがあるか。",
                "choices": [
                    "早く目的地に着ける。",
                    "周りをよく見て、町を体で覚えられる。",
                    "新しいアプリを試せる。",
                    "時間を無駄にしなくてすむ。",
                ],
                "answer": 1,
                "why": "迷いながら歩くからこそ、周りをよく見て、町を自分の体で覚える.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "地図アプリは、使わないほうがいい。",
                    "急いでいないときは、アプリを使わずに歩くのもいい。",
                    "紙の地図を持って、出かけるべきだ。",
                    "迷うのは時間の無駄なので、避けるべきだ。",
                ],
                "answer": 1,
                "why": "急がない日には、あえてアプリを閉じて歩いてみるのも悪くない: only on days when you're not in a hurry. "
                       "Choice 1 goes too far.",
            },
        ],
        "vocab": [
            {"word": "目的地", "reading": "もくてきち", "meaning": "destination"},
            {"word": "最短", "reading": "さいたん", "meaning": "shortest"},
            {"word": "頼る", "reading": "たよる", "meaning": "to rely on"},
            {"word": "矢印", "reading": "やじるし", "meaning": "arrow"},
            {"word": "記憶", "reading": "きおく", "meaning": "memory"},
            {"word": "ふと", "reading": "ふと", "meaning": "suddenly, by chance"},
        ],
    },
    # ------------------------------------------------------------------ N1
    {
        "id": "n1-r01",
        "title": "Library closure notice",
        "jp_title": "システム更新に伴う休館のお知らせ",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "市立図書館をご利用の皆様へ",
            "このたび、蔵書管理システムの更新に伴い、下記の期間、全館を休館いたします。休館中は、返却ポストのご利用も停止いたしますので、ご了承ください。",
            "休館期間：2月10日（月）〜2月16日（日）",
            "なお、休館期間中に返却期限を迎える資料につきましては、期限を自動的に2月23日まで延長いたします。延長の手続きは不要です。"
            "予約資料の受け取り期限も同様に延長されますが、新たな予約の受け付けは、休館明けの2月17日からとなります。",
            "市立中央図書館",
        ],
        "en": [
            "To all users of the city library,",
            "Because the library's catalogue system is being updated, all branches will be closed during the period below. "
            "The return box will also be out of use while we are closed. We appreciate your understanding.",
            "Closed: Monday 10 February to Sunday 16 February",
            "Please note that items due back during the closure will automatically have their due date extended to 23 February. "
            "You do not need to do anything. Pick-up deadlines for reserved items will be extended in the same way, but new "
            "reservations will only be accepted from 17 February, when we reopen.",
            "City Central Library",
        ],
        "questions": [
            {
                "q": "このお知らせの内容と合っているものはどれか。",
                "choices": [
                    "休館中も、返却ポストは利用できる。",
                    "返却期限が休館中の本は、手続きをしなくても期限が延びる。",
                    "休館中も、新しい予約をすることができる。",
                    "予約していた本は、2月16日までに受け取らなければならない。",
                ],
                "answer": 1,
                "why": "期限を自動的に…延長いたします。延長の手続きは不要です. The return box is closed, new reservations start on "
                       "the 17th, and pick-up deadlines are extended too.",
            },
        ],
        "vocab": [
            {"word": "蔵書", "reading": "ぞうしょ", "meaning": "library holdings, book collection"},
            {"word": "伴う", "reading": "ともなう", "meaning": "to accompany, come with (〜に伴い = due to)"},
            {"word": "了承", "reading": "りょうしょう", "meaning": "understanding, acknowledgement"},
            {"word": "期限", "reading": "きげん", "meaning": "deadline, time limit"},
            {"word": "延長", "reading": "えんちょう", "meaning": "extension"},
            {"word": "同様", "reading": "どうよう", "meaning": "the same way, likewise"},
        ],
    },
    {
        "id": "n1-r02",
        "title": "The value of the long way round",
        "jp_title": "効率と遠回り",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "効率を重んじる現代社会では、最短距離で目的地にたどり着くことが良しとされる。無駄を省き、成果を早く出すことが求められるのは、"
            "ある意味で当然であろう。",
            "しかし、遠回りの中にこそ、思いがけない発見が潜んでいることも少なくない。寄り道をしたからこそ出会えた人や、"
            "失敗を重ねたからこそ得られた知恵は、効率だけを追い求めていては決して手に入らないものだ。",
        ],
        "en": [
            "In modern society, which values efficiency, reaching your destination by the shortest route is considered good. "
            "In a sense it's only natural that we're expected to cut out waste and produce results quickly.",
            "But surprising discoveries are often hidden precisely in the long way round. The people you meet because you took a "
            "detour, and the wisdom you gain because you failed again and again, are things you could never get by chasing "
            "efficiency alone.",
        ],
        "questions": [
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "現代社会では、効率を重んじるべきではない。",
                    "遠回りや失敗にも、効率では得られない価値がある。",
                    "寄り道をすれば、必ず新しい発見がある。",
                    "成果を早く出すことが、何より大切だ。",
                ],
                "answer": 1,
                "why": "効率だけを追い求めていては決して手に入らないもの: detours and failures give things efficiency can't. "
                       "The writer calls efficiency natural (当然), so 1 goes too far, and 3 says 必ず (always) where the text says 少なくない.",
            },
        ],
        "vocab": [
            {"word": "重んじる", "reading": "おもんじる", "meaning": "to value, attach importance to"},
            {"word": "省く", "reading": "はぶく", "meaning": "to cut out, omit"},
            {"word": "成果", "reading": "せいか", "meaning": "result, outcome"},
            {"word": "潜む", "reading": "ひそむ", "meaning": "to lie hidden"},
            {"word": "寄り道", "reading": "よりみち", "meaning": "detour, stopping off on the way"},
            {"word": "知恵", "reading": "ちえ", "meaning": "wisdom"},
        ],
    },
    {
        "id": "n1-r03",
        "title": "A cancelled lecture",
        "jp_title": "講演会中止のお知らせ",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "件名：講演会中止のお知らせとお詫び",
            "講演会にお申し込みいただいた皆様",
            "3月8日（土）に予定しておりました「これからの地域づくり」講演会は、講師の急病により、誠に勝手ながら中止とさせていただくこととなりました。"
            "楽しみにしてくださっていた皆様には、心よりお詫び申し上げます。",
            "お支払いいただいた参加費につきましては、全額を返金いたします。お手数ですが、3月20日までに、添付の用紙に振込先をご記入のうえ、"
            "メールでご返送ください。なお、講演会は日程を改めて開催する予定です。決まり次第、改めてご案内いたします。",
            "さくら市文化センター",
        ],
        "en": [
            "Subject: Cancellation of the lecture, with our apologies",
            "To everyone who signed up for the lecture,",
            "We regret to announce that the lecture \"Building our community\", scheduled for Saturday 8 March, has been cancelled "
            "because the speaker has suddenly fallen ill. We sincerely apologise to everyone who was looking forward to it.",
            "We will refund your entry fee in full. We're sorry for the trouble, but please fill in your bank details on the attached "
            "form and send it back by email by 20 March. We plan to hold the lecture on a new date and will let you know as soon as "
            "it's decided.",
            "Sakura City Culture Centre",
        ],
        "questions": [
            {
                "q": "このメールを受け取った人が、しなければならないことは何か。",
                "choices": [
                    "新しい日程の講演会に申し込む。",
                    "3月20日までに、振込先を書いた用紙を送る。",
                    "文化センターへ、参加費を受け取りに行く。",
                    "講師に、お見舞いのメールを送る。",
                ],
                "answer": 1,
                "why": "To get the refund: 3月20日までに、添付の用紙に振込先をご記入のうえ、メールでご返送ください. The new date "
                       "hasn't been decided yet.",
            },
        ],
        "vocab": [
            {"word": "講演会", "reading": "こうえんかい", "meaning": "lecture (event)"},
            {"word": "講師", "reading": "こうし", "meaning": "speaker, lecturer"},
            {"word": "お詫び", "reading": "おわび", "meaning": "apology"},
            {"word": "全額", "reading": "ぜんがく", "meaning": "the full amount"},
            {"word": "振込先", "reading": "ふりこみさき", "meaning": "account to transfer money to"},
            {"word": "添付", "reading": "てんぷ", "meaning": "attachment"},
        ],
    },
    {
        "id": "n1-r04",
        "title": "Saying things in words",
        "jp_title": "察することと伝えること",
        "kind": "Short passage",
        "minutes": 4,
        "text": [
            "日本語には、相手に察してもらうことを前提とした表現が多い。「ちょっと考えておきます」が、実際には断りの意味であることは、"
            "日本で暮らした経験のある人なら一度は耳にしたことがあるだろう。",
            "こうした言い方は、相手を傷つけまいとする配慮から生まれたものに違いない。だが、価値観の異なる人々が共に暮らす社会においては、"
            "察することを相手に求めすぎず、伝えるべきことははっきり言葉にする姿勢もまた、もう一つの思いやりと言えるのではないか。",
        ],
        "en": [
            "Japanese has many expressions that assume the listener will read between the lines. Anyone who has lived in Japan has "
            "probably heard at least once that \"I'll think about it\" actually means no.",
            "Such expressions surely come from a wish not to hurt the other person. But in a society where people with different "
            "values live together, couldn't an attitude of not expecting others to read between the lines too much, and putting "
            "what needs saying clearly into words, also be called another kind of consideration?",
        ],
        "questions": [
            {
                "q": "筆者が最も言いたいことは何か。",
                "choices": [
                    "日本語の遠回しな表現は、なくすべきだ。",
                    "相手に察してもらう表現は、相手を傷つけやすい。",
                    "はっきり言葉にして伝えることも、相手への思いやりになりうる。",
                    "日本で暮らすには、相手の気持ちを察する力が必要だ。",
                ],
                "answer": 2,
                "why": "伝えるべきことははっきり言葉にする姿勢もまた、もう一つの思いやり. The writer respects indirect expressions "
                       "as consideration (配慮) and doesn't call for removing them.",
            },
        ],
        "vocab": [
            {"word": "察する", "reading": "さっする", "meaning": "to sense, read between the lines"},
            {"word": "前提", "reading": "ぜんてい", "meaning": "premise, assumption"},
            {"word": "断り", "reading": "ことわり", "meaning": "refusal"},
            {"word": "配慮", "reading": "はいりょ", "meaning": "consideration, care"},
            {"word": "価値観", "reading": "かちかん", "meaning": "values, sense of values"},
            {"word": "思いやり", "reading": "おもいやり", "meaning": "thoughtfulness, consideration"},
        ],
    },
    {
        "id": "n1-r05",
        "title": "What wealth means",
        "jp_title": "豊かさとは",
        "kind": "Medium passage",
        "minutes": 8,
        "text": [
            "かつて豊かさとは、物をたくさん持つことであった。冷蔵庫、洗濯機、テレビといった電化製品を手に入れることが、"
            "生活が良くなったことの証だったのである。",
            "ところが、物があふれる今日、人々の関心は「持つこと」から「体験すること」へと移りつつある。高価な品物を買うよりも、"
            "旅行や習い事など、心に残る経験にお金を使いたいと考える人が増えているという。物はいずれ古びるが、体験から得た喜びや学びは、"
            "その人の中に残り続けるからだろう。",
            "とはいえ、体験の価値を他人と比べ、SNSで見せることが目的となってしまえば、それは物を持つことを競っていた時代と何ら変わらない。"
            "豊かさとは、他人の目を気にすることなく、自分にとって何が大切かを知っていることなのかもしれない。",
        ],
        "en": [
            "Wealth once meant owning lots of things. Getting electrical appliances such as a fridge, a washing machine and a TV was "
            "proof that life had improved.",
            "But today, with things everywhere, people's interest is shifting from \"having\" to \"experiencing\". More and more "
            "people reportedly prefer to spend money on memorable experiences, like travel or lessons, rather than expensive goods. "
            "Probably because things eventually grow old, while the joy and learning gained from experience stay with a person.",
            "Even so, if comparing the value of experiences with others and showing them off on social media becomes the goal, "
            "that's no different from the days when people competed over possessions. Perhaps wealth means knowing what matters "
            "to you, without worrying about how others see you.",
        ],
        "questions": [
            {
                "q": "かつて、豊かさとはどのようなことだと考えられていたか。",
                "choices": ["物をたくさん持つこと", "旅行にたくさん行くこと", "心に残る経験をすること", "他人と比べないこと"],
                "answer": 0,
                "why": "かつて豊かさとは、物をたくさん持つことであった.",
            },
            {
                "q": "筆者によると、体験にお金を使う人が増えているのはなぜか。",
                "choices": [
                    "物の値段が高くなったから",
                    "体験から得たものは、その人の中に残り続けるから",
                    "SNSで他人に見せられるから",
                    "電化製品が必要なくなったから",
                ],
                "answer": 1,
                "why": "物はいずれ古びるが、体験から得た喜びや学びは、その人の中に残り続けるからだろう. Showing off on social media "
                       "is what the writer warns against.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "物を持つより、体験をするほうが必ず豊かだ。",
                    "体験を他人に見せることが、豊かさにつながる。",
                    "自分にとって何が大切かを知っていることが、豊かさなのかもしれない。",
                    "豊かさは、時代とともに失われつつある。",
                ],
                "answer": 2,
                "why": "The last sentence is the conclusion. Choice 1 goes too far: experiences shown off for others are no better "
                       "than possessions (何ら変わらない).",
            },
        ],
        "vocab": [
            {"word": "証", "reading": "あかし", "meaning": "proof, evidence"},
            {"word": "電化製品", "reading": "でんかせいひん", "meaning": "electrical appliances"},
            {"word": "あふれる", "reading": "あふれる", "meaning": "to overflow, be everywhere"},
            {"word": "関心", "reading": "かんしん", "meaning": "interest, concern"},
            {"word": "古びる", "reading": "ふるびる", "meaning": "to grow old, become worn"},
            {"word": "競う", "reading": "きそう", "meaning": "to compete"},
        ],
    },
    {
        "id": "n1-r06",
        "title": "AI and creative work",
        "jp_title": "人工知能と創作",
        "kind": "Medium passage",
        "minutes": 8,
        "text": [
            "近年、人工知能が文章や絵、音楽までも作り出せるようになった。わずか数秒で、プロが描いたかのような絵が完成するのだから、驚くほかない。",
            "こうした技術に対し、「人間の創作は不要になるのではないか」という不安の声も聞かれる。しかし私は、そうは思わない。"
            "人が作品に心を動かされるのは、完成度の高さだけによるのではない。そこに込められた作り手の迷いや苦しみ、"
            "そしてそれを乗り越えた喜びを、無意識のうちに感じ取っているからではないだろうか。",
            "もっとも、人工知能を道具として使いこなす作り手も、今後ますます増えていくだろう。大切なのは、技術を拒むことでも、"
            "技術に頼り切ることでもなく、自分は何を表現したいのかを問い続けることである。",
        ],
        "en": [
            "In recent years, AI has become able to produce writing, pictures and even music. A picture that looks as if a "
            "professional drew it can be finished in just a few seconds, which is nothing short of astonishing.",
            "In response to such technology, some people worry that \"human creative work may become unnecessary\". But I don't "
            "think so. People are moved by a work not only because of how polished it is. Isn't it because they unconsciously sense "
            "the creator's doubts and struggles that went into it, and the joy of overcoming them?",
            "That said, more and more creators will probably use AI skilfully as a tool. What matters is neither rejecting the "
            "technology nor relying on it entirely, but continuing to ask yourself what you want to express.",
        ],
        "questions": [
            {
                "q": "「不安の声」とは、どのような不安か。",
                "choices": [
                    "人工知能の作品は質が低いという不安",
                    "人間が作品を作る必要がなくなるのではないかという不安",
                    "プロの絵が売れなくなるという不安",
                    "人工知能は使い方が難しいという不安",
                ],
                "answer": 1,
                "why": "The worry is quoted just before: 「人間の創作は不要になるのではないか」.",
            },
            {
                "q": "筆者によると、人が作品に心を動かされるのはなぜか。",
                "choices": [
                    "作品の完成度が高いから",
                    "短い時間で作られたから",
                    "作り手の迷いや喜びを感じ取るから",
                    "有名なプロが作ったから",
                ],
                "answer": 2,
                "why": "完成度の高さだけによるのではない; people sense 作り手の迷いや苦しみ…喜び.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "人工知能は、創作に使うべきではない。",
                    "これからは、創作を人工知能にすべて任せたほうがいい。",
                    "自分が何を表現したいのかを、問い続けることが大切だ。",
                    "人間の創作は、いずれなくなるだろう。",
                ],
                "answer": 2,
                "why": "技術を拒むことでも、技術に頼り切ることでもなく、自分は何を表現したいのかを問い続けること. "
                       "Choices 1 and 2 are the two extremes the writer rejects.",
            },
        ],
        "vocab": [
            {"word": "人工知能", "reading": "じんこうちのう", "meaning": "artificial intelligence"},
            {"word": "創作", "reading": "そうさく", "meaning": "creative work, creation"},
            {"word": "完成度", "reading": "かんせいど", "meaning": "degree of polish, completeness"},
            {"word": "込める", "reading": "こめる", "meaning": "to put into (feelings, effort)"},
            {"word": "乗り越える", "reading": "のりこえる", "meaning": "to overcome"},
            {"word": "拒む", "reading": "こばむ", "meaning": "to refuse, reject"},
        ],
    },
    {
        "id": "n1-r07",
        "title": "Questions without answers",
        "jp_title": "答えのない問い",
        "kind": "Long passage",
        "minutes": 12,
        "text": [
            "学校の試験では、たいてい一つの正しい答えが用意されている。私たちは子供のころから、その正解をいかに早く、正確に見つけるかを競ってきた。",
            "ところが、社会に出てから直面する問題の多くには、あらかじめ決まった答えなどない。環境問題にせよ、高齢化にせよ、"
            "立場によって望ましい解決策は異なり、どれか一つを選べば、別の誰かが不利益を被ることもある。",
            "そうした問いに向き合うには、正解を探す力よりも、異なる意見に耳を傾け、自分なりの考えを組み立てていく力が求められる。"
            "にもかかわらず、学校教育は依然として、正解を覚えさせることに重きを置いているように見える。",
            "もちろん、基礎的な知識が不要だというわけではない。知識がなければ、考えることすらできないからだ。ただ、知識はあくまで"
            "考えるための材料にすぎない。これからの教育に必要なのは、答えを教えることではなく、答えのない問いを前にしても"
            "立ち止まらずに考え続ける姿勢を育てることではないだろうか。",
        ],
        "en": [
            "School exams usually have a single correct answer prepared. Since childhood, we have competed over how quickly and "
            "accurately we can find it.",
            "But many of the problems we face once we're out in the world have no answer decided in advance. Whether it's the "
            "environment or the ageing population, the best solution differs depending on where you stand, and choosing any one of "
            "them can leave someone else worse off.",
            "To face questions like these, what's needed is less the ability to find the right answer than the ability to listen to "
            "different opinions and build up your own thinking. Even so, school education still seems to put its weight on making "
            "students memorise correct answers.",
            "Of course, that doesn't mean basic knowledge is unnecessary. Without knowledge, you can't even think. But knowledge is "
            "only material for thinking. Isn't what education needs from now on not teaching answers, but nurturing the attitude of "
            "continuing to think without stopping, even in front of a question with no answer?",
        ],
        "questions": [
            {
                "q": "社会に出てから直面する問題について、筆者はどのように述べているか。",
                "choices": [
                    "学校で習った答えで、ほとんど解決できる。",
                    "決まった答えがなく、立場によって望ましい解決策が違う。",
                    "一つの解決策を選べば、誰も困らない。",
                    "早く正確に答えを見つけることが、最も大切だ。",
                ],
                "answer": 1,
                "why": "あらかじめ決まった答えなどない…立場によって望ましい解決策は異なり. Choosing one can even harm someone (不利益を被る).",
            },
            {
                "q": "「そうした問い」とは、どのような問いか。",
                "choices": [
                    "試験で出される問い",
                    "正しい答えが一つだけある問い",
                    "決まった答えがない問い",
                    "子供のころに習った問い",
                ],
                "answer": 2,
                "why": "そうした points back to the previous paragraph: problems with no answer decided in advance.",
            },
            {
                "q": "筆者は、知識についてどのように考えているか。",
                "choices": [
                    "考えるための材料として、必要だ。",
                    "これからの教育には、必要ない。",
                    "知識さえあれば、どんな問題も解決できる。",
                    "知識を覚えることが、教育の最大の目的だ。",
                ],
                "answer": 0,
                "why": "基礎的な知識が不要だというわけではない…知識はあくまで考えるための材料にすぎない.",
            },
            {
                "q": "筆者が最も言いたいことは何か。",
                "choices": [
                    "学校の試験を、なくすべきだ。",
                    "基礎的な知識を、もっと教えるべきだ。",
                    "答えのない問いに向き合い、考え続ける姿勢を育てるべきだ。",
                    "社会問題については、専門家に任せるべきだ。",
                ],
                "answer": 2,
                "why": "The final sentence is the main point: 答えのない問いを前にしても立ち止まらずに考え続ける姿勢を育てること.",
            },
        ],
        "vocab": [
            {"word": "直面", "reading": "ちょくめん", "meaning": "facing, confronting"},
            {"word": "あらかじめ", "reading": "あらかじめ", "meaning": "in advance"},
            {"word": "高齢化", "reading": "こうれいか", "meaning": "ageing (of the population)"},
            {"word": "不利益", "reading": "ふりえき", "meaning": "disadvantage, loss"},
            {"word": "被る", "reading": "こうむる", "meaning": "to suffer (damage, loss)"},
            {"word": "依然として", "reading": "いぜんとして", "meaning": "still, as before"},
            {"word": "姿勢", "reading": "しせい", "meaning": "attitude, stance"},
        ],
    },
    {
        "id": "n1-r08",
        "title": "Going cashless",
        "jp_title": "キャッシュレス決済",
        "kind": "Comparison (A/B)",
        "minutes": 7,
        "text": [
            "A\n現金を使わない支払いは、今後さらに広げていくべきだ。会計にかかる時間が短くなり、店側も現金を数えたり管理したりする手間が省ける。"
            "また、支出の記録が自動的に残るため、家計の管理もしやすくなる。お金の流れが見えることは、社会全体にとっても利点が大きいだろう。",
            "B\nキャッシュレス化の便利さは認めるが、急ぎすぎることには懸念がある。機械の操作に不慣れな高齢者が取り残されかねないし、"
            "災害で停電が起きれば、支払いそのものができなくなるおそれもある。何より、お金を使っている実感が薄れ、"
            "つい使いすぎてしまう人も少なくない。現金という選択肢は、残しておくべきではないか。",
        ],
        "en": [
            "A\nPaying without cash should spread even further. Checkout takes less time, and shops are spared the trouble of "
            "counting and managing cash. Spending is also recorded automatically, which makes household budgeting easier. Being "
            "able to see the flow of money is probably a big advantage for society as a whole.",
            "B\nI accept that going cashless is convenient, but I'm concerned about rushing it. Older people who aren't used to "
            "operating machines could be left behind, and if a disaster causes a power cut, paying at all may become impossible. "
            "Above all, many people lose the sense that they're spending money and end up spending too much. Shouldn't cash be "
            "kept as an option?",
        ],
        "questions": [
            {
                "q": "AとBのどちらも触れている点は何か。",
                "choices": [
                    "キャッシュレス決済の便利さ",
                    "災害のときの問題",
                    "高齢者への影響",
                    "店の手間が省けること",
                ],
                "answer": 0,
                "why": "A lists the conveniences, and B begins by accepting them (便利さは認める). Disasters and older people appear "
                       "only in B; the shop's workload only in A.",
            },
            {
                "q": "キャッシュレス決済について、AとBはどのような立場か。",
                "choices": [
                    "AもBも、すぐに現金をなくすべきだと考えている。",
                    "Aはさらに広げるべきだとし、Bは現金も残すべきだとしている。",
                    "Aは慎重な立場で、Bは積極的な立場だ。",
                    "AもBも、高齢者のために現金を残すべきだとしている。",
                ],
                "answer": 1,
                "why": "A: さらに広げていくべきだ. B: 現金という選択肢は、残しておくべきではないか.",
            },
        ],
        "vocab": [
            {"word": "決済", "reading": "けっさい", "meaning": "payment, settlement"},
            {"word": "手間", "reading": "てま", "meaning": "trouble, effort"},
            {"word": "支出", "reading": "ししゅつ", "meaning": "spending, expenditure"},
            {"word": "懸念", "reading": "けねん", "meaning": "concern, worry"},
            {"word": "不慣れ", "reading": "ふなれ", "meaning": "unfamiliar, not used to"},
            {"word": "選択肢", "reading": "せんたくし", "meaning": "option, choice"},
        ],
    },
    {
        "id": "n1-r09",
        "title": "A scholarship for international students",
        "jp_title": "留学生奨学金　募集要項",
        "kind": "Information search",
        "minutes": 7,
        "text": [
            "さくら国際交流財団　留学生奨学金　募集要項",
            "◆対象\n"
            "・日本の大学または大学院に在籍する外国人留学生\n"
            "・申請時に30歳以下であること\n"
            "・他の奨学金を受けていないこと",
            "◆支給額・期間\n"
            "・月額5万円\n"
            "・4月から1年間（返済不要）",
            "◆応募方法\n"
            "・応募用紙、成績証明書、指導教員の推薦書を、在籍する大学の留学生担当窓口に提出すること。\n"
            "・個人での直接応募は受け付けない。",
            "◆締め切り\n"
            "・12月15日（大学窓口必着）",
            "◆その他\n"
            "・採用者は、年に2回、財団主催の交流行事に参加しなければならない。",
        ],
        "en": [
            "Sakura International Exchange Foundation: scholarship for international students, application guidelines",
            "Eligibility\n"
            "- International students enrolled at a Japanese university or graduate school\n"
            "- Aged 30 or under when applying\n"
            "- Not receiving any other scholarship",
            "Amount and period\n"
            "- 50,000 yen a month\n"
            "- For one year from April (no repayment needed)",
            "How to apply\n"
            "- Submit the application form, a transcript and a recommendation from your supervisor to the international student "
            "office at your university.\n"
            "- Applications from individuals directly to the foundation are not accepted.",
            "Deadline\n"
            "- 15 December (must reach the university office by then)",
            "Other\n"
            "- Scholarship holders must take part in foundation exchange events twice a year.",
        ],
        "questions": [
            {
                "q": "次の留学生のうち、この奨学金に応募できるのは誰か。",
                "choices": [
                    "大学院で学んでいる、32歳のリーさん",
                    "ほかの財団から奨学金を受けている、大学3年のキムさん",
                    "日本語学校で学んでいる、20歳のアンナさん",
                    "ほかの奨学金を受けていない、大学2年で25歳のトムさん",
                ],
                "answer": 3,
                "why": "Lee is over 30, Kim already has a scholarship, and Anna is at a language school, not a university. "
                       "Tom meets all three conditions.",
            },
            {
                "q": "応募の方法について、正しいものはどれか。",
                "choices": [
                    "必要な書類を、財団に直接郵送する。",
                    "必要な書類を、在籍する大学の担当窓口に出す。",
                    "応募用紙だけを、12月15日までに出せばよい。",
                    "指導教員が、財団に推薦書を直接送る。",
                ],
                "answer": 1,
                "why": "在籍する大学の留学生担当窓口に提出すること. Direct applications aren't accepted, and all three documents are needed.",
            },
        ],
        "vocab": [
            {"word": "財団", "reading": "ざいだん", "meaning": "foundation"},
            {"word": "募集要項", "reading": "ぼしゅうようこう", "meaning": "application guidelines"},
            {"word": "在籍", "reading": "ざいせき", "meaning": "being enrolled"},
            {"word": "支給", "reading": "しきゅう", "meaning": "payment, provision"},
            {"word": "返済", "reading": "へんさい", "meaning": "repayment"},
            {"word": "主催", "reading": "しゅさい", "meaning": "hosting, sponsorship (of an event)"},
        ],
    },
    {
        "id": "n1-r10",
        "title": "Reading fast and reading deep",
        "jp_title": "速く読むことと深く読むこと",
        "kind": "Medium passage",
        "minutes": 8,
        "text": [
            "インターネットの普及により、私たちは毎日膨大な量の文字を目にするようになった。ニュースの見出しをざっと眺め、"
            "気になった記事だけを拾い読みする。そうした読み方が、すっかり習慣になっている人も多いだろう。",
            "確かに、限られた時間で多くの情報を得るには、それも一つの方法である。しかし、拾い読みに慣れてしまうと、長い文章をじっくり読み、"
            "書き手の考えをたどる力が衰えていくおそれがある。一冊の本と何日もかけて向き合い、立ち止まっては考える。"
            "そうした経験を通してしか育たない思考の深さがあるはずだ。",
            "速く読むことと、深く読むこと。どちらか一方を捨てる必要はない。目的に応じて読み方を使い分けることこそ、"
            "情報があふれる時代を生きる私たちに求められている力なのだろう。",
        ],
        "en": [
            "With the spread of the internet, we now see an enormous amount of text every day. We glance over news headlines and "
            "skim only the articles that catch our eye. For many people, that way of reading has probably become a firm habit.",
            "It's true that to get a lot of information in limited time, it's one way to do it. But once you get used to skimming, "
            "your ability to read long texts carefully and follow the writer's thinking may decline. Spending days with one book, "
            "stopping to think now and then: there must be a depth of thought that only grows through experiences like that.",
            "Reading fast and reading deeply. There's no need to throw either away. Using different ways of reading to suit your "
            "purpose is surely the skill we need, living in an age overflowing with information.",
        ],
        "questions": [
            {
                "q": "「そうした読み方」とは、どのような読み方か。",
                "choices": [
                    "一冊の本を、何日もかけて読む読み方",
                    "見出しを見て、気になった記事だけを読む読み方",
                    "書き手の考えをたどりながら読む読み方",
                    "声に出して読む読み方",
                ],
                "answer": 1,
                "why": "そうした points back to the previous sentence: 見出しをざっと眺め、気になった記事だけを拾い読みする.",
            },
            {
                "q": "筆者は、拾い読みに慣れるとどうなるおそれがあると述べているか。",
                "choices": [
                    "情報を速く得られなくなる。",
                    "長い文章をじっくり読む力が衰える。",
                    "インターネットが使えなくなる。",
                    "本を買わなくなる。",
                ],
                "answer": 1,
                "why": "長い文章をじっくり読み、書き手の考えをたどる力が衰えていくおそれがある.",
            },
            {
                "q": "筆者の考えに最も近いものはどれか。",
                "choices": [
                    "拾い読みは、やめるべきだ。",
                    "本は、速く読むほうがいい。",
                    "目的に応じて、速く読むことと深く読むことを使い分けるべきだ。",
                    "インターネットの記事は、読まないほうがいい。",
                ],
                "answer": 2,
                "why": "どちらか一方を捨てる必要はない; 目的に応じて読み方を使い分けることこそ…求められている力.",
            },
        ],
        "vocab": [
            {"word": "普及", "reading": "ふきゅう", "meaning": "spread, becoming common"},
            {"word": "膨大", "reading": "ぼうだい", "meaning": "enormous, vast"},
            {"word": "見出し", "reading": "みだし", "meaning": "headline"},
            {"word": "拾い読み", "reading": "ひろいよみ", "meaning": "skimming, reading bits"},
            {"word": "衰える", "reading": "おとろえる", "meaning": "to decline, weaken"},
            {"word": "思考", "reading": "しこう", "meaning": "thinking, thought"},
        ],
    },
]

_BY_ID = {p["id"]: p for p in PASSAGES}


def get(passage_id: str) -> dict | None:
    return _BY_ID.get(passage_id)


def level(passage: dict) -> str:
    """The JLPT level from the id prefix: n3-r01 -> "N3", n2-r01 -> "N2"."""
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
