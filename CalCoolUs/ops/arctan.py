from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Arctan(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Sin GOT: {a}, {b}")
        return (1.0/(1.0+b**2)) * a

    def __call__(self, a):
        return math.atan(a)

