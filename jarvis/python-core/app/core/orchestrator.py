from app.core.planner import Planner
from app.memory.memory import Memory
from app.tasks.graph import TaskGraph
from app.tasks.scheduler import PriorityScheduler
from app.runtime.runtime import AgentRuntime
from app.events.bus import Event, EventBus
from app.security.policy import SecurityPolicy
from app.perception.engine import PerceptionEngine
from app.perception.models import PerceptionInput
from app.reasoning.engine import ReasoningEngine
from app.reasoning.models import ReasoningRequest

class JarvisOrchestrator:
    """Coordinates perception, reasoning, planning, scheduling, agents, events and security."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.memory = Memory()
        self.task_graph = TaskGraph()
        self.scheduler = PriorityScheduler()
        self.runtime = AgentRuntime()
        self.events = EventBus()
        self.security = SecurityPolicy()
        self.perception = PerceptionEngine()
        self.reasoning = ReasoningEngine()

    def handle(self, command: str) -> str:
        perception = self.perception.process(
            PerceptionInput(source="cli", content=command, modality="text")
        )
        normalized = perception.normalized_text or ""
        self.memory.remember("last_command", normalized)
        self.events.publish(Event("jarvis.command.received", {"command": normalized}))

        reasoning = self.reasoning.create_plan(
            ReasoningRequest(
                command=normalized,
                context={"memory": self.memory.recall("last_command")},
            )
        )

        plan = reasoning.steps or self.planner.create_plan(normalized)
        for index, step in enumerate(plan):
            self.scheduler.submit(f"task-{index + 1}", step, priority=50)

        task = self.scheduler.next_task()
        if task is None:
            return "No executable task."

        result = self.runtime.execute(task.command)
        self.events.publish(Event("jarvis.task.completed", {
            "task_id": task.task_id,
            "status": result.status,
            "confidence": reasoning.confidence,
        }))
        return str(result.output)
