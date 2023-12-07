import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType


# sub = OpType.SUB
# print(sub.value)
#
# print(sub.value.)

myshunt = ShuntingYard()

shuntres = myshunt.tokenize("-x-1-(x-1-x)+-(-x-1)")
print(shuntres)

shuntres = myshunt.getPostfix("-x-1-(x-1-x)+-(-x-1)")
exit(3)
from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
pos = nx.planar_layout(graph, scale=10)
nx.draw_networkx(nx.DiGraph.reverse(graph, copy=False), with_labels=True)
plt.savefig("fig.png")

# plt.show(bbox_inches='tight')

for n, z in zip(graph.nodes(data=True), graph.nodes):
	neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(z))
	if len(neighbors):
		print(n[1]["Op"].value.getDerivative(a=1))
		print(z, neighbors)

	print("-------------------------------------------------------")