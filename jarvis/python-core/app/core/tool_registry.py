from collections.abc import Callable

Tool = Callable[[str], str]

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, name: str, tool: Tool) -> None:
        self._tools[name] = tool

    def resolve(self, step: str) -> Tool | None:
        for name, tool in self._tools.items():
            if name.lower() in step.lower():
                return tool
        return None
