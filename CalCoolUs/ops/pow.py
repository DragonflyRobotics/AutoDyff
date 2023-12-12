from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Pow(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, a_val, b_val, *args, **kwargs):
        print(f"POW GOT: {a}, {b}, {a_val}, {b_val}")
        return (a_val ** b_val)*(b_val*a/a_val + math.log(a_val) * b)

    def __call__(self, a, b):
        return a**b
