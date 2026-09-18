from app.core.planner import Planner
from app.memory.memory import Memory
from app.memory.store import MemoryStore
from app.tasks.graph import TaskGraph
from app.tasks.scheduler import PriorityScheduler
from app.runtime.runtime import AgentRuntime
from app.runtime.executor import ActionExecutor
from app.events.bus import Event, EventBus
from app.security.policy import SecurityPolicy
from app.perception.engine import PerceptionEngine
from app.perception.models import PerceptionInput
from app.reasoning.engine import ReasoningEngine
from app.reasoning.models import ReasoningRequest
from app.reasoning.dag_planner import DAGPlanner

class JarvisOrchestrator:
    """Cognitive coordinator for perception, planning, DAG execution, reflection and memory."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.memory = Memory()
        self.long_term_memory = MemoryStore()
        self.task_graph = TaskGraph()
        self.scheduler = PriorityScheduler()
        self.runtime = AgentRuntime()
        self.executor = ActionExecutor(self.runtime)
        self.events = EventBus()
        self.security = SecurityPolicy()
        self.perception = PerceptionEngine()
        self.reasoning = ReasoningEngine()
        self.dag_planner = DAGPlanner()

    def handle(self, command: str, event_sink=None) -> str:
        perception = self.perception.process(
            PerceptionInput(source="cli", content=command, modality="text")
        )
        normalized = perception.normalized_text or ""
        if not normalized:
            return "I need a command, sir."

        self.memory.remember("last_command", normalized)
        self.long_term_memory.add("command", normalized, "episodic", 0.6)
        self.events.publish(Event("jarvis.command.received", {"command": normalized}), event_sink)

        reasoning = self.reasoning.create_plan(
            ReasoningRequest(
                command=normalized,
                context={"working_memory": self.memory.recall("last_command")},
            )
        )
        action_plan = self.dag_planner.build(normalized)
        self.events.publish(Event("jarvis.plan.created", {
            "goal": action_plan.goal,
            "actions": len(action_plan.actions),
            "confidence": action_plan.confidence,
        }))

        self.task_graph = TaskGraph()
        for action in action_plan.actions:
            self.task_graph.add_task(action.action_id, set(action.dependencies))
            self.scheduler.submit(
                action.action_id,
                action.target,
                priority=action.priority,
            )

        completed: set[str] = set()
        outputs: dict[str, object] = {}
        action_map = {a.action_id: a for a in action_plan.actions}

        while True:
            ready = self.task_graph.ready_tasks(completed)
            if not ready:
                break
            for task_id in ready:
                action = action_map[task_id]
                if action.kind == "respond":
                    output = {
                        "status": "success",
                        "message": "Task graph completed.",
                        "goal": action_plan.goal,
                        "completed_actions": list(completed),
                        "confidence": action_plan.confidence,
                    }
                elif action.kind == "delegate" and action.target == "security":
                    output = {
                        "status": "confirmation_required",
                        "message": "This action requires explicit confirmation.",
                    }
                else:
                    preferred = action.target if action.kind == "agent" else None
                    result = self.runtime.execute(normalized, preferred)
                    output = result.output
                self.events.publish(Event("jarvis.action.started", {\n                    "action_id": task_id, "kind": action.kind, "target": action.target,\n                }), event_sink)\n                outputs[task_id] = output
                completed.add(task_id)
                self.events.publish(Event("jarvis.action.completed", {
                    "action_id": task_id,
                    "completed": len(completed),
                    "total": len(action_plan.actions),
                }))

        self.long_term_memory.add(
            "execution",
            {"goal": normalized, "outputs": outputs},
            "episodic",
            0.7,
        )
        self.events.publish(Event("jarvis.task.completed", {
            "goal": normalized,
            "actions_completed": len(completed),
            "confidence": action_plan.confidence,
        }))

        if any(isinstance(v, dict) and v.get("status") == "confirmation_required" for v in outputs.values()):
            return "Confirmation required before I can perform that action."

        return (
            f"JARVIS plan completed: {len(completed)}/{len(action_plan.actions)} actions. "
            f"Confidence: {action_plan.confidence:.2f}"
        )
