
import networkx as nx
from matplotlib import pyplot as plt
import re
from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *

regex_latex = r"(\\sin)|(\\cos)|(\\tan)|(\\ln)|(\\log)|(\\arcsin)|(\\arccos)|(\\arctan)|(\\cot)|(\\csc)|(\\sec)|(\\sinh)|(\\cosh)|(\\tanh)|(\\arccsc)|(\\arcsec)|(\\arccot)|(\\sigmoid)|(\\sqrt)|((?<=\))-(?=.*))|({)|(})|(\\left\()|(\\right\))|(\d+\.\d+)|((?<!=\.)\d+(?!=\.))|((?<=\B)-\d+\.\d+)|((?<=\B)(?<!=\.)-\d+(?!=\.))|(x|(?<=\B)-x)|(e)|(\\pi)|(\^)|(\*)|(\\frac)|(\+)|(-\()|(-)" 

string = r"2^{\left(x^2+5\right)}+\frac{4+x}{2\cdot\cos\left(x\right)}"

myshunt = ShuntingYard()
print(myshunt.tokenize_latex(r"2\cos\left(x\right)"))
