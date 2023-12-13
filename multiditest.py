import networkx as nx
from matplotlib import pyplot as plt
G = nx.MultiDiGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
G.add_edge(1, 2)
nx.draw_networkx(G, with_labels=True)
plt.savefig("fig.png")


neighbors = list(nx.DiGraph.reverse(G, copy=False).neighbors(2))
print(neighbors)
