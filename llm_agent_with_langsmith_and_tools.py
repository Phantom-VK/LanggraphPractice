"""
Langgraph practice with Langsmith tracing and Tool calls
- Deepseek LLM
1) Google Serper search tool
2) Pushover notification tool
"""
import os
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool, StructuredTool
import requests
from dotenv import load_dotenv

from projectbase.llm import llm

load_dotenv(override=True)

### Create tools
serper = GoogleSerperAPIWrapper()
# Search Tool (Tool from a function)
search_tool = StructuredTool.from_function(
    func = serper.run,
    name = "search",
    description="Useful for when you need more information from an online search"
)
# Push notification tool (Tool using decorator)
pushover_token = os.getenv("PUSHOVER_API_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER_KEY")
pushover_url = "https://api.pushover.net/1/messages.json"

@tool
def send_notification(text: str) -> dict:
    """
    Use this when you want to send a push notification to the user's device.
    :param text: Text to be sent as an email
    :return: dict with status code and response text
    """
    data = {"token": pushover_token,"user":pushover_user,  "message": text}
    response = requests.post(pushover_url, data= data)

    return {"status_code": response.status_code, "text": response.text}

tools = [search_tool, send_notification]

# Bind LLM with tools
llm_with_tools = llm.bind_tools(tools)

### Create State
class State(TypedDict):
    messages: Annotated[list, add_messages]

### Build Graph
gbuilder = StateGraph(State)


## Create node
def chatbot(state: State):
    return { "messages": [llm_with_tools.invoke(state["messages"])]}

gbuilder.add_node("chatbot", chatbot)
gbuilder.add_node("tools", ToolNode(tools=tools))

## Create Edges
gbuilder.add_edge(START, "chatbot")
gbuilder.add_conditional_edges("chatbot", tools_condition, "tools")
gbuilder.add_edge("tools", "chatbot")

graph = gbuilder.compile()


def chat(user_input: str, history):
    result = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    return result["messages"][-1].content

if __name__ == "__main__":
    # display_graph(graph)
    gr.ChatInterface(chat).launch()
