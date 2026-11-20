"use strict";

/* ================= helpers ================= */

const $ = (sel, root = document) => root.querySelector(sel);

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "class") node.className = v;
    else if (k.startsWith("on")) node.addEventListener(k.slice(2), v);
    else node.setAttribute(k, v === true ? "" : v);
  }
  for (const c of children.flat()) {
    if (c === null || c === undefined || c === false) continue;
    node.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return node;
}

const api = {
  async get(path) {
    const r = await fetch(path);
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    return r.json();
  },
  async post(path, body) {
    const r = await fetch(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    return r.json();
  },
};

// Per-browser conveniences only (chosen tab, toggles). Real progress lives in SQLite.
const prefs = {
  get(key, fallback) {
    try {
      const v = localStorage.getItem(key);
      return v === null ? fallback : JSON.parse(v);
    } catch { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* ignore */ }
  },
};

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function timeUntil(ts) {
  const s = ts - Date.now() / 1000;
  if (s < 60) return "in under a minute";
  if (s < 3600) return `in ${Math.round(s / 60)} min`;
  if (s < 86400) return `in ${Math.round(s / 3600)} h`;
  const d = Math.round(s / 86400);
  return d === 1 ? "tomorrow" : `in ${d} days`;
}

const isCorrect = (item, answer) => item.accept.includes(answer.trim().toLowerCase());

const SCRIPT_LABEL = { hiragana: "ひらがな", katakana: "カタカナ" };

/* ================= speech ================= */

let jaVoice = null;

function pickVoice() {
  const voices = speechSynthesis.getVoices().filter(v => v.lang.replace("_", "-").startsWith("ja"));
  // Prefer the higher quality "Natural"/"Online" voices when the browser offers them.
  jaVoice = voices.find(v => /natural|online|google/i.test(v.name)) || voices[0] || null;
}

if ("speechSynthesis" in window) {
  pickVoice();
  speechSynthesis.addEventListener("voiceschanged", pickVoice);
}

function speak(text) {
  if (!jaVoice) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.voice = jaVoice;
  u.lang = "ja-JP";
  u.rate = 0.8;
  speechSynthesis.speak(u);
}

function speakButton(text) {
  return el("button", {
    class: "speak",
    type: "button",
    title: jaVoice ? "Play sound" : "No Japanese voice found in this browser",
    "aria-label": "Play sound",
    onclick: e => { e.stopPropagation(); speak(text); },
  }, "🔊");
}

/* ================= routing ================= */

let cleanups = [];

function onCleanup(fn) { cleanups.push(fn); }

function addKeyHandler(handler) {
  document.addEventListener("keydown", handler);
  onCleanup(() => document.removeEventListener("keydown", handler));
}

function later(fn, ms) {
  const id = setTimeout(fn, ms);
  onCleanup(() => clearTimeout(id));
}

const views = {
  home: renderHome,
  learn: renderLearn,
  review: renderReview,
  practice: renderPractice,
};

function route() {
  cleanups.forEach(fn => fn());
  cleanups = [];
  const name = views[location.hash.slice(1)] ? location.hash.slice(1) : "home";
  for (const section of document.querySelectorAll(".view")) {
    section.hidden = section.id !== `view-${name}`;
  }
  for (const link of document.querySelectorAll(".nav a")) {
    link.classList.toggle("active", link.dataset.view === name);
  }
  views[name]().catch(showError);
  if (name !== "home") refreshBadge();
}

function showError(err) {
  console.error(err);
  const section = document.querySelector(".view:not([hidden]) .panel") || $("main");
  section.append(el("p", { class: "feedback bad" }, `Something went wrong: ${err.message}`));
}

function updateBadge(count) {
  const badge = $("#due-badge");
  badge.hidden = !count;
  badge.textContent = count;
}

async function refreshBadge() {
  try { updateBadge((await api.get("/api/kana/stats")).due_count); } catch { /* ignore */ }
}

/* script toggles (ひらがな / カタカナ) */

function getScript(key) { return prefs.get(`script.${key}`, "hiragana"); }

function syncToggles() {
  for (const toggle of document.querySelectorAll("[data-script-toggle]")) {
    const current = getScript(toggle.dataset.scriptToggle);
    for (const b of toggle.querySelectorAll("button")) {
      b.classList.toggle("active", b.dataset.script === current);
    }
  }
}

document.addEventListener("click", e => {
  const button = e.target.closest("[data-script-toggle] button");
  if (!button) return;
  prefs.set(`script.${button.parentElement.dataset.scriptToggle}`, button.dataset.script);
  syncToggles();
  route();
});

/* ================= home ================= */

async function renderHome() {
  const script = getScript("home");
  const [stats, data] = await Promise.all([
    api.get("/api/kana/stats"),
    api.get(`/api/kana/groups?script=${script}`),
  ]);

  updateBadge(stats.due_count);
  $("#stat-due").textContent = stats.due_count;
  $("#stat-due-btn").hidden = stats.due_count === 0;
  $("#stat-next").textContent = stats.due_count
    ? ""
    : stats.next_due ? `Next review ${timeUntil(stats.next_due)}` : "Learn your first kana to start";
  $("#stat-streak").textContent = stats.streak_days;
  $("#stat-today").textContent = stats.reviews_today;
  $("#stat-accuracy").textContent = stats.accuracy_today === null
    ? "reviews"
    : `reviews · ${Math.round(stats.accuracy_today * 100)}% correct`;

  const s = stats.scripts[script];
  const known = s.known + s.mastered;
  $("#chart-progress").style.width = `${(known / s.total) * 100}%`;
  $("#chart-progress-label").textContent = `${known} / ${s.total} known`;

  const chart = $("#kana-chart");
  chart.replaceChildren(...data.groups.map(g => {
    const isNext = g.id === data.next_group;
    return el("div", { class: `chart-row${isNext ? " next" : ""}` },
      el("div", { class: "chart-label" },
        g.label,
        isNext && el("a", { class: "btn btn-primary", href: "#learn",
          onclick: () => prefs.set("script.learn", script) }, "Learn next →"),
      ),
      el("div", { class: "chart-cells" }, g.items.map(item =>
        el("button", {
          class: `cell ${item.status}${item.kana.length > 1 ? " wide" : ""}`,
          type: "button",
          title: `${item.kana} — ${item.romaji} (${item.status === "locked" ? "not learned" : item.status})`,
          onclick: () => speak(item.kana),
        },
          el("span", { class: "k", lang: "ja" }, item.kana),
          el("span", { class: "r" }, item.romaji),
        ),
      )),
    );
  }));
}

/* ================= learn ================= */

async function renderLearn() {
  syncToggles();
  const script = getScript("learn");
  const body = $("#learn-body");
  const data = await api.get(`/api/kana/groups?script=${script}`);

  if (!data.next_group) {
    const other = script === "hiragana" ? "katakana" : "hiragana";
    body.replaceChildren(el("div", { class: "empty" },
      el("div", { class: "big" }, "🎉"),
      el("h2", {}, `You've learned every ${script} character!`),
      el("p", {}, "Keep them fresh with your daily reviews."),
      el("div", { class: "btn-row" },
        el("button", { class: "btn btn-primary", onclick: () => {
          prefs.set("script.learn", other); syncToggles(); route();
        } }, `Learn ${other}`),
        el("a", { class: "btn", href: "#practice" }, "Practice"),
      ),
    ));
    return;
  }

  const index = data.groups.findIndex(g => g.id === data.next_group);
  const group = data.groups[index];
  studyStep(body, script, group, `Set ${index + 1} of ${data.groups.length}`);
}

function studyStep(body, script, group, position) {
  let i = 0;
  const stage = el("div", { class: "card-stage" });
  const dots = el("div", { class: "dots" });
  const prevBtn = el("button", { class: "btn", onclick: () => show(i - 1) }, "← Back");
  const nextBtn = el("button", { class: "btn btn-primary", onclick: () => next() });

  body.replaceChildren(
    el("p", { class: "muted" },
      `${position} · ${group.label}. Study each one, then pass a quick check to add them to your reviews.`),
    stage,
    dots,
    el("div", { class: "btn-row" },
      prevBtn, nextBtn,
      el("button", { class: "btn btn-ghost", onclick: () => checkStep(body, script, group) },
        "I already know these → quick check"),
    ),
    el("p", { class: "hint", style: "text-align:center" },
      el("kbd", {}, "←"), " ", el("kbd", {}, "→"), " to move, ", el("kbd", {}, "Space"), " to hear it again"),
  );

  function next() {
    if (i < group.items.length - 1) show(i + 1);
    else checkStep(body, script, group);
  }

  function show(n) {
    i = Math.max(0, Math.min(group.items.length - 1, n));
    const item = group.items[i];
    stage.replaceChildren(
      el("div", { class: "card-meta" }, `${i + 1} / ${group.items.length}`, speakButton(item.kana)),
      el("div", { class: "big-kana", lang: "ja" }, item.kana),
      el("div", { class: "big-romaji" }, item.romaji),
      item.note && el("div", { class: "note" }, item.note),
    );
    dots.replaceChildren(...group.items.map((it, n2) =>
      el("button", { class: n2 === i ? "active" : "", lang: "ja", onclick: () => show(n2) }, it.kana)));
    prevBtn.disabled = i === 0;
    nextBtn.textContent = i === group.items.length - 1 ? "Quick check →" : "Next →";
    speak(item.kana);
  }

  addKeyHandler(e => {
    if (e.key === "ArrowRight" || e.key === "Enter") { e.preventDefault(); next(); }
    else if (e.key === "ArrowLeft") show(i - 1);
    else if (e.key === " ") { e.preventDefault(); speak(group.items[i].kana); }
  });

  show(0);
}

function checkStep(body, script, group) {
  cleanups.forEach(fn => fn());
  cleanups = [];

  let queue = shuffle(group.items);
  const total = queue.length;
  let passed = 0;

  const bar = el("div", { class: "progress-fill" });
  const label = el("span");
  const stage = el("div", { class: "card-stage" });

  body.replaceChildren(
    el("p", { class: "muted" }, `Quick check · ${group.label}. Type the reading of each kana. Misses come back until you get them.`),
    el("div", { class: "session-bar" }, el("div", { class: "progress" }, bar), label),
    stage,
  );

  function render() {
    bar.style.width = `${(passed / total) * 100}%`;
    label.textContent = `${passed} / ${total}`;
    if (!queue.length) return finish();

    const item = queue[0];
    let answered = false;
    let correct = false;
    let moved = false;
    const input = el("input", {
      class: "answer", autocomplete: "off", autocapitalize: "off", spellcheck: "false",
      placeholder: "romaji", "aria-label": "Reading in romaji",
    });
    const feedback = el("div", { class: "feedback" });

    input.addEventListener("keydown", e => {
      if (e.key !== "Enter") return;
      e.preventDefault();
      if (answered) return advance(correct);
      if (!input.value.trim()) return;
      answered = true;
      input.readOnly = true;
      speak(item.kana);
      correct = isCorrect(item, input.value);
      if (correct) {
        input.classList.add("ok");
        feedback.className = "feedback ok";
        feedback.textContent = `✓ ${item.romaji}`;
        later(() => advance(true), 650);
      } else {
        input.classList.add("bad");
        feedback.className = "feedback bad";
        feedback.textContent = `✗ It's “${item.romaji}” — press Enter to continue`;
      }
    });

    function advance(ok) {
      if (moved) return; // Enter and the auto-advance timer can both fire
      moved = true;
      queue.shift();
      if (ok) passed++;
      else queue.splice(Math.min(queue.length, 2 + Math.floor(Math.random() * 2)), 0, item);
      render();
    }

    stage.replaceChildren(
      el("div", { class: "big-kana", lang: "ja" }, item.kana),
      input,
      feedback,
    );
    input.focus();
  }

  async function finish() {
    try {
      const res = await api.post("/api/kana/unlock", { script, group: group.id });
      refreshBadge();
      body.replaceChildren(el("div", { class: "empty" },
        el("div", { class: "big" }, "✨"),
        el("h2", {}, `${group.label} learned!`),
        el("p", {}, res.added
          ? `${res.added} kana added to your reviews. They'll come back right before you'd forget them.`
          : "These were already in your reviews."),
        el("div", { class: "btn-row" },
          el("a", { class: "btn btn-primary", href: "#review" }, "Review now"),
          el("button", { class: "btn", onclick: () => route() }, "Learn the next set"),
        ),
      ));
    } catch (err) {
      showError(err);
    }
  }

  render();
}

/* ================= review ================= */

async function renderReview() {
  const body = $("#review-body");
  const autoplay = $("#opt-autoplay");
  autoplay.checked = prefs.get("autoplay", true);
  autoplay.onchange = () => prefs.set("autoplay", autoplay.checked);

  const session = { reviewed: 0, correct: 0 };
  await loadBatch();

  async function loadBatch() {
    const data = await api.get("/api/kana/review");
    updateBadge(data.due_count);
    if (!data.cards.length) return finished(data.next_due);
    showCard(data.cards, 0, data.due_count);
  }

  function showCard(cards, idx, dueCount) {
    if (idx >= cards.length) return loadBatch();
    const card = cards[idx];
    const remaining = dueCount - idx;
    const shownAt = performance.now();
    let answered = false;

    const input = el("input", {
      class: "answer", autocomplete: "off", autocapitalize: "off", spellcheck: "false",
      placeholder: "romaji", "aria-label": "Reading in romaji",
    });
    const feedback = el("div", { class: "feedback" });
    const noteBox = el("div");

    input.addEventListener("keydown", async e => {
      if (e.key !== "Enter") return;
      e.preventDefault();
      if (answered) return next();
      if (!input.value.trim()) return;
      answered = true;
      input.readOnly = true;

      const res = await api.post("/api/kana/review", {
        card_id: card.id,
        answer: input.value,
        elapsed_ms: Math.round(performance.now() - shownAt),
      });
      session.reviewed++;
      if (res.correct) session.correct++;
      updateBadge(Math.max(0, remaining - 1));
      if (autoplay.checked) speak(card.kana);

      if (res.correct) {
        input.classList.add("ok");
        feedback.className = "feedback ok";
        feedback.textContent = `✓ ${res.romaji}`;
        later(next, 700);
      } else {
        input.classList.add("bad");
        feedback.className = "feedback bad";
        feedback.textContent = `✗ It's “${res.romaji}” — press Enter to continue`;
        if (card.note) noteBox.replaceChildren(el("div", { class: "note" }, card.note));
      }
    });

    let moved = false;
    function next() {
      if (moved) return;
      moved = true;
      showCard(cards, idx + 1, dueCount);
    }

    body.replaceChildren(
      el("div", { class: "session-bar" },
        el("span", {}, `${remaining} left`),
        el("div", { class: "progress" },
          el("div", { class: "progress-fill",
            style: `width:${(session.reviewed / (session.reviewed + remaining)) * 100}%` })),
        el("span", {}, `${session.reviewed} done`),
      ),
      el("div", { class: "card-stage" },
        el("div", { class: "card-meta" }, el("span", { lang: "ja" }, SCRIPT_LABEL[card.script]), speakButton(card.kana)),
        el("div", { class: "big-kana", lang: "ja" }, card.kana),
        input,
        feedback,
        noteBox,
      ),
    );
    input.focus();
  }

  function finished(nextDue) {
    const pct = session.reviewed ? Math.round((session.correct / session.reviewed) * 100) : null;
    body.replaceChildren(el("div", { class: "empty" },
      el("div", { class: "big" }, session.reviewed ? "🌸" : "🍵"),
      el("h2", {}, session.reviewed ? "Review complete!" : "Nothing to review right now"),
      session.reviewed && el("div", { class: "summary" },
        el("div", {}, el("strong", {}, session.reviewed), "reviewed"),
        el("div", {}, el("strong", {}, `${pct}%`), "correct"),
      ),
      el("p", {}, nextDue ? `Next review ${timeUntil(nextDue)}.` : "Learn some kana to fill your review queue."),
      el("div", { class: "btn-row" },
        el("a", { class: "btn btn-primary", href: "#learn" }, "Learn new kana"),
        el("a", { class: "btn", href: "#practice" }, "Free practice"),
      ),
    ));
    // Fresh cards come back within minutes; pick them up without a manual refresh.
    if (nextDue && nextDue - Date.now() / 1000 < 15 * 60) {
      later(() => loadBatch().catch(showError), Math.max(1000, (nextDue * 1000) - Date.now() + 500));
    }
  }
}

/* ================= practice ================= */

async function renderPractice() {
  const body = $("#practice-body");
  const [hira, kata] = await Promise.all(
    ["hiragana", "katakana"].map(s => api.get(`/api/kana/groups?script=${s}`)));
  const byScript = { hiragana: hira.groups, katakana: kata.groups };

  const saved = prefs.get("practice", null);
  const unlockedIds = new Set(
    [...hira.groups, ...kata.groups].filter(g => g.unlocked).map(g => g.id));
  const settings = saved || {
    scripts: ["hiragana"],
    groups: unlockedIds.size ? [...unlockedIds] : ["a"],
    mode: "type",
  };

  const scriptChips = ["hiragana", "katakana"].map(s =>
    el("label", { class: "chip" },
      el("input", { type: "checkbox", value: s, checked: settings.scripts.includes(s) }),
      el("span", { lang: "ja" }, SCRIPT_LABEL[s])));

  const groupChips = hira.groups.map(g =>
    el("label", { class: "chip", title: g.items.map(i => i.kana).join(" ") },
      el("input", { type: "checkbox", value: g.id, checked: settings.groups.includes(g.id) }),
      g.label,
      unlockedIds.has(g.id) ? null : el("span", { class: "muted" }, "· new")));

  const modeToggle = el("div", { class: "segmented" },
    el("button", { "data-mode": "type", type: "button" }, "Type the reading"),
    el("button", { "data-mode": "pick", type: "button" }, "Pick the kana"));
  const setMode = m => {
    settings.mode = m;
    modeToggle.querySelectorAll("button").forEach(b => b.classList.toggle("active", b.dataset.mode === m));
  };
  modeToggle.addEventListener("click", e => e.target.dataset.mode && setMode(e.target.dataset.mode));
  setMode(settings.mode);

  const setAllGroups = on => groupChips.forEach(c => { c.querySelector("input").checked = on; });
  const error = el("p", { class: "feedback bad" });

  body.replaceChildren(
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Scripts"),
      el("div", { class: "chips" }, scriptChips)),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Sets",
        el("span", {},
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => setAllGroups(true) }, "All"),
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => setAllGroups(false) }, "None"))),
      el("div", { class: "chips" }, groupChips)),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Mode"),
      modeToggle),
    error,
    el("div", { class: "btn-row" },
      el("button", { class: "btn btn-primary", onclick: start }, "Start practice")),
  );

  function start() {
    settings.scripts = scriptChips.map(c => c.querySelector("input")).filter(i => i.checked).map(i => i.value);
    settings.groups = groupChips.map(c => c.querySelector("input")).filter(i => i.checked).map(i => i.value);
    const pool = settings.scripts.flatMap(s =>
      byScript[s].filter(g => settings.groups.includes(g.id))
        .flatMap(g => g.items.map(item => ({ ...item, script: s }))));
    if (pool.length < 4) {
      error.textContent = "Pick at least one script and enough sets for 4+ kana.";
      return;
    }
    prefs.set("practice", settings);
    runPractice(body, pool, settings.mode);
  }
}

function runPractice(body, pool, mode) {
  const score = { right: 0, total: 0, streak: 0 };
  const retry = []; // missed items, each with a countdown until it comes back
  let last = null;

  const scoreLabel = el("span");
  const stage = el("div", { class: "card-stage" });

  body.replaceChildren(
    el("div", { class: "session-bar" },
      scoreLabel,
      el("span", { style: "flex:1" }),
      el("button", { class: "btn", onclick: () => route() }, "Stop")),
    stage,
  );

  function pickItem() {
    retry.forEach(r => r.wait--);
    const ready = retry.findIndex(r => r.wait <= 0);
    if (ready !== -1) return retry.splice(ready, 1)[0].item;
    let item;
    do { item = pool[Math.floor(Math.random() * pool.length)]; } while (item === last && pool.length > 1);
    return item;
  }

  function record(item, correct) {
    score.total++;
    if (correct) { score.right++; score.streak++; }
    else { score.streak = 0; retry.push({ item, wait: 3 }); }
  }

  function updateScore() {
    scoreLabel.textContent = score.total
      ? `${score.right} / ${score.total} correct · streak ${score.streak}`
      : "Let's go!";
  }

  function nextQuestion() {
    cleanups.forEach(fn => fn());
    cleanups = [];
    updateScore();
    const item = pickItem();
    last = item;
    (mode === "pick" ? askPick : askType)(item);
  }

  function askType(item) {
    let answered = false;
    const input = el("input", {
      class: "answer", autocomplete: "off", autocapitalize: "off", spellcheck: "false",
      placeholder: "romaji", "aria-label": "Reading in romaji",
    });
    const feedback = el("div", { class: "feedback" });

    input.addEventListener("keydown", e => {
      if (e.key !== "Enter") return;
      e.preventDefault();
      if (answered) return nextQuestion();
      if (!input.value.trim()) return;
      answered = true;
      input.readOnly = true;
      const ok = isCorrect(item, input.value);
      record(item, ok);
      updateScore();
      speak(item.kana);
      input.classList.add(ok ? "ok" : "bad");
      feedback.className = `feedback ${ok ? "ok" : "bad"}`;
      feedback.textContent = ok ? `✓ ${item.romaji}` : `✗ It's “${item.romaji}” — press Enter to continue`;
      if (ok) later(nextQuestion, 600);
    });

    stage.replaceChildren(
      el("div", { class: "card-meta" }, el("span", { lang: "ja" }, SCRIPT_LABEL[item.script])),
      el("div", { class: "big-kana", lang: "ja" }, item.kana),
      input,
      feedback,
    );
    input.focus();
  }

  function askPick(item) {
    // Distractors from the same script, never sharing the same reading (ぢ/じ, づ/ず).
    const others = shuffle(pool.filter(p =>
      p.script === item.script && p.romaji !== item.romaji));
    const fallback = shuffle(pool.filter(p => p.romaji !== item.romaji && !others.includes(p)));
    const options = shuffle([item, ...[...others, ...fallback].slice(0, 3)]);
    let answered = false;

    const feedback = el("div", { class: "feedback" });
    const buttons = options.map((opt, n) =>
      el("button", { class: "choice", lang: "ja", type: "button", onclick: () => choose(n) }, opt.kana));

    function choose(n) {
      if (answered) return;
      answered = true;
      const ok = options[n] === item;
      record(item, ok);
      updateScore();
      speak(item.kana);
      buttons.forEach((b, i) => {
        b.disabled = true;
        if (options[i] === item) b.classList.add("ok");
        else if (i === n) b.classList.add("bad");
      });
      feedback.className = `feedback ${ok ? "ok" : "bad"}`;
      feedback.textContent = ok ? "✓ Correct" : `✗ “${item.romaji}” is ${item.kana}`;
      later(nextQuestion, ok ? 600 : 1600);
    }

    addKeyHandler(e => {
      const n = Number(e.key) - 1;
      if (n >= 0 && n < buttons.length) choose(n);
    });

    stage.replaceChildren(
      el("div", { class: "card-meta" }, "Which kana is…"),
      el("div", { class: "big-romaji", style: "font-size:3rem;margin:.5rem 0" }, item.romaji),
      el("div", { class: "choices" }, buttons),
      feedback,
      el("p", { class: "hint" }, "Keys ", el("kbd", {}, "1"), "–", el("kbd", {}, "4"), " also work"),
    );
  }

  nextQuestion();
}

/* ================= boot ================= */

window.addEventListener("hashchange", route);
syncToggles();
route();
