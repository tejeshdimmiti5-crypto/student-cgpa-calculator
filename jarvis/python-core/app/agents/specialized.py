from app.agents.base import Agent, AgentResult

def result(agent: str, command: str, mode: str) -> AgentResult:
    return AgentResult(agent=agent, status="success", output={"agent": agent, "task": command, "mode": mode}, metadata={"mode": mode})

class ResearchAgent(Agent):
    name = "research"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("research", "search", "find information"))
    def run(self, command: str) -> AgentResult:
        return result(self.name, command, "research-ready")

class CoderAgent(Agent):
    name = "coder"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("code", "build", "create", "implement", "develop"))
    def run(self, command: str) -> AgentResult:
        return result(self.name, command, "coding-ready")

class TesterAgent(Agent):
    name = "tester"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("test", "verify", "validate"))
    def run(self, command: str) -> AgentResult:
        return result(self.name, command, "test-ready")

class ValidatorAgent(Agent):
    name = "validator"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("review", "validate", "verify"))
    def run(self, command: str) -> AgentResult:
        return result(self.name, command, "validation-ready")

class PlannerAgent(Agent):
    name = "planner"
    def can_handle(self, command: str) -> bool:
        return True
    def run(self, command: str) -> AgentResult:
        return result(self.name, command, "planning-ready")
