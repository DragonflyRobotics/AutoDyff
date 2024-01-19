from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs import *
myShunt = ShuntingYard()


def test_postfix():
    assert myShunt.getPostfix("(2(4x+5))/3") == ["2", "4", "x", "5",  "+", "3", "/"]
    assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("2(1+(1/x))") == ["2", "1", "1", "x", "/", "+"]
    assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]
    assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]
