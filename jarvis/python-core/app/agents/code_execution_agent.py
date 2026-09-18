from app.agents.base import Agent, AgentResult

class CodeExecutionAgent(Agent):
    name = "code_execution"
    def __init__(self, tools):
        self.tools = tools

    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("run python", "execute python", "execute code"))

    def run(self, command: str) -> AgentResult:
        return AgentResult(
            agent=self.name,
            status="success",
            output={"status": "execution-agent-ready", "command": command},
            metadata={"sandbox": True},
        )
