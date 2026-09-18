from dataclasses import dataclass

@dataclass
class BrowserRequest:
    url: str
    action: str = "inspect"

class BrowserTool:
    """Browser boundary; actual Playwright integration can be enabled as a separate worker."""

    def open(self, url: str) -> dict:
        if not url.startswith(("https://", "http://")):
            return {"status": "error", "error": "Only HTTP(S) URLs are accepted"}
        return {"status": "browser_worker_required", "url": url}

    def inspect(self, url: str) -> dict:
        return self.open(url)
