from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser

# tools.py - Browser as global singleton
from functools import lru_cache

@lru_cache(maxsize=1)
def get_browser():
    return create_async_playwright_browser(headless=True)

async_browser = get_browser()
toolkit = PlayWrightBrowserToolkit(async_browser = async_browser)
playwright_tools = toolkit.get_tools()


# for tool in tools:
#     print(f"{tool.name}={tool}")