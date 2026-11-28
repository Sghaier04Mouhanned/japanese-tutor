# 日本語 Tutor

A personal Japanese tutor that runs in the browser, built for going from zero to
passing the JLPT (N5, then N4, N3, N2 and N1), powered by a free AI API or a local model.

## Features

**Today's plan (Home)**
- A short daily checklist built from your progress: due reviews, the next kana set, the next
  lesson, 10 new words, one reading passage and one listening item at your level, and up to 5
  missed questions to retry
- Your level is the level of your next unfinished lesson; words, reading and listening join once
  hiragana is learned (or a lesson is finished)
- Steps tick themselves off from what you did today (mock tests count for reading and listening),
  with a time estimate and a streak of fully finished days
- The Home button leads to the next open step

**Backups (Home → Your data)**
- All progress lives in `data/tutor.db`; a copy goes to `data/backups` each day the app runs
  (the last 14 are kept)
- Download a backup to keep elsewhere, and restore from a downloaded file or any daily copy
- Restoring saves your current progress first (the last 5 of these are kept), so it can be undone;
  files that aren't a healthy tutor database are refused, and older backups get the newer tables

**JLPT N5 lessons**
- 30 hand-written lessons covering the core N5 grammar: greetings, self-introduction, です,
  questions, これ/それ/あれ, の, polite verbs, past tense, particles, time, い- and な-adjectives,
  あります/います, ここ/そこ/どこ, 〜たい/ほしい, 〜てください, 〜ませんか/〜ましょう,
  adjective past, counting and prices, 〜ています, days and dates, から/が, て-form linking,
  comparisons, もう/まだ and frequency, できます/上手/分かります, 〜てもいい/〜てはいけない,
  〜ないでください, dictionary form, counters
- Key points, example sentences with furigana and romaji, and vocabulary in each lesson
- "Practice with Sensei" runs exercises grounded in the lesson's own content
- Completing a lesson adds its vocabulary to your reviews
- `python -m app.lessons` cross-checks every example's kana, romaji and furigana

**JLPT-style quizzes**
- Kanji reading (漢字読み), spelling (表記), vocabulary (語彙), particles (文法) and listening (聴解)
- Kanji questions: a kanji's meaning, pick the kanji for a meaning (look-alike choices with similar
  stroke counts), and the reading of a kanji word; drawn from your studied kanji or the N5-N1 lists
- Generated from verified lesson content and your saved words, never by the AI
- Reading distractors are near misses like on the real test (がっこう / がこう / かっこう)
- Per-type scores, explanations, and one click to add missed words to your reviews

**Timed mock tests (Quiz → Mock test)**
- One per level, N5 to N1, laid out like the JLPT at about half its length: 言語知識（文字・語彙）, then
  言語知識（文法）・読解 (N2 and N1 sit them together, as on the real test), each against the clock, then 聴解
- Vocabulary: kanji reading, spelling and word meaning from the level's word list, using kanji up to
  that level; readings never offer another valid reading as a wrong answer, spellings never offer
  a word read the same way
- Grammar: 238 hand-written questions (`app/mock.py`, 40 for N5 and N4, 50 or more for N3 to N1) on
  the level's patterns, where only one choice fits in form or meaning, plus particle questions from
  the N5 and N4 lessons
- Reading: two short passages, a medium one and an information search, comparison or long passage;
  furigana only on kanji beyond the level, as on the test
- Listening: one item of each kind, played once with no replay; the audio is prepared in the
  background while you work on the first parts
- The report scales each section to the JLPT's points (0-60, or 0-120 for N5/N4 language and
  reading) and checks the real pass marks and section minimums. The JLPT equates scores across
  tests, so it's an estimate. Then every question again with the answer and explanation,
  transcripts and translations, and one click to add missed words to your reviews
- Each new test picks the passages, listening items and grammar questions you've met least in
  earlier mock tests (then ones you haven't practised), so every level gives 5 full tests before
  anything repeats; the level's card says how many fresh tests are left
- `python -m app.mock` checks the grammar questions, builds sample tests and checks that each level's
  fresh tests in a row share nothing (`--readings` prints their furigana)

**Speaking (local Whisper)**
- 🎤 in the chat: speak Japanese, check the transcript, send it to Sensei
- 🎤 on every lesson example: say the sentence and see which sounds were recognized
- Runs on your own machine (faster-whisper, CPU); compares by sound, so 学校 = がっこう

**Progress dashboard (Home)**
- JLPT building blocks: kana, lessons, words and kanji per level list, reading and listening, quiz
  accuracy per section
- Last 30 days of study (kana, words & mistakes, quizzes) with hover details and a table view
- Quiz score trend; study days, total reviews and quizzes

**JLPT word lists (Words in the top bar)**
- About 8,000 words by level: N5 (731), N4 (667), N3 (about 2,100), N2 (about 1,750) and N1 (about
  2,700), from Jonathan Waller's JLPT lists (CC BY) via open-anki-jlpt-decks (MIT), in
  `app/jlpt_words.tsv`. There has been no official word list since 2010, so these are close guides
- Cleaned up for learners: spellings matched to JMdict (終る → 終わる), words usually written in kana
  shown in kana (綺麗 → きれい, with the kanji as a note), and everyday greetings moved to N5
- Words your lessons teach come first, then the most common; search by word, reading or meaning
- Add the next 10 to your reviews, or one at a time; words you saved from lessons or the dictionary
  count too (a lesson's 行きます is the list's 行く)
- Each word has up to three example sentences from the lessons, listening scripts and reading
  passages, matched by spelling and reading (四人 is not ～人); review cards show one with the answer
- The dictionary popup shows a word's JLPT level, and the dashboard tracks each level list
- `python -m app.words` checks the lists and counts the words with example sentences

**Kanji study**
- Lists closest to N5 (103), N4 (181), N3 (about 370), N2 (about 370) and N1 (about 1,110), plus
  the few other kanji used in the lessons (2,138 in all). KANJIDIC only has the pre-2010 JLPT levels:
  old levels 4 and 3 match N5 and N4; old level 2 mixes N3 and N2, so the N3 list is its 300 most
  common kanji plus the ones the N5-N3 lessons use, and the N2 list is the rest. N1 expects about the
  whole Jōyō list, so the N1 list is every other Jōyō kanji, including the 2010 additions (誰, 頃…)
  that have no old level; old level 1's name-only kanji aren't tested and are left out. There has been
  no official kanji list since 2010, so these are close guides, not official lists
- Animated stroke order (KanjiVG), on/kun readings with audio, meanings, and example words
  (lesson vocabulary first, then common dictionary words, then other dictionary words for the
  rarest N1 kanji)
- Meanings put what learners actually meet first: KANJIDIC's order can mislead (緒 starts with
  "thong", 校 with "exam"), so 812 kanji have hand-checked meanings first (緒 = together, as in
  一緒) in `app/kanji_meanings.py`. Quiz and writing prompts never show a note containing the answer
- Add kanji to your reviews one by one or five at a time; they join the Review tab and the dashboard
- Handwriting: draw each stroke with a mouse, finger or pen; order, direction and shape are checked
  stroke by stroke against KanjiVG, with hints after repeated misses. Trace or write from memory on
  any kanji page, or run a writing session (see the meaning and reading, write the kanji)
- Writing from memory updates the kanji's review schedule: no mistakes counts as Good, one or two
  as Hard, three or more (or using a hint) as Again. Tracing never counts, kanji not in your reviews
  are left alone, and a kanji reviewed in the last 12 hours that isn't due yet isn't graded again.
  Turn on "Write kanji from memory" in the Review tab to answer due kanji by writing them

**Reading practice (JLPT 読解, N5 to N1)**
- 20 N5 passages (30 questions): notes, a class notice, a diary, an invitation, library rules, family
  routines, a new flat, a birthday, a lunch menu, library hours, a supermarket flyer, a moved test, a
  cooking class, a trip to Kyoto, pool prices and a bus timetable, mostly in hiragana with N5 kanji
- 20 N4 passages (30 questions): memos, emails, notices, a diary entry, simple essays, a timetable,
  rubbish collection rules, part-time job ads, a lift inspection, learning to swim, station bicycle
  parking, a first part-time job, Japanese classes and bicycle hire
- 25 hand-written N3 passages: notes, emails, notices, short essays and information-search pages
  such as removal prices and a café job advert, with 46 JLPT-style questions in Japanese and an
  English explanation for every answer
- 24 N2 passages (47 questions): formal notices and emails, opinion essays, information-search pages,
  and A/B comparisons where two writers argue opposite sides, as in the N2 test
- 20 N1 passages (37 questions): formal notices, a product recall, dense opinion essays on boredom,
  silence, tourism and memory, a long passage with four questions, A/B comparisons and
  information-search pages
- Furigana toggle; kanji beyond the passage's level keep their furigana, as on the real test
- Tap any word to look it up; 🔊 reads each paragraph; after answering, see the translation and add
  the key words to your reviews. Scores are saved, and the dashboard counts passages read
- `python -m app.reading` checks the questions; add `--readings` to proofread the furigana

**Listening practice (JLPT 聴解, N5 to N1)**
- 30 N5 items: what to bring, buying fruit, a family's size, a meeting time, homework, birthdays, the
  post office, a cinema trip, asking for water or a price, borrowing a pen, greetings and simple
  replies, in the same four formats as N4
- 30 N4 items: shopping for a party, a first clinic visit, a library card, a changed meeting time, a
  noisy flat, a doctor's advice, which platform, a lost umbrella, plus utterance expressions
  (発話表現: what would you say in this situation?) and quick responses
- 35 hand-written N3 items in the four test formats: task-based (課題理解), key point (ポイント理解),
  summary (概要理解) and quick response (即時応答)
- 35 N2 items, adding integrated comprehension (統合理解): a staff member explains three or four
  options, two people discuss them, and you work out which one they choose
- 35 N1 items: a thesis supervision, city hall procedures, expense claims, a film review, lectures on
  dialects, free services and forestry, business and honorific quick responses, and integrated
  items weighing four options
- Read by VOICEVOX with a different voice per role (narrator 九州そら, woman 春日部つむぎ, man 玄野武宏,
  staff 青山龍星);
  the clips are made before the first play so lines follow each other smoothly. Without VOICEVOX the
  browser's voice is used at a different pitch per role
- As on the test, summary, utterance and quick-response choices are only spoken; after answering you get the
  transcript with furigana, a translation of every line, and the key words
- Under "Read & listen" in the top bar, next to reading practice; `python -m app.listening` checks the
  items (`--readings` prints the transcripts' furigana)

**Mistakes (Read & listen → Mistakes)**
- Every reading and listening question you get wrong, in practice or in a mock test (unanswered ones
  too), comes back here until you answer it right; the tab shows how many are left
- A reading mistake shows its passage again with just that question; a listening mistake can be
  replayed as often as you like. After answering: the explanation, translation or transcript, and
  a link to the next mistake
- Answers are logged per question in `question_attempts`; on first start it is filled from earlier
  listening answers, finished mock tests and reading scores that were all right or all wrong

**Dictionary, notebook and reviews**
- Click any Japanese word (chat or lessons) to look it up in JMdict and save it
- Sensei logs the mistakes it corrects; they come back as review cards
- The Review tab covers kana, saved words (typed readings checked strictly), mistakes and kanji
- Notebook lists your saved words and mistakes

**AI tutor chat**
- "Sensei" teaches in English, brings in Japanese gradually, starting with polite です/ます form
- Knows which kana you've learned and adds romaji until you can read them
- Furigana on every kanji, generated by a dictionary (MeCab/UniDic), not guessed by the AI
- Checks the tutor's kana against its romaji and warns you when they disagree
- Streams replies; falls back to a lighter Gemini model when the main one is overloaded
- Works with Google Gemini (free API key) or local models through Ollama; switch in ⚙ settings
- Chats are saved; "Listen" reads the Japanese aloud

**Kana trainer**
- Learn hiragana and katakana set by set: study each character with audio, then pass a quick check
- Spaced-repetition reviews (FSRS) so each kana comes back right before you'd forget it
- Free practice in two directions: type the reading, or pick the kana from four choices
- Progress chart, daily streak and accuracy
- Accepts common alternative spellings (si/shi, tu/tsu, zya/ja…)

**JLPT N4 lessons (30)**
- Plain forms, 〜たことがある, 〜たり〜たり, potential form, 〜と思う/〜と言う, 〜つもり/〜予定,
  volitional form, 〜なければならない/〜なくてもいい, 〜ので/〜のに, 〜たら/〜と
- Giving and receiving, 〜てあげる/くれる/もらう, passive, causative, 〜そうだ (looks / heard),
  〜ておく/〜てしまう, 〜ながら/〜てから/〜た後で, 〜ようになる/〜ことにする,
  〜かもしれない/〜でしょう, keigo basics
- 〜ば, 〜ために/〜ように, 〜すぎる, 〜やすい/〜にくい, 〜し, 〜はず, 〜ようだ/〜みたい/〜らしい,
  〜てみる, の/こと, transitive/intransitive pairs with 〜ている/〜てある
- Once you start N4, Sensei may use N4 grammar too; progress and quizzes track N5 and N4 separately

**JLPT N3 lessons (30)**
- 〜ところだ (about to / in the middle of / just did), 〜うちに, 〜ばかり, 〜わけだ/〜わけではない/〜わけがない,
  〜について/〜に対して/〜にとって, 〜によって/〜による, 〜おかげで/〜せいで, 〜ようとする/〜ようにする,
  〜まま/〜ずに, 〜ことになる/〜ことになっている
- 〜たびに, 〜ば〜ほど, 〜っぽい/〜らしい (typical), 〜として, 〜かわりに, 〜わりに, 〜とおりに,
  〜させてください, 〜という/〜って, 〜さえ/〜さえ〜ば
- 〜ように言う/〜ますように, 〜がる/〜たがる, 〜なんて, 〜最中に, 〜だけでなく/〜はもちろん,
  〜てほしい/〜てもらいたい, たとえ〜ても/〜としても, 〜わけにはいかない, 〜につれて/〜にしたがって,
  〜ばよかった/〜のに (regret)
- Once you start N3, Sensei may use N3 grammar too; kanji from these lessons join the Kanji section
  automatically (the kanji index rebuilds itself when lessons add new kanji)

**JLPT N2 lessons (30)**
- 〜にもかかわらず, 〜からこそ/〜こそ, 〜に違いない/〜に決まっている, 〜ものの/〜とはいえ,
  〜をきっかけに/〜を通じて, 〜に関して/〜に基づいて, 〜ばかりか/〜うえに, 〜ざるを得ない,
  〜次第/〜次第で, 〜一方だ/〜つつある
- 〜に限らず/〜に限って, 〜にすぎない, 〜かねる/〜かねない, 〜おそれがある, 〜つつ/〜つつも,
  〜からには/〜以上は, 〜にしては, 〜としたら/〜とすれば, 〜ようがない, 〜ものだ
- 〜に応じて/〜に沿って, 〜をはじめ, 〜反面, 〜とともに, 〜ないことはない, 〜にかけては, 〜ことに,
  〜ことから, 〜上で/〜上, 〜ずにはいられない
- Sensei may use grammar up to the highest level you've started a lesson in

**JLPT N1 lessons (30)**
- 〜ならではの, 〜ともなると, 〜をよそに, 〜といえども, 〜や否や/〜なり, 〜べく, 〜きらいがある,
  〜をものともせず, 〜たりとも, 〜を禁じ得ない
- 〜であれ, 〜とあって, 〜ずにはおかない/〜ずにはすまない, 〜まじき, 〜をもって, 〜ながらも,
  〜がてら/〜かたがた, 〜ずくめ, 〜に至るまで/〜に至っては, 〜までもない
- 〜と相まって, 〜ものを, 〜んがため, 〜てやまない, 〜をおいて, 〜にかこつけて, 〜ともなく,
  〜ばこそ, 〜にひきかえ, 〜を皮切りに

## Setup

Copy `.env.example` to `.env` and add a free Gemini key from
https://aistudio.google.com. For local models, install [Ollama](https://ollama.com)
and pull a small model that fits your GPU (e.g. `ollama pull qwen3:4b`).

For word lookups, download the dictionary once and build its index:

```bash
curl -o data/dict/JMdict_e.gz http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz
python -m app.dictionary
```

JMdict is © the Electronic Dictionary Research and Development Group, used under
[CC BY-SA 4.0](https://www.edrdg.org/edrdg/licence.html).

Speech recognition downloads the Whisper "small" model (~480 MB) into `data/models/`
the first time you press a 🎤 button.

For kanji study, add KANJIDIC2 and KanjiVG (the index builds itself on first use):

```bash
curl -o data/dict/kanjidic2.xml.gz http://ftp.edrdg.org/pub/Nihongo/kanjidic2.xml.gz
# KanjiVG "main" zip from https://github.com/KanjiVG/kanjivg/releases, unzipped into data/kanjivg/
```

KANJIDIC2 is © EDRDG (CC BY-SA 4.0); KanjiVG is © Ulrich Apel (CC BY-SA 3.0).

For natural Japanese voices, download the VOICEVOX engine (Windows CPU `.vvpp` from
https://github.com/VOICEVOX/voicevox_engine/releases, ~1.9 GB) and unzip it into
`data/voicevox/engine/`. The app starts it automatically and falls back to the browser's
voice without it. Pick a voice and speed in the Tutor tab's ⚙ settings. VOICEVOX voices
are free to use with credit to "VOICEVOX:<character name>".

## Run it

Requires Python 3.11+. On Windows, double-click `run.bat`, or:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000.

Audio uses your browser's built-in Japanese voice. Microsoft Edge has the best
ones on Windows; in Chrome, the "Google 日本語" voice works well.

## Project layout

```
app/
  main.py       FastAPI app
  chat_api.py   tutor chat endpoints (chats, streaming replies, model settings)
  tutor.py      the tutor's instructions, built from your progress
  llm.py        OpenAI-compatible client for Gemini and Ollama
  furigana.py   kanji readings via MeCab/UniDic
  checks.py     kana vs romaji consistency check
  lessons.py    the hand-written N5 lessons (+ lessons_api.py)
  dictionary.py JMdict import and lookup
  words.py      JLPT word lists (jlpt_words.tsv) and example sentences (+ words_api.py)
  deck_api.py   saved words, mistakes and their reviews
  quiz.py       JLPT-style question generator (+ quiz_api.py)
  mock.py       timed mock tests: grammar questions, test builder and scoring (+ mock_api.py)
  missed_api.py reading and listening questions whose latest answer was wrong
  plan_api.py   today's study plan on Home
  backup_api.py daily copies of tutor.db, download and restore
  speech.py     Whisper transcription and shadowing comparison (+ speech_api.py)
  tts.py        VOICEVOX engine control and cached speech synthesis (+ tts_api.py)
  kanji.py      kanji index from KANJIDIC2 + KanjiVG strokes (+ kanji_api.py)
  kana_api.py   kana endpoints (groups, unlock, review, stats)
  kana.py       kana tables and answer checking
  srs.py        FSRS spaced-repetition wrapper
  db.py         SQLite schema
  static/       web UI (HTML/CSS/JS)
data/           your progress database (git-ignored)
```
