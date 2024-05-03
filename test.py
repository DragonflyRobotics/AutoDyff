
import networkx as nx
from matplotlib import pyplot as plt
import re
from CalCoolUs.preprocess import ShuntingYard, OpType, ASTGraph
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *
from CalCoolUs.numerical_engine import Numerical_Engine


string = r"\sin\left(-x^{\frac{2\cdot-x}{4+-e^{x}}}\right)"
myshunt = ShuntingYard()

tokens = myshunt.tokenize_latex(string)
print(tokens)
shuntres = myshunt.getPostfixLatex(tokens)
print(shuntres)
exit(3)
myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
ne = Numerical_Engine(graph, myASTGraph)
print(ne.solve(1))
