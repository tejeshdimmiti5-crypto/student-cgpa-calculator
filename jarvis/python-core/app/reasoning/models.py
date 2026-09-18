from dataclasses import dataclass, field
from typing import Any

@dataclass
class ReasoningRequest:
    command: str
    context: dict[str, Any] = field(default_factory=dict)

@dataclass
class ReasoningPlan:
    goal: str
    steps: list[str]
    confidence: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class CognitiveDecision:
    intent: str
    agent: str | None
    tool: str | None
    requires_confirmation: bool
    confidence: float
    rationale: str = ""
