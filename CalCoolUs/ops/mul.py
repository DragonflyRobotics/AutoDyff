from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const


class Mul(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, *args, **kwargs):
        if type(a) == Const:
            return b.value
        elif type(b) == Const:
            return a.value
        else:
            raise RuntimeError("At least one value in Mul must be cast to const to differentiate the partial derivative")
        

    def __call__(self, a, b):
        return a*b
