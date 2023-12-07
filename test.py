import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType


# sub = OpType.SUB
# print(sub.value)
#
# print(sub.value.)

myshunt = ShuntingYard()

shuntres = myshunt.tokenize("2-x")
print(shuntres)
shuntres = myshunt.getPostfix("2-x")

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
		# print(n[1])
		# print(neighbors)
		print(n[1]["Op"].value.getDerivative(a=1, b=2))
		all_operands = []
		for operands in neighbors:
			print(graph.nodes(data=True)[operands])
			all_operands.append(graph.nodes(data=True)[operands]['Op'].value)
		print(all_operands)
		print(z, neighbors)
		print(n[1]["Op"].value.getDerivative(a=all_operands[0], b=all_operands[1]))

	print("-------------------------------------------------------")