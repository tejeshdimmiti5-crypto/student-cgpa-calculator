from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class TemporalMemory:
    key: str
    value: Any
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    importance: float = 0.5

class TemporalMemoryIndex:
    """Time-aware memory index for recent and historical JARVIS context."""
    def __init__(self):
        self.items: list[TemporalMemory] = []

    def add(self,key,value,importance=.5):
        item=TemporalMemory(key,value,datetime.now(timezone.utc),max(0,min(1,importance)))
        self.items.append(item)
        return item

    def recent(self, limit=10):
        return sorted(self.items,key=lambda x:x.timestamp,reverse=True)[:limit]

    def between(self,start,end):
        return [x for x in self.items if start <= x.timestamp <= end]
