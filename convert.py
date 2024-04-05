
#print(myShunt.getPostfix("-x"))


# for o in operations:
#     print(f"|({o})", end="")
#

"""
^[^\d]*(\d+\.\d+)|((?<!=\.)\d+(?!=\.))
^(-(?=...))(sin)|(\()|(\))|$



(sin)|(cos)|(tan)|(ln)|(log)|(arcsin)|(arccos)|(arctan)|(cot)|(csc)|(sec)|(sinh)|(cosh)|(tanh)|(arccsc)|(arcsec)|(arccot)|(sigmoid)|(sqrt)|(\()|(\))|(\d+\.\d+)|(\d+(?!=\.)(?<!=\.))|(x)|(e)|(\^)|(\*)|(\/)|(\+)|(-)
"""

import re

regex = r"(sin)|(cos)|(tan)|(ln)|(log)|(arcsin)|(arccos)|(arctan)|(cot)|(csc)|(sec)|(sinh)|(cosh)|(tanh)|(arccsc)|(arcsec)|(arccot)|(sigmoid)|(sqrt)|(\()|(\))|(\d+\.\d+)|(\d+(?!=\.)(?<!=\.))|(x)|(e)|(\^)|(\*)|(\/)|(\+)|(-)"
pattern = re.compile(regex)
#a = re.findall(regex, "sin(x)+2.5*x^2-3.5")
tokenized = [] 
for m in pattern.finditer("sin(x)+2.5*x^2-3.5"):
    tokenized.append(m.group())
print(tokenized)
