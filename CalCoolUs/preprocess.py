import random, string
import networkx as nx
from matplotlib import pyplot as plt
import re

from CalCoolUs.ops.op_types import OpType

from CalCoolUs.ops.var import Var
from CalCoolUs.ops.const import Const
import math
from CalCoolUs.log_init import MainLogger
from CalCoolUs.error_types import *

class ShuntingYard:
    def __init__(self):
        self.operations = ["+", "-", "/", "*", "^"]
        self.funcitons = ["sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid"]
        root_log = MainLogger()
        self.log = root_log.StandardLogger("ShuntingYard")  # Create a script specific logging instance

    
    def tokenize(self, string):
        self.log.info(f"Starting grand tokenizer...")
        string = string.replace(" ", "")
        tokenized = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\^\-\/])", string)
        lowerBound = 0
        upperBound = len(tokenized)
        while lowerBound < upperBound:
            if self.isCoef(tokenized[lowerBound]) == True:
                tokenized = self.splitCoef(tokenized, lowerBound)
                lowerBound += 1
                upperBound += 1
            lowerBound += 1
         
        for index in range(0, len(tokenized)):
            if tokenized[index] == "e":
                tokenized[index] = f"{math.e}"
            if tokenized[index] == "π":
                tokenized[index] = f"{math.pi}"
        '''
        for index in range(0,len(tokenized)):
            value = tokenized[index]
            if value == "-" and index < (len(tokenized) - 1 ):
                assert tokenized[index + 1] != "-", "Can't have two negatives in a row"
            if (self.isfloat(value) == True or value == "x") and index < (len(tokenized) - 1 ):
                assert tokenized[index + 1] != "x", "Coefficients not accepted, use multiplication signs"
                assert tokenized[index + 1] != "(", "Coefficients not accepted, use multiplication signs"
                assert self.isFunction(tokenized[index + 1]) != True, "Coefficients not accepted, use multiplication signs"
            assert(self.isfloat(value) == True or self.isFunction(value) == True or value == "(" or value == ")" or value == "x" or value in self.operations), "Coefficients not accepted, use multiplication signs"
        '''   
        lowerBound = 0
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:
            if tokenized[lowerBound] == "-" and (tokenized[lowerBound - 1] in self.operations or tokenized[lowerBound - 1] == "(" or tokenized[lowerBound - 1] == "-(" or lowerBound == 0):
                token = tokenized[lowerBound + 1]
                tokenized[lowerBound] = f"-{token}"
                tokenized.pop(lowerBound + 1)
                upperBound -=1
            lowerBound += 1
        lowerBound = 0    
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:
            if self.isNegFunction(tokenized[lowerBound]) == True:
                temp = tokenized[lowerBound][1:]
                tokenized[lowerBound] = "-("
                tokenized.insert(lowerBound + 1 , temp)
                end = self.findEnd(tokenized, lowerBound + 3)
                tokenized.insert(end , ")")
                upperBound -=1
            lowerBound += 1
                
        lowerBound = 0
        upperBound = len(tokenized) 
                
        while lowerBound < upperBound:
            if tokenized[lowerBound] == "-x":
                tokenized[lowerBound] = "-("
                tokenized.insert(lowerBound + 1, "x")
                tokenized.insert(lowerBound + 2 , ")")
                lowerBound += 2
                upperBound += 2
            lowerBound += 1 
        lowerBound = 0
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:    
            if tokenized[lowerBound] == "-(":
                original = len(tokenized)
                tokenized = self.negParenth(tokenized, lowerBound)
                change = len(tokenized) - original
                lowerBound += 1
                upperBound += change
            lowerBound += 1
        lowerBound = 0
        upperBound = len(tokenized) - 1
        
        while lowerBound < upperBound:
            higher = tokenized[lowerBound + 1]
            if self.isValue(tokenized[lowerBound]) and (self.isFunction(higher) or higher == "x" or self.isfloat(higher)):
                original = len(tokenized)
                tokenized = self.evalCoef(tokenized, lowerBound)
                lowerBound += 1
                upperBound += len(tokenized)
                upperBound -= original
            lowerBound += 1
        lowerBound = 0
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:
            higher = lowerBound + 1
            isValid = (tokenized[lowerBound] == ")" and (tokenized[higher] == "(" or self.isValue(tokenized[higher]) or self.isFunction(tokenized[higher])))
            if isValid == True:
                raise ParenthesisMulError
            isValid = (tokenized[higher] == "(" and (self.isValue(tokenized[lowerBound]) or tokenized[lowerBound] == ")"))
            if isValid == True:
                raise ParenthesisMulError
            lowerBound += 1
        return tokenized
    def splitCoef(self, inputArray, inputIndex):
        array = list(inputArray[inputIndex])
        check = 0
        number = array[0]
        string = ""
        for index in range(1, len(array)):
            if (self.isAlphanumeric(array[index]) == True or array[index] == "π") and check == 0:
                check += 1
                string += array[index]
            elif check == 1:
                string += array[index]
            elif self.isValue(array[index]) == True or array[index] == ".": 
                
                number += array[index]
        
        inputArray[inputIndex] = number
        inputArray.insert(inputIndex + 1, string)
        return inputArray
    def isCoef(self, string):
        
        array = list(string)
        check = 0
        number = array[0]
        string = ""
        for index in range(1, len(array)):
            if (self.isAlphanumeric(array[index]) == True or array[index] == "π") and check == 0:
                check += 1
                string += array[index]
            elif check == 1:
                string += array[index]
            elif self.isValue(array[index]) == True or array[index] == ".": 
                number += array[index]
        
        
        return (self.isValue(number) == True and number != "-")  and (self.isFunction(string) == True or string == "x" or string == "e" or string == "π")
            
    def negParenth(self, array, startIndex):
        array[startIndex] = "("
        array.insert(startIndex + 1, "-1")
        array.insert(startIndex + 2, "*")
        array.insert(startIndex + 3, "(")
        endIndex = startIndex + 4
        array.insert(self.findEnd(array, endIndex), ")")
        #print(array)
        return array
    def evalCoef(self, array, startIndex):
        
        first = array[startIndex]
        #second = array[startIndex + 1] 
        array[startIndex] = "("
        array.insert(startIndex + 1, first)
        array.insert(startIndex + 2, "*")
        array.insert(startIndex + 3, "(")
        array.insert(startIndex + 5, ")")
        endIndex = startIndex + 6
        end = self.findEnd(array, endIndex)
        array.insert(end, ")")
        
        return array                
    def findEnd(self, array, startIndex):
        endIndex = startIndex
        flag = 1
        while flag != 0:    
            if endIndex == len(array):
                
                return endIndex
            #if endIndex == len(array):
            if array[endIndex] == "(" or array[endIndex] == "-(":
                flag += 1
            if array[endIndex] == ")":
                flag -= 1
            
            endIndex += 1
        endIndex -= 1
        
        if len(array) == endIndex + 1:
            return endIndex    
        
        if array[endIndex + 1] == "^":    
            higher = array[endIndex + 3]
            if array[endIndex + 2] == "(":
                return self.findEnd(array, endIndex + 3)
            if array[endIndex + 2] == "-(":
                return self.findEnd(self.negParenth(array, endIndex + 2), endIndex + 3)
            if self.isValue(array[endIndex + 2]) and (self.isFunction(higher) or higher == "x" or self.isfloat(higher)):
                print("e")
                return self.findEnd(self.evalCoef(array, endIndex + 2), endIndex + 3)
            else: 
                return endIndex + 3        
        return endIndex
    
            
    def isfloat(self, number):
        try:
            float(number)
            return True
        except:
            
            return False
    def isAlphanumeric(self, number):
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for letter in number:
            if letter not in alphabet:
                return False
        return True
    def isFunction(self, string):
        if string in self.funcitons:
            return True
        else:
            return False
    def isValue(self, number):
        return self.isfloat(number) or number == "x" or number == "π" or number == "e"
    def isNegFunction(self, string):
        if string[0] != "-":
            return False
        temp = string[1:]
        if self.isFunction(temp) == False:
            return False
        return True
        
    def precedence(self, operator):
        match operator:
            case "+":
                return 1
            case "-":
                return 1
            case "*":
                return 2
            case "/":
                return 2
            case "^":
                return 3
        return 0

    def getPostfix(self, diffEquation):
        self.log.info(f"Computing postfix of {diffEquation}")
        diffEquation = diffEquation.replace(" ", "")
        diffEquation = self.tokenize(diffEquation)
        outputQueue = []
        operatorStack = []
        for value in diffEquation:
            if self.isfloat(value) or value == "x":
                outputQueue.append(value)
            elif value == "(":
                operatorStack.append(value)

            elif value == ")":
                while operatorStack[-1] != "(":
                    assert (len(operatorStack) != 0)
                    outputQueue.append(operatorStack.pop())
                assert (operatorStack[-1] == "(")
                operatorStack.pop()

                if len(operatorStack) != 0:
                    if self.isFunction(operatorStack[-1]) == True:
                        outputQueue.append(operatorStack.pop())
            elif self.isFunction(value) == True:
                operatorStack.append(value)
            elif value in self.operations:

                while (operatorStack and operatorStack[-1] != "("
                       and self.precedence(operatorStack[-1]) >= self.precedence(value)):
                    outputQueue.append(operatorStack.pop())
                operatorStack.append(value)
            elif self.isFunction(value) == True:
                operatorStack.append(value)
        while operatorStack:
            outputQueue.append(operatorStack.pop())

        self.log.info(f"Computed Output Queue: {outputQueue}")

        return outputQueue


class ASTGraph:
    def __init__(self):
        self.operations = ["+", "-", "/", "*", "^", "sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid"]
        self.unary = ["sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid"]            
        root_log = MainLogger()
        self.log = root_log.StandardLogger("ASTGraph")  # Create a script specific logging instance


    def isValue(self, number):
        return self.isfloat(number) or number == 'x' or isinstance(number, str)

    def isfloat(self, number):
        try:
            float(number)
            return True
        except:
            return False

    def checkForOperators(self, queue):
        for q in queue:
            if q in self.operations:
                return True
        return False

    def returnOperatorName(self, operator, name=""):
        match operator:
            case "+":
                return OpType.ADD
            case "-":
                return OpType.SUB
            case "*":
                return OpType.MUL
            case "/":
                return OpType.DIV
            case "^":
                return OpType.POW
            case "sin":
                return OpType.SIN
            case "cos":
                return OpType.COS
            case "tan":
                return OpType.TAN
            case "sinh":
                return OpType.SINH
            case "cosh":
                return OpType.COSH
            case "tanh":
                return OpType.TANH
            case "log":
                return OpType.LOG
            case "ln":
                return OpType.LN
            case "arcsin":
                return OpType.ARCSIN
            case "arccos":
                return OpType.ARCCOS
            case "arctan":
                return OpType.ARCTAN
            case "cot":
                return OpType.COT
            case "csc":
                return OpType.CSC       
            case "sec":
                return OpType.SEC
            case "arccsc":
                return OpType.ARCCSC
            case "arcsec":
                return OpType.ARCSEC
            case "arccot":
                return OpType.ARCCOT
            case "sigmoid":
                return OpType.SIGMOID
        return "UNK"

    def getAST(self, shuntyardresult):
        assert len(shuntyardresult) > 1
        self.log.info(f"Running AST compute from the Shunt Yard: {shuntyardresult}")
        graph = nx.MultiDiGraph()

        opDict = {}

        while self.checkForOperators(shuntyardresult):
            counter = 0
            while shuntyardresult[counter] not in self.operations:
                counter += 1
            # print(f"Stopped @: {shuntyardresult[counter]}")

            if shuntyardresult[counter] in self.unary:
                if (counter - 1 >= 0 and self.isValue(shuntyardresult[counter - 1])):
                    node_name = self.returnOperatorName(shuntyardresult[counter]).name + "_" + ''.join(
                        random.choices(string.ascii_uppercase +
                                       string.digits, k=3))
                    
                    #else:
                    #    raise RuntimeError(f"Couldn't classify counter-2: {shuntyardresult[counter-2]}")
                    graph.add_edge(str(shuntyardresult[counter - 1]), node_name)
                    if str(shuntyardresult[counter - 1]) == 'x':
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": OpType.VAR.value}})
                    elif self.isfloat(shuntyardresult[counter - 1]):
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": Const("CONST", float(shuntyardresult[counter - 1]))}})
                    #else:
                    #    raise RuntimeError("Couldn't classify counter-1")
                    self.log.info(f"{str(shuntyardresult[counter - 2])} --> {node_name}")
                    self.log.info(f"{str(shuntyardresult[counter - 1])} --> {node_name}")

                    nx.set_node_attributes(graph, {node_name: {"Op": self.returnOperatorName(shuntyardresult[counter]).value}})

                    for _ in range(2):
                        shuntyardresult.pop(counter - 1)
                    shuntyardresult.insert(counter - 1, node_name)

            else:
                if (counter - 2 >= 0 and self.isValue(shuntyardresult[counter - 1]) and self.isValue(shuntyardresult[counter - 2])):
                    node_name = self.returnOperatorName(shuntyardresult[counter]).name + "_" + ''.join(
                        random.choices(string.ascii_uppercase +
                                       string.digits, k=3))
                    print(f"Nodes: {shuntyardresult[counter - 2]} --> {node_name} --> {shuntyardresult[counter - 1]}")
                    if shuntyardresult[counter - 2] == shuntyardresult[counter - 1]:
                        shuntyardresult[counter - 2] = shuntyardresult[counter - 2] + ''.join(random.choices(string.digits, k=3))
                    graph.add_edge(str(shuntyardresult[counter - 2]), node_name)
                    if 'x' in str(shuntyardresult[counter - 2]):
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 2]): {"Op": OpType.VAR.value}})
                    elif self.isfloat(shuntyardresult[counter - 2]):
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 2]): {"Op": Const("CONST", float(shuntyardresult[counter - 2]))}})
                    #else:
                    #    raise RuntimeError(f"Couldn't classify counter-2: {shuntyardresult[counter-2]}")
                    graph.add_edge(str(shuntyardresult[counter - 1]), node_name)
                    if 'x' in str(shuntyardresult[counter - 1]):
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": OpType.VAR.value}})
                    elif self.isfloat(shuntyardresult[counter - 1]):
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": Const("CONST", float(shuntyardresult[counter - 1]))}})
                    #else:
                    #    raise RuntimeError("Couldn't classify counter-1")
                    self.log.info(f"{str(shuntyardresult[counter - 2])} --> {node_name}")
                    self.log.info(f"{str(shuntyardresult[counter - 1])} --> {node_name}")

                    nx.set_node_attributes(graph, {node_name: {"Op": self.returnOperatorName(shuntyardresult[counter]).value}})

                    for _ in range(3):
                        shuntyardresult.pop(counter - 2)
                    shuntyardresult.insert(counter - 2, node_name)
                

        return graph

    def saveGraph(self, graph, filename):
        self.log.info(f"Saving graph to {filename}")
        pos = nx.planar_layout(graph, scale=40)
        nx.draw_networkx(graph, pos=pos, with_labels=True)
        plt.savefig(filename)
    def getFinalNode(self, graph):
        for n in graph.nodes:
            #print(graph.degree[n])
            if graph.out_degree[n] <= 0:
                self.log.info(f"Got final node called {n}")
                return n
            else:
                pass
    def getNodes(self, graph):
        return (list(nx.all_simple_paths(graph, source='x', target=self.getFinalNode(graph))))
    def displayGraph(self, graph):
        pos = nx.planar_layout(graph, scale=40)
        nx.draw_networkx(graph, pos=pos, with_labels=True)
        plt.show(bbox_inches='tight')
#class AutoDiff:
    
    

