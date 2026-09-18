from app.agents.base import Agent, AgentResult

class ResearchAgent(Agent):
    name = "research"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("research", "search", "find information"))
    def run(self, command: str) -> AgentResult:
        return AgentResult("success", {"agent": self.name, "query": command, "mode": "research-ready"})

class CoderAgent(Agent):
    name = "coder"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("code", "build", "create", "implement", "develop"))
    def run(self, command: str) -> AgentResult:
        return AgentResult("success", {"agent": self.name, "task": command, "mode": "coding-ready"})

class TesterAgent(Agent):
    name = "tester"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("test", "verify", "validate"))
    def run(self, command: str) -> AgentResult:
        return AgentResult("success", {"agent": self.name, "task": command, "mode": "test-ready"})

class ValidatorAgent(Agent):
    name = "validator"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("review", "validate", "verify"))
    def run(self, command: str) -> AgentResult:
        return AgentResult("success", {"agent": self.name, "task": command, "mode": "validation-ready"})

class PlannerAgent(Agent):
    name = "planner"
    def can_handle(self, command: str) -> bool:
        return True
    def run(self, command: str) -> AgentResult:
        return AgentResult("success", {"agent": self.name, "task": command, "mode": "planning-ready"})
