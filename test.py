
import networkx as nx
from matplotlib import pyplot as plt
import re
from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *


string = r"2+x"
myshunt = ShuntingYard()
tokens = myshunt.tokenize_latex(string)
print(tokens)
print(myshunt.getPostfixLatex(tokens))
