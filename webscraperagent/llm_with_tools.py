from projectbase.llm import llm
from webscraperagent.tools import playwright_tools

ws_llm_with_tools = llm.bind_tools(playwright_tools)