from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class AuditEvent:
    event: str
    actor: str
    allowed: bool
    details: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class AuditLog:
    def __init__(self) -> None:
        self.events: list[AuditEvent] = []

    def record(self, event: str, actor: str, allowed: bool, **details: Any) -> AuditEvent:
        item = AuditEvent(event, actor, allowed, details)
        self.events.append(item)
        return item

    def recent(self, limit: int = 20) -> list[AuditEvent]:
        return self.events[-limit:]
