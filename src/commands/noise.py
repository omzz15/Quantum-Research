import networkx as nx
import random
import matplotlib.pyplot as plt

class Qbit: #TODO make the noise tracking better
    def __init__(self, noise : str = "I") -> None:
        self.input_noise = noise
        self.output_noise = None

    def push_noise(self, graph : nx.Graph):
        if self.input_noise == "X":
            for n in graph.neighbors(self): n.add_output_noise()
        elif self.input_noise == "Y":
            for n in graph.neighbors(self): n.add_output_noise()
            self.add_output_noise()
        elif self.input_noise == "Z":
            self.add_output_noise()
        elif not self.input_noise == "I":
            raise Exception(f"Invalid noise {self.input_noise}")

        self.input_noise = None

    def add_output_noise(self):
        if not self.output_noise:
            self.output_noise = "Z"
            return
        
        self.output_noise = None

    def __str__(self):
        if self.input_noise:
            return self.input_noise
        return self.output_noise if self.output_noise else ""
    
graph = nx.Graph()

for i in range(12):
    graph.add_node(Qbit(random.choice(["X", "Y", "Z", "I"])))

for i in range(20):
    n1 = random.choice(list(graph.nodes))
    n2 = random.choice(list(graph.nodes))

    if n1 == n2:
        continue

    graph.add_edge(n1,n2)

pos = nx.spring_layout(graph)

plt.subplot(211)
plt.title("pre noise")
plt1 = nx.draw(graph, pos, with_labels = True)

for node in graph.nodes:
    node.push_noise(graph)

plt.subplot(212)
plt.title("post noise")
plt2 = nx.draw(graph, pos, with_labels = True)

plt.show()

print("done")