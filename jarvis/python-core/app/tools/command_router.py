from dataclasses import dataclass
from typing import Any

@dataclass
class CommandIntent:
    tool: str
    arguments: dict[str, Any]
    confidence: float

class CommandRouter:
    """Maps structured intents to registered tools without allowing arbitrary execution."""

    ALIASES = {
        "system info": "system_info",
        "system status": "system_info",
        "machine status": "system_info",
    }

    def resolve(self, text: str) -> CommandIntent | None:
        normalized = " ".join(text.lower().strip().split())
        for phrase, tool in self.ALIASES.items():
            if phrase in normalized:
                return CommandIntent(tool, {}, 0.92)
        return None
