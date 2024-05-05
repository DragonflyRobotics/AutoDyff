from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Tanh(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return ((1.0/math.cosh(b))**2) * a

    def __call__(self, a):
        print(f"Tanh({a}) = {math.tanh(a)}")
        return math.tanh(a)

