from src.mcp_server import Tool
from typing import Dict, Any
from playwright.async_api import async_playwright

class BrowserTool(Tool):
    def __init__(self):
        super().__init__(
            name="browser",
            description="Browser automation tool for web interactions"
        )
        self.browser = None
        
    async def setup(self):
        if not self.browser:
            playwright = await async_playwright().start()
            self.browser = await playwright.chromium.launch()
    
    async def execute(self, params: Dict[str, Any]) -> Any:
        await self.setup()
        
        action = params.get("action")
        url = params.get("url")
        
        if not action or not url:
            raise ValueError("Action and URL are required")
            
        page = await self.browser.new_page()
        
        try:
            if action == "navigate":
                await page.goto(url)
                return {"status": "success", "title": await page.title()}
            elif action == "screenshot":
                await page.goto(url)
                screenshot = await page.screenshot()
                return {"status": "success", "screenshot": screenshot}
            else:
                raise ValueError(f"Unsupported action: {action}")
        finally:
            await page.close()
