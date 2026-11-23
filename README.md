# 日本語 Tutor

A personal Japanese tutor that runs in the browser, built for going from zero to
passing the JLPT (N5, then N4, N3 and N2), powered by a free AI API or a local model.

## Features

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
  stroke counts), and the reading of a kanji word; drawn from your studied kanji or the N5/N4/N3/N2 lists
- Generated from verified lesson content and your saved words, never by the AI
- Reading distractors are near misses like on the real test (がっこう / がこう / かっこう)
- Per-type scores, explanations, and one click to add missed words to your reviews

**Speaking (local Whisper)**
- 🎤 in the chat: speak Japanese, check the transcript, send it to Sensei
- 🎤 on every lesson example: say the sentence and see which sounds were recognized
- Runs on your own machine (faster-whisper, CPU); compares by sound, so 学校 = がっこう

**Progress dashboard (Home)**
- JLPT N5 building blocks: kana, lessons, vocabulary toward ~800 words, quiz accuracy per section
- Last 30 days of study (kana, words & mistakes, quizzes) with hover details and a table view
- Quiz score trend; study days, total reviews and quizzes

**Kanji study**
- Lists closest to N5 (103), N4 (181), N3 (about 400) and N2 (about 340), plus every other kanji
  used in the lessons. KANJIDIC only has the pre-2010 JLPT levels: old levels 4 and 3 match N5 and
  N4; old level 2 mixes N3 and N2, so the N3 list is its 300 most common kanji plus the ones the
  lessons use, and the N2 list is the rest. There has been no official kanji list since 2010, so
  these are close guides, not official lists
- Animated stroke order (KanjiVG), on/kun readings with audio, meanings, and example words
  (lesson vocabulary first, then common dictionary words)
- Meanings put what learners actually meet first: KANJIDIC's order can mislead (緒 starts with
  "thong", 校 with "exam"), so 232 kanji have hand-checked meanings first (緒 = together, as in
  一緒) in `app/kanji_meanings.py`. Quiz and writing prompts never show a note containing the answer
- Add kanji to your reviews one by one or five at a time; they join the Review tab and the dashboard
- Handwriting: draw each stroke with a mouse, finger or pen; order, direction and shape are checked
  stroke by stroke against KanjiVG, with hints after repeated misses. Trace or write from memory on
  any kanji page, or run a writing session (see the meaning and reading, write the kanji)
- Writing from memory updates the kanji's review schedule: no mistakes counts as Good, one or two
  as Hard, three or more (or using a hint) as Again. Tracing never counts, kanji not in your reviews
  are left alone, and a kanji reviewed in the last 12 hours that isn't due yet isn't graded again.
  Turn on "Write kanji from memory" in the Review tab to answer due kanji by writing them

**Reading practice (JLPT 読解, N3 and N2)**
- 20 hand-written N3 passages: notes, emails, notices, short essays and information-search pages,
  with 36 JLPT-style questions in Japanese and an English explanation for every answer
- 20 N2 passages (40 questions): formal notices and emails, opinion essays, information-search pages,
  and A/B comparisons where two writers argue opposite sides, as in the N2 test
- Furigana toggle; kanji beyond the passage's level keep their furigana, as on the real test
- Tap any word to look it up; 🔊 reads each paragraph; after answering, see the translation and add
  the key words to your reviews. Scores are saved, and the dashboard counts passages read
- `python -m app.reading` checks the questions; add `--readings` to proofread the furigana

**Listening practice (JLPT 聴解, N3 and N2)**
- 20 hand-written N3 items in the four test formats: task-based (課題理解), key point (ポイント理解),
  summary (概要理解) and quick response (即時応答)
- 10 N2 items, adding integrated comprehension (統合理解): a staff member explains three options, two
  people discuss them, and you work out which one a person chooses
- Read by VOICEVOX with a different voice per role (narrator 九州そら, woman 春日部つむぎ, man 玄野武宏,
  staff 青山龍星);
  the clips are made before the first play so lines follow each other smoothly. Without VOICEVOX the
  browser's voice is used at a different pitch per role
- As on the test, summary and quick-response choices are only spoken; after answering you get the
  transcript with furigana, a translation of every line, and the key words
- Under "Read & listen" in the top bar, next to reading practice; `python -m app.listening` checks the
  items (`--readings` prints the transcripts' furigana)

**Dictionary, notebook and reviews**
- Click any Japanese word (chat or lessons) to look it up in JMdict and save it
- Sensei logs the mistakes it corrects; they come back as review cards
- The Review tab covers kana, saved words (typed readings checked strictly) and mistakes
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
  deck_api.py   saved words, mistakes and their reviews
  quiz.py       JLPT-style question generator (+ quiz_api.py)
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
