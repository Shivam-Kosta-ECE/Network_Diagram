import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = [
    "MME", "PCRF", "HSS", "External Network",
    "DRA", "DEA", "NSSF", "NRF", "DNS", "NEF", "PCF", "UDM", "AUSF", "AMF", "SMF", "SCP", "BSF", "SEPP", "USFW", "UPF",
    "STP"
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define interfaces (connections between nodes)
interfaces = [
    ("MME", "DRA"),
    ("PCRF", "DRA"),
    ("HSS", "DRA"),
    ("DRA", "DEA"),
    ("External Network", "DEA"),
    ("NRF", "BSF"),
    ("NSSF", "BSF"),
    ("DNS", "BSF"),
    ("NEF", "SEPP"),
    ("PCF", "BSF"),
    ("UDM", "DRA"),
    ("AUSF", "DRA"),
    ("AMF", "BSF"),
    ("SMF", "BSF"),
    ("SCP", "BSF"),
    ("SEPP", "BSF"),
    ("SEPP", "USFW"),
    ("DEA", "USFW"),
    ("UPF", "AMF"),
    ("SMF", "AMF"),
    ("SMF", "UPF"),
    ("STP", "USFW")

]

# Add interfaces to the graph
G.add_edges_from(interfaces)

# Define position for nodes
pos = {
    "MME": (-2, 1),
    "PCRF": (-2, -1),
    "HSS": (2, 0),
    "External Network": (-2, -3),
    "DRA": (0, 0),
    "DEA": (-1, 0),
    "NSSF": (-3, 2), 
    "NRF": (-2, 2), 
    "DNS": (-1, 2), 
    "NEF": (0, 2), 
    "PCF": (1, 2), 
    "UDM": (2, 2), 
    "AUSF": (3, 2), 
    "AMF": (-1, -2), 
    "SMF": (-2, -2), 
    "SCP": (-3, -2), 
    "BSF": (1, 1), 
    "SEPP": (2, -2), 
    "USFW": (3, -2), 
    "UPF": (1, -1),
    "STP": (2, -3)
}

# Draw the graph
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Network Disign for Customer-X")
plt.axis('off')
plt.show()
