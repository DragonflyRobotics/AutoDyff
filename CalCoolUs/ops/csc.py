from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Csc(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Csc GOT: {a}, {b}")
        return (-1/math.sin(b))*a/math.tan(b)

    def __call__(self, a):
        return 1/(math.sin(a))
