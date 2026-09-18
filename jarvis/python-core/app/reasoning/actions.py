from dataclasses import dataclass, field
from typing import Any, Literal

ActionKind = Literal["tool", "agent", "respond", "delegate"]

@dataclass
class Action:
    action_id: str
    kind: ActionKind
    target: str
    input: dict[str, Any] = field(default_factory=dict)
    dependencies: list[str] = field(default_factory=list)
    priority: int = 50
    requires_confirmation: bool = False

@dataclass
class ActionPlan:
    goal: str
    actions: list[Action]
    confidence: float
    rationale: str = ""
