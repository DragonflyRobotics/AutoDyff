from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
from CalCoolUs.error_types import *


class Div(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, a_val, b_val, *args, **kwargs):
        if (b_val == 0):
            raise ZeroDivisionError
        return (a*b_val - a_val*b) / (b_val*b_val)

    def __call__(self, a, b):
        if b == 0:
            raise DNE
        return a/b
