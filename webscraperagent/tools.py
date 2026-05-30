from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
import asyncio


def get_playwright_tools():
    """Initialize async playwright browser and return tools.
    Must be called from within a running async context (e.g. inside an async graph)."""
    loop = asyncio.get_event_loop()
    async_browser = loop.run_until_complete(create_async_playwright_browser(headless=True))
    toolkit = PlayWrightBrowserToolkit(async_browser=async_browser)
    return toolkit.get_tools()


async def get_async_browser():
    """Await and return an async playwright browser instance."""
    return await create_async_playwright_browser(headless=True)


async def get_playwright_tools_async():
    """Async factory: create browser and return playwright tools. 
    Call this once at startup inside an async entrypoint."""
    async_browser = await create_async_playwright_browser(headless=True)
    toolkit = PlayWrightBrowserToolkit(async_browser=async_browser)
    return toolkit.get_tools()


# Module-level tools initialized synchronously for import compatibility.
# If you hit event loop issues, switch to get_playwright_tools_async() in your async entrypoint.
try:
    loop = asyncio.get_event_loop()
    if loop.is_running():
        # Already inside an async context (e.g. Jupyter/Gradio startup)
        # tools will be None — use get_playwright_tools_async() instead
        playwright_tools = []
    else:
        async_browser = loop.run_until_complete(create_async_playwright_browser(headless=True))
        toolkit = PlayWrightBrowserToolkit(async_browser=async_browser)
        playwright_tools = toolkit.get_tools()
except Exception as e:
    print(f"[tools.py] Warning: could not init playwright browser at import time: {e}")
    playwright_tools = []
