import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType
from CalCoolUs.ops.const import Const
import random
from CalCoolUs.error_types import *
#print(random.random())
#exit(9)

myshunt = ShuntingYard()


shuntres = myshunt.getPostfix("(2(4x+5))/3")
print(shuntres)



