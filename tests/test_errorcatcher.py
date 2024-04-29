from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine
from CalCoolUs.error_types import *
import random, pytest
def solve(postfix, x):
    shuntres = myshunt.getPostfix(postfix)
    graph = myASTGraph.getAST(shuntres)
    ne = Numerical_Engine(graph, myASTGraph)
    return ne.solve(x)
import numpy as np

myshunt = ShuntingYard()
myASTGraph = ASTGraph()
def test_postfix_errors():
    with pytest.raises(ParenthesisMulError):
        myshunt.tokenize("(x+2)(x)")
        myshunt.tokenize("e^5(x+5)")
        myshunt.tokenize("(x+7)5^4")
def test_function_errors():
    with pytest.raises(DomainError):
        solve("arcsin(x)",2)
        solve("arccos(4x)",0.5)
        solve("arcsec(x/2)",1.5)
    with pytest.raises(DNE):
        solve("1/x",0)
        solve("ln(x)",-1)
        solve("(x+1)/(x+1)",-1)