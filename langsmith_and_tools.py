from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_deepseek import ChatDeepSeek
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool, tool, StructuredTool
from dotenv import load_dotenv

load_dotenv(override=True)

## Setup LLM
llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    temperature=0.3
)

## Convert a function to a tool
serper = GoogleSerperAPIWrapper()

search_tool_from_func = StructuredTool.from_function(
    func = serper.run,
    name = "search",
    description="Useful for when you need more information from an online search"
)

print(search_tool_from_func.invoke("Who are you? Answering my questions"))