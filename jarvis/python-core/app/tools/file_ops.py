from pathlib import Path

class SafeFileTools:
    """File operations constrained to explicitly configured workspace roots."""

    def __init__(self, roots: list[str] | None = None) -> None:
        self.roots = [Path(x).expanduser().resolve() for x in (roots or ["."])]

    def _safe(self, path: str) -> Path:
        target = Path(path).expanduser().resolve()
        if not any(target == root or root in target.parents for root in self.roots):
            raise PermissionError("Path is outside the JARVIS workspace")
        return target

    def list_files(self, path: str = ".") -> dict:
        target = self._safe(path)
        return {"path": str(target), "files": [p.name for p in target.iterdir()]}

    def read(self, path: str) -> dict:
        target = self._safe(path)
        if not target.is_file():
            raise FileNotFoundError(str(target))
        if target.stat().st_size > 2_000_000:
            raise ValueError("File exceeds 2 MB limit")
        return {"path": str(target), "content": target.read_text(encoding="utf-8")}
