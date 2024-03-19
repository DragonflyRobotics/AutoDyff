import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
import random
from CalCoolUs.error_types import *
#print(random.random())
#exit(9)

myshunt = ShuntingYard()


shuntres = myshunt.getPostfix("sin(9^(2e^(arctan(2arccos(2e^(2cos(2x^2tan(e)+4))+4)-2))))-cos(9^e)")
#shuntres = myshunt.tokenize("arccos(2x^sin(cos(x^2-2)))")



#shuntres = myshunt.tokenize("2*x")
shuntres = myshunt.getPostfix("2e")
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

print(ne.solve(1))
print(ne.differentiate(0.1))
