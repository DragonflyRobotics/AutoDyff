from networkx import all_pairs_bellman_ford_path
from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Pow(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, a_val, b_val, *args, **kwargs):
        #assert a_val > 0 
        if b == 0: # if it is x ^ constant
            return b_val * (a_val**(b_val-1)) * a
        else:
            return math.log(a_val) * (a_val**b_val) * b
        #return (a_val ** b_val)*(b_val*a/a_val + math.log(a_val) * b)


    def __call__(self, a, b):
        return a**b
