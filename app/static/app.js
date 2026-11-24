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
  kanji: renderKanji,
  reading: renderReading,
  listening: renderListening,
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
  // Practice lives under Kana, Listening under Reading.
  const navName = { practice: "learn", listening: "reading" }[name] || name;
  for (const link of document.querySelectorAll(".nav a, .topbar-end a")) {
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

/* ================= night sky (decorative) ================= */

// Small seeded random so the sky looks the same on every visit.
function seeded(seed) {
  return () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// One cloud band as SVG: puffs repeated across two widths so the CSS drift can
// loop seamlessly; a turbulence filter roughens the edges like brush strokes.
function cloudBand(name, seed, { base, light, puffs, top }) {
  const rnd = seeded(seed);
  const shapes = [];
  for (let i = 0; i < puffs; i++) {
    const cx = rnd() * 1000, cy = top + rnd() * (300 - top) * 0.7;
    const rx = 70 + rnd() * 170, ry = 28 + rnd() * 55;
    for (const shift of [0, 1000]) {
      shapes.push(`<ellipse cx="${(cx + shift).toFixed(1)}" cy="${cy.toFixed(1)}" rx="${rx.toFixed(1)}" ry="${ry.toFixed(1)}" fill="${base}"/>`);
      shapes.push(`<ellipse cx="${(cx + shift - rx * 0.15).toFixed(1)}" cy="${(cy - ry * 0.35).toFixed(1)}" rx="${(rx * 0.55).toFixed(1)}" ry="${(ry * 0.45).toFixed(1)}" fill="${light}" opacity=".55"/>`);
    }
  }
  return `<svg viewBox="0 0 2000 300" preserveAspectRatio="none" focusable="false">
    <defs><filter id="paint-${name}" x="-5%" y="-20%" width="110%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.009 0.035" numOctaves="3" seed="${seed}"/>
      <feDisplacementMap in="SourceGraphic" scale="34"/>
      <feGaussianBlur stdDeviation="2.2"/>
    </filter></defs>
    <g filter="url(#paint-${name})">${shapes.join("")}<rect x="0" y="${top + 120}" width="2000" height="${300 - top - 120}" fill="${base}"/></g>
  </svg>`;
}

function paintSky() {
  const stars = $("#sky-stars");
  if (!stars || stars.childElementCount) return;
  const rnd = seeded(7);
  for (let i = 0; i < 110; i++) {
    const size = rnd() < 0.85 ? 1 + rnd() * 1.2 : 2 + rnd() * 1.2;
    stars.append(el("span", { class: "star", style:
      `left:${(rnd() * 100).toFixed(2)}%;top:${(rnd() * 100).toFixed(2)}%;width:${size.toFixed(1)}px;height:${size.toFixed(1)}px;` +
      `--o:${(0.35 + rnd() * 0.6).toFixed(2)};--t:${(3 + rnd() * 5).toFixed(1)}s;--d:${(-rnd() * 8).toFixed(1)}s` }));
  }
  const layers = {
    back: { base: "#4e5d8c", light: "#6f7fb3", puffs: 16, top: 40 },   // slate blue
    mid: { base: "#6b5a9e", light: "#9481c4", puffs: 14, top: 90 },    // muted violet
    front: { base: "#b47f9f", light: "#dcaac3", puffs: 12, top: 150 }, // dusty pink
  };
  document.querySelectorAll(".cloud-layer").forEach((node, i) => {
    const name = node.dataset.layer;
    node.innerHTML = cloudBand(name, 11 + i * 17, layers[name]);
  });
}

// Canvas tabs jump to sections of the home page (they're not routes).
document.addEventListener("click", e => {
  const tab = e.target.closest(".canvas-tabs button");
  if (!tab) return;
  document.querySelectorAll(".canvas-tabs button").forEach(b => b.classList.toggle("active", b === tab));
  const target = tab.dataset.scroll === "top" ? null : document.getElementById(tab.dataset.scroll);
  if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
  else window.scrollTo({ top: 0, behavior: "smooth" });
});

// Fade sections up as they scroll into view (skipped for reduced motion).
const revealObserver = "IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches
  ? new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add("in"); revealObserver.unobserve(entry.target); }
    }), { threshold: 0.08 })
  : null;
if (revealObserver) document.documentElement.classList.add("motion");
function observeReveals() {
  if (!revealObserver) return;
  document.querySelectorAll(".fade-up:not(.in)").forEach(node => revealObserver.observe(node));
}

function setState(id, text, kind) {
  const node = document.getElementById(id);
  if (!node) return;
  node.textContent = text;
  node.className = `state ${kind}`;
}

/* ================= home ================= */

async function renderHome() {
  paintSky();
  observeReveals();
  for (const id of ["state-due", "state-streak", "state-today"]) setState(id, "syncing…", "syncing");
  const script = getScript("home");
  const [stats, data] = await Promise.all([
    api.get("/api/kana/stats"),
    api.get(`/api/kana/groups?script=${script}`),
  ]);

  // Hero button leads to whatever is most useful right now.
  const due = stats.due_count;
  $("#hero-primary").href = due ? "#review" : "#lessons";
  $("#hero-primary-label").textContent = due ? `Start review (${due})` : "Continue learning";
  setState("state-due", due ? `${due} due` : "all clear", due ? "todo" : "ok");
  setState("state-streak", stats.streak_days ? "on track" : "start today", stats.streak_days ? "ok" : "todo");
  setState("state-today", stats.reviews_today ? "studied" : "not yet", stats.reviews_today ? "ok" : "todo");

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
  ["deck", "Word, kanji & mistake reviews", "var(--series-2)"],
  ["quiz", "Quiz, reading & listening", "var(--series-3)"],
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
    ...Object.entries(data.lessons).map(([lvl, l]) => meter(`${lvl} lessons`, l.done, l.total, `${l.done} / ${l.total} complete`)),
    ...["N5", "N4", "N3", "N2"].filter(lvl => data.kanji?.[lvl]).map(lvl =>
      meter(`Kanji (${lvl} list)`, known(data.kanji[lvl]), data.kanji[lvl].total,
        `${known(data.kanji[lvl])} known · ${data.kanji[lvl].total} total`)),
    ...Object.entries(data.reading || {}).map(([lvl, r]) => meter(`${lvl} reading passages`, r.done, r.total, `${r.done} / ${r.total} read`)),
    ...Object.entries(data.listening || {}).map(([lvl, r]) => meter(`${lvl} listening items`, r.done, r.total, `${r.done} / ${r.total} done`)),
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
  // Kanji cards can be answered by writing them; the drawing grades the card instead of self-grading.
  const writeKanji = $("#opt-write-kanji");
  writeKanji.checked = prefs.get("review.writeKanji", false);
  let dropCardKeys = () => {};  // the shown card's keyboard shortcuts, dropped when the batch reloads
  writeKanji.onchange = () => { prefs.set("review.writeKanji", writeKanji.checked); dropCardKeys(); loadBatch(); };
  await loadBatch();

  // Kana first (quick, typed), then saved words and mistakes (self-graded).
  // Order: kana, then saved words and mistakes, then kanji.
  async function loadBatch() {
    const [kanaData, deckData, kanjiData] = await Promise.all([
      api.get("/api/kana/review"), api.get("/api/deck/review"),
      api.get("/api/kanji/review").catch(() => ({ cards: [], due_count: 0, next_due: null })),
    ]);
    const total = kanaData.due_count + deckData.due_count + kanjiData.due_count;
    updateBadge(total);
    if (kanaData.cards.length) return showCard(kanaData.cards, 0, total);
    if (deckData.cards.length) return showDeckCard(deckData.cards, 0, deckData.due_count + kanjiData.due_count);
    if (kanjiData.cards.length) return showKanjiCard(kanjiData.cards, 0, kanjiData.due_count);
    const upcoming = [kanaData.next_due, deckData.next_due, kanjiData.next_due].filter(Boolean);
    finished(upcoming.length ? Math.min(...upcoming) : null);
  }

  function showKanjiCard(cards, idx, dueCount) {
    if (idx >= cards.length) return loadBatch();
    const card = cards[idx];
    const remaining = dueCount - idx;
    const shownAt = performance.now();
    const stage = el("div", { class: "card-stage" });
    const reveal = el("div", { class: "reveal" });
    let keyHandler = null;
    const setKeys = fn => {
      if (keyHandler) document.removeEventListener("keydown", keyHandler);
      keyHandler = fn;
      if (fn) document.addEventListener("keydown", fn);
    };
    onCleanup(() => setKeys(null));
    dropCardKeys = () => setKeys(null);

    async function grade(rating) {
      setKeys(null);
      stage.querySelectorAll("button").forEach(b => { b.disabled = true; });
      await api.post("/api/kanji/review", { card_id: card.id, rating, elapsed_ms: Math.round(performance.now() - shownAt) });
      session.reviewed++;
      if (rating !== "again") session.correct++;
      updateBadge(Math.max(0, remaining - 1));
      showKanjiCard(cards, idx + 1, dueCount);
    }

    function showAnswer() {
      const example = card.examples[0];
      const diagram = strokeDiagram(card.strokes, { size: 120, numbers: false });
      reveal.replaceChildren(
        el("div", { class: "kanji-review-answer" },
          diagram.node,
          el("div", {},
            el("div", { class: "meaning" }, card.meanings.slice(0, 3).join(", ")),
            card.on.length ? el("div", { class: "kanji-reading" }, el("span", { class: "label" }, "On"), el("span", { lang: "ja" }, card.on.join("、"))) : "",
            card.kun.length ? el("div", { class: "kanji-reading" }, el("span", { class: "label" }, "Kun"), el("span", { lang: "ja" }, card.kun.join("、"))) : "",
            example ? el("div", { class: "muted" }, el("span", { lang: "ja" }, `${example.word} (${example.reading})`), ` ${example.meaning}`) : "")),
        el("div", { class: "grade-row" },
          [["again", "Again", "forgot"], ["hard", "Hard", "barely"], ["good", "Good", "knew it"], ["easy", "Easy", "instant"]]
            .map(([r, label, hint], n) => el("button", { class: `btn grade-${r}`, type: "button", onclick: () => grade(r) },
              label, el("small", {}, `${n + 1} · ${hint}`)))));
      later(diagram.play, 100);
      if (example) speak(example.word);
      setKeys(e => {
        const r = ["again", "hard", "good", "easy"][Number(e.key) - 1];
        if (r) grade(r);
      });
    }

    if (prefs.get("review.writeKanji", false) && card.strokes?.length) return writeCard();

    reveal.append(el("button", { class: "btn btn-primary", type: "button", onclick: showAnswer }, "Show answer"));
    setKeys(e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); showAnswer(); } });
    stage.append(
      el("div", { class: "prompt-label" }, "What does this kanji mean, and how is it read?"),
      el("div", { class: "big-word kanji-review-char", lang: "ja" }, card.kanji),
      reveal);
    body.replaceChildren(sessionBar(remaining), stage);

    // Writing mode: see the meaning and readings, draw the kanji; the drawing grades the card.
    function writeCard() {
      let revealed = false;
      const note = el("div", { class: "muted write-note", role: "status" });
      const next = el("button", { class: "btn btn-primary", type: "button", hidden: true,
        onclick: () => { setKeys(null); showKanjiCard(cards, idx + 1, dueCount); } }, el("span", { class: "arrow" }, "Next"));
      const answer = el("div", { class: "write-answer", hidden: true },
        el("span", { lang: "ja", class: "kanji-big", style: "font-size:2.5rem" }, card.kanji),
        card.examples[0] ? el("span", { class: "muted", lang: "ja" }, `${card.examples[0].word} (${card.examples[0].reading})`) : "");
      const helpers = el("div", { class: "btn-row" },
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => { revealed = true; pad.showHint(); } }, "Hint for this stroke"),
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => { revealed = true; pad.reset("trace"); } }, "Show the kanji"));
      const pad = writingPad(card.strokes, { mode: "memory", onDone: async (mistakes, info) => {
        helpers.hidden = true;
        const hinted = revealed || info.hinted;
        note.textContent = await recordWriting(card.kanji, mistakes, { ...info, hinted });
        session.reviewed++;
        if (!hinted && mistakes < 3) session.correct++;
        updateBadge(Math.max(0, remaining - 1));
        answer.hidden = false;
        next.hidden = false;
        next.focus();
        speak(card.examples[0]?.word || card.kanji);
        setKeys(e => { if (e.key === "Enter") { e.preventDefault(); next.click(); } });
      } });
      stage.replaceChildren(
        el("div", { class: "prompt-label" }, `Write the kanji (${card.strokes.length} strokes):`),
        el("div", { class: "quiz-meaning" }, `“${card.cue.join(", ")}”`),
        el("div", { class: "muted", lang: "ja" }, [card.kun.join("、"), card.on.join("、")].filter(Boolean).join(" ・ ")),
        el("div", { class: "write-wrap" }, pad.canvas, pad.status, note, helpers),
        answer,
        next);
      body.replaceChildren(sessionBar(remaining), stage);
    }
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
    dropCardKeys = () => setKeys(null);

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
  const levels = [...new Set(lessons.map(l => l.level))];
  const intro = {
    N5: "The basics: polite sentences, particles, verbs, adjectives and counting.",
    N4: "Builds on N5: plain forms, experience, ability, plans, obligations and conditions.",
    N3: "Everyday intermediate grammar: timing, cause and effect, viewpoints, rules and decisions.",
    N2: "Upper-intermediate grammar for news, notices and essays: formal contrasts, reasons, trends and certainty.",
    N1: "Advanced, mostly written grammar for speeches, editorials and literature: emphasis, formal purpose, strong feeling.",
  };
  body.replaceChildren(
    el("div", { class: "panel-head" },
      el("h2", {}, "JLPT lessons"),
      el("span", { class: "muted" }, "Read, practice with Sensei, then mark complete to add the words to your reviews")),
    ...levels.map(level => {
      const ofLevel = lessons.filter(l => l.level === level);
      const done = ofLevel.filter(l => l.status === "done").length;
      return el("section", { class: "level-block", "aria-labelledby": `level-${level}` },
        el("div", { class: "level-head" },
          el("h3", { id: `level-${level}` }, `JLPT ${level}`),
          el("span", { class: "muted" }, `${done} / ${ofLevel.length} complete`)),
        intro[level] && el("p", { class: "muted level-intro" }, intro[level]),
        el("div", { class: "lesson-grid" }, ofLevel.map(l =>
          el("a", { class: `lesson-card${l === next ? " next" : ""}`, href: `#lessons/${l.id}` },
            el("div", { class: "num" }, `${l.level} · Lesson ${l.number}`,
              l.status !== "new" && el("span", { class: `status-pill ${l.status}` }, l.status === "done" ? "Done ✓" : "In progress")),
            el("div", { class: "jp", lang: "ja" }, l.jp_title),
            el("div", { class: "title" }, l.title),
            el("div", { class: "goal" }, l.goal)))));
    }));
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
      el("div", { class: "lesson-level" }, `JLPT ${lesson.level} · Lesson ${lesson.number}`),
      el("h2", {}, lesson.title),
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

/* ================= reading practice ================= */

const READING_INTRO = {
  N3: "Short notes, notices and essays like the JLPT N3 reading section. Read, answer every question, then check the explanations and the translation.",
  N2: "Longer essays, formal notices and A/B opinion pieces like the JLPT N2 reading section. Look for the writer's main point.",
  N1: "Dense, abstract essays, formal notices and a long passage like the JLPT N1 reading section. Follow the argument and watch for choices that go too far.",
};

async function renderReading() {
  const body = $("#reading-body");
  if (routeArg) return renderPassage(body, routeArg);

  const { passages } = await api.get("/api/reading");
  const next = passages.find(p => !p.result);
  const levels = [...new Set(passages.map(p => p.level))];
  body.replaceChildren(
    el("div", { class: "panel-head" }, practiceTabs("reading"),
      el("span", { class: "muted" }, "Tap any word to look it up")),
    ...levels.map(level => {
      const ofLevel = passages.filter(p => p.level === level);
      const done = ofLevel.filter(p => p.result).length;
      return el("section", { class: "level-block", "aria-labelledby": `reading-${level}` },
        el("div", { class: "level-head" },
          el("h3", { id: `reading-${level}` }, `JLPT ${level}`),
          el("span", { class: "muted" }, `${done} / ${ofLevel.length} read`)),
        READING_INTRO[level] && el("p", { class: "muted level-intro" }, READING_INTRO[level]),
        el("div", { class: "lesson-grid" }, ofLevel.map(p =>
          el("a", { class: `lesson-card${p === next ? " next" : ""}`, href: `#reading/${p.id}` },
            el("div", { class: "num" }, `${p.level} · Passage ${p.number}`,
              p.result && el("span", { class: `status-pill ${p.result.best === p.result.total ? "done" : "started"}` },
                `Best ${p.result.best} / ${p.result.total}`)),
            el("div", { class: "jp", lang: "ja" }, p.jp_title),
            el("div", { class: "title" }, p.title),
            el("div", { class: "goal" }, `${p.kind} · ${p.questions} question${p.questions > 1 ? "s" : ""} · about ${p.minutes} min`)))));
    }));
}

// Furigana inside an answer button: plain ruby, no clickable words, so a tap picks the answer.
function inlineRuby(segments) {
  const span = el("span", { class: "choice-text", lang: "ja" });
  span.innerHTML = renderRich(segments).replace(/^<p>|<\/p>$/g, "");
  return span;
}

async function renderPassage(body, id) {
  const p = await api.get(`/api/reading/${id}`);
  const startedAt = performance.now();
  const chosen = p.questions.map(() => null);
  let checked = false;

  const furiganaOn = prefs.get("reading.furigana", true);
  const page = el("div", { class: `reading-page${furiganaOn ? "" : " no-furigana"}` });
  const furiganaToggle = el("label", { class: "toggle" },
    el("input", { type: "checkbox", checked: furiganaOn, onchange: e => {
      prefs.set("reading.furigana", e.target.checked);
      page.classList.toggle("no-furigana", !e.target.checked);
    } }), "Furigana");

  const text = el("div", { class: "reading-text" }, p.text.map(t =>
    el("div", { class: "reading-para" },
      richEl("div", { class: "jp-line", lang: "ja" }, t.segments),
      speakButton(t.jp.replace(/\n/g, "。")))));

  const check = el("button", { class: "btn btn-primary", type: "button", disabled: true }, "Check answers");
  const summary = el("div", { role: "status" });
  const questions = p.questions.map((q, qi) => {
    const explain = el("div");
    const buttons = q.choices.map((c, ci) =>
      el("button", { class: "quiz-choice jp reading-choice", type: "button", "aria-pressed": "false",
        onclick: () => pick(qi, ci) }, el("span", { class: "key" }, ci + 1), inlineRuby(c)));
    return { buttons, explain, node: el("div", { class: "reading-q" },
      el("div", { class: "reading-q-head" }, el("span", { class: "reading-q-num" }, `問${qi + 1}`),
        richEl("div", { class: "jp-line", lang: "ja" }, q.segments)),
      el("div", { class: "quiz-choices reading-choices" }, buttons),
      explain) };
  });

  function pick(qi, ci) {
    if (checked) return;
    chosen[qi] = ci;
    questions[qi].buttons.forEach((b, i) => {
      b.classList.toggle("picked", i === ci);
      b.setAttribute("aria-pressed", String(i === ci));
    });
    check.disabled = chosen.includes(null);
  }

  check.addEventListener("click", async () => {
    if (checked || chosen.includes(null)) return;
    checked = true;
    check.disabled = true;
    const res = await api.post(`/api/reading/${id}/answers`,
      { answers: chosen, elapsed_ms: Math.round(performance.now() - startedAt) });
    res.results.forEach((r, qi) => {
      const q = questions[qi];
      q.buttons.forEach((b, i) => {
        b.disabled = true;
        b.classList.remove("picked");
        if (i === r.answer) b.classList.add("ok");
        else if (i === r.chosen) b.classList.add("bad");
      });
      q.explain.replaceChildren(
        el("p", { class: `feedback ${r.correct ? "ok" : "bad"}` }, r.correct ? "✓ Correct" : `✗ The answer is ${r.answer + 1}`),
        el("div", { class: "quiz-explain" }, r.why));
    });
    const minutes = Math.max(1, Math.round((performance.now() - startedAt) / 60000));
    summary.replaceChildren(el("p", { class: "reading-score" },
      el("strong", {}, `${res.correct} / ${res.total} correct`), ` · ${minutes} min (suggested: about ${p.minutes} min)`));
    check.hidden = true;
    after.replaceChildren(...afterSections(res));
  });

  function afterSections(res) {
    const unsaved = res.vocab.filter(v => !v.saved).length;
    const addWords = el("button", { class: "btn", type: "button", disabled: !unsaved },
      unsaved ? `＋ Add ${unsaved} key word${unsaved > 1 ? "s" : ""} to reviews` : "Key words are in your reviews ✓");
    addWords.addEventListener("click", async () => {
      addWords.disabled = true;
      const r = await api.post(`/api/reading/${id}/words`, {});
      addWords.textContent = `${r.words_added} word${r.words_added === 1 ? "" : "s"} added ✓`;
      refreshBadge();
    });
    return [
      el("details", { class: "lesson-section reading-translation" },
        el("summary", {}, "English translation"),
        res.translation.map(t => el("p", { class: "reading-en" }, t))),
      el("div", { class: "lesson-section" },
        el("h3", {}, "Key words"),
        el("table", { class: "vocab-table" }, el("tbody", {}, res.vocab.map(v =>
          el("tr", {},
            el("td", {}, richEl("div", { class: "vw", lang: "ja" }, v.segments)),
            el("td", { class: "vr", lang: "ja" }, v.reading !== v.word ? v.reading : ""),
            el("td", { class: "vm" }, v.meaning),
            el("td", {}, speakButton(v.reading))))))),
      el("div", { class: "lesson-actions" },
        addWords,
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => renderPassage(body, id) }, "↻ Try again"),
        p.next_id && el("a", { class: "btn btn-primary", href: `#reading/${p.next_id}` }, "Next passage →")),
    ];
  }

  addKeyHandler(e => {
    if (checked || e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
    if (e.key === "Enter" && !check.disabled) check.click();
  });

  const after = el("div");
  page.append(
    el("div", { class: "lesson-head" },
      el("a", { class: "back", href: "#reading" }, "← All passages"),
      el("div", { class: "lesson-level" }, `JLPT ${p.level} · Passage ${p.number} · ${p.kind}`),
      el("h2", {}, p.title),
      el("div", { class: "jp", lang: "ja" }, p.jp_title),
      el("p", { class: "goal" }, `${p.questions.length} question${p.questions.length > 1 ? "s" : ""} · about ${p.minutes} minutes`)),
    el("div", { class: "reading-toolbar" }, furiganaToggle,
      el("span", { class: "muted" }, "Kanji beyond the study lists keep their furigana, as on the JLPT.")),
    text,
    el("div", { class: "lesson-section" },
      el("h3", {}, "Questions"),
      questions.map(q => q.node),
      el("div", { class: "lesson-actions" }, check),
      summary),
    after);
  body.replaceChildren(page);
  window.scrollTo(0, 0);
}

/* ================= listening practice ================= */

const LISTENING_INTRO = {
  N3: "Conversations and short talks like the JLPT N3 listening section, read by a narrator, a woman and a man. Listen, answer, then check the transcript.",
  N2: "Faster, longer conversations like the JLPT N2 listening section, including integrated comprehension: weigh several options against what people say.",
  N1: "Lectures, reviews and formal conversations like the JLPT N1 listening section. Listen for the speaker's real point and for subtle replies.",
};
const LISTENING_HOWTO = {
  task: "Listen and choose what the person will do. The question is asked before and after the conversation.",
  point: "Listen for the detail the question asks about. The question is asked before and after the conversation.",
  summary: "Listen to the whole talk. On the test the question and the choices are only spoken, so they appear here as numbers.",
  quick: "Listen to one line and three replies, then choose the best reply. The replies are only spoken.",
  integrated: "Listen to the explanation of the options, then to the conversation. Keep track of each person's conditions.",
};

// The Reading / Listening switch at the top of both lists.
function practiceTabs(active) {
  return el("div", { class: "segmented" },
    el("a", { class: active === "reading" ? "active" : "", href: "#reading" }, "Reading"),
    el("a", { class: active === "listening" ? "active" : "", href: "#listening" }, "Listening"));
}

// Plays a script line by line, each role in its own VOICEVOX voice (or the browser's
// voice at a different pitch when VOICEVOX isn't running).
function dialoguePlayer(script, voices, { onLine } = {}) {
  let stopped = false;
  let audio = null;
  const pitch = { N: 1, F: 1.3, M: 0.75 };
  const pause = ms => new Promise(r => setTimeout(r, ms));

  function browserLine(line) {
    return new Promise(resolve => {
      if (!jaVoice) return resolve();
      const u = new SpeechSynthesisUtterance(line.text);
      u.voice = jaVoice;
      u.lang = "ja-JP";
      u.rate = 0.9;
      u.pitch = pitch[line.who] ?? 1;
      u.onend = resolve;
      u.onerror = resolve;
      speechSynthesis.speak(u);
    });
  }

  function playLine(line) {
    if (!voices) return browserLine(line);
    return new Promise(resolve => {
      audio = new Audio(dialogueUrl(line, voices));
      currentAudio = audio;  // so other 🔊 buttons stop it
      audio.onended = resolve;
      audio.onerror = () => browserLine(line).then(resolve);
      audio.play().catch(() => browserLine(line).then(resolve));
    });
  }

  return {
    async play() {
      stopped = false;
      for (let i = 0; i < script.length; i++) {
        if (stopped) return false;
        onLine?.(i);
        await playLine(script[i]);
        // A longer pause after the narrator's opening, as on the test.
        if (!stopped) await pause(i === 0 && script[0].who === "N" ? 1500 : 600);
      }
      onLine?.(-1);
      return !stopped;
    },
    stop() {
      stopped = true;
      audio?.pause();
      if ("speechSynthesis" in window) speechSynthesis.cancel();
      onLine?.(-1);
    },
  };
}

function dialogueUrl(line, voices) {
  return `/api/tts?text=${encodeURIComponent(line.text)}&speaker=${voices[line.who]}`;
}

async function renderListening() {
  const body = $("#listening-body");
  if (routeArg) return renderListeningItem(body, routeArg);

  const { items } = await api.get("/api/listening");
  const next = items.find(i => !i.result);
  const levels = [...new Set(items.map(i => i.level))];
  body.replaceChildren(
    el("div", { class: "panel-head" }, practiceTabs("listening"),
      el("span", { class: "muted" }, hasVoice() ? "Headphones recommended" : "No Japanese voice found: install VOICEVOX or a system voice")),
    ...levels.map(level => {
      const ofLevel = items.filter(i => i.level === level);
      const done = ofLevel.filter(i => i.result).length;
      return el("section", { class: "level-block", "aria-labelledby": `listening-${level}` },
        el("div", { class: "level-head" },
          el("h3", { id: `listening-${level}` }, `JLPT ${level}`),
          el("span", { class: "muted" }, `${done} / ${ofLevel.length} done`)),
        LISTENING_INTRO[level] && el("p", { class: "muted level-intro" }, LISTENING_INTRO[level]),
        el("div", { class: "lesson-grid" }, ofLevel.map(i =>
          el("a", { class: `lesson-card${i === next ? " next" : ""}`, href: `#listening/${i.id}` },
            el("div", { class: "num" }, `${i.level} · Item ${i.number}`,
              i.result && el("span", { class: `status-pill ${i.result.last ? "done" : "started"}` }, i.result.last ? "Correct ✓" : "Try again")),
            el("div", { class: "jp", lang: "ja" }, i.kind_jp),
            el("div", { class: "title" }, i.title),
            el("div", { class: "goal" }, i.kind_en)))));
    }));
}

async function renderListeningItem(body, id) {
  await ttsChecked;
  const item = await api.get(`/api/listening/${id}`);
  let plays = 0;
  let answered = false;
  let playing = false;

  const status = el("div", { class: "listen-status", role: "status" });
  const playBtn = el("button", { class: "play-big", type: "button", "aria-label": "Play" }, "▶");
  const player = dialoguePlayer(item.script, item.voices, {
    onLine: i => {
      status.textContent = i >= 0 ? `Playing… ${i + 1} / ${item.script.length}` : (plays ? `Played ${plays} time${plays > 1 ? "s" : ""}` : "");
      if (answered) transcript.querySelectorAll(".listen-line").forEach((n, k) => n.classList.toggle("speaking", k === i));
    },
  });
  onCleanup(() => player.stop());

  async function togglePlay() {
    if (playing) { player.stop(); return; }
    playing = true;
    plays++;
    playBtn.textContent = "■";
    playBtn.setAttribute("aria-label", "Stop");
    await player.play();
    playing = false;
    playBtn.textContent = "▶";
    playBtn.setAttribute("aria-label", "Play");
  }
  playBtn.addEventListener("click", togglePlay);

  // Make every clip once before the first play, so lines follow each other without gaps.
  async function prepare() {
    if (!item.voices) { status.textContent = hasVoice() ? "Using the browser's voice (VOICEVOX isn't running)." : "No Japanese voice available."; return; }
    playBtn.disabled = true;
    for (let i = 0; i < item.script.length; i++) {
      status.textContent = `Preparing audio… ${i + 1} / ${item.script.length}`;
      try { await fetch(dialogueUrl(item.script[i], item.voices)); } catch { /* playing will fall back */ }
      if (!body.isConnected) return;
    }
    playBtn.disabled = false;
    status.textContent = "Ready. Press play when you're ready.";
  }

  const feedback = el("div");
  const transcript = el("div");
  const after = el("div");
  const buttons = item.choices.map((c, n) =>
    el("button", { class: `quiz-choice jp listen-choice${c ? "" : " number-only"}`, type: "button", onclick: () => choose(n) },
      el("span", { class: "key" }, n + 1), c ? inlineRuby(c) : el("span", { class: "muted" }, `Choice ${n + 1}`)));

  async function choose(n) {
    if (answered) return;
    answered = true;
    buttons.forEach(b => { b.disabled = true; });
    const res = await api.post(`/api/listening/${id}/answer`, { answer: n, plays });
    buttons.forEach((b, i) => {
      // Reveal what the spoken-only choices said.
      if (!item.choices[i]) b.replaceChildren(el("span", { class: "key" }, i + 1), inlineRuby(res.choices[i]));
      if (i === res.answer) b.classList.add("ok");
      else if (i === n) b.classList.add("bad");
    });
    feedback.replaceChildren(
      el("p", { class: `feedback ${res.correct ? "ok" : "bad"}` }, res.correct ? "✓ Correct" : `✗ The answer is ${res.answer + 1}`),
      el("div", { class: "quiz-explain" }, res.why));
    transcript.replaceChildren(el("div", { class: "lesson-section" },
      el("h3", {}, "Transcript"),
      el("div", { class: "listen-transcript" }, res.transcript.map(line =>
        el("div", { class: `listen-line role-${line.who}` },
          el("span", { class: "listen-who" }, line.label),
          el("div", { class: "listen-text" },
            richEl("div", { class: "jp-line", lang: "ja" }, line.segments),
            line.en && el("div", { class: "en" }, line.en)),
          el("button", { class: "speak", type: "button", "aria-label": "Play this line",
            onclick: () => dialoguePlayer([line].map(l => ({ who: l.who, text: l.jp })), item.voices).play() }, "🔊"))))));
    after.replaceChildren(...listeningAfter(res));
  }

  function listeningAfter(res) {
    const unsaved = res.vocab.filter(v => !v.saved).length;
    const addWords = el("button", { class: "btn", type: "button", disabled: !unsaved },
      unsaved ? `＋ Add ${unsaved} key word${unsaved > 1 ? "s" : ""} to reviews` : "Key words are in your reviews ✓");
    addWords.addEventListener("click", async () => {
      addWords.disabled = true;
      const r = await api.post(`/api/listening/${id}/words`, {});
      addWords.textContent = `${r.words_added} word${r.words_added === 1 ? "" : "s"} added ✓`;
      refreshBadge();
    });
    return [
      el("div", { class: "lesson-section" },
        el("h3", {}, "Key words"),
        el("table", { class: "vocab-table" }, el("tbody", {}, res.vocab.map(v =>
          el("tr", {},
            el("td", {}, richEl("div", { class: "vw", lang: "ja" }, v.segments)),
            el("td", { class: "vr", lang: "ja" }, v.reading !== v.word ? v.reading : ""),
            el("td", { class: "vm" }, v.meaning),
            el("td", {}, speakButton(v.reading))))))),
      el("div", { class: "lesson-actions" },
        addWords,
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => renderListeningItem(body, id) }, "↻ Try again"),
        item.next_id && el("a", { class: "btn btn-primary", href: `#listening/${item.next_id}` }, "Next item →")),
    ];
  }

  addKeyHandler(e => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
    if (e.key === " " && !playBtn.disabled) { e.preventDefault(); togglePlay(); return; }
    const n = Number(e.key) - 1;
    if (!answered && n >= 0 && n < buttons.length) choose(n);
  });

  body.replaceChildren(
    el("div", { class: "lesson-head" },
      el("a", { class: "back", href: "#listening" }, "← All listening"),
      el("div", { class: "lesson-level" }, `JLPT ${item.level} · Item ${item.number} · ${item.kind_en} (${item.kind_jp})`),
      el("h2", {}, item.title),
      el("p", { class: "goal" }, LISTENING_HOWTO[item.kind])),
    el("div", { class: "listen-player" }, playBtn, status),
    el("div", { class: "lesson-section" },
      el("h3", {}, "Question"),
      item.choices_printed && item.question_segments.length
        ? richEl("div", { class: "jp-line listen-question", lang: "ja" }, item.question_segments)
        : el("p", { class: "muted" }, item.kind === "quick" ? "Which reply is best?" : "Listen for the question at the end."),
      el("div", { class: "quiz-choices listen-choices" }, buttons),
      feedback),
    transcript,
    after);
  window.scrollTo(0, 0);
  prepare();
}

/* ================= kanji ================= */

const KANJI_GROUPS = {
  N5: ["N5", "Closest to JLPT N5 (KANJIDIC's old level-4 list)"],
  N4: ["N4", "Closest to JLPT N4 (KANJIDIC's old level-3 list)"],
  N3: ["N3", "Closest to JLPT N3: the 300 most common kanji of KANJIDIC's old level-2 list (which mixes N3 and N2), plus the ones your lessons use"],
  N2: ["N2", "Closest to JLPT N2: the rest of KANJIDIC's old level-2 list, after the N3 share"],
  lessons: ["From lessons", "Kanji used in your lessons that are on none of the lists above"],
};

// Stroke-order diagram from KanjiVG paths (109×109). Strokes draw one by one;
// a faint copy underneath shows the whole character.
function strokeDiagram(paths, { size = 220, numbers = true } = {}) {
  const ghost = svg("g", { class: "stroke-ghost" }, paths.map(d => svg("path", { d })));
  const ink = svg("g", { class: "stroke-ink" }, paths.map(d => svg("path", { d })));
  const nums = svg("g", { class: "stroke-nums" });
  const root = svg("svg", { viewBox: "0 0 109 109", width: size, height: size, role: "img",
    "aria-label": `Stroke order, ${paths.length} strokes` },
    svg("path", { class: "stroke-grid", d: "M54.5 0V109M0 54.5H109" }), ghost, ink, nums);
  let run = 0;

  async function play() {
    const myRun = ++run;
    const strokes = [...ink.children];
    nums.replaceChildren();
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    for (const [i, p] of strokes.entries()) {
      const len = p.getTotalLength();
      p.style.strokeDasharray = `${len}`;
      p.style.strokeDashoffset = reduce ? "0" : `${len}`;
    }
    for (const [i, p] of strokes.entries()) {
      if (myRun !== run) return; // replay pressed: abandon this run
      if (numbers) {
        const start = p.getPointAtLength(0);
        nums.append(svg("text", { x: start.x - 3, y: start.y - 2 }, String(i + 1)));
      }
      if (reduce) continue;
      const len = p.getTotalLength();
      await p.animate([{ strokeDashoffset: len }, { strokeDashoffset: 0 }],
        { duration: Math.max(280, len * 9), easing: "ease-in-out", fill: "forwards" }).finished;
      p.style.strokeDashoffset = "0";
      await new Promise(r => setTimeout(r, 90));
    }
  }
  return { node: root, play };
}

/* ---------- handwriting: draw strokes, check them against KanjiVG ---------- */

const PAD_POINTS = 32;   // every stroke is compared as 32 evenly spaced points
const PAD_TOLERANCE = 18; // mean distance allowed, in KanjiVG's 109×109 units
let samplerSvg = null;

function samplePath(d, n = PAD_POINTS) {
  if (!samplerSvg) {
    samplerSvg = svg("svg", { width: 0, height: 0, "aria-hidden": "true",
      style: "position:absolute;width:0;height:0;overflow:hidden" });
    document.body.append(samplerSvg);
  }
  const p = svg("path", { d });
  samplerSvg.append(p);
  const len = p.getTotalLength();
  const pts = Array.from({ length: n }, (_, i) => {
    const q = p.getPointAtLength(len * i / (n - 1));
    return [q.x, q.y];
  });
  p.remove();
  return pts;
}

function resampleStroke(points, n = PAD_POINTS) {
  if (points.length < 2) return Array.from({ length: n }, () => points[0]);
  const dist = [0];
  for (let i = 1; i < points.length; i++) {
    dist.push(dist[i - 1] + Math.hypot(points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1]));
  }
  const total = dist.at(-1) || 1;
  const out = [];
  let j = 0;
  for (let i = 0; i < n; i++) {
    const t = total * i / (n - 1);
    while (j < dist.length - 2 && dist[j + 1] < t) j++;
    const seg = dist[j + 1] - dist[j] || 1;
    const f = Math.min(1, Math.max(0, (t - dist[j]) / seg));
    out.push([points[j][0] + (points[j + 1][0] - points[j][0]) * f, points[j][1] + (points[j + 1][1] - points[j][1]) * f]);
  }
  return out;
}

const meanDistance = (a, b) => a.reduce((s, p, i) => s + Math.hypot(p[0] - b[i][0], p[1] - b[i][1]), 0) / a.length;

const pointGap = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
const strokeLength = pts => pts.slice(1).reduce((s, p, i) => s + pointGap(p, pts[i]), 0);

// Compare one drawn stroke with the stroke expected next (index k).
function judgeStroke(drawn, targets, k) {
  const u = resampleStroke(drawn);
  // Position and shape, ignoring direction (that's checked separately below).
  const fit = t => Math.min(meanDistance(u, t), meanDistance(u, [...t].reverse()));
  // If a later stroke fits clearly better, the learner skipped ahead.
  let best = k, bestFit = fit(targets[k]);
  for (let j = k + 1; j < targets.length; j++) {
    const f = fit(targets[j]);
    if (f < bestFit * 0.7) { best = j; bestFit = f; }
  }
  if (bestFit > PAD_TOLERANCE) return { ok: false, why: "shape" };
  if (best !== k) return { ok: false, why: "order", j: best };
  // Direction by the end points, which works even for short strokes, where the
  // point-by-point distance can't tell forwards from backwards. Tiny dots are exempt.
  const t = targets[k];
  const forwards = pointGap(u[0], t[0]) + pointGap(u.at(-1), t.at(-1));
  const backwards = pointGap(u[0], t.at(-1)) + pointGap(u.at(-1), t[0]);
  if (strokeLength(t) > 6 && backwards < forwards) return { ok: false, why: "direction" };
  return { ok: true };
}

// A drawing pad for one character. mode: "trace" (faint guide) or "memory".
function writingPad(paths, { mode = "trace", onDone } = {}) {
  const RES = 600, SCALE = RES / 109;
  const targets = paths.map(d => samplePath(d));
  const shapes = paths.map(d => new Path2D(d));
  const canvas = el("canvas", { class: "write-canvas", width: RES, height: RES,
    "aria-label": "Writing area: draw the strokes in order", role: "img" });
  const status = el("div", { class: "write-status", role: "status", "aria-live": "polite" });
  const ctx = canvas.getContext("2d");
  let k, mistakes, missesHere, current, flash, hint, finished, usedHint, startedAt;

  const css = name => getComputedStyle(document.documentElement).getPropertyValue(name).trim();

  function polyline(points, color, width) {
    if (!points?.length) return;
    ctx.beginPath();
    ctx.moveTo(points[0][0] * SCALE, points[0][1] * SCALE);
    for (const p of points.slice(1)) ctx.lineTo(p[0] * SCALE, p[1] * SCALE);
    if (points.length === 1) ctx.lineTo(points[0][0] * SCALE + .5, points[0][1] * SCALE + .5);
    ctx.strokeStyle = color; ctx.lineWidth = width * SCALE; ctx.lineCap = "round"; ctx.lineJoin = "round";
    ctx.stroke();
  }

  function draw() {
    ctx.clearRect(0, 0, RES, RES);
    ctx.save();
    ctx.setLineDash([6, 8]); ctx.strokeStyle = "rgba(255,255,255,.08)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(RES / 2, 0); ctx.lineTo(RES / 2, RES); ctx.moveTo(0, RES / 2); ctx.lineTo(RES, RES / 2); ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.scale(SCALE, SCALE); ctx.lineCap = "round"; ctx.lineJoin = "round";
    if (mode === "trace") {
      ctx.strokeStyle = "rgba(255,255,255,.13)"; ctx.lineWidth = 3.2;
      shapes.forEach(s => ctx.stroke(s));
    }
    ctx.strokeStyle = css("--text"); ctx.lineWidth = 3.4;
    shapes.slice(0, k).forEach(s => ctx.stroke(s));
    if (hint && !finished) {
      ctx.setLineDash([3, 3]); ctx.strokeStyle = css("--accent"); ctx.lineWidth = 3;
      ctx.stroke(shapes[k]);
      ctx.setLineDash([]); ctx.fillStyle = css("--accent");
      ctx.beginPath(); ctx.arc(targets[k][0][0], targets[k][0][1], 3, 0, Math.PI * 2); ctx.fill(); // where to start
    }
    ctx.restore();
    if (flash) polyline(flash, css("--bad"), 3.4);
    if (current) polyline(current, css("--accent"), 3.4);
  }

  function say(text, kind = "") {
    status.className = `write-status ${kind}`;
    status.textContent = text;
  }

  function reset(newMode = mode) {
    mode = newMode;
    k = 0; mistakes = 0; missesHere = 0; current = null; flash = null; hint = false; finished = false;
    usedHint = false; startedAt = null;
    say(`Stroke 1 of ${paths.length}. Start drawing.`);
    draw();
  }

  function finishStroke() {
    const drawn = current;
    current = null;
    if (!drawn || finished) return draw();
    const verdict = judgeStroke(drawn, targets, k);
    if (verdict.ok) {
      k++; missesHere = 0; hint = false; flash = null;
      if (k === paths.length) {
        finished = true;
        say(mistakes ? `✓ Done, with ${mistakes} mistake${mistakes > 1 ? "s" : ""}.` : "✓ Perfect! Every stroke in the right order and direction.", "ok");
        // Tracing a guide or seeing a hint means it wasn't written purely from memory.
        onDone?.(mistakes, { hinted: usedHint || mode === "trace", mode,
                             elapsedMs: startedAt ? Math.round(performance.now() - startedAt) : null });
      } else {
        say(`✓ Stroke ${k} correct. Now stroke ${k + 1} of ${paths.length}.`, "ok");
      }
    } else {
      mistakes++; missesHere++;
      flash = drawn;
      later(() => { flash = null; draw(); }, 700);
      const message = {
        direction: `Right place, wrong direction: stroke ${k + 1} starts from the other end.`,
        order: `That's stroke ${verdict.j + 1}. Stroke ${k + 1} comes first.`,
        shape: `Not quite. Check where stroke ${k + 1} starts and how it moves.`,
      }[verdict.why];
      if (missesHere >= 2) { hint = true; usedHint = true; }
      say(message + (hint ? " The dotted line shows it." : ""), "bad");
    }
    draw();
  }

  const toPad = e => {
    const r = canvas.getBoundingClientRect();
    return [(e.clientX - r.left) / r.width * 109, (e.clientY - r.top) / r.height * 109];
  };
  canvas.addEventListener("pointerdown", e => {
    if (finished) return;
    startedAt ??= performance.now();
    try { canvas.setPointerCapture(e.pointerId); } catch { /* keep drawing without capture */ }
    current = [toPad(e)];
    draw();
  });
  canvas.addEventListener("pointermove", e => {
    if (!current) return;
    const p = toPad(e);
    const last = current.at(-1);
    if (Math.hypot(p[0] - last[0], p[1] - last[1]) > .6) { current.push(p); draw(); }
  });
  canvas.addEventListener("pointerup", finishStroke);
  canvas.addEventListener("pointercancel", () => { current = null; draw(); });

  const showHint = () => { if (!finished) { hint = true; usedHint = true; draw(); say(`Stroke ${k + 1}: follow the dotted line from the dot.`); } };
  reset(mode);
  return { canvas, status, reset, showHint, get mistakes() { return mistakes; }, get mode() { return mode; } };
}

// Send a from-memory drawing to the review schedule; returns a short note to show.
async function recordWriting(ch, mistakes, { hinted, elapsedMs }) {
  try {
    const res = await api.post(`/api/kanji/${encodeURIComponent(ch)}/written`,
      { mistakes, hinted, elapsed_ms: elapsedMs });
    if (res.counted) return `Review updated (${res.rating}): next review ${timeUntil(res.next_due)}.`;
    if (res.reason === "reviewed_recently") return "Already reviewed recently, so the schedule wasn't changed.";
    return "Not in your reviews yet, so the schedule wasn't changed.";
  } catch {
    return "";
  }
}

function kanjiTile(k) {
  return el("a", { class: `kanji-tile cell ${k.status}`, href: `#kanji/${encodeURIComponent(k.kanji)}`,
    title: `${k.kanji}: ${k.meaning}` },
    el("span", { class: "k", lang: "ja" }, k.kanji),
    el("span", { class: "r" }, k.meaning));
}

async function renderKanji() {
  const body = $("#kanji-body");
  if (routeArg === "write") return renderWritingSession(body);
  if (routeArg) return renderKanjiDetail(body, decodeURIComponent(routeArg));
  const data = await api.get("/api/kanji");
  if (!data.available) {
    body.replaceChildren(el("div", { class: "empty" },
      el("h2", {}, "Kanji data isn't installed"),
      el("p", {}, "Download KANJIDIC2 (data/dict/kanjidic2.xml.gz) and KanjiVG (data/kanjivg) to use this section.")));
    return;
  }
  const group = prefs.get("kanji.group", "N5");
  const items = data.groups[group] || [];
  const known = items.filter(k => k.status === "known" || k.status === "mastered").length;
  const studying = items.filter(k => k.status !== "locked").length;

  const tabs = el("div", { class: "segmented" }, Object.entries(KANJI_GROUPS).map(([g, [label]]) =>
    el("button", { type: "button", class: g === group ? "active" : "",
      onclick: () => { prefs.set("kanji.group", g); renderKanji(); } }, label)));
  const learnBtn = el("button", { class: "btn btn-primary", type: "button", disabled: studying === items.length },
    el("span", { class: "arrow" }, "Add next 5 to reviews"));
  learnBtn.addEventListener("click", async () => {
    learnBtn.disabled = true;
    const { added } = await api.post("/api/kanji/learn-next", { group, count: 5 });
    refreshBadge();
    await renderKanji();
    if (added.length) $("#kanji-added").textContent = `Added ${added.join(" ")} to your reviews.`;
  });

  body.replaceChildren(
    el("div", { class: "panel-head" },
      el("h2", {}, "Kanji"),
      tabs),
    el("p", { class: "muted", style: "margin-top:-.4rem" }, KANJI_GROUPS[group][1],
      ". Tap a kanji for its stroke order, readings and example words."),
    el("div", { class: "progress-line" },
      el("div", { class: "progress" }, el("div", { class: "progress-fill", style: `width:${items.length ? known / items.length * 100 : 0}%` })),
      el("span", {}, `${known} / ${items.length} known · ${studying} studying`)),
    el("div", { class: "kanji-actions" }, learnBtn,
      el("a", { class: "btn", href: "#kanji/write" }, "✍ Writing practice"),
      el("span", { class: "muted", id: "kanji-added", role: "status" })),
    el("div", { class: "legend" },
      el("span", {}, el("i", { class: "dot locked" }), "Not studied"),
      el("span", {}, el("i", { class: "dot learning" }), "Learning"),
      el("span", {}, el("i", { class: "dot known" }), "Known"),
      el("span", {}, el("i", { class: "dot mastered" }), "Mastered")),
    el("div", { class: "kanji-grid" }, items.map(kanjiTile)),
    el("p", { class: "credit" }, "Readings and meanings: KANJIDIC2 (EDRDG, CC BY-SA 4.0). Stroke order: KanjiVG (Ulrich Apel, CC BY-SA 3.0)."),
  );
}

function writingSection(paths, ch) {
  const mode = prefs.get("write.mode", "trace");
  const note = el("div", { class: "muted write-note", role: "status" });
  const pad = writingPad(paths, { mode, onDone: async (mistakes, info) => {
    // Only writing from memory counts as a review; tracing is copying.
    note.textContent = info.mode === "memory" ? await recordWriting(ch, mistakes, info) : "Tracing doesn't change your review schedule. Try From memory.";
    refreshBadge();
  } });
  const modes = el("div", { class: "segmented" }, [["trace", "Trace"], ["memory", "From memory"]].map(([m, label]) =>
    el("button", { type: "button", class: m === mode ? "active" : "", onclick: e => {
      prefs.set("write.mode", m);
      modes.querySelectorAll("button").forEach(b => b.classList.toggle("active", b === e.currentTarget));
      note.textContent = "";
      pad.reset(m);
    } }, label)));
  return el("div", { class: "lesson-section write-section" },
    el("h3", {}, "Practice writing", modes),
    el("p", { class: "muted" }, "Draw each stroke with your mouse, finger or pen. Order and direction are checked as you go. " +
      "Writing from memory counts as a review of this kanji."),
    el("div", { class: "write-wrap" },
      pad.canvas,
      pad.status,
      note,
      el("div", { class: "btn-row" },
        el("button", { class: "btn btn-ghost", type: "button", onclick: pad.showHint }, "Show hint"),
        el("button", { class: "btn btn-ghost", type: "button", onclick: () => pad.reset() }, "↻ Start over"))));
}

// Write kanji from memory: see the meaning and reading, draw the character.
async function renderWritingSession(body) {
  const source = prefs.get("write.source", "studied");
  let { items } = await api.get(`/api/kanji/writing-set?source=${source}&limit=10`);
  let usedSource = source;
  if (!items.length && source === "studied") {  // nothing studied yet: start with the N5 list
    ({ items } = await api.get("/api/kanji/writing-set?source=N5&limit=10"));
    usedSource = "N5";
  }
  const results = [];
  let i = 0;

  const sources = el("div", { class: "segmented" }, [["studied", "My kanji"], ["N5", "N5 list"], ["N4", "N4 list"], ["N3", "N3 list"], ["N2", "N2 list"]].map(([s, label]) =>
    el("button", { type: "button", class: s === source ? "active" : "",
      onclick: () => { prefs.set("write.source", s); renderWritingSession(body); } }, label)));

  function show() {
    if (i >= items.length) return summary();
    const item = items[i];
    const next = el("button", { class: "btn btn-primary", type: "button", hidden: true,
      onclick: () => { i++; show(); } }, el("span", { class: "arrow" }, i + 1 < items.length ? "Next kanji" : "See results"));
    let revealed = false;
    const note = el("div", { class: "muted write-note", role: "status" });
    const helpers = el("div", { class: "btn-row" },
      el("button", { class: "btn btn-ghost", type: "button", onclick: () => { revealed = true; pad.reset("trace"); } }, "Show the kanji"),
      el("button", { class: "btn btn-ghost", type: "button", onclick: () => { revealed = true; pad.showHint(); } }, "Hint for this stroke"),
      el("button", { class: "btn btn-ghost", type: "button", onclick: () => { results.push({ kanji: item.kanji, mistakes: null, peeked: true }); i++; show(); } }, "Skip"));
    const pad = writingPad(item.stroke_paths, { mode: "memory", onDone: async (mistakes, info) => {
      helpers.hidden = true;  // once written, it can't be redone or skipped (that would count it twice)
      const peeked = revealed || info.hinted;
      const result = { kanji: item.kanji, mistakes, peeked, counted: false };
      results.push(result);
      answer.hidden = false;
      next.hidden = false;
      next.focus();
      note.textContent = await recordWriting(item.kanji, mistakes, { ...info, hinted: peeked });
      result.counted = note.textContent.startsWith("Review updated");
      refreshBadge();
    } });
    const answer = el("div", { class: "write-answer", hidden: true },
      el("span", { lang: "ja", class: "kanji-big", style: "font-size:2.5rem" }, item.kanji),
      el("a", { href: `#kanji/${encodeURIComponent(item.kanji)}` }, "Open kanji page"));
    body.replaceChildren(
      el("div", { class: "session-bar" },
        el("a", { class: "back", href: "#kanji" }, "← Kanji"),
        el("span", {}, `Kanji ${i + 1} / ${items.length}`),
        el("div", { class: "progress" }, el("div", { class: "progress-fill", style: `width:${i / items.length * 100}%` })),
        sources),
      el("div", { class: "card-stage" },
        el("div", { class: "prompt-label" }, `Write the kanji for (${item.strokes} strokes):`),
        el("div", { class: "quiz-meaning" }, `“${item.meanings.join(", ")}”`),
        el("div", { class: "muted", lang: "ja" }, [item.kun.join("、"), item.on.join("、")].filter(Boolean).join(" ・ ")),
        el("div", { class: "write-wrap" }, pad.canvas, pad.status, note, helpers),
        answer,
        next));
  }

  function summary() {
    const clean = results.filter(r => r.mistakes === 0 && !r.peeked).length;
    const counted = results.filter(r => r.counted).length;
    body.replaceChildren(el("div", { class: "empty" },
      el("div", { class: "big" }, clean === results.length ? "🎉" : "✍️"),
      el("div", { class: "score-big" }, `${clean} / ${results.length}`),
      el("p", {}, "written from memory without mistakes"),
      el("p", { class: "muted" }, counted
        ? `${counted} kanji review${counted > 1 ? "s" : ""} updated from your writing.`
        : "No reviews changed (these kanji aren't in your reviews yet, or were reviewed recently)."),
      el("div", { class: "write-results" }, results.map(r =>
        el("a", { class: `cell kanji-tile ${r.mistakes === 0 && !r.peeked ? "mastered" : r.mistakes === null ? "locked" : "learning"}`,
          href: `#kanji/${encodeURIComponent(r.kanji)}`,
          title: r.mistakes === null ? "skipped" : `${r.mistakes} mistake(s)${r.peeked ? ", used a hint" : ""}` },
          el("span", { class: "k", lang: "ja" }, r.kanji),
          el("span", { class: "r" }, r.mistakes === null ? "skipped" : r.mistakes === 0 && !r.peeked ? "perfect" : `${r.mistakes} miss${r.mistakes === 1 ? "" : "es"}${r.peeked ? " · hint" : ""}`)))),
      el("div", { class: "btn-row" },
        el("button", { class: "btn btn-primary", type: "button", onclick: () => renderWritingSession(body) }, "Practice again"),
        el("a", { class: "btn", href: "#kanji" }, "Back to kanji"))));
  }

  if (!items.length) {
    body.replaceChildren(el("div", { class: "empty" }, el("p", {}, "No kanji to practise yet."),
      el("a", { class: "btn", href: "#kanji" }, "Back to kanji")));
    return;
  }
  if (usedSource !== source) prefs.set("write.source", usedSource);
  show();
}

async function renderKanjiDetail(body, ch) {
  const k = await api.get(`/api/kanji/${encodeURIComponent(ch)}`);
  prefetchSpeech(k.examples.map(e => e.word));
  const diagram = strokeDiagram(k.stroke_paths);
  const kunForSpeech = r => r.replace(/[()]/g, "");
  const reading = (label, list, speakText) => list.length ? el("div", { class: "kanji-reading" },
    el("span", { class: "label" }, label),
    el("span", { class: "values", lang: "ja" }, list.join("、")),
    speakButton(speakText(list[0]))) : "";

  const add = el("button", { class: "btn btn-primary", type: "button", disabled: k.status !== "locked" },
    k.status === "locked" ? el("span", { class: "arrow" }, "Add to reviews") : "In your reviews ✓");
  add.addEventListener("click", async () => {
    add.disabled = true;
    await api.post(`/api/kanji/${encodeURIComponent(ch)}/learn`, {});
    add.textContent = "In your reviews ✓";
    refreshBadge();
  });

  body.replaceChildren(
    el("div", { class: "lesson-head" },
      el("a", { class: "back", href: "#kanji" }, "← All kanji"),
      el("div", { class: "lesson-level" }, `${KANJI_GROUPS[k.group][0]} · ${k.position} / ${k.group_size} · ${k.strokes} strokes`)),
    el("div", { class: "kanji-detail" },
      el("div", { class: "kanji-stage" },
        diagram.node,
        el("button", { class: "btn btn-ghost", type: "button", onclick: diagram.play }, "↻ Replay strokes")),
      el("div", { class: "kanji-info" },
        el("div", { class: "kanji-big", lang: "ja" }, k.kanji),
        el("h2", { class: "kanji-meaning" }, k.meanings.join(", ")),
        reading("On (音)", k.on, r => r),
        reading("Kun (訓)", k.kun, kunForSpeech),
        k.lesson_label && el("p", { class: "muted" }, "First used in ",
          el("a", { href: `#lessons/${k.lesson}` }, k.lesson_label)),
        el("div", { class: "btn-row", style: "justify-content:flex-start" }, add))),
    writingSection(k.stroke_paths, k.kanji),
    el("div", { class: "lesson-section" },
      el("h3", {}, "Example words"),
      el("table", { class: "vocab-table" }, el("tbody", {}, k.examples.map(x =>
        el("tr", {},
          el("td", {}, richEl("div", { class: "vw", lang: "ja" }, x.segments)),
          el("td", { class: "vr", lang: "ja" }, x.reading),
          el("td", { class: "vm" }, x.meaning, x.lesson ? el("span", { class: "tag", style: "margin-left:.4rem" }, "lesson") : ""),
          el("td", {}, speakButton(x.word))))))),
    el("div", { class: "lesson-actions" },
      k.prev && el("a", { class: "btn", href: `#kanji/${encodeURIComponent(k.prev)}` }, `← ${k.prev}`),
      k.next && el("a", { class: "btn", href: `#kanji/${encodeURIComponent(k.next)}` }, `${k.next} →`)),
  );
  window.scrollTo(0, 0);
  later(diagram.play, 250);
}

/* ================= quiz ================= */

const QUIZ_TYPES = {
  reading: ["漢字読み", "Kanji reading"],
  writing: ["表記", "Spelling"],
  meaning: ["語彙", "Vocabulary"],
  particle: ["文法", "Particles"],
  listening: ["聴解", "Listening"],
  kanji_meaning: ["漢字の意味", "Kanji meaning"],
  kanji_pick: ["漢字を選ぶ", "Pick the kanji"],
  kanji_word: ["漢字語の読み", "Kanji word reading"],
};
const KANJI_QUIZ_TYPES = ["kanji_meaning", "kanji_pick", "kanji_word"];

async function renderQuiz() {
  const body = $("#quiz-body");
  const opts = await api.get("/api/quiz/options");
  const saved = prefs.get("quiz", null);
  const studied = opts.lessons.filter(l => l.status !== "new").map(l => l.id);
  const settings = saved || {
    lessons: studied.length ? studied : opts.lessons.slice(0, 2).map(l => l.id),
    include_saved: true, count: 10, types: Object.keys(QUIZ_TYPES),
  };
  // Settings saved before kanji questions existed: switch them on once.
  if (!settings.typesVersion) {
    settings.types = [...new Set([...settings.types, ...KANJI_QUIZ_TYPES])];
    settings.typesVersion = 2;
  }
  settings.kanji_source ||= opts.studied_kanji >= 4 ? "studied" : "N5";
  const typeEntries = Object.entries(QUIZ_TYPES).filter(([t]) => opts.kanji_available || !KANJI_QUIZ_TYPES.includes(t));

  const chip = (value, label, checked) =>
    el("label", { class: "chip" }, el("input", { type: "checkbox", value, checked }), label);
  const lessonChips = opts.lessons.map(l =>
    chip(l.id, `${l.number}. ${l.title}${l.status === "done" ? " ✓" : ""}`, settings.lessons.includes(l.id)));
  // Shown grouped by level; lessonChips keeps the flat list the buttons and start() use.
  const lessonGroups = [...new Set(opts.lessons.map(l => l.level))].map(level =>
    el("div", { class: "chip-group" },
      el("div", { class: "chip-group-label" }, `JLPT ${level}`),
      el("div", { class: "chips" }, lessonChips.filter((_, i) => opts.lessons[i].level === level))));
  const typeChips = typeEntries.map(([t, [jp, en]]) =>
    chip(t, el("span", {}, el("span", { lang: "ja" }, jp), ` ${en}`), settings.types.includes(t)));
  const kanjiSources = [["studied", `My kanji (${opts.studied_kanji})`], ["N5", "N5 list"], ["N4", "N4 list"], ["N3", "N3 list"], ["N2", "N2 list"], ["lessons", "From lessons"]];
  const kanjiSource = el("div", { class: "segmented" }, kanjiSources.map(([value, label]) =>
    el("button", { type: "button", class: value === settings.kanji_source ? "active" : "",
      disabled: value === "studied" && !opts.studied_kanji,
      onclick: e => { settings.kanji_source = value; kanjiSource.querySelectorAll("button").forEach(b => b.classList.toggle("active", b === e.currentTarget)); } },
      label)));
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
      el("h2", {}, "JLPT practice quiz"),
      el("span", { class: "muted" }, "Questions come from verified lessons and dictionaries, never from the AI")),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Lessons",
        el("span", {},
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => lessonChips.forEach(c => { c.querySelector("input").checked = true; }) }, "All"),
          el("button", { class: "btn btn-ghost", type: "button", onclick: () => lessonChips.forEach(c => { c.querySelector("input").checked = false; }) }, "None"))),
      lessonGroups),
    el("div", { class: "field" },
      el("label", { class: "toggle" }, savedBox, `Include my saved words (${opts.saved_words})`)),
    el("div", { class: "field" },
      el("div", { class: "field-label" }, "Question types"),
      el("div", { class: "chips" }, typeChips)),
    opts.kanji_available ? el("div", { class: "field" },
      el("div", { class: "field-label" }, "Kanji questions use"),
      kanjiSource) : "",
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
    const jpChoices = ["reading", "writing", "particle", "kanji_pick", "kanji_word"].includes(q.type);
    let answered = false;

    const prompt = [];
    if (q.type === "reading" || q.type === "kanji_word") prompt.push(el("div", { class: "quiz-word", lang: "ja" }, q.prompt.word));
    if (q.type === "kanji_meaning") prompt.push(el("div", { class: "quiz-word quiz-kanji", lang: "ja" }, q.prompt.kanji));
    if (q.type === "kanji_pick") prompt.push(el("div", { class: "quiz-meaning" }, `“${q.prompt.meaning}”`));
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
      el("button", { class: `quiz-choice${jpChoices ? " jp" : ""}${q.type === "kanji_pick" ? " big" : ""}`, type: "button", lang: jpChoices ? "ja" : null,
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
    // Kanji meaning / pick questions: offer the kanji itself for the reviews.
    const missedKanji = [...new Set(results.filter(r => !r.ok && r.q.item.kanji && !r.q.item.word).map(r => r.q.item.kanji))];
    const missedCount = uniqueMissed.length + missedKanji.length;
    const addBtn = missedCount ? el("button", { class: "btn btn-primary", type: "button" },
      `Add ${missedCount} missed item${missedCount > 1 ? "s" : ""} to reviews`) : null;
    addBtn?.addEventListener("click", async () => {
      addBtn.disabled = true;
      const res = await api.post("/api/quiz/add-missed", {
        words: uniqueMissed.map(w => ({ word: w.word, reading: w.reading, meaning: w.meaning })),
        kanji: missedKanji,
      });
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
    ? `<span class="w${s.rare ? " rare" : ""}" data-i="${i}">${s.parts ? ruby(s.parts) : escapeHtml(s.t)}</span>`
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
