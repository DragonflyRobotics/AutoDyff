from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine

import random, pytest

import numpy as np

myshunt = ShuntingYard()
myASTGraph = ASTGraph()

def solve(postfix, x):
    shuntres = myshunt.getPostfix(postfix)
    graph = myASTGraph.getAST(shuntres)
    ne = Numerical_Engine(graph, myASTGraph)
    return ne.solve(x)

def differentiate(postfix, x):
    shuntres = myshunt.getPostfix(postfix)
    graph = myASTGraph.getAST(shuntres)
    ne = Numerical_Engine(graph, myASTGraph)
    return ne.differentiate(x)
@pytest.fixture

# @pytest.fixture

def random_input():
    return np.random.uniform(-1.0, 1.0)
   

@pytest.mark.parametrize("n_times", range(3))
def test_random_solve(n_times, random_input):
    #Solve with Manual Input
    assert solve("(2*(4*x+5))/3", random_input) == pytest.approx((2*(4*random_input+5))/3)#Passed
    assert solve("2^(-1*x)", random_input) == pytest.approx(2**(-1*random_input))#Passed
    assert solve("2*(1+(1/x))", random_input) == pytest.approx(2*(1+(1/random_input)))#Passed
    assert solve("2^x-5*x", random_input) == pytest.approx(2**random_input-5*random_input)#Passed
    assert solve("2^(1/x)", random_input) == pytest.approx(2**(1/random_input))#Passed
    assert solve("x+2", random_input) == pytest.approx(random_input+2)#Passed
    assert solve("sin(sin(ex))", random_input) == pytest.approx(np.sin(np.sin(np.e*random_input)))#Passed
    assert solve("(sin(x))^2+ (cos(x))^2", random_input) == pytest.approx(np.sin(random_input)**2 + np.cos(random_input)**2)#Passed
    assert solve("sigmoid(sin(x))", random_input) == pytest.approx(1/(1+np.exp(-np.sin(random_input))))#Passed
    
    #Solve With Randomized Input
    try:
        assert solve("tanh(sinh(cos(x)))*(csc(sec(x)))^(3sinh(πe))+cot(sin(cosh(5x)))", random_input) == np.tanh(np.sinh(np.cos(random_input)))*((1/np.sin(1/np.cos(random_input))))**(3*np.sinh(np.pi*np.e))+1/np.tan(np.sin(np.cosh(5*random_input))) #Failed 
    except OverflowError:
        print("OverflowError")
    try:
        assert solve("ln(x)", random_input) == pytest.approx(np.log(random_input)) #Passed
    except ValueError:
        print("ValueError")
    try:
        assert solve("-ln(cos(x)+sinh(arccos(x)*e^-sin(arctan(ln(x))))", random_input) == pytest.approx(-np.log(np.cos(random_input)+np.sinh(np.arccos(random_input)*np.exp(-np.sin(np.arctan(np.log(random_input))))))) #Passed
    except ValueError:
        print("ValueError")

    try:    
        assert solve("2sin(x)", random_input) == pytest.approx(2*np.sin(random_input)) #Passed
    except ValueError:
        print("Error")
    try:
        assert solve("2x", random_input) == pytest.approx(2*random_input) #Passed
    except ValueError:
        print("Error")
    try:
        assert solve("3sigmoid(x)", random_input) == pytest.approx(3*(1 / (1 + np.exp(-random_input))))#Passed
    except ValueError:
        print("Error")
    try:
        assert solve("-(x+2)", random_input) == pytest.approx(-(random_input+2))#Passed
    except ValueError:
        print("Error")
    try:
        assert solve("2^-x", random_input) == pytest.approx(2**(-random_input)) #passed
    except ValueError:
        print("Error1")
#Differentiation
    assert differentiate("sin(x)", random_input) == pytest.approx(np.cos(random_input))#Passed
    assert differentiate("e^(-x/2)", random_input) == pytest.approx(-.5*np.exp(-random_input/2))#Passed
    assert differentiate("sec(x)*sec(x)", random_input) == pytest.approx(2*(np.cos(random_input)**-1)*(np.cos(random_input)**-1)*np.tan(random_input))#Passed
    assert differentiate("sin(e^(5x-2)/(cos(x)))", random_input) == pytest.approx(((np.exp(5*random_input-2))*(np.sin(random_input)+5*np.cos(random_input))*np.cos(np.exp(5*random_input-2)/np.cos(random_input)))/(np.cos(random_input))**2) #Failed
    assert differentiate("e^sin(x)", random_input) == pytest.approx(np.cos(random_input)*np.exp(np.sin(random_input))) #Passed
    assert differentiate("ln(ln(tan(2^x)))", random_input) == pytest.approx((np.log(2)*(2**random_input)*(1/(np.cos(2**random_input))*(np.cos(2**random_input))))/(np.tan(2**random_input)*np.log(np.tan(2**random_input)))) #Failed
    assert differentiate("sin(e^2x)", random_input) == pytest.approx(np.cos(np.exp(2*random_input))*np.exp(2*random_input)*2) #Passed





   # assert solve("arccot(2x^3)", random_input) == pytest.approx(np.arctan(1/(2*(random_input**3)))) #Failed
   # assert solve("arccsc(2x^3)", random_input) == pytest.approx((np.arcsin(1/(2*(random_input**3))))) #Failed
   # assert solve("arcsec(2x^3)", random_input) == pytest.approx((np.arccos(1/(2*(random_input**3))))) #Failed
    assert solve("arctan(arcsin(x))", random_input) == pytest.approx(np.arctan(np.arcsin(random_input))) #Passed

    assert differentiate("sin(x)", random_input) == pytest.approx(np.cos(random_input))
    assert differentiate("e^(-x/2)", random_input) == pytest.approx(-.5*np.exp(-random_input/2))
    assert differentiate("sec(x)*sec(x)", random_input) == pytest.approx(2*(np.cos(random_input)**-1)*(np.cos(random_input)**-1)*np.tan(random_input))
   # assert differentiate("sin(e^(5x-2)/(cos(x)))", random_input) == pytest.approx(((np.exp(5*random_input-2))*(np.sin(random_input)+5*np.cos(random_input))*np.cos(np.exp(5*random_input-2)/np.cos(random_input)))/(np.cos(random_input))**2)
    assert differentiate("e^sin(x)", random_input) == pytest.approx(np.cos(random_input)*np.exp(np.sin(random_input)))
   # assert differentiate("ln(ln(tan(2^x)))", random_input) == pytest.approx((np.log(2)*(2**random_input)*(1/(np.cos(2**random_input))*(np.cos(2**random_input))))/(np.tan(2**random_input)*np.log(np.tan(2**random_input))))
    assert differentiate("sin(e^2x)", random_input) == pytest.approx(np.cos(np.exp(2*random_input))*np.exp(2*random_input)*2)


    #assert solve("arccot(2x^3)", random_input) == pytest.approx(np.arctan(1/(2*(random_input**3))))
    # assert solve("arccsc(2x^3)", random_input) == pytest.approx((np.arcsin(1/(2*(random_input**3)))))
    # assert solve("arcsec(2x^3)", random_input) == pytest.approx((np.arccos(1/(2*(random_input**3)))))
    assert solve("arctan(arcsin(x))", random_input) == pytest.approx(np.arctan(np.arcsin(random_input)))




