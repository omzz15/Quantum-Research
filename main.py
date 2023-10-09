import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# pentigram
G.add_nodes_from([
    (2, {"seed":12}),
    (1, {"seed":34}),
    (3, {"seed":245}),
    (4, {"seed":345}),
    (5, {"seed":7}),
])
# G.add_edges_from([
#     (1,2),
#     (1,3),
#     (1,4),
#     (1,5),
#     (2,3),
#     (2,4),
#     (2,5),
#     (3,4),
#     (3,5),
#     (4,5),
# ])
G.add_edges_from([
    (1,2),
    (2,3),
    (3,1),
])
a = G.adj
adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
H = nx.Graph(adjacency_dict)  # create a Graph dict mapping nodes to nbrs

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()
print("Graph Made")