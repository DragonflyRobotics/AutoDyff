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
def random_input():
    return np.random.uniform(-1.0, 1.0)
   

@pytest.mark.parametrize("n_times", range(10))
def test_random_solve(n_times, random_input):
    
    assert solve("(2*(4*x+5))/3", random_input) == pytest.approx((2*(4*random_input+5))/3)#test1
    assert solve("2^(-1*x)", random_input) == pytest.approx(2**(-1*random_input))
    assert solve("2*(1+(1/x))", random_input) == pytest.approx(2*(1+(1/random_input)))
    assert solve("2^x-5*x", random_input) == pytest.approx(2**random_input-5*random_input)
    assert solve("2^(1/x)", random_input) == pytest.approx(2**(1/random_input))
    assert solve("x+2", random_input) == pytest.approx(random_input+2)
    assert solve("sin(sin(ex))", random_input) == pytest.approx(np.sin(np.sin(np.e*random_input)))
    assert solve("(sin(x))^2+ (cos(x))^2", random_input) == pytest.approx(np.sin(random_input)**2 + np.cos(random_input)**2)
    assert solve("sigmoid(sin(x))", random_input) == pytest.approx(1/(1+np.exp(-np.sin(random_input))))
    
    #try:
    #    assert solve("tanh(sinh(cos(x)))*(csc(sec(x)))^(3sinh(πe))+cot(sin(cosh(5x)))", random_input) == np.tanh(np.sinh(np.cos(random_input)))*((1/np.sin(1/np.cos(random_input))))**(3*np.sinh(np.pi*np.e))+1/np.tan(np.sin(np.cosh(5*random_input)))
    #except OverflowError:
    #    print("OverflowError")
    try:
        assert solve("ln(x)", random_input) == pytest.approx(np.log(random_input))
    except ValueError:
        print("ValueError")
    try:
        assert solve("-ln(cos(x)+sinh(arccos(x)*e^-sin(arctan(ln(x))))", random_input) == pytest.approx(-np.log(np.cos(random_input)+np.sinh(np.arccos(random_input)*np.exp(-np.sin(np.arctan(np.log(random_input)))))))
    except ValueError:
        print("ValueError")
    assert solve("2sin(x)", random_input) == pytest.approx(2*np.sin(random_input))
    assert solve("2x", random_input) == pytest.approx(2*random_input)
    assert solve("3sigmoid(x)", random_input) == pytest.approx(3*(1 / (1 + np.exp(-random_input))))
    assert solve("-(x+2)", random_input) == pytest.approx(-(random_input+2))
    assert solve("2^-x", random_input) == pytest.approx(2**(-random_input))
    assert differentiate("sin(x)", random_input) == pytest.approx(np.cos(random_input))
    assert differentiate("e^(-x/2)", random_input) == pytest.approx(-.5*np.exp(-random_input/2))
    assert differentiate("sec(x)*sec(x)", random_input) == pytest.approx(2*(np.cos(random_input)**-1)*(np.cos(random_input)**-1)*np.tan(random_input))
    #assert differentiate("sin(e^(5x-2)/(cos(x)))", random_input) == pytest.approx(((np.exp(5*random_input-2))*(np.sin(random_input)+5*np.cos(random_input))*np.cos(np.exp(5*random_input-2)/np.cos(random_input)))/(np.cos(random_input))**2)
    assert differentiate("e^sin(x)", random_input) == pytest.approx(np.cos(random_input)*np.exp(np.sin(random_input)))
    #assert differentiate("ln(ln(tan(2^x)))", random_input) == pytest.approx((np.log(2)*(2**random_input)*(1/(np.cos(2**random_input))*(np.cos(2**random_input))))/(np.tan(2**random_input)*np.log(np.tan(2**random_input))))
    assert differentiate("sin(e^2x)", random_input) == pytest.approx(np.cos(np.exp(2*random_input)))
