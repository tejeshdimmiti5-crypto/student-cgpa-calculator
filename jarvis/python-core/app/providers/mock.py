from app.providers.base import LLMProvider
from app.reasoning.models import ReasoningRequest, ReasoningPlan

class MockProvider(LLMProvider):
    name = "mock"

    def plan(self, request: ReasoningRequest) -> ReasoningPlan:
        return ReasoningPlan(
            goal=request.command,
            steps=[request.command] if request.command else [],
            confidence=0.50,
            metadata={"provider": self.name},
        )
