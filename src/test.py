import networkx as nx
import matplotlib.pyplot as plt
import random

weight_function = lambda u, v : random.randint(1,100)
sides = 20

G = nx.Graph()

for i in range(1, sides + 1):
    for j in range(i + 1, sides + 1):
        G.add_weighted_edges_from([
            (i,j,weight_function(i,j))
        ])

pos=nx.circular_layout(G)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=2)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
