from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Sin(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return math.cos(b) * a

    def __call__(self, a):
        return math.sin(a)

