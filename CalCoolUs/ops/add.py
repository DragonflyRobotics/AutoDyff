from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const


class Add(Generic_Op):
    def __init__(self, name):
        super().__init__(name)
        self.value = self

    def getDerivative(self, a, b, *args, **kwargs):
        return Const("Const", 1)

    def __call__(self, a, b):
        return a+b

