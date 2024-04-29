from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
import math
from CalCoolUs.error_types import *

class Arccos(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self
        self.unary = True

    def getDerivative(self, a, b, *args, **kwargs):
        if (1-(b**2)) == 0:
            raise ZeroDivisionError
        if (1-(b**2)) < 0:
            raise ImaginaryNumberError
        return (-1.0/math.sqrt(1-(b**2))) * a

    def __call__(self, a):
        if a > 1 or a < -1:
            raise DomainError
        return math.acos(a)

