from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Cot(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Cot GOT: {a}, {b}")
        return (-1 * ((1.0/math.sin(b))**2) * a)

    def __call__(self, a):
        return 1/(math.tan(a))

