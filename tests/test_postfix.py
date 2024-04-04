from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs import *
myShunt = ShuntingYard()


# Operations in use "+", "-", "/", "*", "^", "sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh"
def test_postfix():




    #Exponentials and Polynomial
    assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfix("2(1+(1/x))") == ["2", "1", "1", "x", "/", "+", "*"]#Passed
    assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]#Passed
    assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]#Passed
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]#Passed
    assert myShunt.getPostfix("-x-2") == ["-1", "x", "*", "2", "-"]#Passed
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"] or myShunt.getPostfix("2^-x") == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfix("-((x-3/2)/(x+1/2))^(-3/2)") == ['-1', 'x', '3', '2', '/', '-', 'x', '1', '2', '/', '+', '/', '-3', '2', '/', '^', '*']#Passed
    assert myShunt.getPostfix("(2*(4*x+5))/3") == ["2", "4", "x", "*", "5",  "+", "*", "3", "/"] #Passed
    assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfix("2*(1+(1/x))") == ["2", "1", "1", "x", "/", "+", "*"]#Passed
    assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]#Passed
    assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]#Passed
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]#Passed

    #assert myShunt.getPostfix("(2(4x+5))/3") == ["2", "4", "x", "*", "5","+", "3", "/", "*"]
    assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("2(1+(1/x))") == ["2", "1", "1", "x", "/", "+", "*"]
    assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]
    assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]
    assert myShunt.getPostfix("-x-2") == ["-1", "x", "*", "2", "-"]
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"] or myShunt.getPostfix("2^-x") == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfix("-((x-3/2)/(x+1/2))^(-3/2)") == ['-1', 'x', '3', '2', '/', '-', 'x', '1', '2', '/', '+', '/', '-3', '2', '/', '^', '*']
   
    assert myShunt.getPostfix("(2*(4*x+5))/3") == ["2", "4", "x", "*", "5",  "+", "*", "3", "/"]

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
    #assert myShunt.getPostfix("(-(-x+1))^(-x+3)") == []
    #assert myShunt.getPostfix("-((x-3/2)/(x+1/2))^(-3/2)") == []
   
    #assert myShunt.getPostfix("(2*(4*x+5))/3") == ["2", "4", "x", "*", "5",  "+", "*", "3", "/"]
    #assert myShunt.getPostfix("2^(-1*x)") == ["2", "-1", "x", "*", "^"]
    #assert myShunt.getPostfix("2*(1+(1/x))") == ["2", "1", "1", "x", "/", "+", "*"]
    #assert myShunt.getPostfix("2^x-5*x") == ["2", "x", "^", "5", "x", "*", "-" ]
    #assert myShunt.getPostfix("2^(1/x)") == ["2", "1", "x", "/", "^"]
    #assert myShunt.getPostfix("x+2") == ["x", "2", "+"]




    #Trig
    assert myShunt.getPostfix("sin(sin(ex))") == ["2.718281828459045", "x", "*", "sin", "sin"]#Passed
    assert myShunt.getPostfix("arcsin(tanh(πx))^csc(1/(2e^(-1/2)))") == ["3.141592653589793", "x", "*", "tanh", "arcsin", "1", "2", "2.718281828459045", "-1", "2", "/", "^", "*", "/", "csc", "^"]#Passed
    assert myShunt.getPostfix("(sin(x))^2+ (cos(x))^2") == ["x", "sin", "2", "^", "x", "cos", "2", "^", "+"]#Passed
    assert myShunt.getPostfix("tanh(sinh(cos(x)))*(csc(sec(x)))^(3sinh(πe))+cot(sin(cosh(5x)))") == ["x", "cos", "sinh", "tanh", "x", "sec", "csc", "3", "3.141592653589793", "2.718281828459045", "*", "sinh", "*", "^", "*", "5", "x", "*", "cosh", "sin", "cot", "+"]#Passed
    #Exponentials and Logarithms
    assert myShunt.getPostfix("ln(x)") == ["x", "ln"]#Passed
    assert myShunt.getPostfix("-ln(cos(x)+sinh(arccos(x)*e^-sin(arctan(ln(x)))))") == ["-1", "x", "cos", "x", "arccos", "2.718281828459045", "-1", "x", "ln", "arctan", "sin", "*", "^", "*", "sinh", "+", "ln", "*"] #Passed
    assert myShunt.getPostfix("2sin(x)") == ["2", "x", "sin", "*"]#Passed
    assert myShunt.getPostfix("2x") == ["2", "x", "*"]#Passed
    assert myShunt.getPostfix("3sigmoid(x)") == ["3", "x", "sigmoid", "*"]#Passed
    assert myShunt.getPostfix("-(x+2)") == ["-1", "x", "2", "+", "*"]#Passed
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"] or myShunt.getPostfix("2^-x") == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfix("-(-x-1)-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "*", "-2", "x", "-", "-"]#Passed
    assert myShunt.getPostfix("-(-x-1)^-(-2-x)") == ["-1","-1", "x", "*", "1", "-", "-1", "-2", "x", "-", "*", "^", "*"]#Passed
    assert myShunt.getPostfix("(-(-x+1))^(-x+3)") == ['-1', '-1', 'x', '*', '1', '+', '*', '-1', 'x', '*', '3', '+', '^']#Passed
    assert myShunt.getPostfix("2((x-3/2)/(x+1/2))^2(-3/2)") == ["2", "x", "3", "2", "/", "-", "x", "1", "2", "/", "+", "/","2", "-3", "2", "/", "*", "^", "*"]#Passed
    assert myShunt.getPostfix("xarccot(2x)")  == ['x', '2', 'x', '*', 'arccot', '*']#Passed
    assert myShunt.getPostfix("5*(arcsec(3x^2))^2") == ['5', '3', 'x', '2', '^', '*', 'arcsec', '2', '^', '*']#Passed
    assert myShunt.getPostfix("2e") == ['2', '2.718281828459045', '*']#Passed
    assert myShunt.getPostfix("arccsc(arcsec(arccot(2x^3)))") == ["2", "x", "3", "^", "*", "arccot", "arcsec", "arccsc"] #Passed

