# Clearly, neither my first Python script of my life nor my first script of Langgraph
# Just first script of my Langgraph practice.
import random
from typing import Annotated

import gradio as gr
from langgraph.graph import StateGraph, START, END
from langgraph.graph import add_messages
from pydantic import BaseModel

# Some useful constants
nouns = ["Cabbages", "Unicorns", "Toasters", "Penguins", "Bananas", "Zombies", "Rainbows", "Eels", "Pickles", "Muffins"]
adjectives = ["outrageous", "smelly", "pedantic", "existential", "moody", "sparkly", "untrustworthy", "sarcastic", "squishy", "haunted"]


## Create a state object

class State(BaseModel):

    messages: Annotated[list, add_messages]

## Start Graph Builder
graph_builder = StateGraph(State)

## Create a node
def first_node(state: State):

    reply = f"{random.choice(nouns)} are {random.choice(adjectives)}"

    messages = [{"role":"ai","content":reply}]

    new_state = State(messages=messages)
    return new_state

graph_builder.add_node("first node",first_node)

## Create edges

graph_builder.add_edge(START, "first node")
graph_builder.add_edge("first node", END)


## Compile graph
graph = graph_builder.compile()

## Entry point

def chat(user_input: str, history):
    message = {"role": "user", "content": user_input}
    messages = [message]
    state = State(messages=messages)
    result = graph.invoke(state)
    print(result)
    return result["messages"][-1].content




if __name__ == "__main__":
    gr.ChatInterface(chat).launch()
