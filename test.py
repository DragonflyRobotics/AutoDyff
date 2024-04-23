
import networkx as nx
from matplotlib import pyplot as plt
import re
from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *


string = "ex"
myshunt = ShuntingYard()
tokens = myshunt.tokenize_latex(string)
print(myshunt.getPostfixLatex(tokens))
