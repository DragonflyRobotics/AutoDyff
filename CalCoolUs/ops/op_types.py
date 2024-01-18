from enum import Enum

from CalCoolUs.ops.add import Add
from CalCoolUs.ops.sub import Sub
from CalCoolUs.ops.mul import Mul
from CalCoolUs.ops.var import Var
from CalCoolUs.ops.const import Const
from CalCoolUs.ops.div import Div
from CalCoolUs.ops.pow import Pow
from CalCoolUs.ops.sin import Sin

class OpType(Enum):
    ADD = Add("ADD")
    SUB = Sub("SUB")
    MUL = Mul("MUL")
    DIV = Div("DIV")
    POW = Pow("POW")
#   CONST = Const("Const")
    VAR = Var("Var")
    SIN = Sin("SIN")
