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

from CalCoolUs.ops.cot import Cot
from CalCoolUs.ops.csc import Csc
from CalCoolUs.ops.sec import Sec

from CalCoolUs.ops.sinh import Sinh
from CalCoolUs.ops.cosh import Cosh
from CalCoolUs.ops.tanh import Tanh
from CalCoolUs.ops.log import Log
from CalCoolUs.ops.ln import Ln
from CalCoolUs.ops.arcsin import Arcsin
from CalCoolUs.ops.arccos import Arccos
from CalCoolUs.ops.arctan import Arctan

from CalCoolUs.ops.arccsc import Arccsc
from CalCoolUs.ops.arcsec import Arcsec
from CalCoolUs.ops.arccot import Arccot

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

    COT = Cot("Cot")
    CSC = Csc("Csc")
    SEC = Sec("Sec")

    SINH = Sinh("Sinh")
    COSH = Cosh("Cosh")
    TANH = Tanh("Tanh")
    LOG = Log("Log")
    LN = Ln("Ln")
    ARCSIN = Arcsin("Arcsin")
    ARCCOS = Arccos("Arccos")
    ARCTAN = Arctan("Arctan")
    
    ARCCSC = Arccsc("Arccsc")
    ARCSEC = Arcsec("Arcsec")
    ARCCOT = Arccot("Arccot")
