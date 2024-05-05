from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs import *
myShunt = ShuntingYard()


def test_postfix():
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\left(-1\cdot x\right)}")) == ["2", "-1", "x", "*", "^"]#Passed

    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2\left(1+\left(\frac{1}{x}\right)\right)")) == ["2", "1", "1", "x", "/", "+", "*"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^x-5\cdot x")) == ["2", "x", "^", "5", "x", "*", "-" ]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\frac{1}{x}}")) == ["2", "1", "x", "/", "^"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"x+2")) == ["x", "2", "+"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"-x-2")) == ["-1", "x", "*", "2", "-"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{-x}")) == ["2", "x", "-1", "*", "^"] or myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{-x}")) == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"-\left(\frac{\left(x-\frac{3}{2}\right)}{x+\frac{1}{2}}\right)^{\left(-\frac{3}{2}\right)}")) ==  ['-1', 'x', '3', '2', '/', '-', 'x', '1', '2', '/', '+', '/', '-1', '3', '*', '2', '/', '^', '*']
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\frac{2\left(4\cdot x+5\right)}{3}")) == ["2", "4", "x", "*", "5",  "+", "*", "3", "/"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\left(-1\cdot x\right)}")) == ["2", "-1", "x", "*", "^"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2\left(1+\left(\frac{1}{x}\right)\right)")) == ["2", "1", "1", "x", "/", "+", "*"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^x-5\cdot x")) == ["2", "x", "^", "5", "x", "*", "-" ]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\frac{1}{x}}")) == ["2", "1", "x", "/", "^"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"x+2")) == ["x", "2", "+"]#Passed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\frac{\left(2\left(4x+5\right)\right)}{3}")) == ["2", "4", "x", "*", "5","+", "*", "3", "/"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"-x-2")) == ["-1", "x", "*", "2", "-"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"-\left(-x-1\right)-\left(-2-x\right)")) == ["-1","-1", "x", "*", "1", "-", "*", "-2", "x", "-", "-"]
    #Failed
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\frac{\left(2\left(4x+5\right)\right)}{3}")) == ["2", "4", "x", "*", "5","+", "*", "3", "/"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\left(-1\cdot x\right)}")) == ["2", "-1", "x", "*", "^"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2\left(1+\left(\frac{1}{x}\right)\right)")) == ["2", "1", "1", "x", "/", "+", "*"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^x-5\cdot x")) == ["2", "x", "^", "5", "x", "*", "-"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"2^{\frac{1}{x}}")) == ["2", "1", "x", "/", "^"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"x+2")) == ["x", "2", "+"]
    #Trig
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\sin\left(\sin\left(ex\right)\right)")) == ["2.718281828459045", "x", "*", "sin", "sin"]
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\left(\sin\left(x\right)\right)^2+ \left(\cos\left(x\right)\right)^2")) == ["x", "sin", "2", "^", "x", "cos", "2", "^", "+"]
    #Exponentials and Logarithms
    assert myShunt.getPostfixLatex(myShunt.tokenize_latex(r"\ln\left(x\right)")) == ["x", "ln"]
