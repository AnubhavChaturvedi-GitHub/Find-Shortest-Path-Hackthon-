import networkx as nx
import random
import math
import matplotlib.pyplot as plt

# Number of nodes
num_nodes = 10

# Create an empty graph
G = nx.Graph()

# Add nodes labeled z1s1, z1s2, ..., z2s10
zone1_nodes = [f"z1s{i}" for i in range(1, 6)]
zone2_nodes = [f"z2s{i}" for i in range(6, 11)]
G.add_nodes_from(zone1_nodes)
G.add_nodes_from(zone2_nodes)

# Arrange nodes in a circle
pos = {}
for i, node in enumerate(zone1_nodes + zone2_nodes):
    angle = 2 * math.pi * i / num_nodes
    x = math.cos(angle)
    y = math.sin(angle)
    pos[node] = (x, y)

# Add edges within zone 1
for i in range(len(zone1_nodes)):
    for j in range(i+1, len(zone1_nodes)):
        if random.random() < 0.5:  # Adjust the probability of edge creation as needed
            length = random.randint(1, 10)  # Assign random length values
            G.add_edge(zone1_nodes[i], zone1_nodes[j], length=length)  # Specify the 'length' attribute

# Add edges within zone 2
for i in range(len(zone2_nodes)):
    for j in range(i+1, len(zone2_nodes)):
        if random.random() < 0.5:  # Adjust the probability of edge creation as needed
            length = random.randint(1, 10)  # Assign random length values
            G.add_edge(zone2_nodes[i], zone2_nodes[j], length=length)  # Specify the 'length' attribute

# Add exit points e1 and e2
G.add_nodes_from(["e1", "e2"])

# Position exit points
pos["e1"] = (1.1, 0)  # Adjust position as needed
pos["e2"] = (-1.1, 0)  # Adjust position as needed

# Connect exit points to random nodes in each zone
random_node_zone1 = random.choice(zone1_nodes)
random_node_zone2 = random.choice(zone2_nodes)
G.add_edge("e1", random_node_zone1)
G.add_edge("e2", random_node_zone2)

# Add edges between all nodes within each zone
for nodes in [zone1_nodes, zone2_nodes]:
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if random.random() < 0.5:  # Adjust the probability of edge creation as needed
                length = random.randint(1, 10)  # Assign random length values
                G.add_edge(nodes[i], nodes[j], length=length)  # Specify the 'length' attribute

# Add edges between nodes in different zones
for node1 in zone1_nodes:
    for node2 in zone2_nodes:
        if random.random() < 0.5:  # Adjust the probability of edge creation as needed
            length = random.randint(1, 10)  # Assign random length values
            G.add_edge(node1, node2, length=length)  # Specify the 'length' attribute

# Save graph data to a text file
nx.write_adjlist(G, "graph_data.txt")

zone_names = [
    "z1s1",
    "z1s2",
    "z1s3",
    "z1s4",
    "z1s5",
    "z2s6",
    "z2s7",
    "z2s8",
    "z2s9",
    "z2s10",
]

zone_code = random.choice(zone_names)
# Find all possible paths from z1s1 to e1 or e2
all_paths_e1 = list(nx.all_simple_paths(G, source=zone_code, target="e1"))
all_paths_e2 = list(nx.all_simple_paths(G, source=zone_code, target="e2"))

# Print all possible paths and their total length to terminal
print("All possible paths from z1s1 to e1:")
shortest_length_e1 = float('inf')
shortest_path_e1 = None
for path in all_paths_e1:
    total_length = sum(G[path[i]][path[i+1]].get('length', 0) for i in range(len(path)-1))
    print(path, "Total Length:", total_length)
    if total_length < shortest_length_e1:
        shortest_length_e1 = total_length
        shortest_path_e1 = path

print("\nAll possible paths from z1s1 to e2:")
shortest_length_e2 = float('inf')
shortest_path_e2 = None
for path in all_paths_e2:
    total_length = sum(G[path[i]][path[i+1]].get('length', 0) for i in range(len(path)-1))
    print(path, "Total Length:", total_length)
    if total_length < shortest_length_e2:
        shortest_length_e2 = total_length
        shortest_path_e2 = path


print(f"\nShortest path from {zone_code} to e1:", shortest_path_e1, "Total Length:", shortest_length_e1)
print(f"Shortest path from {zone_code} to e2:", shortest_path_e2, "Total Length:", shortest_length_e2)

my_list = shortest_path_e1
my_list2 = shortest_path_e2
# Convert list to a single string with elements separated by commas
my_string = ', '.join(my_list)
my_string2 = ', '.join(my_list2)
# Print the resulting string

# Replace specific substrings in the string and assign the result back to my_string
if my_string.startswith(("z1s1","z1s2","z1s3","z1s4","z1s5","z1s6")):
    my_string = my_string.replace("z1s1,", "⚠️ RED ZONE")
    my_string = my_string.replace("z1s2,", "⚠️ RED ZONE")
    my_string = my_string.replace("z1s3,", "⚠️ RED ZONE")
    my_string = my_string.replace("z1s4,", "⚠️ RED ZONE")
    my_string = my_string.replace("z1s5,", "⚠️ RED ZONE")
    my_string = f"{zone_code}"+ "," +my_string
    my_string = my_string.replace("⚠️ RED ZONE","")
else:
    my_string = my_string.replace("z2s6,", "⚠️ RED ZONE")
    my_string = my_string.replace("z2s7,", "⚠️ RED ZONE")
    my_string = my_string.replace("z2s8,", "⚠️ RED ZONE")
    my_string = my_string.replace("z2s9,", "⚠️ RED ZONE")
    my_string = my_string.replace("z2s10,", "⚠️ RED ZONE")
    my_string = f"{zone_code}"+ "," +my_string
    my_string = my_string.replace("⚠️ RED ZONE","")
    
if my_string2.startswith(("z1s1","z1s2","z1s3","z1s4","z1s5","z1s6")):
    my_string2 = my_string.replace("z1s1,", "⚠️ RED ZONE")
    my_string2 = my_string.replace("z1s2,", "⚠️ RED ZONE")
    my_string2 = my_string.replace("z1s3,", "⚠️ RED ZONE")
    my_string2 = my_string.replace("z1s4,", "⚠️ RED ZONE")
    my_string2 = my_string.replace("z1s5,", "⚠️ RED ZONE")
    my_string2 = f"{zone_code}"+ "," +my_string
    my_string2 = my_string.replace("⚠️ RED ZONE","")
else:
    my_string2 = my_string2.replace("z2s6,", "⚠️ RED ZONE")
    my_string2 = my_string2.replace("z2s7,", "⚠️ RED ZONE")
    my_string2 = my_string2.replace("z2s8,", "⚠️ RED ZONE")
    my_string2 = my_string2.replace("z2s9,", "⚠️ RED ZONE")
    my_string2 = my_string2.replace("z2s10,", "⚠️ RED ZONE")
    my_string2 = f"{zone_code}"+ "," +my_string
    my_string2 = my_string2.replace("⚠️ RED ZONE","")
# Print the modified string
print(my_string)
print(my_string2)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color=['green' if node in ["e1", "e2"] else 'skyblue' for node in G.nodes()], edge_color='gray')

# Show the plot
plt.show()
