from app.agents.base import Agent, AgentResult
from app.tools.command_router import CommandRouter

class ToolAgent(Agent):
    name = "tool"

    def __init__(self, registry):
        self.registry = registry
        self.router = CommandRouter()

    def can_handle(self, command: str) -> bool:
        return self.router.resolve(command) is not None

    def run(self, command: str) -> AgentResult:
        intent = self.router.resolve(command)
        if intent is None:
            return AgentResult(self.name, "error", None, {"reason": "unknown intent"})
        output = self.registry.execute(intent.tool, **intent.arguments)
        status = "success" if not (isinstance(output, dict) and output.get("status") == "error") else "error"
        return AgentResult(self.name, status, output, {"tool": intent.tool, "confidence": intent.confidence})
