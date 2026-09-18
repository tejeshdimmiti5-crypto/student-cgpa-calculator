from dataclasses import dataclass, field

@dataclass
class TaskNode:
    task_id: str
    dependencies: set[str] = field(default_factory=set)

class TaskGraph:
    """Dependency graph foundation for multi-step JARVIS tasks."""

    def __init__(self) -> None:
        self.nodes: dict[str, TaskNode] = {}

    def add_task(self, task_id: str, dependencies: set[str] | None = None) -> None:
        self.nodes[task_id] = TaskNode(task_id, dependencies or set())

    def ready_tasks(self, completed: set[str]) -> list[str]:
        return [
            node.task_id
            for node in self.nodes.values()
            if node.task_id not in completed and node.dependencies <= completed
        ]
