from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math

class Arccot(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return (1.0/(-1*(1/math.pow(math.sin(self.__call__(b)), 2)))) * a

    def __call__(self, a):
        if a == 0:
            return math.pi/2 
        elif a > 0:
            return math.atan(1/a)
        elif a < 0:
            return math.atan(1/a) + math.pi
        else:
            raise RuntimeError("You bozo just broke arccot")

