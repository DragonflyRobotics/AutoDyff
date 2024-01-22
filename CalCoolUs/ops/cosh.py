from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Cosh(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Cos GOT: {a}, {b}")
        return math.sinh(b) * a

    def __call__(self, a):
        return math.cosh(a)

