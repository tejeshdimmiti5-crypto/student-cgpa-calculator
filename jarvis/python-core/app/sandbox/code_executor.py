import subprocess
import sys
import tempfile
from pathlib import Path

class CodeSandbox:
    """Restricted, time-bounded Python execution for generated snippets."""

    def __init__(self, timeout_seconds: int = 5) -> None:
        self.timeout_seconds = timeout_seconds

    def run_python(self, code: str) -> dict:
        if len(code) > 20_000:
            return {"status": "error", "error": "Code exceeds sandbox size limit"}
        with tempfile.TemporaryDirectory(prefix="jarvis-sandbox-") as tmp:
            path = Path(tmp) / "main.py"
            path.write_text(code, encoding="utf-8")
            try:
                completed = subprocess.run(
                    [sys.executable, str(path)],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout_seconds,
                    cwd=tmp,
                    check=False,
                )
                return {
                    "status": "success" if completed.returncode == 0 else "error",
                    "returncode": completed.returncode,
                    "stdout": completed.stdout[-10_000:],
                    "stderr": completed.stderr[-10_000:],
                }
            except subprocess.TimeoutExpired:
                return {"status": "error", "error": "Sandbox execution timed out"}
