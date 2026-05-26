from webscraperagent.graph import build_ws_graph
import gradio as gr
config = {"configurable": {"thread_id": "10"}}

graph = build_ws_graph()

async def chat(user_input: str, history):
    result = await graph.ainvoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config
    )
    return result["messages"][-1].content

if __name__ == "__main__":
    gr.ChatInterface(chat).launch()