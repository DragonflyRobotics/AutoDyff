from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Sin(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        print(f"Sin GOT: {a}, {b}")
        return (1/(b*math.log(10))) * a

    def __call__(self, a):
        return math.log10(a)

