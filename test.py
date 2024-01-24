import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const

myshunt = ShuntingYard()

shuntres = myshunt.getPostfix("ln(e^x)")
print(shuntres)
#shuntres = myshunt.getPostfix("sec(x)")
#shuntres = myshunt.getPostfix("2^x")
#shuntres = myshunt.getPostfix("(x+1)^2")


from CalCoolUs.preprocess import ASTGraph
myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
#pos = nx.planar_layout(graph, scale=10)
nx.draw_networkx(graph, with_labels=True)
plt.savefig("fig.png")



from CalCoolUs.numerical_engine import Numerical_Engine

ne = Numerical_Engine(graph, myASTGraph)

#ne.solve(0.2)
print(ne.differentiate(2.3))
