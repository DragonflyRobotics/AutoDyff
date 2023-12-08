from CalCoolUs.ops.op import Generic_Op

class Sub(Generic_Op):
    def __init__(self, name):
        super().__init__(name)

    def getDerivative(self, a, b, *args, **kwargs):
        return a.getDerivative() - b.getDerivative()

    def __call__(self, a, b):
        return a-b

