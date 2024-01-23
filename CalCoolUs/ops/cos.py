from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Cos(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Cos GOT: {a}, {b}")
        return math.sin(b) * a * -1

    def __call__(self, a):
        return math.cos(a)

