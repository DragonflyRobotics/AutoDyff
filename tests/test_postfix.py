from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs import *
myShunt = ShuntingYard()

def test_postfix():
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]
    assert myShunt.getPostfix("-x-2") == ["-1", "x", "*", "2", "-"]
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"] or myShunt.getPostfix("2^-x") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("-(-x-1)-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "*", "-2", "x", "-", "-"]
    assert myShunt.getPostfix("-(-x-1)^-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "-1", "-2", "x", "-", "*", "^", "*"]
    #Failed
    assert myShunt.getPostfix("(-(-x+1))^(-x+3)") == []
    assert myShunt.getPostfix("-((x-3/2)/(x+1/2))^(-3/2)") == []
