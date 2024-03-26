from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine
from CalCoolUs.error_types import *
import random, pytest

import numpy as np

myshunt = ShuntingYard()
myASTGraph = ASTGraph()
def test_postfix_errors():
    with pytest.raises(ParenthesisMulError):
        myshunt.tokenize("(x+2)(x)")
        myshunt.tokenize("e^5(x+5)")
        myshunt.tokenize("(x+7)5^4")
        