from dataclasses import dataclass, field
from typing import Any, Literal

TaskStatus = Literal["pending", "running", "completed", "failed", "blocked", "cancelled"]

@dataclass
class TaskState:
    task_id: str
    status: TaskStatus = "pending"
    attempts: int = 0
    max_attempts: int = 3
    output: Any = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

class TaskStateStore:
    def __init__(self) -> None:
        self._states: dict[str, TaskState] = {}

    def create(self, task_id: str, max_attempts: int = 3) -> TaskState:
        state = TaskState(task_id=task_id, max_attempts=max_attempts)
        self._states[task_id] = state
        return state

    def get(self, task_id: str) -> TaskState:
        return self._states[task_id]

    def all(self) -> list[TaskState]:
        return list(self._states.values())
