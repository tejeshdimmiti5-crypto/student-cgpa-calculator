import os, platform, shutil

def get_system_status():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count(),
        "disk_free_gb": round(shutil.disk_usage(os.getcwd()).free / 1024**3, 2),
    }

def register_system_tools(registry):
    from app.tools.registry import Tool
    registry.register(Tool("system_status", "Read safe system status", get_system_status))
