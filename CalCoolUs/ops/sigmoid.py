from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Sigmoid(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return (math.exp(-1*b)/math.pow((1+math.exp(-1*b)), 2)) * a

    def __call__(self, a):
        return 1/(1+math.exp(-1*a))
