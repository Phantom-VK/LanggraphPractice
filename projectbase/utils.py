import matplotlib.pyplot as plt
from PIL import Image
import io
from langgraph.graph.state import CompiledStateGraph


## Function to visualize a graph
def display_graph(input_graph: CompiledStateGraph):
    """Display the graph in a standalone window"""
    # Get the PNG image as bytes
    img_data = input_graph.get_graph().draw_mermaid_png()

    # Convert bytes to PIL Image
    img = Image.open(io.BytesIO(img_data))

    # Display with matplotlib
    plt.figure(figsize=(10, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.title("Graph Visualization")
    plt.show()