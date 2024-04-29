
import networkx as nx
from matplotlib import pyplot as plt
import re
from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *


string = r"\frac{e^{x\left(x+1\right)\left(x+2\right)\cos\left(x\right)}}{e^{\cos\left(e\cdot x\right)}}"
myshunt = ShuntingYard()
tokens = myshunt.tokenize_latex(string)
print(tokens)
print(myshunt.getPostfixLatex(tokens))
