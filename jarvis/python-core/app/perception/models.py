from dataclasses import dataclass
from typing import Any

@dataclass
class PerceptionInput:
    source: str
    content: Any
    modality: str = "text"

@dataclass
class PerceptionResult:
    modality: str
    normalized_text: str | None
    metadata: dict[str, Any]
