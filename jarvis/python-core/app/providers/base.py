from abc import ABC, abstractmethod
from app.reasoning.models import ReasoningRequest, ReasoningPlan

class LLMProvider(ABC):
    name = "unknown"

    @abstractmethod
    def plan(self, request: ReasoningRequest) -> ReasoningPlan:
        ...
