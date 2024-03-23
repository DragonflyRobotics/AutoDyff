from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math
from CalCoolUs.error_types import *

class Sqrt(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return 1.0/(2.0*math.sqrt(b)) * a

    def __call__(self, a):
        if a < 0:
            raise DNE
        return math.sqrt(a)

