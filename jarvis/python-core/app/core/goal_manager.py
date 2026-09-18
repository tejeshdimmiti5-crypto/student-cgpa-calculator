from dataclasses import dataclass, field
from typing import Any

@dataclass
class Goal:
    goal_id: str
    description: str
    status: str = "active"
    progress: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

class GoalManager:
    def __init__(self) -> None:
        self.goals: dict[str, Goal] = {}

    def create(self, goal_id: str, description: str) -> Goal:
        goal = Goal(goal_id, description)
        self.goals[goal_id] = goal
        return goal

    def update_progress(self, goal_id: str, progress: float) -> Goal:
        goal = self.goals[goal_id]
        goal.progress = max(0.0, min(1.0, progress))
        if goal.progress >= 1.0:
            goal.status = "completed"
        return goal
