from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

ToolHandler = Callable[..., Any]

@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: ToolHandler
    requires_confirmation: bool = False

class AdvancedToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list_tools(self) -> list[Tool]:
        return list(self._tools.values())

    def execute(self, name: str, *args: Any, confirmed: bool = False, **kwargs: Any) -> Any:
        tool = self.get(name)
        if tool is None:
            raise KeyError(f"Unknown tool: {name}")
        if tool.requires_confirmation and not confirmed:
            return {"status": "confirmation_required", "tool": name}
        return tool.handler(*args, **kwargs)
