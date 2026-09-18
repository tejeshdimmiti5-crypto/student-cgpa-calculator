from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

@dataclass(frozen=True)
class Event:
    topic: str
    payload: dict[str, Any]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class EventBus:
    """In-process event bus with optional per-command sinks."""
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Event], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[Event], None]) -> None:
        self._subscribers.setdefault(topic, []).append(handler)

    def publish(self, event: Event, sink: Callable[[Event], None] | None = None) -> None:
        for handler in self._subscribers.get(event.topic, []):
            handler(event)
        if sink:
            sink(event)
