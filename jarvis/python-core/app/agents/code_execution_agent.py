from app.agents.base import Agent, AgentResult
from app.sandbox.code_executor import CodeExecutor

class CodeExecutionAgent(Agent):
    name = "code_execution"
    def __init__(self, tools):
        self.tools = tools
        self.sandbox = CodeExecutor()
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("run python", "execute python", "execute code"))
    def run(self, command: str) -> AgentResult:
        text = command.strip()
        marker = text.lower().find("run python")
        source = text[marker + len("run python"):].strip() if marker >= 0 else ""
        if not source:
            return AgentResult(self.name, "error", {"status":"error","error":"No Python source supplied."}, {})
        result = self.sandbox.run(source)
        return AgentResult(self.name, result.get("status","success"), result, {"sandbox":True})
