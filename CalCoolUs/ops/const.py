from CalCoolUs.ops.op import Generic_Op

class Const(Generic_Op):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)
        self.differentiable = False
        self.numerical_value = self.value

    def getValue(self):
        return self.value

    def getDerivative(self, *args, **kwargs):
        return Const("CONST", 0)

    def __call__(self, a):
        return a

