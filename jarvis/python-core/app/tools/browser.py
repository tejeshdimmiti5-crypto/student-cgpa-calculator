from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class BrowserRequest:
    url: str
    action: str = "inspect"

class BrowserTool:
    """Safe browser facade backed by Playwright when available."""

    def __init__(self, headless: bool = True):
        self.headless = headless

    @staticmethod
    def _validate(url: str) -> str:
        parsed = urlparse(url.strip())
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Only valid HTTP(S) URLs are accepted")
        return url.strip()

    def open(self, url: str) -> dict:
        url = self._validate(url)
        try:
            import asyncio
            from app.browser.playwright_engine import PlaywrightEngine
            return asyncio.run(self._inspect(url))
        except Exception as exc:
            return {"status": "error", "error": f"Browser unavailable: {type(exc).__name__}: {exc}", "url": url}

    async def _inspect(self, url: str) -> dict:
        from app.browser.playwright_engine import PlaywrightEngine
        engine = PlaywrightEngine(headless=self.headless)
        try:
            result = await engine.inspect(url)
            return {"status": "success", **result}
        finally:
            await engine.close()

    def inspect(self, url: str) -> dict:
        return self.open(url)
