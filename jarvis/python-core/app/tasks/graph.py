from dataclasses import dataclass, field
from collections import deque

@dataclass
class TaskNode:
    task_id: str
    dependencies: set[str] = field(default_factory=set)

class TaskGraph:
    """Dependency DAG with cycle detection and topological traversal."""
    def __init__(self) -> None:
        self.nodes: dict[str, TaskNode] = {}

    def add_task(self, task_id: str, dependencies: set[str] | None = None) -> None:
        deps = dependencies or set()
        unknown = deps - self.nodes.keys()
        if unknown:
            # Dependencies may be added later; validation happens before execution.
            pass
        self.nodes[task_id] = TaskNode(task_id, deps)

    def validate(self) -> None:
        for node in self.nodes.values():
            missing = node.dependencies - self.nodes.keys()
            if missing:
                raise ValueError(f"Unknown dependencies for {node.task_id}: {sorted(missing)}")
        indegree = {k: 0 for k in self.nodes}
        children = {k: [] for k in self.nodes}
        for node in self.nodes.values():
            for dep in node.dependencies:
                indegree[node.task_id] += 1
                children[dep].append(node.task_id)
        q = deque(k for k,v in indegree.items() if v == 0)
        seen = 0
        while q:
            current=q.popleft(); seen+=1
            for child in children[current]:
                indegree[child]-=1
                if indegree[child]==0: q.append(child)
        if seen != len(self.nodes):
            raise ValueError("Task graph contains a dependency cycle.")

    def ready_tasks(self, completed: set[str]) -> list[str]:
        return [n.task_id for n in self.nodes.values()
                if n.task_id not in completed and n.dependencies <= completed]

    def topological_order(self) -> list[str]:
        self.validate()
        indegree={k:len(v.dependencies) for k,v in self.nodes.items()}
        children={k:[] for k in self.nodes}
        for n in self.nodes.values():
            for d in n.dependencies: children[d].append(n.task_id)
        q=deque(k for k,v in indegree.items() if v==0)
        order=[]
        while q:
            x=q.popleft(); order.append(x)
            for c in children[x]:
                indegree[c]-=1
                if indegree[c]==0:q.append(c)
        return order
