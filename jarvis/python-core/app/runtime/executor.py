from app.reasoning.actions import Action
from app.reasoning.reflection import ReflectionEngine
from app.security.audit import AuditLog

class ActionExecutor:
    """Central action execution boundary. Sensitive actions are never silently executed."""

    def __init__(self, runtime) -> None:
        self.runtime = runtime
        self.reflection = ReflectionEngine()
        self.audit = AuditLog()

    def execute(self, action: Action):
        if action.requires_confirmation:
            self.audit.record("confirmation_required", "jarvis", False, action=action.action_id)
            return {"status": "confirmation_required", "action": action.action_id}

        result = self.runtime.execute(action.target if action.kind == "agent" else str(action.input.get("command", "")))
        output = result.output
        reflection = self.reflection.evaluate(output)
        self.audit.record(
            "action_completed",
            "jarvis",
            reflection.success,
            action=action.action_id,
            confidence=reflection.confidence,
        )
        return {"status": result.status, "output": output, "reflection": reflection.__dict__}
