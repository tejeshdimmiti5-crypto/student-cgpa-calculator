from app.providers.base import LLMProvider
from app.reasoning.models import ReasoningPlan, ReasoningRequest

class LLMReasoningEngine:
    """Provider-backed reasoning with deterministic fallback for reliability."""

    def __init__(self, provider: LLMProvider, fallback) -> None:
        self.provider = provider
        self.fallback = fallback

    def create_plan(self, request: ReasoningRequest) -> ReasoningPlan:
        try:
            plan = self.provider.plan(request)
            if plan.steps:
                return plan
        except Exception as exc:
            fallback = self.fallback.create_plan(request)
            fallback.metadata["llm_error"] = type(exc).__name__
            return fallback
        return self.fallback.create_plan(request)
