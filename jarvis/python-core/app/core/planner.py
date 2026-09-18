class Planner:
    """Initial deterministic planner; LLM planning will be plugged in here."""

    def create_plan(self, command: str) -> list[str]:
        command = command.strip()
        if not command:
            return []
        return [command]
