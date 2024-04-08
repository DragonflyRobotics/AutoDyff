
import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
import random
from CalCoolUs.error_types import *
#print(random.random())
#exit(9)

myshunt = ShuntingYard()

#shuntres = myshunt.getPostfix("-2cos(x^2)")
shuntres = myshunt.getPostfix("sin(9^(2e^(arctan(2arccos(2e^(2cos(2x^2tan(e)+4))+4)-2))))-cos(9^e)")
print(shuntres)
#shuntres = myshunt.tokenize("arccos(2x^sin(cos(x^2-2)))")
exit(3)


#shuntres = myshunt.tokenize("2*x")
#shuntres = myshunt.getPostfix("2e")
print(shuntres)



print(ne.solve(0))
print(ne.differentiate(0))
