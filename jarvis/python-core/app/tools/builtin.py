from app.tools.registry import AdvancedToolRegistry, Tool

def register_builtin_tools(registry: AdvancedToolRegistry) -> None:
    registry.register(Tool(
        name="system_info",
        description="Return safe basic runtime information.",
        handler=lambda: {"service": "JARVIS", "status": "online"},
    ))

    registry.register(Tool(
        name="shutdown",
        description="Shutdown JARVIS after explicit confirmation.",
        handler=lambda: {"status": "shutdown_requested"},
        requires_confirmation=True,
    ))
