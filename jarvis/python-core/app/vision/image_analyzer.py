from pathlib import Path

class ImageAnalyzer:
    """Vision boundary for screenshots/images; model-specific inference plugs in here."""

    def inspect_file(self, path: str) -> dict:
        p = Path(path).expanduser().resolve()
        if not p.is_file():
            raise FileNotFoundError(str(p))
        if p.stat().st_size > 10_000_000:
            raise ValueError("Image exceeds 10 MB limit")
        return {
            "path": str(p),
            "size_bytes": p.stat().st_size,
            "mode": "vision-provider-required",
        }
