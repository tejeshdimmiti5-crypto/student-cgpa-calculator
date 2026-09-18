from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class AgentResult:
    agent: str
    status: str
    output: Any
    metadata: dict[str, Any]

class Agent(ABC):
    name: str = "agent"

    @abstractmethod
    def can_handle(self, command: str) -> bool:
        ...

    @abstractmethod
    def run(self, command: str) -> AgentResult:
        ...
