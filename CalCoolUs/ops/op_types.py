from enum import Enum

from CalCoolUs.ops.add import Add
from CalCoolUs.ops.sub import Sub
from CalCoolUs.ops.var import Var
from CalCoolUs.ops.const import Const

class OpType(Enum):
	ADD = Add("ADD")
	SUB = 1 #Sub("works_again?")
	MUL = 2
	DIV = 3
	POW = 4
	CONST = Const("Const")
	VAR = Var("Var")