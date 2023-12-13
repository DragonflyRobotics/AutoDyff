from CalCoolUs.ops.op import Generic_Op
<<<<<<< HEAD

class Var(Generic_Op):
	def __init__(self, name):
		super().__init__(name)

	def getDerivative(self, *args, **kwargs):
		return 1

	def __call__(self, a):
		return a

=======
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
>>>>>>> 72e2775e10c085db109dccc99e87c25c780b1226
