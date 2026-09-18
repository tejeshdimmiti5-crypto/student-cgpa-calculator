from app.core.planner import Planner
from app.memory.memory import Memory
from app.tasks.graph import TaskGraph
from app.tasks.scheduler import PriorityScheduler
from app.runtime.runtime import AgentRuntime
from app.events.bus import Event, EventBus
from app.security.policy import SecurityPolicy

class JarvisOrchestrator:
    """Coordinates planning, scheduling, agents, tools, events and security."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.memory = Memory()
        self.task_graph = TaskGraph()
        self.scheduler = PriorityScheduler()
        self.runtime = AgentRuntime()
        self.events = EventBus()
        self.security = SecurityPolicy()

    def handle(self, command: str) -> str:
        self.memory.remember("last_command", command)
        self.events.publish(Event("jarvis.command.received", {"command": command}))
        plan = self.planner.create_plan(command)

        for index, step in enumerate(plan):
            task_id = f"task-{index + 1}"
            self.scheduler.submit(task_id, step, priority=50)

        task = self.scheduler.next_task()
        if task is None:
            return "No executable task."

        result = self.runtime.execute(task.command)
        self.events.publish(Event("jarvis.task.completed", {
            "task_id": task.task_id,
            "status": result.status,
        }))
        return str(result.output)
