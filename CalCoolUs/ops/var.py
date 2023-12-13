from CalCoolUs.ops.op import Generic_Op
from CalCoolUs.ops.const import Const
class Var(Generic_Op):
    def __init__(self, name):
        self.value = self
        super().__init__(name)

    def getValue(self):
        self.value

    def getDerivative(self, *args, **kwargs):
        return Const("CONST", 1)

    def __call__(self, a):
        return a
