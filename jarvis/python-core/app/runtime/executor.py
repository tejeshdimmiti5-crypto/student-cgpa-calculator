from app.reasoning.actions import Action
from app.reasoning.reflection import ReflectionEngine
from app.runtime.recovery import RecoveryManager
from app.security.audit import AuditLog

class ActionExecutor:
    """Single execution boundary with confirmation, audit, reflection and bounded recovery."""

    def __init__(self, runtime, max_attempts: int = 2) -> None:
        self.runtime = runtime
        self.max_attempts = max(1, max_attempts)
        self.reflection = ReflectionEngine()
        self.recovery = RecoveryManager()
        self.audit = AuditLog()

    def execute(self, action: Action):
        if action.requires_confirmation:
            self.audit.record("confirmation_required", "jarvis", False, action=action.action_id)
            return {"status": "confirmation_required", "action": action.action_id}

        command = action.target if action.kind == "agent" else str(action.input.get("command", ""))
        attempt = 1
        while True:
            try:
                result = self.runtime.execute(command, preferred=action.target if action.kind == "agent" else None)
                output = result.output
                reflection = self.reflection.evaluate(output)
            except Exception as exc:
                output = {"status": "error", "error": f"{type(exc).__name__}: {exc}"}
                reflection = self.reflection.evaluate(output)

            self.audit.record(
                "action_completed",
                "jarvis",
                reflection.success,
                action=action.action_id,
                attempt=attempt,
                confidence=reflection.confidence,
            )

            decision = self.recovery.decide(attempt, self.max_attempts, reflection.retryable)
            if reflection.success or not decision.retry:
                return {
                    "status": "success" if reflection.success else "error",
                    "output": output,
                    "reflection": reflection.__dict__,
                    "attempts": attempt,
                }
            attempt = decision.attempt
