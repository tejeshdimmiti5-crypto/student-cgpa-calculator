import re
from app.agents.base import Agent, AgentResult
from app.tools.browser import BrowserTool

class BrowserAgent(Agent):
    name = "browser"
    def __init__(self):
        self.browser = BrowserTool()
    def can_handle(self, command: str) -> bool:
        text = command.lower()
        return any(x in text for x in ("open website", "browse", "web page", "url", "visit "))
    def run(self, command: str) -> AgentResult:
        urls = re.findall(r"https?://[^\s]+", command)
        if not urls:
            return AgentResult(self.name, "error", {"status":"error","error":"Provide an HTTP(S) URL."}, {})
        result = self.browser.inspect(urls[0].rstrip(".,)"))
        return AgentResult(self.name, result.get("status","success"), result, {"browser":"playwright"})
