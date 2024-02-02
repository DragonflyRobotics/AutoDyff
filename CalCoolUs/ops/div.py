from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const


class Div(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, a_val, b_val, *args, **kwargs):
        return (a*b_val - a_val*b) / (b_val*b_val)

    def __call__(self, a, b):
        return a/b
