from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from projectbase.utils import display_graph
from webscraperagent.state import State
from webscraperagent.nodes import chatbot_node
from webscraperagent.tools import playwright_tools


def build_ws_graph():
    ws_graphbuilder = StateGraph(State)

    ws_graphbuilder.add_node("chatbot", chatbot_node)
    ws_graphbuilder.add_node("tools", ToolNode(tools=playwright_tools))
    ws_graphbuilder.add_conditional_edges("chatbot",tools_condition, "tools")
    ws_graphbuilder.add_edge("tools", "chatbot")
    ws_graphbuilder.add_edge(START, "chatbot")

    memory = MemorySaver()

    return ws_graphbuilder.compile(checkpointer=memory)


# if __name__ == "__main__":
#     grph = build_ws_graph()
#     display_graph(grph)