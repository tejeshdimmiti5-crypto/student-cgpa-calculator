from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class MemoryItem:
    key: str
    value: Any
    memory_type: str = "working"
    importance: float = 0.5
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class MemoryStore:
    """In-memory abstraction designed to be backed by PostgreSQL + vector storage later."""

    def __init__(self) -> None:
        self.items: list[MemoryItem] = []

    def add(self, key: str, value: Any, memory_type: str = "episodic", importance: float = 0.5) -> MemoryItem:
        item = MemoryItem(key, value, memory_type, max(0.0, min(1.0, importance)))
        self.items.append(item)
        return item

    def search(self, query: str, limit: int = 5) -> list[MemoryItem]:
        terms = set(query.lower().split())
        scored = []
        for item in self.items:
            haystack = f"{item.key} {item.value}".lower()
            score = sum(term in haystack for term in terms) + item.importance
            if score:
                scored.append((score, item))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:limit]]
