"""One small client for every provider: all of them speak the OpenAI chat API
(POST /chat/completions, streamed back as `data: {...}` lines).

API keys are read from the environment (.env) and never sent to the browser.
"""

from __future__ import annotations

import json
import os
import re
from collections.abc import AsyncIterator
from dataclasses import dataclass

import httpx

from . import config  # noqa: F401  (loads .env before the providers below read it)


@dataclass(frozen=True)
class Provider:
    id: str
    label: str
    base_url: str
    key_env: str | None             # None = no key needed (local)
    model_env: str
    preferred: tuple[str, ...]      # default model: exact ids first, then substrings
    fallback: str | None = None     # tried once when the chosen model is overloaded
    include: tuple[str, ...] = ()   # model id prefixes worth showing
    exclude: tuple[str, ...] = ()   # substrings of models that aren't chat models
    first_byte_timeout: float = 45  # seconds to wait for the reply to start


PROVIDERS: dict[str, Provider] = {
    "gemini": Provider(
        id="gemini",
        label="Google Gemini (free tier)",
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        key_env="GEMINI_API_KEY",
        model_env="GEMINI_MODEL",
        preferred=("gemini-flash-latest", "flash"),
        fallback="gemini-flash-lite-latest",
        include=("gemini", "gemma"),
        exclude=("embedding", "image", "banana", "tts", "audio", "transcribe", "live",
                 "computer-use", "robotics", "customtools"),
        # Overloaded models sometimes hang instead of returning 503; don't wait long.
        first_byte_timeout=20,
    ),
    "ollama": Provider(
        id="ollama",
        label="Ollama (local)",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
        key_env=None,
        model_env="OLLAMA_MODEL",
        preferred=("qwen", "gemma", "llama"),
        exclude=("embed",),
        first_byte_timeout=180,  # loading a model into a 4 GB GPU takes a while
    ),
}


class LLMError(Exception):
    """A problem worth showing to the learner in plain words."""

    def __init__(self, message: str, *, retryable: bool = False):
        super().__init__(message)
        self.retryable = retryable  # a different model might work right now


def is_configured(provider: Provider) -> bool:
    return provider.key_env is None or bool(os.getenv(provider.key_env))


def _url(provider: Provider, path: str) -> str:
    # Base URLs may or may not end in "/" (Gemini's does, Ollama's doesn't).
    return provider.base_url.rstrip("/") + "/" + path


def _headers(provider: Provider) -> dict[str, str]:
    if not is_configured(provider):
        raise LLMError(f"{provider.label}: add {provider.key_env} to your .env file and restart the app.")
    key = os.getenv(provider.key_env) if provider.key_env else "ollama"
    return {"Authorization": f"Bearer {key}"}


def _error_detail(body: bytes) -> str:
    try:
        data = json.loads(body)
    except ValueError:
        return body.decode(errors="replace")[:200]
    if isinstance(data, list) and data:  # Gemini wraps errors in a list
        data = data[0]
    err = data.get("error", data) if isinstance(data, dict) else data
    return (err.get("message") if isinstance(err, dict) else str(err)) or ""


def _status_error(provider: Provider, status: int, body: bytes) -> LLMError:
    detail = _error_detail(body)
    if status == 429:
        return LLMError(f"{provider.label}: free-tier limit reached for this model. "
                        "Wait a minute, or pick another model in settings.", retryable=True)
    if status in (500, 502, 503, 504):
        return LLMError(f"{provider.label} is overloaded right now (that's on their side). "
                        "Try again in a minute.", retryable=True)
    if status in (401, 403):
        return LLMError(f"{provider.label} rejected the API key. Check {provider.key_env} in your .env file.")
    if status == 404:
        return LLMError(f"{provider.label}: this model isn't available. Pick another one in settings. "
                        f"({detail})", retryable=True)
    return LLMError(f"{provider.label} error {status}: {detail}")


def _connection_error(provider: Provider, err: Exception) -> LLMError:
    if isinstance(err, httpx.TimeoutException):
        return LLMError(f"{provider.label} took too long to answer. Try again.", retryable=True)
    if provider.id == "ollama":
        return LLMError("Can't reach Ollama. Is it installed and running?")
    return LLMError(f"Can't reach {provider.label}. Check your internet connection.")


async def list_models(provider: Provider) -> list[str]:
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(_url(provider, "models"), headers=_headers(provider))
    except httpx.HTTPError as err:
        raise _connection_error(provider, err) from err
    if r.status_code >= 400:
        raise _status_error(provider, r.status_code, r.content)

    ids = sorted({m["id"].removeprefix("models/") for m in r.json().get("data", [])})
    return [
        m for m in ids
        if (not provider.include or m.startswith(provider.include))
        and not any(x in m for x in provider.exclude)
    ]


async def default_model(provider: Provider) -> str | None:
    if os.getenv(provider.model_env):
        return os.getenv(provider.model_env)
    models = await list_models(provider)
    for wanted in provider.preferred:
        if wanted in models:
            return wanted
        # Otherwise the newest-sorting stable match; previews can vanish without notice.
        stable = [m for m in models if wanted in m and "preview" not in m]
        if stable:
            return stable[-1]
    return models[0] if models else None


_THINK_TAG = "<think>"


def _visible(text: str) -> str:
    """Hide reasoning that models like DeepSeek-R1 put inside <think> tags."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    text = re.sub(r"<think>.*\Z", "", text, flags=re.S)  # still thinking
    for n in range(len(_THINK_TAG) - 1, 0, -1):  # don't show half of a tag yet
        if text.endswith(_THINK_TAG[:n]):
            return text[:-n]
    return text


_forced_thinking: dict[str, bool] = {}


async def _forces_thinking(provider: Provider, model: str) -> bool:
    """Some Ollama models (e.g. Qwen3 "Thinking" builds) open a <think> block in
    their prompt template, so the reply starts mid-reasoning and only contains
    the closing </think>. Ask Ollama once per model."""
    if provider.id != "ollama":
        return False
    if model not in _forced_thinking:
        root = provider.base_url.rstrip("/").removesuffix("/v1")
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                r = await client.post(f"{root}/api/show", json={"model": model})
            template = r.json().get("template", "") if r.status_code == 200 else ""
        except (httpx.HTTPError, ValueError):
            template = ""
        # e.g. "<|im_start|>assistant\n<think>\n{{ end }}": the reply is opened mid-thought.
        _forced_thinking[model] = bool(re.search(r"assistant\s*<think>\s*(\{\{|$)", template))
    return _forced_thinking[model]


def _tune_for_model(model: str, messages: list[dict]) -> list[dict]:
    # Qwen3 reasons step by step before answering unless told not to; on a
    # small local GPU that makes every reply slow for little gain in a chat.
    if "qwen3" in model and messages and messages[0]["role"] == "system":
        return [{**messages[0], "content": messages[0]["content"] + "\n/no_think"}, *messages[1:]]
    return messages


async def stream_chat(provider: Provider, model: str, messages: list[dict]) -> AsyncIterator[str]:
    """Yield the reply text piece by piece."""
    messages = _tune_for_model(model, messages)
    payload = {"model": model, "messages": messages, "stream": True, "temperature": 0.6}
    timeout = httpx.Timeout(connect=10, read=provider.first_byte_timeout, write=10, pool=10)
    thinking_first = await _forces_thinking(provider, model)
    raw, sent = "", 0
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream("POST", _url(provider, "chat/completions"),
                                     json=payload, headers=_headers(provider)) as r:
                if r.status_code >= 400:
                    raise _status_error(provider, r.status_code, await r.aread())
                async for line in r.aiter_lines():
                    if not line.startswith("data:"):
                        continue
                    data = line[5:].strip()
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    if "error" in chunk:
                        raise LLMError(f"{provider.label}: {_error_detail(data.encode())}")
                    choices = chunk.get("choices") or [{}]
                    piece = (choices[0].get("delta") or {}).get("content")
                    if not piece:
                        continue
                    raw += piece
                    if thinking_first:
                        # Everything before </think> is reasoning the learner shouldn't see.
                        if "</think>" not in raw:
                            continue
                        visible = _visible(raw.split("</think>", 1)[1]).lstrip()
                    else:
                        visible = _visible(raw).lstrip()
                    if len(visible) > sent:
                        yield visible[sent:]
                        sent = len(visible)
    except httpx.HTTPError as err:
        raise _connection_error(provider, err) from err
