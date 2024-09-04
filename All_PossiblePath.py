import networkx as nx
import random
import math
import matplotlib.pyplot as plt

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

# Connect exit points to random nodes in the circle
for exit_point in ["e1", "e2"]:
    random_node = random.choice(list(G.nodes()))
    while random_node in ["e1", "e2"]:  # Avoid connecting exit points to themselves
        random_node = random.choice(list(G.nodes()))
    G.add_edge(exit_point, random_node)

# Save graph data to a text file
nx.write_adjlist(G, "graph_data.txt")

# Find all possible paths from s1 to e1 or e2
all_paths_e1 = list(nx.all_simple_paths(G, source="s1", target="e1"))
all_paths_e2 = list(nx.all_simple_paths(G, source="s1", target="e2"))

# Print all possible paths to terminal
print("All possible paths from s1 to e1:")
for path in all_paths_e1:
    print(path)

print("\nAll possible paths from s1 to e2:")
for path in all_paths_e2:
    print(path)

nx.draw(G, pos, with_labels=True, node_size=500, node_color=['green' if node in ["e1", "e2"] else 'skyblue' for node in G.nodes()], edge_color='gray')

# Show the plot
plt.show()


