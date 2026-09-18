from pathlib import Path

def read_text_file(path: str):
    p=Path(path).expanduser().resolve()
    if not p.is_file(): raise FileNotFoundError(str(p))
    if p.stat().st_size > 2_000_000: raise ValueError("File exceeds safe 2 MB limit")
    return {"path":str(p), "content":p.read_text(encoding="utf-8")}

def register_file_tools(registry):
    from app.tools.registry import Tool
    registry.register(Tool("read_text_file", "Read a text file under the execution boundary", read_text_file))
