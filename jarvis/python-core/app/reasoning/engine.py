import os

from app.reasoning.models import ReasoningPlan, ReasoningRequest
from app.providers.mock import MockProvider
from app.reasoning.llm_engine import LLMReasoningEngine

class ReasoningEngine:
    """Provider-aware cognitive planner with safe deterministic fallback."""

    def __init__(self) -> None:
        fallback = DeterministicReasoningEngine()
        provider_name = os.getenv("JARVIS_LLM_PROVIDER", "mock").lower()

        if provider_name == "gemini":
            try:
                from app.providers.gemini import GeminiProvider
                provider = GeminiProvider()
            except Exception:
                provider = MockProvider()
        else:
            provider = MockProvider()

        self._engine = LLMReasoningEngine(provider, fallback)

    def create_plan(self, request: ReasoningRequest) -> ReasoningPlan:
        return self._engine.create_plan(request)

class DeterministicReasoningEngine:
    def create_plan(self, request: ReasoningRequest) -> ReasoningPlan:
        command = request.command.strip()
        if not command:
            return ReasoningPlan(goal="", steps=[], confidence=1.0)
        return ReasoningPlan(
            goal=command,
            steps=[command],
            confidence=0.50,
            metadata={"engine": "deterministic-v2"},
        )
