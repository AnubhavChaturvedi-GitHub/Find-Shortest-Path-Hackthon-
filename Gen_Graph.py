import networkx as nx
import matplotlib.pyplot as plt
import random
import math

# Number of nodes
num_nodes = 10

# Create an empty graph
G = nx.Graph()

# Add nodes labeled s1, s2, ..., s10
for i in range(num_nodes):
    G.add_node(f"s{i+1}")

# Arrange nodes in a circle
pos = {}
for i, node in enumerate(G.nodes()):
    angle = 2 * math.pi * i / num_nodes
    x = math.cos(angle)
    y = math.sin(angle)
    pos[node] = (x, y)

# Add random edges
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        if random.random() < 0.5:  # Adjust the probability of edge creation as needed
            G.add_edge(f"s{i+1}", f"s{j+1}")

# Add exit points e1 and e2
G.add_nodes_from(["e1", "e2"])

# Position exit points
pos["e1"] = (1.1, 0)  # Adjust position as needed
pos["e2"] = (-1.1, 0)  # Adjust position as needed

# Draw the network
nx.draw(G, pos, with_labels=True, node_size=500, node_color=['green' if node in ["e1", "e2"] else 'skyblue' for node in G.nodes()], edge_color='gray')

# Show the plot
plt.show()
