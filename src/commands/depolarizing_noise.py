import networkx as nx
import random
import matplotlib.pyplot as plt

class QBit:
    def __init__(self, x_prob: float = 0, y_prob: float = 0, z_prob: float = 0, i_prob: float = 1):
        self.x_prob = x_prob
        self.y_prob = y_prob
        self.z_prob = z_prob
        self.i_prob = i_prob
        self.z_out_probs = []
        self.validate()

    def validate(self):
        """Ensures that the starting noise probibilities of the qbit are valid"""
        if self.x_prob + self.y_prob + self.z_prob + self.i_prob != 1:
            raise Exception("The probabilities must add up to 1")
        
    def do_pauli_operations(self, graph: nx.Graph):
        """Performs the pauli operations on the qbit and its neighbors"""
        self.z_out_probs.append(self.z_prob + self.y_prob) # Add probibility of Z noise on current qbit
        for n in graph.neighbors(self):
            n.z_out_probs.append(self.x_prob + self.y_prob) # Add probibility of Z noise on neighbor qbit

    def compute_z_out_prob(self): #TODO fix this with recursion
        """Computes the probability of Z noise on the qbit after all pauli operations have been performed
        Note: this should only be computed after all pauli operations have been performed"""
        
        probs = {k: 0 for k in range(len(self.z_out_probs)+1)}

        possibilities = 2**len(self.z_out_probs)
        for i in range(possibilities):
            num_of_z = 0
            prob = 1
            bin_str = format(i, f"0{len(self.z_out_probs)}b")
            for j,b in enumerate(bin_str):
                if b == "1":
                    num_of_z += 1
                    prob *= self.z_out_probs[j]
                else:
                    prob *= 1 - self.z_out_probs[j]

            probs[num_of_z] += prob
        
        return probs

    def __str__(self):
        return f"X: {self.x_prob}\nY: {self.y_prob}\nZ: {self.z_prob}\nI: {self.i_prob}"
    
graph = nx.Graph()

p = 0.25
inv_p = 1 - p

# Simple test
# q1 = QBit(inv_p/3, inv_p/3, inv_p/3, p)
# q2 = QBit()

# graph.add_node(q1)
# graph.add_node(q2)
# graph.add_edge(q1, q2)

# Advanced test
for i in range(6):
    graph.add_node(QBit(inv_p/3, inv_p/3, inv_p/3, p))

for i in range(10):
    n1 = random.choice(list(graph.nodes))
    n2 = random.choice(list(graph.nodes))

    if n1 == n2:
        continue

    graph.add_edge(n1,n2)

# Preform pauli operations
for node in graph.nodes:
    node.do_pauli_operations(graph)

for node in graph.nodes:
    print(node.compute_z_out_prob())

nx.draw(graph, with_labels=True)
plt.show()