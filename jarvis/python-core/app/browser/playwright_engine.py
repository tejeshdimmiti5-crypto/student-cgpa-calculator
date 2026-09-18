class PlaywrightEngine:
    """Optional browser worker using Playwright; disabled until dependency is installed."""

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser = None
        self.playwright = None

    async def start(self):
        from playwright.async_api import async_playwright
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.headless)
        return self

    async def inspect(self, url: str) -> dict:
        if self.browser is None:
            await self.start()
        page = await self.browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=15000)
        title = await page.title()
        text = await page.locator("body").inner_text(timeout=5000)
        await page.close()
        return {"url": url, "title": title, "text": text[:20000]}

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
