from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math
from CalCoolUs.error_types import *

class Arccsc(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        return (1.0/(-1.0*(1/math.sin(self.__call__(b)))*(1/math.tan(self.__call__(b))))) * a

    def __call__(self, a):
        if a > or a < -1:
            raise DomainError
        return math.asin(1.0/a)

