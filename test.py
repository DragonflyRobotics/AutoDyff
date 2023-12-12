import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const

# sub = OpType.SUB
# print(sub.value)
#
# print(sub.value.)

myshunt = ShuntingYard()

shuntres = myshunt.tokenize("-x-1-(x-1-x)+-(-x-1)")
print(shuntres)

shuntres = myshunt.getPostfix("(x+1)*(x+3)*(x+4)")

from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
#pos = nx.planar_layout(graph, scale=10)
nx.draw_networkx(graph, with_labels=True)
plt.savefig("fig.png")

print(myASTGraph.getFinalNode(graph))
 #exit(3)
og_nodes = myASTGraph.getNodes(graph)
x = 5

def solve(node):
    #print(f"Working on: {node}")
    if node == "x":
        graph.nodes(data=True)['x']['Op'].numerical_value = x
        #print(f"x={x}")
        return x
    elif type(graph.nodes(data=True)[node]["Op"]) == Const:
        a = graph.nodes(data=True)[node]["Op"].numerical_value
        #print(f"{node}={a}")
        return a
    else:
        neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(node))
        #print(neighbors)
        graph.nodes(data=True)[node]["Op"].numerical_value = graph.nodes(data=True)[node]["Op"](solve(neighbors[0]), solve(neighbors[1]))
        a = graph.nodes(data=True)[node]["Op"].numerical_value
        print(f"{node}={a}")
        return a

def differentiate(node):
    temp = graph.nodes(data=True)[node]["Op"].numerical_value
    print(f"Working on: {node}={temp}")
    if node == "x":
        print(f"x'={1}")
        return 1
    elif type(graph.nodes(data=True)[node]["Op"]) == Const:
        print(f"{node}'={0}")
        return 0
    else:
        neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(node))
        print(neighbors)
        #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
        a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), solve(neighbors[0]), solve(neighbors[1]))

        print(f"{node}'={a}")
        return a

solve(myASTGraph.getFinalNode(graph))
differentiate(myASTGraph.getFinalNode(graph))
exit()


for o in og_nodes:
    for n in o:
        print(n, graph.nodes(data=True)[n]["Op"].numerical_value) 
        if n == 'x':
            graph.nodes(data=True)['x']['Op'].numerical_value = x
        else:
            neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(n))
            #print(neighbors)
            graph.nodes(data=True)[n]['Op'].numerical_value = graph.nodes(data=True)[n]["Op"](graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
        #print(n, graph.nodes(data=True)[n]["Op"].numerical_value)
exit()
for i in range(len(og_nodes)):
    og_nodes[i] = list(og_nodes[i].__reversed__())

print(og_nodes)
for o in og_nodes:
    for i in range(len(o)):
        z = o[i]
        neighbors = list(nx.DiGraph.reverse(graph, copy=False).neighbors(z))
        if i+1 > len(o)-1:
            print(f"Just taking derivative of {z}")
        else:
            print(f"Taking the derivative of {z} with neighbors {neighbors} with respect to {o[i+1]}")
            if neighbors[0] == o[i+1]:
                print(graph.nodes(data=True)[z]["Op"].getDerivative(a=graph.nodes(data=True)[neighbors[0]]["Op"], b=Const(neighbors[1], graph.nodes(data=True)[neighbors[1]]["Op"])))
    print("----")
exit()
# plt.show(bbox_inches='tight')

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
