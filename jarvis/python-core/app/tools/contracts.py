from dataclasses import dataclass, field
from typing import Any

@dataclass
class ToolCall:
    call_id: str
    tool: str
    arguments: dict[str, Any] = field(default_factory=dict)
    confirmed: bool = False

@dataclass
class ToolResult:
    call_id: str
    tool: str
    status: str
    output: Any = None
    error: str | None = None
