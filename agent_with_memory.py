from typing import TypedDict, Annotated

from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages

from projectbase.llm import llm
from projectbase.utils import display_graph
import gradio as gr


## Generic Langgraph initializations
class State(TypedDict):
    messages: Annotated[list, add_messages]

graphbuilder = StateGraph(State)

def chatbot(state: State):
    return {"messages":[llm.invoke(state["messages"])]}

graphbuilder.add_node("chatbot", chatbot)

graphbuilder.add_edge(START, "chatbot")
graphbuilder.add_edge("chatbot", END)

##Add memory
# Using in memory db
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver() # This is in-memory, runtime memory only.

# Using sqlite
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
dp_path = "llm_memory.db"
conn = sqlite3.connect(dp_path, check_same_thread=False)
sql_memory = SqliteSaver(conn)


# graph_with_in_memory = graphbuilder.compile(checkpointer=memory)
graph_with_sqlite = graphbuilder.compile(checkpointer=sql_memory)

config = {"configurable": {"thread_id": "1"}} # Checkpointer requires one or more of the following 'configurable' keys: thread_id, checkpoint_ns, checkpoint_id
def chat(user_input: str, history):
    result = graph_with_sqlite.invoke({"messages": [{"role": "user", "content": user_input}]}, config=config)
    return result["messages"][-1].content

if __name__ == "__main__":
    # display_graph(graph)
    gr.ChatInterface(chat).launch()
    # print(graph_with_sqlite.get_state(config))
    # print(list(graph_with_sqlite.get_state_history(config)))


