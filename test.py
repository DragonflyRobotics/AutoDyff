import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const

# sub = OpType.SUB
# print(sub.value)
#
# print(sub.value.)

myshunt = ShuntingYard()


#shuntres = myshunt.getPostfix("(x+1)*(x+3)*(x+4)")
shuntres = myshunt.getPostfix("((((x+1)^2)/((x+3)^3)) * 2^x) * (2-x)")
#shuntres = myshunt.getPostfix("x*x")



from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
#pos = nx.planar_layout(graph, scale=10)
nx.draw_networkx(graph, with_labels=True)
plt.savefig("fig.png")



from CalCoolUs.numerical_engine import Numerical_Engine

ne = Numerical_Engine(graph, myASTGraph)

ne.differentiate(6)
