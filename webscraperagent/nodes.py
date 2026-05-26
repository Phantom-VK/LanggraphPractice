from webscraperagent.llm_with_tools import ws_llm_with_tools
from webscraperagent.state import State

def chatbot_node(state: State):
    return {"messages":[ws_llm_with_tools.invoke(state["messages"])]}