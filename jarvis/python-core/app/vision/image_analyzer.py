from pathlib import Path

class ImageAnalyzer:
    """Validated image input boundary with optional provider hook."""

    MAX_BYTES = 10_000_000
    ALLOWED = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

    def inspect_file(self, path: str) -> dict:
        p = Path(path).expanduser().resolve()
        if not p.is_file():
            raise FileNotFoundError(str(p))
        if p.suffix.lower() not in self.ALLOWED:
            raise ValueError("Unsupported image format")
        if p.stat().st_size > self.MAX_BYTES:
            raise ValueError("Image exceeds 10 MB limit")
        return {
            "status": "ready",
            "path": str(p),
            "size_bytes": p.stat().st_size,
            "mode": "provider-hook",
        }
