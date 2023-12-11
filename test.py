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

shuntres = myshunt.getPostfix("(x+2)*(x+3)")

from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
#pos = nx.planar_layout(graph, scale=10)
nx.draw_networkx(graph, with_labels=True)
plt.savefig("fig.png")

def getFinalNode(graph):
    for n in graph.nodes:
        #print(graph.degree[n])
        if graph.out_degree[n] <= 0:
            print(n)
            return n
        else:
            pass

print(list(list(nx.all_simple_paths(graph, source='x', target=getFinalNode(graph))).reverse))

# plt.show(bbox_inches='tight')
exit()
for n, z in zip(graph.nodes(data=True), graph.nodes):
	neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(z))
	if len(neighbors):
		# print(n[1])
		# print(neighbors)
		# print(n[1]["Op"].value.getDerivative(a=1, b=2))
		all_operands = []
		for operands in neighbors:
			print(graph.nodes(data=True)[operands])
			all_operands.append(graph.nodes(data=True)[operands]['Op'])
		print(all_operands)
		print(z, neighbors)
		print(n[1]["Op"].getDerivative(a=all_operands[0], b=all_operands[1]))

	print("-------------------------------------------------------")
