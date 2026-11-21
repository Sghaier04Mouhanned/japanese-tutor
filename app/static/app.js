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

async function request(method, path, body) {
  const r = await fetch(path, body === undefined ? { method } : {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
  return r.json();
}

const api = {
  get: path => request("GET", path),
  post: (path, body) => request("POST", path, body),
  put: (path, body) => request("PUT", path, body),
  delete: path => request("DELETE", path),
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

// VOICEVOX (natural voices, run locally by the server) when it's available,
// otherwise the browser's built-in Japanese voice.
let tts = { running: false, installed: false };
let currentAudio = null;

async function refreshTts() {
  try { tts = await api.get("/api/tts/status"); } catch { tts = { running: false, installed: false }; }
  return tts;
}

// Resolves once we know whether VOICEVOX is up. The engine needs a little
// while to start with the app, so keep checking for a bit.
const ttsChecked = (async () => {
  for (let i = 0; i < 24; i++) {
    const s = await refreshTts();
    if (s.running || !s.installed) break;
    await new Promise(r => setTimeout(r, 5000));
  }
})();

const hasVoice = () => tts.running || !!jaVoice;

function browserSpeak(text) {
  if (!jaVoice) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.voice = jaVoice;
  u.lang = "ja-JP";
  u.rate = 0.8;
  speechSynthesis.speak(u);
}

function speak(text) {
  if (!text) return;
  currentAudio?.pause();
  if ("speechSynthesis" in window) speechSynthesis.cancel();
  if (!tts.running || text.length > 300) return browserSpeak(text);
  const audio = new Audio(`/api/tts?text=${encodeURIComponent(text)}`);
  currentAudio = audio;
  let fellBack = false;
  const fallback = () => { if (!fellBack) { fellBack = true; browserSpeak(text); } };
  audio.addEventListener("error", fallback);
  audio.play().catch(fallback);
}

// Generate audio ahead of time (one sentence at a time, the engine is single-file),
// so 🔊 plays instantly from the server's cache when pressed.
let prefetchQueue = Promise.resolve();
function prefetchSpeech(texts) {
  for (const text of texts) {
    if (!text || text.length > 300) continue;
    prefetchQueue = prefetchQueue
      .then(() => ttsChecked)  // pages can open before we know whether the engine is up
      .then(() => tts.running && fetch(`/api/tts?text=${encodeURIComponent(text)}`))
      .catch(() => {});
  }
}

function speakButton(text) {
  return el("button", {
    class: "speak",
    type: "button",
    title: hasVoice() ? "Play sound" : "No Japanese voice available",
    "aria-label": "Play sound",
    onclick: e => { e.stopPropagation(); speak(text); },
  }, "🔊");
}

/* ================= microphone + speech recognition ================= */

let speechStatus = null;

async function refreshSpeechStatus() {
  try { speechStatus = await api.get("/api/speech/status"); } catch { speechStatus = null; }
  return speechStatus;
}

let activeRecording = null;

async function startRecording() {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true } });
  const type = ["audio/webm;codecs=opus", "audio/webm", "audio/ogg;codecs=opus", "audio/mp4"]
    .find(t => window.MediaRecorder?.isTypeSupported(t)) || "";
  const recorder = new MediaRecorder(stream, type ? { mimeType: type } : undefined);
  const chunks = [];
  recorder.addEventListener("dataavailable", e => { if (e.data.size) chunks.push(e.data); });
  recorder.start();
  const stopped = new Promise(resolve => recorder.addEventListener("stop", () => {
    stream.getTracks().forEach(t => t.stop());
    resolve(new Blob(chunks, { type: recorder.mimeType }));
  }));
  // Safety net: never record forever if the learner forgets to stop.
  const timer = setTimeout(() => recorder.state === "recording" && recorder.stop(), 30000);
  activeRecording = { stop: () => { clearTimeout(timer); if (recorder.state === "recording") recorder.stop(); return stopped; } };
  return activeRecording;
}

async function transcribeBlob(blob) {
  const form = new FormData();
  form.append("audio", blob, "speech.webm");
  const r = await fetch("/api/speech/transcribe", { method: "POST", body: form });
  if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
  return r.json();
}

// A mic button: click to record, click again to stop. `onText(result)` gets the transcript.
function micButton({ onText, onError, label = "🎤", title = "Speak (click again to stop)" }) {
  const button = el("button", { class: "mic", type: "button", title, "aria-label": title }, label);
  let recording = null;
  button.addEventListener("click", async () => {
    if (button.classList.contains("busy")) return;
    if (recording) {
      const rec = recording;
      recording = null;
      button.classList.remove("recording");
      button.classList.add("busy");
      button.textContent = "…";
      try {
        onText(await transcribeBlob(await rec.stop()));
      } catch (err) {
        onError(err.message);
      } finally {
        button.classList.remove("busy");
        button.textContent = label;
      }
      return;
    }
    const status = speechStatus?.model_ready ? speechStatus : await refreshSpeechStatus();
    if (!status?.available) return onError("Speech recognition isn't installed on the server yet.");
    if (!status.model_ready) {
      api.post("/api/speech/prepare", {});
      return onError("The speech model is downloading (about 480 MB, one time). Try again in a few minutes.");
    }
    try {
      recording = await startRecording();
      button.classList.add("recording");
      button.textContent = "■";
    } catch (err) {
      recording = null;
      onError(err.name === "NotAllowedError" ? "Microphone access was blocked. Allow it in the browser's address bar." : err.message);
    }
  });
  onCleanup(() => { if (recording) recording.stop(); });
  return button;
}

/* ================= routing ================= */

let cleanups = [];
let routeArg = null;

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
  tutor: renderTutor,
  learn: renderLearn,
  review: renderReview,
  practice: renderPractice,
  notebook: renderNotebook,
  lessons: renderLessons,
  quiz: renderQuiz,
};

function route() {
  cleanups.forEach(fn => fn());
  cleanups = [];
  // "#lessons/n5-03" -> view "lessons", argument "n5-03"
  const [hashName, ...rest] = location.hash.slice(1).split("/");
  const name = views[hashName] ? hashName : "home";
  routeArg = rest.join("/") || null;
  for (const section of document.querySelectorAll(".view")) {
    section.hidden = section.id !== `view-${name}`;
  }
  const navName = name === "practice" ? "learn" : name; // Practice lives under Kana
  for (const link of document.querySelectorAll(".nav a")) {
    link.classList.toggle("active", link.dataset.view === navName);
  }
  closeWordPopup();
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

  renderProgress().catch(showError);

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

/* ================= progress dashboard ================= */

const SVG_NS = "http://www.w3.org/2000/svg";

function svg(tag, attrs = {}, ...children) {
  const node = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) if (v !== null && v !== undefined) node.setAttribute(k, v);
  node.append(...children.flat().filter(c => c !== null && c !== undefined && c !== false));
  return node;
}

// Round an axis maximum up to 1, 2 or 5 × a power of ten.
function niceMax(value) {
  if (value <= 0) return 1;
  const p = 10 ** Math.floor(Math.log10(value));
  return [1, 2, 5, 10].map(m => m * p).find(v => v >= value);
}

function shortDate(iso) {
  return new Date(`${iso}T12:00:00`).toLocaleDateString(undefined, { month: "short", day: "numeric" });
}

function chartTip(container) {
  const tip = el("div", { class: "chart-tip", hidden: true });
  container.append(tip);
  return {
    show(x, y, ...content) { tip.replaceChildren(...content); tip.style.left = `${x}px`; tip.style.top = `${y}px`; tip.hidden = false; },
    hide() { tip.hidden = true; },
  };
}

const SERIES = [
  ["kana", "Kana reviews", "var(--series-1)"],
  ["deck", "Word & mistake reviews", "var(--series-2)"],
  ["quiz", "Quiz questions", "var(--series-3)"],
];

function drawActivity(container, days) {
  container.replaceChildren();
  const totals = days.map(d => d.kana + d.deck + d.quiz);
  if (!totals.some(Boolean)) {
    container.append(el("div", { class: "chart-empty" }, "No study activity in the last 30 days yet."));
    return;
  }
  const W = Math.max(300, container.clientWidth), H = 190;
  const m = { l: 34, r: 8, t: 10, b: 24 };
  const plotW = W - m.l - m.r, plotH = H - m.t - m.b;
  const max = niceMax(Math.max(...totals));
  const y = v => m.t + plotH - (v / max) * plotH;
  const slot = plotW / days.length;
  const barW = Math.min(24, slot * 0.7);
  const root = svg("svg", { viewBox: `0 0 ${W} ${H}`, role: "img",
    "aria-label": "Study activity per day for the last 30 days. Use Show table for the numbers." });

  for (const v of [0, max / 2, max]) {
    root.append(svg("line", { class: v ? "grid" : "baseline", x1: m.l, x2: W - m.r, y1: y(v), y2: y(v) }));
    root.append(svg("text", { x: m.l - 6, y: y(v) + 4, "text-anchor": "end" }, String(Math.round(v))));
  }

  const tip = chartTip(container);
  days.forEach((d, i) => {
    const cx = m.l + slot * i + slot / 2;
    const band = svg("rect", { class: "hover-band", x: m.l + slot * i, y: m.t, width: slot, height: plotH, rx: 4 });
    root.append(band);
    // Stack bottom-up with a 2px surface gap between segments; only the top one gets rounded ends.
    const segs = SERIES.map(([key, , color]) => ({ v: d[key], color })).filter(s => s.v > 0);
    let base = y(0);
    segs.forEach((s, n) => {
      const h = (s.v / max) * plotH - (n > 0 ? 2 : 0);
      if (h <= 0) return;
      const top = base - h - (n > 0 ? 2 : 0);
      const x0 = cx - barW / 2;
      if (n === segs.length - 1) {
        const r = Math.min(4, h / 2, barW / 2);
        root.append(svg("path", { fill: s.color, d:
          `M${x0},${top + h} V${top + r} Q${x0},${top} ${x0 + r},${top} H${x0 + barW - r} ` +
          `Q${x0 + barW},${top} ${x0 + barW},${top + r} V${top + h} Z` }));
      } else {
        root.append(svg("rect", { fill: s.color, x: x0, y: top, width: barW, height: h }));
      }
      base = top;
    });
    // Weekly ticks, plus "Today"; drop a weekly tick that would crowd the last label.
    if (i === 0 || i === days.length - 1 || (i % 7 === 0 && days.length - 1 - i >= 4)) {
      root.append(svg("text", { x: cx, y: H - 6, "text-anchor": i === 0 ? "start" : i === days.length - 1 ? "end" : "middle" },
        i === days.length - 1 ? "Today" : shortDate(d.date)));
    }
    const hit = svg("rect", { class: "hit", x: m.l + slot * i, y: m.t, width: slot, height: plotH });
    const showTip = () => {
      band.classList.add("on");
      const scale = container.clientWidth / W;
      tip.show(cx * scale, (y(totals[i]) - 8) * scale,
        el("strong", {}, `${shortDate(d.date)} · ${totals[i]} total`),
        ...SERIES.map(([key, label, color]) => el("div", { class: "row" }, el("i", { style: `background:${color}` }), `${label}: ${d[key]}`)));
    };
    hit.addEventListener("mouseenter", showTip);
    hit.addEventListener("mouseleave", () => { band.classList.remove("on"); tip.hide(); });
    root.append(hit);
  });
  container.prepend(root);
}

function activityTable(days) {
  const rows = days.filter(d => d.kana + d.deck + d.quiz).reverse();
  return el("table", { class: "data-table" },
    el("thead", {}, el("tr", {}, el("th", {}, "Day"), SERIES.map(([, label]) => el("th", {}, label)), el("th", {}, "Total"))),
    el("tbody", {}, rows.map(d => el("tr", {},
      el("td", {}, shortDate(d.date)), SERIES.map(([key]) => el("td", {}, d[key])), el("td", {}, d.kana + d.deck + d.quiz)))));
}

function drawQuizTrend(container, history) {
  container.replaceChildren();
  if (!history.length) {
    container.append(el("div", { class: "chart-empty" }, "Take a quiz to start tracking your scores."));
    return;
  }
  const W = Math.max(300, container.clientWidth), H = 170;
  const m = { l: 40, r: 44, t: 12, b: 24 };
  const plotW = W - m.l - m.r, plotH = H - m.t - m.b;
  const pts = history.map((q, i) => ({
    ...q, pct: Math.round(q.correct / q.total * 100),
    x: m.l + (history.length === 1 ? plotW / 2 : (plotW * i) / (history.length - 1)),
  }));
  const y = v => m.t + plotH - (v / 100) * plotH;
  const root = svg("svg", { viewBox: `0 0 ${W} ${H}`, role: "img",
    "aria-label": `Quiz scores over your last ${pts.length} quizzes; latest ${pts.at(-1).pct}%.` });
  for (const v of [0, 50, 100]) {
    root.append(svg("line", { class: v ? "grid" : "baseline", x1: m.l, x2: W - m.r, y1: y(v), y2: y(v) }));
    root.append(svg("text", { x: m.l - 6, y: y(v) + 4, "text-anchor": "end" }, `${v}%`));
  }
  if (pts.length > 1) {
    root.append(svg("path", { fill: "var(--series-1)", opacity: 0.1,
      d: `M${pts[0].x},${y(0)} ${pts.map(p => `L${p.x},${y(p.pct)}`).join(" ")} L${pts.at(-1).x},${y(0)} Z` }));
    root.append(svg("path", { fill: "none", stroke: "var(--series-1)", "stroke-width": 2, "stroke-linejoin": "round",
      "stroke-linecap": "round", d: pts.map((p, i) => `${i ? "L" : "M"}${p.x},${y(p.pct)}`).join(" ") }));
  }
  const tip = chartTip(container);
  pts.forEach((p, i) => {
    root.append(svg("circle", { cx: p.x, cy: y(p.pct), r: 4, fill: "var(--series-1)", stroke: "var(--surface)", "stroke-width": 2 }));
    const hit = svg("circle", { class: "hit", cx: p.x, cy: y(p.pct), r: 12 });
    hit.addEventListener("mouseenter", () => {
      const scale = container.clientWidth / W;
      tip.show(p.x * scale, (y(p.pct) - 10) * scale,
        el("strong", {}, new Date(p.date * 1000).toLocaleString(undefined, { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" })),
        `${p.correct} / ${p.total} correct (${p.pct}%)`);
    });
    hit.addEventListener("mouseleave", () => tip.hide());
    root.append(hit);
    if (i === pts.length - 1) {
      root.append(svg("text", { class: "end-label", x: p.x + 8, y: y(p.pct) + 4 }, `${p.pct}%`));
    }
  });
  container.prepend(root);
}

async function renderProgress() {
  const data = await api.get("/api/progress");
  const t = data.totals;
  $("#progress-totals").textContent =
    `${t.study_days} study day${t.study_days === 1 ? "" : "s"} · ${t.reviews} reviews · ${t.quizzes} quiz${t.quizzes === 1 ? "" : "zes"}`;

  const meter = (label, value, total, text) => el("div", { class: `meter${total ? "" : " empty"}` },
    el("div", { class: "meter-label" }, el("span", {}, label), el("span", { class: "value" }, text)),
    el("div", { class: "meter-track", role: "progressbar", "aria-label": label,
      "aria-valuenow": total ? Math.round(value / total * 100) : 0, "aria-valuemin": 0, "aria-valuemax": 100 },
      el("div", { class: "meter-fill", style: `width:${total ? Math.min(100, value / total * 100) : 0}%` })));
  const known = c => c.known + c.mastered;
  const quizMeters = Object.entries(QUIZ_TYPES).map(([type, [jp, en]]) => {
    const s = data.quiz_by_type[type];
    return meter(`${jp} ${en}`, s?.correct || 0, s?.total || 0,
      s ? `${Math.round(s.correct / s.total * 100)}% of last ${s.total}` : "no quizzes yet");
  });
  $("#progress-meters").replaceChildren(
    meter("Hiragana", known(data.kana.hiragana), data.kana.hiragana.total, `${known(data.kana.hiragana)} / ${data.kana.hiragana.total}`),
    meter("Katakana", known(data.kana.katakana), data.kana.katakana.total, `${known(data.kana.katakana)} / ${data.kana.katakana.total}`),
    meter("Lessons", data.lessons.done, data.lessons.total, `${data.lessons.done} / ${data.lessons.total} complete`),
    meter("Vocabulary (≈800 for N5)", known(data.vocab), data.vocab.target, `${known(data.vocab)} known · ${data.vocab.saved} saved`),
    ...quizMeters);

  const draw = () => {
    drawActivity($("#activity-chart"), data.activity);
    drawQuizTrend($("#quiz-chart"), data.quiz_history);
  };
  draw();
  const last = data.quiz_history.at(-1);
  $("#quiz-trend-note").textContent = last ? `Last ${data.quiz_history.length} quizzes` : "";

  const tableBtn = $("#activity-table-btn");
  const table = $("#activity-table");
  table.hidden = true;
  tableBtn.textContent = "Show table";
  tableBtn.onclick = () => {
    table.hidden = !table.hidden;
    tableBtn.textContent = table.hidden ? "Show table" : "Hide table";
    if (!table.hidden) table.replaceChildren(activityTable(data.activity));
  };

  let resizeTimer;
  const onResize = () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(draw, 150); };
  window.addEventListener("resize", onResize);
  onCleanup(() => window.removeEventListener("resize", onResize));
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

  // Kana first (quick, typed), then saved words and mistakes (self-graded).
  async function loadBatch() {
    const [kanaData, deckData] = await Promise.all([api.get("/api/kana/review"), api.get("/api/deck/review")]);
    const total = kanaData.due_count + deckData.due_count;
    updateBadge(total);
    if (kanaData.cards.length) return showCard(kanaData.cards, 0, total);
    if (deckData.cards.length) return showDeckCard(deckData.cards, 0, deckData.due_count);
    const upcoming = [kanaData.next_due, deckData.next_due].filter(Boolean);
    finished(upcoming.length ? Math.min(...upcoming) : null);
  }

  function sessionBar(remaining) {
    return el("div", { class: "session-bar" },
      el("span", {}, `${remaining} left`),
      el("div", { class: "progress" },
        el("div", { class: "progress-fill",
          style: `width:${(session.reviewed / (session.reviewed + remaining)) * 100}%` })),
      el("span", {}, `${session.reviewed} done`));
  }

  function showDeckCard(cards, idx, dueCount) {
    if (idx >= cards.length) return loadBatch();
    const card = cards[idx];
    const remaining = dueCount - idx;
    const shownAt = performance.now();
    const stage = el("div", { class: "card-stage" });
    let keyHandler = null;
    const setKeys = fn => {
      if (keyHandler) document.removeEventListener("keydown", keyHandler);
      keyHandler = fn;
      if (fn) document.addEventListener("keydown", fn);
    };
    onCleanup(() => setKeys(null));

    async function grade(rating) {
      setKeys(null);
      stage.querySelectorAll("button").forEach(b => { b.disabled = true; });
      await api.post("/api/deck/review", {
        card_id: card.id, rating, elapsed_ms: Math.round(performance.now() - shownAt),
      });
      session.reviewed++;
      if (rating !== "again") session.correct++;
      updateBadge(Math.max(0, remaining - 1));
      showDeckCard(cards, idx + 1, dueCount);
    }

    const gradeButtons = () => el("div", { class: "grade-row" },
      [["again", "Again", "forgot"], ["hard", "Hard", "barely"], ["good", "Good", "knew it"], ["easy", "Easy", "instant"]]
        .map(([r, label, hint], n) => el("button", { class: `btn grade-${r}`, type: "button", onclick: () => grade(r) },
          label, el("small", {}, `${n + 1} · ${hint}`))));
    const gradeKeys = e => {
      const r = ["again", "hard", "good", "easy"][Number(e.key) - 1];
      if (r && e.target.tagName !== "TEXTAREA") grade(r);
    };

    if (card.kind === "vocab") {
      const reveal = el("div", { class: "reveal" });
      const showAnswer = (readingOk = null) => {
        reveal.replaceChildren(
          el("div", { class: "word-head" },
            el("span", { class: "word-reading", lang: "ja", style: "font-size:1.3rem" }, card.reading),
            speakButton(card.reading)),
          el("div", { class: "meaning" }, card.meaning),
          readingOk === false
            ? el("div", { class: "btn-row" }, el("button", { class: "btn btn-primary", type: "button",
                onclick: () => grade("again") }, "Continue"))
            : gradeButtons());
        speak(card.reading);
        setKeys(readingOk === false
          ? e => { if (e.key === "Enter") { e.preventDefault(); grade("again"); } }
          : gradeKeys);
      };

      stage.append(
        el("div", { class: "prompt-label" }, card.ask_reading ? "How do you read this word, and what does it mean?" : "What does this word mean?"),
        el("div", { class: "big-word", lang: "ja" }, card.word));

      if (card.ask_reading) {
        const input = el("input", { class: "answer", autocomplete: "off", autocapitalize: "off",
          spellcheck: "false", placeholder: "reading in romaji", "aria-label": "Reading in romaji" });
        const feedback = el("div", { class: "feedback" });
        input.addEventListener("keydown", async e => {
          if (e.key !== "Enter" || input.readOnly || !input.value.trim()) return;
          e.preventDefault();
          e.stopPropagation(); // don't let this Enter also press "Continue"
          input.readOnly = true;
          const { correct } = await api.post("/api/deck/check-reading", { reading: card.reading, answer: input.value });
          input.classList.add(correct ? "ok" : "bad");
          feedback.className = `feedback ${correct ? "ok" : "bad"}`;
          feedback.textContent = correct ? "✓ Reading correct. Did you know the meaning?" : "✗ Not quite. It comes back soon.";
          showAnswer(correct);
        });
        stage.append(input, feedback, reveal);
        later(() => input.focus(), 0);
      } else {
        const show = el("button", { class: "btn btn-primary", type: "button", onclick: () => showAnswer() }, "Show answer");
        reveal.append(show);
        stage.append(reveal);
        setKeys(e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); showAnswer(); } });
      }
    } else {
      const attempt = el("textarea", { class: "answer", rows: 2, lang: "ja",
        placeholder: "Your corrected version (optional)", style: "font-size:1.1rem" });
      const reveal = el("div", { class: "reveal" });
      const showAnswer = () => {
        attempt.readOnly = true;
        attempt.blur(); // so the 1–4 grading keys work
        reveal.replaceChildren(
          el("div", { class: "fix", style: "font-size:1.3rem" }, el("span", { class: "new" }, card.correct)),
          card.note && el("div", { class: "note" }, card.note),
          gradeButtons());
        speak(card.correct);
        setKeys(gradeKeys);
      };
      reveal.append(el("button", { class: "btn btn-primary", type: "button", onclick: showAnswer }, "Show correction"));
      attempt.addEventListener("keydown", e => {
        if (e.key === "Enter" && !e.shiftKey && !e.isComposing && !attempt.readOnly) { e.preventDefault(); showAnswer(); }
      });
      stage.append(
        el("div", { class: "prompt-label" }, "You wrote this earlier. How should it be?"),
        el("div", { class: "fix", style: "font-size:1.4rem;margin:.5rem 0 .75rem" }, el("span", { class: "old" }, card.wrong)),
        attempt, reveal);
      later(() => attempt.focus(), 0);
    }

    body.replaceChildren(sessionBar(remaining), stage);
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

/* ================= lessons ================= */

async function renderLessons() {
  const body = $("#lessons-body");
  if (routeArg) return renderLesson(body, routeArg);

  const { lessons } = await api.get("/api/lessons");
  const next = lessons.find(l => l.status !== "done");
  const done = lessons.filter(l => l.status === "done").length;
  body.replaceChildren(
    el("div", { class: "panel-head" },
      el("h2", {}, "JLPT N5 lessons"),
      el("span", { class: "muted" }, `${done} / ${lessons.length} complete`)),
    el("p", { class: "muted", style: "margin-top:-.5rem" },
      "Read a lesson, practice it with Sensei, then mark it complete to add its words to your reviews."),
    el("div", { class: "lesson-grid" }, lessons.map((l, i) =>
      el("a", { class: `lesson-card${l === next ? " next" : ""}`, href: `#lessons/${l.id}` },
        el("div", { class: "num" }, `Lesson ${i + 1}`,
          l.status !== "new" && el("span", { class: `status-pill ${l.status}` }, l.status === "done" ? "Done ✓" : "In progress")),
        el("div", { class: "jp", lang: "ja" }, l.jp_title),
        el("div", { class: "title" }, l.title),
        el("div", { class: "goal" }, l.goal)))));
}

// Shows which sounds of the target sentence Whisper heard (green) or missed (red).
function shadowFeedback(cmp, heardText) {
  const verdict = cmp.perfect ? "Excellent! 🎉"
    : cmp.score >= 70 ? "Close! Compare what Whisper heard with the red parts."
    : "Keep practising. Listen again and repeat slowly.";
  return el("div", {},
    el("div", { class: "shadow-score" }, el("strong", {}, `${cmp.score}%`), ` ${verdict}`),
    el("div", { class: "shadow-runs", lang: "ja" }, cmp.runs.map(r => el("span", { class: r.ok ? "ok" : "miss" }, r.t))),
    el("div", { class: "muted", style: "font-size:.82rem" }, "Whisper heard: ", el("span", { lang: "ja" }, heardText)));
}

async function renderLesson(body, id) {
  const lesson = await api.get(`/api/lessons/${id}`);
  prefetchSpeech(lesson.examples.map(e => e.jp));
  const showRomaji = prefs.get("lesson.romaji", true);
  const romajiToggle = el("label", { class: "toggle" },
    el("input", { type: "checkbox", checked: showRomaji, onchange: e => {
      prefs.set("lesson.romaji", e.target.checked);
      examples.classList.toggle("hide-romaji", !e.target.checked);
    } }), "Romaji");

  const examples = el("div", { class: showRomaji ? "" : "hide-romaji" }, lesson.examples.map(ex => {
    const result = el("div", { class: "shadow-result" });
    return el("div", { class: "example" },
      richEl("div", { class: "jp-line", lang: "ja" }, ex.segments),
      el("div", { class: "romaji" }, ex.romaji),
      el("div", { class: "en" }, ex.en),
      el("div", { class: "example-actions" },
        speakButton(ex.jp),
        micButton({
          title: "Say this sentence (click again to stop)",
          onText: async ({ text }) => {
            if (!text) { result.replaceChildren(el("span", { class: "muted" }, "Didn't catch anything. Try again.")); return; }
            const cmp = await api.post("/api/speech/compare", { target: ex.jp, heard: text });
            result.replaceChildren(shadowFeedback(cmp, text));
          },
          onError: message => result.replaceChildren(el("span", { class: "feedback bad" }, message)),
        })),
      result);
  }));

  const unsaved = lesson.vocab.filter(v => !v.saved).length;
  const complete = el("button", { class: "btn", type: "button", disabled: lesson.status === "done" && !unsaved },
    lesson.status === "done" ? (unsaved ? `Add ${unsaved} words to reviews` : "Completed ✓")
      : `✓ Mark complete${unsaved ? ` · add ${unsaved} words to reviews` : ""}`);
  complete.addEventListener("click", async () => {
    complete.disabled = true;
    const res = await api.post(`/api/lessons/${id}/complete`, {});
    complete.textContent = res.words_added ? `Completed ✓ · ${res.words_added} words added` : "Completed ✓";
    refreshBadge();
  });

  const practice = el("button", { class: "btn btn-primary", type: "button" }, "💬 Practice with Sensei");
  practice.addEventListener("click", async () => {
    practice.disabled = true;
    const { chat_id } = await api.post(`/api/lessons/${id}/practice`, {});
    tutor.chatId = chat_id;
    prefs.set("chat.current", chat_id);
    tutor.autoStart = "I've read the lesson. Let's practice!";
    location.hash = "#tutor";
  });

  body.replaceChildren(
    el("div", { class: "lesson-head" },
      el("a", { class: "back", href: "#lessons" }, "← All lessons"),
      el("h2", {}, `${lesson.number}. ${lesson.title}`),
      el("div", { class: "jp", lang: "ja" }, lesson.jp_title),
      el("p", { class: "goal" }, `Goal: ${lesson.goal}`)),
    el("div", { class: "lesson-section" },
      el("h3", {}, "Key points"),
      el("ul", { class: "lesson-points" }, lesson.points.map(segs => richEl("li", {}, segs)))),
    el("div", { class: "lesson-section" },
      el("h3", {}, "Examples", romajiToggle),
      examples),
    el("div", { class: "lesson-section" },
      el("h3", {}, "Vocabulary"),
      el("table", { class: "vocab-table" }, el("tbody", {}, lesson.vocab.map(v =>
        el("tr", {},
          el("td", {}, richEl("div", { class: "vw", lang: "ja" }, v.segments)),
          el("td", { class: "vr", lang: "ja" }, v.reading !== v.word ? v.reading : ""),
          el("td", { class: "vm" }, v.meaning),
          el("td", {}, speakButton(v.reading))))))),
    el("div", { class: "lesson-actions" },
      practice,
      complete,
      lesson.next_id && el("a", { class: "btn btn-ghost", href: `#lessons/${lesson.next_id}` }, "Next lesson →")),
    el("p", { class: "hint" }, "Tip: click any Japanese word to look it up."),
  );
  window.scrollTo(0, 0);
}

/* ================= quiz ================= */

const QUIZ_TYPES = {
  reading: ["漢字読み", "Kanji reading"],
  writing: ["表記", "Spelling"],
  meaning: ["語彙", "Vocabulary"],
  particle: ["文法", "Particles"],
  listening: ["聴解", "Listening"],
};

async function renderQuiz() {
  const body = $("#quiz-body");
  const opts = await api.get("/api/quiz/options");
  const saved = prefs.get("quiz", null);
  const studied = opts.lessons.filter(l => l.status !== "new").map(l => l.id);
  const settings = saved || {
    lessons: studied.length ? studied : opts.lessons.slice(0, 2).map(l => l.id),
    include_saved: true, count: 10, types: Object.keys(QUIZ_TYPES),
  };

  const chip = (value, label, checked) =>
    el("label", { class: "chip" }, el("input", { type: "checkbox", value, checked }), label);
  const lessonChips = opts.lessons.map((l, i) =>
    chip(l.id, `${i + 1}. ${l.title}${l.status === "done" ? " ✓" : ""}`, settings.lessons.includes(l.id)));
  const typeChips = Object.entries(QUIZ_TYPES).map(([t, [jp, en]]) =>
    chip(t, el("span", {}, el("span", { lang: "ja" }, jp), ` ${en}`), settings.types.includes(t)));
  const savedBox = el("input", { type: "checkbox", checked: settings.include_saved && opts.saved_words > 0,
    disabled: !opts.saved_words });
  const count = el("div", { class: "segmented" }, [10, 20].map(n =>
    el("button", { type: "button", "data-n": n, class: n === settings.count ? "active" : "",
      onclick: e => { settings.count = n; count.querySelectorAll("button").forEach(b => b.classList.toggle("active", b === e.currentTarget)); } },
      `${n} questions`)));
  const checked = chips => chips.map(c => c.querySelector("input")).filter(i => i.checked).map(i => i.value);
  const error = el("p", { class: "feedback bad" });

  body.replaceChildren(
    el("div", { class: "panel-head" },
      el("h2", {}, "JLPT N5 practice quiz"),
      el("span", { class: "muted" }, "Questions come from verified lesson content, never from the AI")),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Lessons",
        el("span", {},
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => lessonChips.forEach(c => { c.querySelector("input").checked = true; }) }, "All"),
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => lessonChips.forEach(c => { c.querySelector("input").checked = false; }) }, "None"))),
      el("div", { class: "chips" }, lessonChips)),
    el("div", { class: "field" },
      el("label", { class: "toggle" }, savedBox, `Include my saved words (${opts.saved_words})`)),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Question types"),
      el("div", { class: "chips" }, typeChips)),
    el("div", { class: "field" }, count),
    error,
    el("div", { class: "btn-row" },
      el("button", { class: "btn btn-primary", type: "button", onclick: start }, "Start quiz")),
    opts.recent.length ? el("div", { class: "lesson-section" },
      el("h3", {}, "Recent results"),
      el("div", { class: "list" }, opts.recent.map(r =>
        el("div", { class: "list-sub" },
          `${new Date(r.created_at * 1000).toLocaleString()} · ${r.correct} / ${r.total} (${Math.round(r.correct / r.total * 100)}%)`)))) : "",
  );

  async function start() {
    settings.lessons = checked(lessonChips);
    settings.types = checked(typeChips);
    settings.include_saved = savedBox.checked;
    if (!settings.types.length) { error.textContent = "Pick at least one question type."; return; }
    if (!settings.lessons.length && !settings.include_saved) { error.textContent = "Pick at least one lesson."; return; }
    prefs.set("quiz", settings);
    try {
      const { questions } = await api.post("/api/quiz/new", settings);
      runQuiz(body, questions);
    } catch (err) {
      error.textContent = err.message;
    }
  }
}

function runQuiz(body, questions) {
  const results = [];
  let index = 0;
  prefetchSpeech(questions.filter(q => q.type === "listening").map(q => q.prompt.audio));

  function show() {
    cleanups.forEach(fn => fn());
    cleanups = [];
    if (index >= questions.length) return finish();
    const q = questions[index];
    const [jp, en] = QUIZ_TYPES[q.type];
    const jpChoices = q.type === "reading" || q.type === "writing" || q.type === "particle";
    let answered = false;

    const prompt = [];
    if (q.type === "reading") prompt.push(el("div", { class: "quiz-word", lang: "ja" }, q.prompt.word));
    if (q.type === "writing") prompt.push(el("div", { class: "quiz-word", lang: "ja" }, q.prompt.reading));
    if (q.type === "meaning") prompt.push(richEl("div", { class: "quiz-word", lang: "ja" }, q.prompt.segments));
    if (q.type === "particle") {
      prompt.push(richEl("div", { class: "quiz-sentence", lang: "ja" }, q.prompt.segments));
      prompt.push(el("div", { class: "quiz-hint" }, `“${q.prompt.hint}”`));
    }
    const reveal = el("div");
    if (q.type === "listening") {
      if (hasVoice()) {
        prompt.push(el("button", { class: "play-big", type: "button", "aria-label": "Play the sentence",
          onclick: () => speak(q.prompt.audio) }, "🔊"));
        prompt.push(el("div", { class: "quiz-hint" }, "Press the button or Space to listen again"));
        later(() => speak(q.prompt.audio), 300);
      } else {
        prompt.push(el("p", { class: "feedback bad" }, "No Japanese voice found in this browser, so here's the text instead:"));
        prompt.push(richEl("div", { class: "quiz-sentence", lang: "ja" }, q.item.segments));
      }
    }

    const feedback = el("div");
    const next = el("button", { class: "btn btn-primary", type: "button", hidden: true, onclick: () => { index++; show(); } },
      index + 1 < questions.length ? "Next →" : "See results");
    const buttons = q.choices.map((c, n) =>
      el("button", { class: `quiz-choice${jpChoices ? " jp" : ""}`, type: "button", lang: jpChoices ? "ja" : null,
        onclick: () => choose(n) }, el("span", { class: "key" }, n + 1), c));

    function choose(n) {
      if (answered) return;
      answered = true;
      const ok = n === q.answer;
      results.push({ q, ok, picked: q.choices[n] });
      buttons.forEach((b, i) => {
        b.disabled = true;
        if (i === q.answer) b.classList.add("ok");
        else if (i === n) b.classList.add("bad");
      });
      feedback.replaceChildren(
        el("p", { class: `feedback ${ok ? "ok" : "bad"}` }, ok ? "✓ Correct" : `✗ The answer is ${q.choices[q.answer]}`),
        el("div", { class: "quiz-explain" }, q.explain));
      if (q.type === "listening" && hasVoice()) reveal.replaceChildren(richEl("div", { class: "quiz-sentence", lang: "ja" }, q.item.segments));
      if (q.type !== "listening") speak(q.item.example || q.item.reading || q.item.word || "");
      next.hidden = false;
      next.focus();
    }

    addKeyHandler(e => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
      const n = Number(e.key) - 1;
      if (!answered && n >= 0 && n < buttons.length) choose(n);
      else if (e.key === " " && q.type === "listening") { e.preventDefault(); speak(q.prompt.audio); }
    });

    body.replaceChildren(
      el("div", { class: "session-bar" },
        el("span", {}, `Question ${index + 1} / ${questions.length}`),
        el("div", { class: "progress" }, el("div", { class: "progress-fill", style: `width:${index / questions.length * 100}%` })),
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => { if (confirm("Stop this quiz? Your answers so far won't be saved.")) route(); } }, "Quit")),
      el("div", { class: "quiz-card" },
        el("div", { class: "quiz-type" }, el("span", { class: "jp", lang: "ja" }, jp), en),
        el("div", { class: "quiz-instruction" }, q.prompt.instruction),
        ...prompt,
        reveal,
        el("div", { class: "quiz-choices" }, buttons),
        feedback,
        next));
  }

  async function finish() {
    const summary = await api.post("/api/quiz/results", { results: results.map(r => ({ type: r.q.type, correct: r.ok })) });
    const pct = Math.round(summary.correct / summary.total * 100);
    const missedWords = results.filter(r => !r.ok && r.q.item.word).map(r => r.q.item);
    const uniqueMissed = [...new Map(missedWords.map(w => [w.word, w])).values()];
    const addBtn = uniqueMissed.length ? el("button", { class: "btn btn-primary", type: "button" },
      `Add ${uniqueMissed.length} missed word${uniqueMissed.length > 1 ? "s" : ""} to reviews`) : null;
    addBtn?.addEventListener("click", async () => {
      addBtn.disabled = true;
      const res = await api.post("/api/quiz/add-missed", { words: uniqueMissed.map(w => ({ word: w.word, reading: w.reading, meaning: w.meaning })) });
      addBtn.textContent = res.added ? `Added ${res.added} ✓` : "Already in your reviews ✓";
      refreshBadge();
    });

    body.replaceChildren(el("div", { class: "empty" },
      el("div", { class: "big" }, pct >= 80 ? "🎉" : pct >= 50 ? "👍" : "💪"),
      el("div", { class: "score-big" }, `${summary.correct} / ${summary.total}`),
      el("p", {}, pct >= 80 ? "Excellent! You're on track for N5." : pct >= 50 ? "Good work. Review the misses below." : "Keep going. Every quiz makes the next one easier."),
      el("div", { class: "type-bars" }, Object.entries(summary.by_type).map(([t, [c, n]]) =>
        el("div", { class: "type-bar" },
          el("span", {}, el("span", { lang: "ja" }, QUIZ_TYPES[t][0]), ` ${QUIZ_TYPES[t][1]}`),
          el("div", { class: "progress" }, el("div", { class: "progress-fill", style: `width:${c / n * 100}%` })),
          el("span", {}, `${c}/${n}`)))),
      results.some(r => !r.ok) && el("div", { class: "lesson-section" },
        el("h3", {}, "Your misses"),
        el("ul", { class: "missed" }, results.filter(r => !r.ok).map(r =>
          el("li", {}, el("strong", {}, `${QUIZ_TYPES[r.q.type][1]}: `), r.q.explain, el("span", { class: "muted" }, ` (you picked ${r.picked})`))))),
      el("div", { class: "btn-row" },
        addBtn,
        el("button", { class: "btn", type: "button", onclick: () => route() }, "New quiz"))));
  }

  show();
}

/* ================= notebook ================= */

async function renderNotebook() {
  const tabs = $("#notebook-tabs");
  const tab = prefs.get("notebook.tab", "words");
  tabs.querySelectorAll("button").forEach(b => {
    b.classList.toggle("active", b.dataset.tab === tab);
    b.onclick = () => { prefs.set("notebook.tab", b.dataset.tab); renderNotebook(); };
  });
  const body = $("#notebook-body");
  const statusDot = status => el("i", { class: `dot ${status}`, title: status });

  if (tab === "words") {
    const { words } = await api.get("/api/vocab");
    $("#notebook-hint").textContent = `${words.length} saved · click words in the Tutor chat to add more`;
    if (!words.length) {
      body.replaceChildren(el("div", { class: "empty" },
        el("div", { class: "big" }, "📖"),
        el("p", {}, "No saved words yet. In the Tutor chat, click any Japanese word to look it up and save it."),
        el("div", { class: "btn-row" }, el("a", { class: "btn btn-primary", href: "#tutor" }, "Open the tutor"))));
      return;
    }
    body.replaceChildren(el("div", { class: "list" }, words.map(w =>
      el("div", { class: "list-row" },
        statusDot(w.status),
        el("div", { class: "list-main" },
          el("div", { class: "list-title", lang: "ja" }, w.word, w.reading !== w.word && el("small", {}, w.reading)),
          el("div", { class: "list-sub" }, w.meaning)),
        el("div", {},
          speakButton(w.reading),
          el("button", { class: "icon-btn", type: "button", title: "Remove word", "aria-label": "Remove word",
            onclick: async () => {
              if (!confirm(`Remove ${w.word} from your words? Its review history is deleted too.`)) return;
              await api.delete(`/api/vocab/${w.id}`);
              renderNotebook();
            } }, "🗑"))))));
  } else {
    const { mistakes } = await api.get("/api/mistakes");
    $("#notebook-hint").textContent = `${mistakes.length} logged · Sensei saves them when correcting you`;
    if (!mistakes.length) {
      body.replaceChildren(el("div", { class: "empty" },
        el("div", { class: "big" }, "✍️"),
        el("p", {}, "No mistakes logged yet. Try writing Japanese to Sensei; corrections land here and in your reviews.")));
      return;
    }
    body.replaceChildren(el("div", { class: "list" }, mistakes.map(m =>
      el("div", { class: "list-row" },
        statusDot(m.status),
        el("div", { class: "list-main" },
          el("div", { class: "fix" }, el("span", { class: "old" }, m.wrong), " → ", el("span", { class: "new" }, m.correct)),
          m.note && el("div", { class: "list-sub" }, m.note)),
        el("button", { class: "icon-btn", type: "button", title: "Remove", "aria-label": "Remove mistake",
          onclick: async () => {
            if (!confirm("Remove this mistake? Its review history is deleted too.")) return;
            await api.delete(`/api/mistakes/${m.id}`);
            renderNotebook();
          } }, "🗑")))));
  }
}

/* ================= tutor chat ================= */

const STARTERS = [
  ["Basic greetings", "おはようございます and friends",
    "Teach me the basic everyday greetings, one at a time."],
  ["What's on the JLPT N5?", "Sections and how to prepare",
    "Explain what the JLPT N5 tests and how I should study for it as a near-beginner."],
  ["です and ます", "The polite form, simply explained",
    "Explain です and ます simply, with a couple of everyday examples."],
  ["Quiz me", "Using the kana I've learned",
    "Give me a short quiz using only the kana I've learned so far."],
];

const tutor = { chatId: prefs.get("chat.current", null), busy: false, bound: false, autoStart: null };

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

// Segments come from the server: plain text {t} or words {t, b, k, p, parts}
// (see app/furigana.py). Words become clickable spans; data-i points back into
// the segment list. Everything is escaped first; the light Markdown pass only
// ever adds tags.
function renderRich(segments) {
  const ruby = parts => parts.map(p => p.r
    ? `<ruby>${escapeHtml(p.t)}<rt>${escapeHtml(p.r)}</rt></ruby>`
    : escapeHtml(p.t)).join("");
  const html = segments.map((s, i) => s.b
    ? `<span class="w" data-i="${i}">${s.parts ? ruby(s.parts) : escapeHtml(s.t)}</span>`
    : escapeHtml(s.t)).join("");
  return markdown(html);
}

function markdown(html) {
  const inline = s => s
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
  return html.trim().split(/\n{2,}/).map(block => {
    const lines = block.split("\n");
    if (lines.every(l => /^\s*[-*•]\s+/.test(l))) {
      return `<ul>${lines.map(l => `<li>${inline(l.replace(/^\s*[-*•]\s+/, ""))}</li>`).join("")}</ul>`;
    }
    // A paragraph that ends in a list: split it so the bullets still render.
    const firstBullet = lines.findIndex(l => /^\s*[-*•]\s+/.test(l));
    if (firstBullet > 0 && lines.slice(firstBullet).every(l => /^\s*[-*•]\s+/.test(l))) {
      return `<p>${inline(lines.slice(0, firstBullet).join("<br>"))}</p>` +
        `<ul>${lines.slice(firstBullet).map(l => `<li>${inline(l.replace(/^\s*[-*•]\s+/, ""))}</li>`).join("")}</ul>`;
    }
    return `<p>${inline(lines.join("<br>"))}</p>`;
  }).join("");
}

function japaneseOnly(text) {
  const runs = text.match(/[぀-ヿ㐀-鿿々ー、。！？「」]+/g) || [];
  return runs.filter(r => /[぀-ヿ㐀-鿿]/.test(r)).join("、");
}

// An element showing Japanese with furigana whose words can be clicked.
function richEl(tag, attrs, segments) {
  const node = el(tag, { ...attrs, class: `rich ${attrs.class || ""}`.trim() });
  node.segments = segments;
  node.innerHTML = renderRich(segments);
  return node;
}

function messageEl(msg) {
  const bubble = richEl("div", { class: "bubble" }, msg.segments || [{ t: msg.content }]);
  const isAssistant = msg.role === "assistant";
  const jp = isAssistant ? japaneseOnly(msg.content) : "";
  return el("div", { class: `msg msg-${msg.role}`, "data-id": msg.id ?? "" },
    isAssistant && el("div", { class: "avatar", lang: "ja", title: msg.model || "" }, "先"),
    el("div", {},
      bubble,
      (msg.warnings || []).map(warningEl),
      jp && el("div", { class: "msg-actions" },
        el("button", { type: "button", onclick: () => speak(jp), title: "Read the Japanese aloud" }, "🔊 Listen")),
    ),
  );
}

// The app checked the tutor's kana against its romaji and they disagree.
function warningEl(w) {
  return el("div", { class: "check-warning" },
    el("strong", {}, "⚠ Kana and romaji don't match. "),
    el("span", { lang: "ja" }, w.kana), " reads as “", w.expected, "”, but Sensei wrote “", w.written, "”. ",
    el("button", {
      type: "button",
      onclick: () => sendMessage(
        `In your last message you wrote ${w.kana} (${w.written}), but the kana reads "${w.expected}". ` +
        "Which one is correct? Please give me the corrected version."),
    }, "Ask Sensei to fix it"),
  );
}

/* word lookup popup */

let wordPopup = null;

function closeWordPopup() {
  wordPopup?.remove();
  wordPopup = null;
  document.querySelector(".w.selected")?.classList.remove("selected");
}

document.addEventListener("click", e => {
  const span = e.target.closest(".rich .w");
  if (span) {
    const bubble = span.closest(".rich");
    const i = Number(span.dataset.i);
    // The next couple of words let the server find compounds (日本 + 人 = 日本人).
    const next = bubble.segments.slice(i + 1, i + 3).filter(s => s.b).map(s => s.t).join("");
    openWordPopup(span, bubble.segments[i], next);
  } else if (wordPopup && !e.target.closest(".word-popup")) {
    closeWordPopup();
  }
});
document.addEventListener("keydown", e => { if (e.key === "Escape") closeWordPopup(); });

async function openWordPopup(span, seg, next) {
  closeWordPopup();
  span.classList.add("selected");
  const body = el("div", { class: "word-popup-body" }, el("p", { class: "muted" }, "Looking up…"));
  wordPopup = el("div", { class: "word-popup", role: "dialog", "aria-label": `Dictionary: ${seg.b}` },
    el("button", { class: "word-popup-close", type: "button", "aria-label": "Close", onclick: closeWordPopup }, "×"),
    body);
  document.body.append(wordPopup);
  placePopup(span);

  const conjugated = seg.t !== seg.b ? el("p", { class: "muted word-form" },
    el("span", { lang: "ja" }, seg.t), ` is a form of `, el("span", { lang: "ja" }, seg.b)) : "";

  let data;
  try {
    const params = new URLSearchParams({ q: seg.b, k: seg.k || "", next, p: seg.p || "" });
    data = await api.get(`/api/dict/lookup?${params}`);
  } catch (err) {
    body.replaceChildren(el("p", { class: "feedback bad" }, err.message));
    return;
  }
  if (!wordPopup) return; // closed while loading

  if (!data.available || !data.entries.length) {
    body.replaceChildren(
      el("div", { class: "word-head" },
        el("span", { class: "word-main", lang: "ja" }, seg.b),
        seg.k && seg.k !== seg.b && el("span", { class: "word-reading", lang: "ja" }, seg.k),
        speakButton(seg.b)),
      el("p", { class: "muted" }, seg.p),
      conjugated,
      el("p", { class: "muted" }, data.available
        ? "No dictionary entry found for this word."
        : "The dictionary isn't installed yet."));
    placePopup(span);
    return;
  }

  body.replaceChildren(
    conjugated,
    ...data.entries.map(entry => {
      // Show the spelling that was clicked: ます stays ます, not its rare kanji form 〼.
      const clicked = [...entry.kanji, ...entry.readings].includes(data.matched) ? data.matched : null;
      const main = clicked || entry.kanji[0] || entry.readings[0];
      const reading = entry.readings.includes(main) ? null : entry.readings[0];
      const save = el("button", { class: "btn btn-primary", type: "button", disabled: entry.saved }, entry.saved ? "Saved ✓" : "+ Save word");
      save.addEventListener("click", async () => {
        save.disabled = true;
        try {
          await api.post("/api/vocab", { entry_id: entry.id, word: main });
          save.textContent = "Saved ✓";
          refreshBadge();
        } catch (err) {
          save.disabled = false;
          save.textContent = "Couldn't save";
        }
      });
      return el("div", { class: "word-entry" },
        el("div", { class: "word-head" },
          el("span", { class: "word-main", lang: "ja" }, main),
          reading && el("span", { class: "word-reading", lang: "ja" }, reading),
          entry.common && el("span", { class: "tag" }, "common"),
          speakButton(reading || main)),
        el("ol", { class: "senses" }, entry.senses.slice(0, 4).map(s =>
          el("li", {},
            s.pos.length ? el("span", { class: "pos" }, s.pos[0].replace(/\s*\(.*\)$/, "")) : null,
            s.gloss.slice(0, 4).join("; ")))),
        save);
    }),
    el("p", { class: "credit" }, "Dictionary: JMdict (EDRDG, CC BY-SA 4.0)"));
  placePopup(span);
}

function placePopup(anchor) {
  if (!wordPopup) return;
  if (window.innerWidth <= 640) {  // bottom sheet on phones
    wordPopup.classList.add("sheet");
    return;
  }
  const r = anchor.getBoundingClientRect();
  const w = wordPopup.offsetWidth;
  const h = wordPopup.offsetHeight;
  const left = Math.max(8, Math.min(window.innerWidth - w - 8, r.left + r.width / 2 - w / 2));
  const below = r.bottom + 8 + h < window.innerHeight;
  wordPopup.style.left = `${left}px`;
  wordPopup.style.top = `${below ? r.bottom + 8 : Math.max(8, r.top - h - 8)}px`;
}

function scrollMessages(force = false) {
  const box = $("#messages");
  if (force || box.scrollHeight - box.scrollTop - box.clientHeight < 120) box.scrollTop = box.scrollHeight;
}

async function renderTutor() {
  bindTutorOnce();
  const furigana = $("#opt-furigana");
  furigana.checked = prefs.get("furigana", true);
  $("#messages").classList.toggle("no-furigana", !furigana.checked);

  await Promise.all([loadChatList(), refreshLlmLabel()]);
  if (tutor.chatId) await openChat(tutor.chatId);
  else showChatEmpty();
  if (tutor.autoStart) {  // a lesson practice chat that was just created
    const text = tutor.autoStart;
    tutor.autoStart = null;
    sendMessage(text);
  }
  $("#composer-input").focus();
}

function bindTutorOnce() {
  if (tutor.bound) return;
  tutor.bound = true;

  const input = $("#composer-input");
  const autosize = () => { input.style.height = "auto"; input.style.height = `${input.scrollHeight}px`; };
  const voiceNote = $("#composer-voice");
  $("#composer").insertBefore(micButton({
    title: "Speak Japanese (click again to stop). You can edit the text before sending.",
    onText: ({ text }) => {
      voiceNote.textContent = text ? "" : "Didn't catch anything. Try again, a little closer to the mic.";
      if (!text) return;
      input.value = input.value ? `${input.value} ${text}` : text;
      autosize();
      input.focus();
    },
    onError: message => { voiceNote.textContent = message; },
  }), $("#composer-send"));
  input.addEventListener("input", autosize);
  input.addEventListener("keydown", e => {
    // isComposing: Enter is confirming a Japanese IME conversion, not sending.
    if (e.key === "Enter" && !e.shiftKey && !e.isComposing) {
      e.preventDefault();
      $("#composer").requestSubmit();
    }
  });
  $("#composer").addEventListener("submit", e => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text || tutor.busy) return;
    input.value = "";
    autosize();
    sendMessage(text);
  });

  $("#opt-furigana").addEventListener("change", e => {
    prefs.set("furigana", e.target.checked);
    $("#messages").classList.toggle("no-furigana", !e.target.checked);
  });
  $("#chat-new").addEventListener("click", () => {
    tutor.chatId = null;
    prefs.set("chat.current", null);
    showChatEmpty();
    loadChatList();
    $("#chat-list").classList.remove("open");
    input.focus();
  });
  $("#chat-list-toggle").addEventListener("click", () => $("#chat-list").classList.toggle("open"));
  $("#messages").addEventListener("scroll", () => { if (!wordPopup?.classList.contains("sheet")) closeWordPopup(); });
  $("#llm-settings-btn").addEventListener("click", toggleLlmSettings);
}

async function loadChatList() {
  const { chats } = await api.get("/api/chats");
  $("#chat-items").replaceChildren(...chats.map(c =>
    el("div", {
      class: `chat-item${c.id === tutor.chatId ? " active" : ""}`,
      onclick: () => { openChat(c.id); $("#chat-list").classList.remove("open"); },
    },
      el("span", { title: c.title }, c.title),
      el("button", {
        type: "button", title: "Delete chat", "aria-label": "Delete chat",
        onclick: async e => {
          e.stopPropagation();
          if (!confirm(`Delete “${c.title}”? This can't be undone.`)) return;
          await api.delete(`/api/chats/${c.id}`);
          if (c.id === tutor.chatId) { tutor.chatId = null; prefs.set("chat.current", null); showChatEmpty(); }
          loadChatList();
        },
      }, "×"),
    )));
}

async function openChat(id) {
  let chat;
  try { chat = await api.get(`/api/chats/${id}`); }
  catch { tutor.chatId = null; prefs.set("chat.current", null); return showChatEmpty(); }
  tutor.chatId = id;
  prefs.set("chat.current", id);
  $("#chat-title").textContent = chat.title;
  const lessonLink = $("#chat-lesson-link");
  lessonLink.hidden = !chat.lesson_id;
  if (chat.lesson_id) lessonLink.href = `#lessons/${chat.lesson_id}`;
  for (const item of document.querySelectorAll(".chat-item")) item.classList.remove("active");
  loadChatList();
  if (!chat.messages.length) {
    if (chat.lesson_id) return $("#messages").replaceChildren(); // practice is about to start
    return showChatEmpty();
  }
  $("#messages").replaceChildren(...chat.messages.map(messageEl));
  const last = chat.messages[chat.messages.length - 1];
  if (last.role === "user") $("#messages").append(errorEl("This message has no reply yet."));
  scrollMessages(true);
}

function showChatEmpty() {
  $("#chat-title").textContent = "Sensei";
  $("#chat-lesson-link").hidden = true;
  $("#messages").replaceChildren(el("div", { class: "chat-empty" },
    el("div", { class: "avatar", lang: "ja" }, "先"),
    el("h2", {}, "こんにちは! I'm your Japanese tutor."),
    el("p", {}, "Ask me anything about Japanese, or try writing a sentence and I'll correct it. " +
      "I know which kana you've learned, so I'll keep things at your level."),
    el("div", { class: "starters" }, STARTERS.map(([title, sub, prompt]) =>
      el("button", { class: "starter", type: "button", onclick: () => sendMessage(prompt) },
        title, el("small", { lang: "ja" }, sub)))),
  ));
}

function errorEl(message) {
  return el("div", { class: "msg msg-assistant msg-error" },
    el("div", { class: "avatar", lang: "ja" }, "先"),
    el("div", {},
      el("div", { class: "bubble" }, message),
      el("div", { class: "msg-actions" },
        el("button", { type: "button", onclick: e => { e.target.closest(".msg").remove(); sendMessage(null); } },
          "↻ Try again"))));
}

async function sendMessage(text) {
  if (tutor.busy) return;
  tutor.busy = true;
  $("#composer-send").disabled = true;
  const box = $("#messages");

  try {
    if (!tutor.chatId) {
      const chat = await api.post("/api/chats", {});
      tutor.chatId = chat.id;
      prefs.set("chat.current", chat.id);
      box.replaceChildren();
    }

    let userEl = null;
    if (text) {
      userEl = messageEl({ role: "user", content: text });
      box.append(userEl);
    }
    const bubble = el("div", { class: "bubble" }, el("span", { class: "typing" }, el("i"), el("i"), el("i")));
    const pending = el("div", { class: "msg msg-assistant" },
      el("div", { class: "avatar", lang: "ja" }, "先"), el("div", {}, bubble));
    box.append(pending);
    scrollMessages(true);

    const res = await fetch(`/api/chats/${tutor.chatId}/messages`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: text }),
    });
    if (!res.ok) throw new Error((await res.json().catch(() => ({}))).detail || res.statusText);

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let reply = "";

    const handle = event => {
      if (event.type === "user" && userEl) {
        const fresh = messageEl(event.message);
        userEl.replaceWith(fresh);
        userEl = fresh;
      } else if (event.type === "notice") {
        pending.before(el("div", { class: "notice" }, event.message));
      } else if (event.type === "delta") {
        reply += event.text;
        bubble.innerHTML = renderRich([{ t: reply }]);
        scrollMessages();
      } else if (event.type === "done") {
        const done = messageEl(event.message);
        if (event.mistakes_saved) {
          done.lastChild.append(el("a", { class: "mistake-chip", href: "#notebook" },
            `📝 ${event.mistakes_saved} mistake${event.mistakes_saved > 1 ? "s" : ""} saved to your reviews`));
          refreshBadge();
        }
        pending.replaceWith(done);
        scrollMessages();
      } else if (event.type === "error") {
        pending.replaceWith(errorEl(event.message));
        scrollMessages();
      }
    };

    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      let cut;
      while ((cut = buffer.indexOf("\n\n")) !== -1) {
        const chunk = buffer.slice(0, cut);
        buffer = buffer.slice(cut + 2);
        if (chunk.startsWith("data: ")) handle(JSON.parse(chunk.slice(6)));
      }
    }
  } catch (err) {
    box.querySelector(".msg-assistant:last-child .typing")?.closest(".msg")?.remove();
    box.append(errorEl(`Couldn't reach the tutor: ${err.message}`));
  } finally {
    tutor.busy = false;
    $("#composer-send").disabled = false;
    loadChatList().then(() => {
      const active = $(".chat-item.active span");
      if (active) $("#chat-title").textContent = active.textContent;
    });
  }
}

/* AI provider settings */

async function refreshLlmLabel() {
  const status = await api.get("/api/llm/status");
  const provider = status.providers.find(p => p.id === status.current.provider);
  $("#llm-label").textContent = provider
    ? `${provider.label}${status.current.model ? ` · ${status.current.model}` : ""}`
    : "";
  return status;
}

async function toggleLlmSettings() {
  const panel = $("#llm-settings");
  if (!panel.hidden) { panel.hidden = true; return; }
  panel.hidden = false;

  const status = await refreshLlmLabel();
  const providerSel = el("select", {}, status.providers.map(p =>
    el("option", { value: p.id, selected: p.id === status.current.provider },
      p.configured ? p.label : `${p.label} — no API key`)));
  const modelSel = el("select", {});
  const info = el("div", { class: "status muted" });
  const save = el("button", { class: "btn btn-primary", type: "button" }, "Save");

  async function loadModels() {
    modelSel.replaceChildren(el("option", {}, "Loading…"));
    save.disabled = true;
    info.textContent = "";
    try {
      const { models } = await api.get(`/api/llm/models?provider=${providerSel.value}`);
      if (!models.length) throw new Error("No models found.");
      const current = providerSel.value === status.current.provider ? status.current.model : null;
      modelSel.replaceChildren(...models.map(m => el("option", { value: m, selected: m === current }, m)));
      save.disabled = false;
      info.textContent = providerSel.value === "ollama"
        ? "Small models (3–4B) fit your GPU best. Their Japanese is weaker than Gemini's."
        : "Flash models are fast and have the most generous free limits.";
    } catch (err) {
      modelSel.replaceChildren();
      info.textContent = err.message;
      info.className = "status feedback bad";
    }
  }

  providerSel.addEventListener("change", loadModels);
  save.addEventListener("click", async () => {
    await api.put("/api/llm/settings", { provider: providerSel.value, model: modelSel.value });
    await refreshLlmLabel();
    panel.hidden = true;
  });

  panel.replaceChildren(
    el("label", {}, "Provider", providerSel),
    el("label", {}, "Model", modelSel),
    save,
    info,
    voiceSettingsRow(),
  );
  loadModels();
}

function voiceSettingsRow() {
  const row = el("div", { class: "voice-settings" }, el("span", { class: "muted" }, "Checking the voice engine…"));
  (async () => {
    const status = await refreshTts();
    if (!status.running) {
      row.replaceChildren(el("span", { class: "muted" }, status.installed
        ? "VOICEVOX is starting up… natural voices will be ready in a moment. Using the browser voice for now."
        : "Using the browser's voice. Install VOICEVOX for natural Japanese voices."));
      return;
    }
    let voices = [];
    try { ({ speakers: voices } = await api.get("/api/tts/speakers")); } catch { /* shown below */ }
    const voiceSel = el("select", {}, voices.map(v =>
      el("option", { value: v.id, selected: v.id === status.speaker }, `${v.name} (${v.style})`)));
    const speedSel = el("select", {}, [[0.8, "Slow"], [0.9, "A bit slow"], [1.0, "Normal"]].map(([v, label]) =>
      el("option", { value: v, selected: Math.abs(v - status.speed) < 0.01 }, label)));
    const credit = el("div", { class: "status muted" });
    const showCredit = () => {
      const v = voices.find(x => String(x.id) === voiceSel.value);
      credit.textContent = v ? `Voice: VOICEVOX:${v.name}` : "";
    };
    const saveVoice = async () => {
      await api.put("/api/tts/settings", { speaker: Number(voiceSel.value), speed: Number(speedSel.value) });
      await refreshTts();
      showCredit();
    };
    voiceSel.addEventListener("change", saveVoice);
    speedSel.addEventListener("change", saveVoice);
    showCredit();
    row.replaceChildren(
      el("label", {}, "Voice", voiceSel),
      el("label", {}, "Speed", speedSel),
      el("button", { class: "btn", type: "button", onclick: () => speak("こんにちは。日本語を勉強しましょう。") }, "🔊 Try it"),
      credit);
  })();
  return row;
}

/* ================= boot ================= */

window.addEventListener("hashchange", route);
syncToggles();
route();
