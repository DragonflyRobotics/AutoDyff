from enum import Enum

from CalCoolUs.ops.add import Add
from CalCoolUs.ops.sub import Sub
from CalCoolUs.ops.mul import Mul
from CalCoolUs.ops.var import Var
from CalCoolUs.ops.const import Const
from CalCoolUs.ops.div import Div
from CalCoolUs.ops.pow import Pow
from CalCoolUs.ops.sin import Sin
from CalCoolUs.ops.cos import Cos
from CalCoolUs.ops.tan import Tan
from CalCoolUs.ops.log import Log
from CalCoolUs.ops.ln import Ln

class OpType(Enum):
    ADD = Add("ADD")
    SUB = Sub("SUB")
    MUL = Mul("MUL")
    DIV = Div("DIV")
    POW = Pow("POW")
#   CONST = Const("Const")
    VAR = Var("Var")
    SIN = Sin("Sis")
    COS = Cos("Cos")
    TAN = Tan("Tan")
    LOG = Log("Log")
    LN = Ln("Ln")
