from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs import *
myShunt = ShuntingYard()

def test_postfix():
<<<<<<< HEAD
    assert myShunt.getPostfix("(2(4x+5))/3") == ["2", "4", "x", "5",  "+", "3", "/"]
    assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("2(1+(1/x))") == ["2", "1", "1", "x", "/", "+"]
    assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]
    assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]
    assert myShunt.getPostfix("-x-2") == ["-1", "x", "*", "2", "-"]
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"] or myShunt.getPostfix("2^-x") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("-(-x-1)-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "*", "-2", "x", "-", "-"]
    assert myShunt.getPostfix("-(-x-1)^-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "-1", "-2", "x", "-", "*", "^", "*"]
    #Failed
    assert myShunt.getPostfix("(-(-x+1))^(-x+3)") == []
    assert myShunt.getPostfix("-((x-3/2)/(x+1/2))^(-3/2)") == []
>>>>>>> 8f07ba72a2457ae17afc3d1282d37783166224b4
