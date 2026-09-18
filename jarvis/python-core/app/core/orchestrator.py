from app.core.planner import Planner
from app.core.tool_registry import ToolRegistry
from app.memory.memory import Memory
from app.tasks.graph import TaskGraph

class JarvisOrchestrator:
    """Coordinates planning, tools, tasks and memory."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.tools = ToolRegistry()
        self.memory = Memory()
        self.task_graph = TaskGraph()

    def handle(self, command: str) -> str:
        self.memory.remember("last_command", command)
        plan = self.planner.create_plan(command)
        return self._execute(plan)

    def _execute(self, plan: list[str]) -> str:
        results = []
        for step in plan:
            tool = self.tools.resolve(step)
            results.append(tool(step) if tool else f"Planned: {step}")
        return "\n".join(results)
