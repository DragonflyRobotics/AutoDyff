from CalCoolUs.preprocess import ShuntingYard

equation = "tanh(sinh(cos(x)))*(csc(sec(x)))^(3sinh(πe))+cot(sin(cosh(5x)))" 
myShunt = ShuntingYard()
print(myShunt.getPostfix(equation))
