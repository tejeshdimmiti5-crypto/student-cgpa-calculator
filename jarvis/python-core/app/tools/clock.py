from datetime import datetime, timezone

def current_time():
    return {"utc": datetime.now(timezone.utc).isoformat()}

def register_clock(registry):
    from app.tools.registry import Tool
    registry.register(Tool("current_time", "Get current UTC time", current_time))
