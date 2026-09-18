from app.agents.base import AgentResult
from app.agents.general import GeneralAgent
from app.tools.builtin import register_builtin_tools
from app.tools.registry import AdvancedToolRegistry

class AgentRuntime:
    def __init__(self) -> None:
        self.tools = AdvancedToolRegistry()
        register_builtin_tools(self.tools)
        self.agents = [GeneralAgent()]

    def select_agent(self, command: str):
        for agent in self.agents:
            if agent.can_handle(command):
                return agent
        raise RuntimeError("No capable agent found")

    def execute(self, command: str) -> AgentResult:
        return self.select_agent(command).run(command)
