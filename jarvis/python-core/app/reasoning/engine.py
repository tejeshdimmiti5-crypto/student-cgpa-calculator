from app.reasoning.models import ReasoningPlan, ReasoningRequest

class ReasoningEngine:
    """Deterministic reasoning contract; an LLM provider can implement this interface later."""

    def create_plan(self, request: ReasoningRequest) -> ReasoningPlan:
        command = request.command.strip()
        if not command:
            return ReasoningPlan(goal="", steps=[], confidence=1.0)
        return ReasoningPlan(
            goal=command,
            steps=[command],
            confidence=0.50,
            metadata={"engine": "deterministic-v1"},
        )
