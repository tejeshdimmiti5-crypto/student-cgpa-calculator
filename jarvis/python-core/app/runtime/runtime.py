from app.agents.base import AgentResult
from app.agents.general import GeneralAgent
from app.agents.specialized import CoderAgent, PlannerAgent, ResearchAgent, TesterAgent, ValidatorAgent
from app.agents.browser_agent import BrowserAgent
from app.agents.vision_agent import VisionAgent
from app.agents.computer_agent import ComputerAgent
from app.agents.code_execution_agent import CodeExecutionAgent
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.tool_agent import ToolAgent
from app.tools.builtin import register_builtin_tools
from app.tools.all_tools import register_all_tools
from app.tools.registry import AdvancedToolRegistry

class AgentRuntime:
    """Multi-agent runtime with a single registered tool fabric."""
    def __init__(self) -> None:
        self.tools = AdvancedToolRegistry()
        register_builtin_tools(self.tools)
        register_all_tools(self.tools)
        self.agents = [
            PlannerAgent(), ResearchAgent(), CoderAgent(), TesterAgent(), ValidatorAgent(),
            BrowserAgent(), VisionAgent(), ComputerAgent(),
            CodeExecutionAgent(self.tools), ToolAgent(self.tools),
            GeneralAgent(), OrchestratorAgent(),
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

    def agent_status(self) -> list[dict[str, str]]:
        return [
            {"name": agent.name, "status": "ready"}
            for agent in self.agents
        ]

    def tool_status(self) -> list[dict[str, str | bool]]:
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "requires_confirmation": tool.requires_confirmation,
            }
            for tool in self.tools.list_tools()
        ]
