"""Thin wrapper around FSRS so the rest of the app never touches its internals."""

from datetime import datetime, timezone

from fsrs import Card, Rating, Scheduler, State

_scheduler = Scheduler(desired_retention=0.9)

# Answers slower than this count as "Hard": you knew it, but had to dig.
SLOW_ANSWER_MS = 6000


def new_card() -> Card:
    return Card(due=datetime.now(timezone.utc))


def rating_for(correct: bool, elapsed_ms: int | None) -> Rating:
    if not correct:
        return Rating.Again
    if elapsed_ms is not None and elapsed_ms > SLOW_ANSWER_MS:
        return Rating.Hard
    return Rating.Good


def review(card_json: str, rating: Rating, elapsed_ms: int | None = None) -> Card:
    card = Card.from_json(card_json)
    card, _log = _scheduler.review_card(card, rating, review_duration=elapsed_ms)
    return card


def to_row(card: Card) -> dict:
    """Columns we keep denormalized for querying."""
    return {
        "state": int(card.state),
        "stability": card.stability,
        "due_ts": card.due.timestamp(),
        "fsrs": card.to_json(),
    }


def status(state: int, stability: float | None) -> str:
    """Bucket a card for the progress chart."""
    if state != State.Review or stability is None:
        return "learning"
    if stability >= 21:
        return "mastered"
    return "known"
