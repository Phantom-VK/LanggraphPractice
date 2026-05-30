from webscraperagent.llm_with_tools import ws_llm_with_tools
from webscraperagent.state import State


async def chatbot_node(state: State):
    response = await ws_llm_with_tools.ainvoke(state["messages"])
    return {"messages": [response]}
