from CalCoolUs.ops.op import Generic_Op

class Var(Generic_Op):
	def __init__(self, name):
		super().__init__(name)

	def getDerivative(self, *args, **kwargs):
		return 1

	def __call__(self, a):
		return a
