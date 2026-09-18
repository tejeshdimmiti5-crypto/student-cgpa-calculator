from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentMessage:
    sender: str
    recipient: str
    message_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    correlation_id: str = ""

@dataclass
class AgentEnvelope:
    message: AgentMessage
    priority: int = 50
    attempt: int = 0
