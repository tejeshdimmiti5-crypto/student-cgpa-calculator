from app.memory.memory import Memory
from app.memory.persistent import PersistentMemory
from app.memory.temporal import TemporalMemoryIndex
from app.memory.graph import MemoryGraph
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
from app.reasoning.cognitive_loop import CognitiveLoop
from app.memory.semantic import SemanticMemory

class JarvisOrchestrator:
    """Cognitive coordinator for perception, reasoning, memory, planning and safe execution."""

    def __init__(self) -> None:
        self.memory = Memory()
        self.long_term_memory = PersistentMemory()
        self.temporal_memory = TemporalMemoryIndex()
        self.memory_graph = MemoryGraph()
        self.task_graph = TaskGraph()
        self.scheduler = PriorityScheduler()
        self.runtime = AgentRuntime()
        self.executor = ActionExecutor(self.runtime)
        self.events = EventBus()
        self.security = SecurityPolicy()
        self.perception = PerceptionEngine()
        self.reasoning = ReasoningEngine()
        self.dag_planner = DAGPlanner()
        self.cognitive_loop = CognitiveLoop(self)
        self.semantic_memory = SemanticMemory()

    def _memory_context(self, query: str) -> dict:
        episodic = self.long_term_memory.search(query, limit=5)
        recent = self.temporal_memory.recent(limit=5)
        return {
            "episodic": [{"key": x.key, "value": x.value, "importance": x.importance} for x in episodic],
            "recent": [{"key": x.key, "value": x.value, "timestamp": x.timestamp.isoformat()} for x in recent],
            "knowledge_graph": self.memory_graph.to_context("jarvis", max_hops=2),
            "semantic": self.semantic_memory.recall(query, limit=5),
        }

    def handle(self, command: str, event_sink=None) -> str:
        perception = self.perception.process(PerceptionInput(source="cli", content=command, modality="text"))
        normalized = perception.normalized_text or ""
        if not normalized:
            return "I need a command, sir."

        self.memory.remember("last_command", normalized)
        self.semantic_memory.remember("command", normalized, memory_type="episodic")
        self.long_term_memory.add("command", normalized, "episodic", 0.6)
        self.temporal_memory.add("command", normalized, 0.6)
        self.events.publish(Event("jarvis.command.received", {"command": normalized}), event_sink)

        context = self._memory_context(normalized)
        reasoning = self.reasoning.create_plan(
            ReasoningRequest(command=normalized, context={
                "working_memory": self.memory.recall("last_command"),
                "memory": context,
            })
        )
        action_plan = self.dag_planner.build(normalized)
        decision = self.cognitive_loop.run(normalized, reasoning)
        self.events.publish(Event("jarvis.plan.created", {
            "goal": action_plan.goal,
            "actions": len(action_plan.actions),
            "confidence": action_plan.confidence,
            "reasoning_steps": len(reasoning.steps),
                    "decision": decision.intent,
                    "decision_agent": decision.agent,
        }), event_sink)

        if not action_plan.actions:
            return "I could not create an executable plan for that command."

        self.task_graph = TaskGraph()
        self.scheduler = PriorityScheduler()
        action_map = {a.action_id: a for a in action_plan.actions}
        for action in action_plan.actions:
            self.task_graph.add_task(action.action_id, set(action.dependencies))
        self.task_graph.validate()

        completed: set[str] = set()
        outputs: dict[str, object] = {}

        while len(completed) < len(action_map):
            ready = set(self.task_graph.ready_tasks(completed)) - completed
            if not ready:
                raise RuntimeError("Task graph made no progress; dependency cycle or invalid plan.")

            self.scheduler.clear()
            for task_id in ready:
                action = action_map[task_id]
                self.scheduler.submit(task_id, action.target, priority=action.priority)

            for item in self.scheduler.drain_ready(ready):
                action = action_map[item.task_id]
                self.events.publish(Event("jarvis.action.started", {
                    "action_id": item.task_id, "kind": action.kind, "target": action.target,
                }), event_sink)

                if action.kind == "respond":
                    prior = {k: v for k, v in outputs.items() if k != action.action_id}
                    output = {
                        "status": "success",
                        "message": "Task graph completed.",
                        "goal": action_plan.goal,
                        "prior_outputs": prior,
                        "confidence": action_plan.confidence,
                    }
                elif action.kind == "delegate" and action.target == "security":
                    output = {"status": "confirmation_required", "message": "Explicit confirmation is required."}
                    self.events.publish(Event("jarvis.security.blocked", {
                        "action_id": item.task_id, "reason": "explicit confirmation required",
                    }), event_sink)
                else:
                    output = self.executor.execute(action)

                outputs[item.task_id] = output
                completed.add(item.task_id)
                self.events.publish(Event("jarvis.action.completed", {
                    "action_id": item.task_id, "completed": len(completed),
                    "total": len(action_plan.actions),
                }), event_sink)

        self.long_term_memory.add("execution", {"goal": normalized, "outputs": outputs}, "episodic", 0.7)
        self.temporal_memory.add("execution", {"goal": normalized, "outputs": outputs}, 0.7)
        self.memory_graph.link("jarvis", "completed", normalized, confidence=action_plan.confidence)
        self.events.publish(Event("jarvis.task.completed", {
            "goal": normalized, "actions_completed": len(completed),
            "confidence": action_plan.confidence,
        }), event_sink)

        if any(isinstance(v, dict) and v.get("status") == "confirmation_required" for v in outputs.values()):
            return "Confirmation required before I can perform that action."

        return f"JARVIS plan completed: {len(completed)}/{len(action_plan.actions)} actions. Confidence: {action_plan.confidence:.2f}"
