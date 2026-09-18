from app.agents.base import AgentResult
from app.agents.general import GeneralAgent
from app.agents.specialized import (
    CoderAgent,
    PlannerAgent,
    ResearchAgent,
    TesterAgent,
    ValidatorAgent,
)
from app.tools.builtin import register_builtin_tools
from app.tools.registry import AdvancedToolRegistry

class AgentRuntime:
    def __init__(self) -> None:
        self.tools = AdvancedToolRegistry()
        register_builtin_tools(self.tools)
        self.agents = [
            ResearchAgent(),
            CoderAgent(),
            TesterAgent(),
            ValidatorAgent(),
            PlannerAgent(),
            GeneralAgent(),
        ]

    def select_agent(self, command: str, preferred: str | None = None):
        if preferred:
            for agent in self.agents:
                if agent.name == preferred:
                    return agent
        for agent in self.agents:
            if agent.can_handle(command):
                return agent
        raise RuntimeError("No capable agent found")

    def execute(self, command: str, preferred: str | None = None) -> AgentResult:
        return self.select_agent(command, preferred).run(command)
