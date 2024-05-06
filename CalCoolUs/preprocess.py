import random, string # For random string generation
import networkx as nx # Importing networkx for graph operations
from matplotlib import pyplot as plt # Importing pyplot for plotting
import re   # Importing regular expression

from CalCoolUs.ops.op_types import OpType # Importing the OpType class from the op_types.py file

from CalCoolUs.ops.const import Const # Importing the Const class from the const.py file
import math # Importing math for mathematical operations
from CalCoolUs.log_init import MainLogger # Importing the MainLogger class from the log_init.py file
from CalCoolUs.error_types import * # Importing all error types from the error_types.py file

import io, cv2
from PIL import Image
import numpy as np

class ShuntingYard:
    def __init__(self):
        self.operations = ["+", "-", "/", "*", "^"] # List of operations
        self.funcitons = ["sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid", "sqrt"] # List of functions
        root_log = MainLogger() # Creating a MainLogger instance
        self.log = root_log.StandardLogger("ShuntingYard")  # Create a script specific logging instance
        self.regex_latex = r"(\\sin(?!h))|(\\cos(?!h))|(\\tan(?!h))|(\\ln)|(\\log)|(\\arcsin)|(\\arccos)|(\\arctan)|(\\cot)|(\\csc)|(\\sec)|(\\sinh)|(\\cosh)|(\\tanh)|(\\arccsc)|(\\arcsec)|(\\arccot)|(\\sigmoid)|(\\sqrt)|((?<=\))-(?=.*))|({)|(})|(\\left\()|(\\right\))|(\d+\.\d+)|((?<!=\.)\d+(?!=\.))|((?<=\B)-\d+\.\d+)|((?<=\B)(?<!=\.)-\d+(?!=\.))|(x|(?<=\B)-x)|(e)|(\\pi)|(\^)|(\\cdot)|(\\frac)|(\+)|(-\()|(-)" 

        regex = r"(sin(?!h))|(cos(?!h))|(tan(?!h))|(ln)|(log)|(arcsin)|(arccos)|(arctan)|(cot)|(csc)|(sec)|(sinh)|(cosh)|(tanh)|(arccsc)|(arcsec)|(arccot)|(sigmoid)|(sqrt)|((?<=\))-(?=.*))|(\()|(\))|(\d+\.\d+)|((?<!=\.)\d+(?!=\.))|((?<=\B)-\d+\.\d+)|((?<=\B)(?<!=\.)-\d+(?!=\.))|(x|(?<=\B)-x)|(e)|(π)|(\^)|(\*)|(\/)|(\+)|(-\()|(-)"
        self.pattern = re.compile(regex)
        self.pattern_latex = re.compile(self.regex_latex)

    def tokenize(self, string): # Function to tokenize the input string
        # Logging
        self.log.info(f"Starting grand tokenizer...")

        # Remove spaces in function
        string = string.replace(" ", "") # Removing spaces from the string

        tokenized = [] 
        for m in self.pattern.finditer(string):
            if m.group() == "e":
                tokenized.append(f"{math.e}")
            elif m.group() == "π":
                tokenized.append(f"{math.pi}")
            else:
                tokenized.append(m.group())
                print(m.group())
        # if there is no parenthesis after e, throw error
        #if tokenized.count("(") != tokenized.count(")"):
        #    raise ParenthesisError
        for index in range(0, len(tokenized)-1):
            if tokenized[index] == ")" and (tokenized[index + 1] == "x" or self.isfloat(tokenized[index + 1])):
                tokenized.insert(index + 1, "*") # Experimental
                raise ParenthesisMulError
        # check for coefficients of x and manually add *
        for index in range(0, len(tokenized)-1):
            if tokenized[index + 1] == "x":
                if self.isfloat(tokenized[index]):
                    tokenized.insert(index + 1, "*")
        for index in range(0, len(tokenized)-1):
            if self.isfloat(tokenized[index]):
                if tokenized[index+1] == "(":
                    tokenized.insert(index + 1, "*")
        # replace -x with -1*x
        while "-x" in tokenized or "-(" in tokenized:
            for index in range(0, len(tokenized)):
                if tokenized[index] == "-x":
                    tokenized[index] = "("
                    tokenized.insert(index + 1, "-1")
                    tokenized.insert(index + 2, "*")
                    tokenized.insert(index + 3, "x")
                    tokenized.insert(index + 4, ")")
                if tokenized[index] == "-(":
                    tokenized[index] = "-1"
                    tokenized.insert(index + 1, "*")
                    tokenized.insert(index + 2, "(")
        # replace numer number with number * number
        for index in range(0, len(tokenized)-1):
            if self.isfloat(tokenized[index]) and self.isfloat(tokenized[index+1]):
                tokenized.insert(index+1, "*")
                print("inserted *")
        # replace 3 trig with 3*trig
        for index in range(0, len(tokenized)-1):
            if self.isfloat(tokenized[index]) and tokenized[index+1] in self.funcitons:
                tokenized.insert(index+1, "*")
                print("inserted *")
        # replace -function with -1*function
        for index in range(0, len(tokenized)-1):
            if tokenized[index] == "-" and tokenized[index+1] in self.funcitons:
                tokenized[index] = "-1"
                tokenized.insert(index+1, "*")
        # check if it is e^(...) or e^... and throw error if it is the later
        for index in range(0, len(tokenized)-1):
            if tokenized[index] == f"{math.e}" and tokenized[index+1] == "^":
                if tokenized[index+2] == "(":
                    pass
                else:
                    print(f"{tokenized[index]}, {tokenized[index+1]}, {tokenized[index+2]}") 
                    raise AmbiguousFunction
        print(tokenized)
        return tokenized
    def findParenthEnd(self,array,startIndex):
        flag = 1
        endIndex = startIndex + 2 
        while flag != 0:

            if array[endIndex] == ")":
                flag -= 1
            if array[endIndex] == "(":
                flag += 1
            endIndex += 1
        return endIndex
    def tokenize_latex(self,string):

        pattern = self.pattern_latex
        tokenized = []
        #Converts the LaTeX into readable mathametical tokens

        for m in pattern.finditer(string):

            token = m.group()
            token = token.replace("\\","")
            if token == "cdot":
                token = "*"
            if token == "{":
                token = "("
            if token == "}":
                token = ")"
            if token == "left(":
                token = "("
            if token == "right)":
                token = ")"
            tokenized.append(token)

        #Turns all fraction symbols into division
        for index in range(len(tokenized)):
            if tokenized[index] == "frac":
                tokenized.insert(self.findParenthEnd(tokenized,index),"/")
                tokenized.pop(index)
        lowerBound = 0 
        upperBound = len(tokenized) - 1

        #Replaces mathametical constants with their real value 
        for index in range(0, len(tokenized)):
            if tokenized[index] == "e":
                tokenized[index] = f"{math.e}"
            if tokenized[index] == "π" or tokenized[index] == "pi":
                tokenized[index] = f"{math.pi}"


        #Converts coeffecients statements by putting mulptiplcation signs between statements without multiplication signs
        while lowerBound < upperBound:
            higher = tokenized[lowerBound + 1]

            if (self.isValue(tokenized[lowerBound]) or tokenized[lowerBound] == ")") and (higher == "(" or self.isFunction(higher) or higher == "x" or self.isValue(higher)):
                original = len(tokenized)
                tokenized.insert(lowerBound + 1, "*")
                lowerBound += 1
                upperBound += len(tokenized)
                upperBound -= original
            lowerBound += 1
        #Converts negative functions and values by multiplying functions and values by -1 
        if tokenized[0] == "-":
            temp = tokenized[1]
            tokenized[0] = "-1"
            tokenized.insert(1, "*")
        if tokenized[0] == "-x":
            tokenized[0] = "-1"
            tokenized.insert(1, "*")
            tokenized.insert(2,"x")
        lowerBound = 1
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:

            if tokenized[lowerBound] == "-x":
                tokenized[lowerBound] = "-1"
                tokenized.insert(lowerBound + 1, "*")
                tokenized.insert(lowerBound + 2, "x")
                lowerBound + 2
                upperBound + 2
            lower = tokenized[lowerBound - 1]
            if (tokenized[lowerBound] == "-" and (lower == "(")) or (tokenized[lowerBound - 1] in self.operations and tokenized[lowerBound] == "-"):
                tokenized[lowerBound] = "-1"

                tokenized.insert(lowerBound + 1 , "*")

                lowerBound += 2
                upperBound += 2
            lowerBound += 1
        #Checks for invalid input and returns comprehensive error messages to user 
        for index in range(len(tokenized)):
            currentElement = tokenized[index]
            if self.isFunction(currentElement):
                if index == len(tokenized) - 1:
                    raise InvalidFunctionFormat
                if tokenized[index + 1] != "(":
                    raise InvalidFunctionFormat
            if currentElement == "(":
                if tokenized[index + 1] == ")":
                    raise EmptyExpression
            if currentElement == "*" or currentElement == "+":
                if index == 0 or index == len(tokenized) - 1:
                    raise UndefinedArguments
                previousElement = tokenized[index - 1]
                nextElement = tokenized[index + 1]
                if previousElement == "(" or self.isFunction(previousElement) == True or previousElement in self.operations or nextElement == ")" or nextElement in self.operations:
                    raise UndefinedArguments
        return tokenized

    def tokenize_aryan_edition(self, string): # Function to tokenize the input string
        # Logging
        self.log.info(f"Starting grand tokenizer...")

        # Remove spaces in function
        string = string.replace(" ", "") # Removing spaces from the string

        # Tokenize using regular expression, spliting operations, functions, constants, and variables
        tokenized = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\^\-\/])", string) # Tokenizing the string

        # Convert special constants like 'e' and 'π' to their mathematical values
        for index in range(0, len(tokenized)):
            if tokenized[index] == "e":
                tokenized[index] = f"{math.e}"
            if tokenized[index] == "π":
                tokenized[index] = f"{math.pi}"

        # Split coefficients if they are attached to functions, parentheses, or x 
        lowerBound = 0
        upperBound = len(tokenized)
        while lowerBound < upperBound:
            if self.isCoef(tokenized[lowerBound]) == True:
                tokenized = self.splitCoef(tokenized, lowerBound)
                lowerBound += 1
                upperBound += 1
            lowerBound += 1

        # Handles negative signs for negative constants and adds them to other negative expressions such as -cos(x), -x, -(x+1)^2
        lowerBound = 0
        upperBound = len(tokenized) - 1
        while lowerBound < upperBound:
            if tokenized[lowerBound] == "-" and (tokenized[lowerBound - 1] in self.operations or tokenized[lowerBound - 1] == "(" or tokenized[lowerBound - 1] == "-(" or lowerBound == 0):
                token = tokenized[lowerBound + 1]
                tokenized[lowerBound] = f"-{token}"
                tokenized.pop(lowerBound + 1)
                upperBound -=1
            lowerBound += 1

        # Handle negative functions like -cos(x)
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

        # Handle '-x' notation
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

        # Handle '-(' notation
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

        # Handle coefficients multiplication
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

        # Check for invalid combinations of parentheses and values
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
        #splits a coeffecient into its 2 parts by checking when the first part ends and the second part begins
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
        #splits a string into 2 through the use of coeffecient proprties
        for index in range(1, len(array)):
            if (self.isAlphanumeric(array[index]) == True or array[index] == "π") and check == 0:
                check += 1
                string += array[index]
            elif check == 1:
                string += array[index]
            elif self.isValue(array[index]) == True or array[index] == ".": 
                number += array[index]
        #determines whether the 2 parts are valid expressions
        return (self.isValue(number) == True and number != "-")  and (self.isFunction(string) == True or string == "x" or string == "e" or string == "π")

    def negParenth(self, array, startIndex):
        #replaces a negative expression from the form "-expression" to the form (-1*expression)
        array[startIndex] = "("
        array.insert(startIndex + 1, "-1")
        array.insert(startIndex + 2, "*")
        array.insert(startIndex + 3, "(")
        endIndex = startIndex + 4
        #finds the place where the first parenthesis should stop by checking for coeffecients, other parnethesis, functions
        array.insert(self.findEnd(array, endIndex), ")")
        #print(array)
        return array
    def evalCoef(self, array, startIndex):
        #replaces a coeffecient expression from the form ab to a*b without changing prorpeties of the whole expression
        first = array[startIndex]
        #second = array[startIndex + 1] 
        array[startIndex] = "("
        array.insert(startIndex + 1, first)
        array.insert(startIndex + 2, "*")
        array.insert(startIndex + 3, "(")

        endIndex = startIndex + 3
        #determines where to end the first parnethesis based on exponenets, other coeffeceints, other parenthesis, functions
        end = self.findCoefEnd(array, endIndex)

        array.insert(end, ")")

        endIndex = end
        #determines where to end the scoend parenthesis based on exponenets, other coeffeceints, other parenthesis, functions
        end = self.findCoefEnd(array, endIndex) - 1

        array.insert(end, ")")

        return array                
    def findCoefEnd(self, array, startIndex):
        # Initialize endIndex and flag
        endIndex = startIndex + 1
        flag = 1
        #print(array)
        #print(endIndex)
        while flag != 0:            
            # If the loop is at the end of the array, return 2 after the end
            if endIndex >= (len(array) - 1):
                return (len(array)) + 1

            higher = array[endIndex + 1]
            # If the current element is a function, look within the function for the new inner parnthesis set and add 1  
            if self.isFunction(array[endIndex]):
                return self.findEnd(array, endIndex + 2) + 1
                # If the currenet element is ')', the coef parnthesis group ends 2 after the current index 
            elif higher == ")":
                return endIndex + 2
                # If the current element is '^', find the end of the exponent expression
            elif array[endIndex] == "^":
                return self.findCoefEnd(array, endIndex + 1)
                # If the currene element is '(', add 1 to the flag as a new set of parenthesis has started
            elif array[endIndex] == "(":
                flag += 1
                # If the current element is a value and the next element is a function, 'x', or a float, increment the flag
            elif self.isValue(array[endIndex]) and (self.isFunction(higher) or higher == "x" or self.isfloat(higher)):
                flag += 1
            else:
                # Increment endIndex and decrement flag
                endIndex += 1

            endIndex += 1

        # Decrement endIndex
        endIndex -= 1

        # If the end of the array is reached, return endIndex
        if len(array) == endIndex + 1:
            return endIndex

        return endIndex
    def findEnd(self, array, startIndex):
        # Initialize endIndex and flag
        endIndex = startIndex
        flag = 1

        # Loop until flag becomes 0
        while flag != 0:
            # Check if endIndex has reached the end of the array
            if endIndex == len(array):
                return endIndex

            # Increment or decrement flag based on the current element
            if array[endIndex] == "(" or array[endIndex] == "-(":
                flag += 1
            elif array[endIndex] == ")":
                flag -= 1

            # Move to the next element in the array
            endIndex += 1

            # Decrement endIndex
            endIndex -= 1

            # If the end of the array is reached, return endIndex
            if len(array) == endIndex + 1:
                return endIndex

            # If the next element after endIndex is '^', handle exponent expressions
            if array[endIndex + 1] == "^":
                if len(array) > endIndex + 2:
                    return endIndex + 3
                higher = array[endIndex + 3]

                # If the exponent expression starts with '(', find its end
                if array[endIndex + 2] == "(":
                    return self.findEnd(array, endIndex + 3)

                # If the exponent expression starts with '-(', handle negative parentheses
                if array[endIndex + 2] == "-(":
                    return self.findEnd(self.negParenth(array, endIndex + 2), endIndex + 3)

                # If the exponent expression starts with a value and is followed by a function, 'x', or float, evaluate the coefficient
                if self.isValue(array[endIndex + 2]) and (self.isFunction(higher) or higher == "x" or self.isfloat(higher)):
                    return self.findEnd(self.evalCoef(array, endIndex + 2), endIndex + 3)
                else: 
                    # Otherwise, return the index after the exponent expression
                    return endIndex + 3

        return endIndex

    def isfloat(self, number):
        #return if the function is a float or not
        try:
            float(number)
            return True
        except:

            return False
    def isAlphanumeric(self, number):
        #return if the funciton is made of alphabet letters or not
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for letter in number:
            if letter not in alphabet:
                return False
        return True
    def isFunction(self, string):
        #return if the function is in our valid list of functions
        if string in self.funcitons:
            return True
        else:
            return False
    def isValue(self, number):
        #return if the function can have a value or not
        return self.isfloat(number) or number == "x" or number == "π" or number == "e"
    def isNegFunction(self, string):
        #determine if the string is in the form -function()
        if string[0] != "-":
            return False
        temp = string[1:]
        if self.isFunction(temp) == False:
            return False
        return True

    def precedence(self, operator):
        #return the precedence of the operation based on PEMDAS
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

    def getPostfixLatex(self, tokens):
        # Logging
        #        self.log.info(f"Computing postfix of {diffEquation}")

        # Remove spaces and tokenize the differential equation
        #diffEquation = diffEquation.replace(" ", "")
        diffEquation = tokens#self.tokenize(diffEquation)

        # Initialize output queue and operator stack
        outputQueue = []
        operatorStack = []

        # Iterate through each token in the differential equation
        for value in diffEquation:
            # If the token is a float or 'x', add it to the output queue
            if self.isfloat(value) or value == "x":
                outputQueue.append(value)
                # If the token is '(', push it onto the operator stack
            elif value == "(":
                operatorStack.append(value)
                # If the token is ')', pop operators from the stack onto the output queue until '(' is encountered
            elif value == ")":
                while operatorStack[-1] != "(":
                    assert (len(operatorStack) != 0)
                    outputQueue.append(operatorStack.pop())
                assert (operatorStack[-1] == "(")
                operatorStack.pop()

                # If the next token on the stack is a function, pop it onto the output queue
                if len(operatorStack) != 0:
                    if self.isFunction(operatorStack[-1]) == True:
                        outputQueue.append(operatorStack.pop())
                # If the token is a function, push it onto the operator stack
            elif self.isFunction(value) == True:
                operatorStack.append(value)
                # If the token is an operator, pop operators from the stack onto the output queue
                # until the stack is empty, '(' is encountered, or the precedence of the operator
                # at the top of the stack is lower than the current operator
            elif value in self.operations:
                while (operatorStack and operatorStack[-1] != "("
                       and self.precedence(operatorStack[-1]) >= self.precedence(value)):
                    outputQueue.append(operatorStack.pop())
                operatorStack.append(value)
                # If the token is a function, push it onto the operator stack
            elif self.isFunction(value) == True:
                operatorStack.append(value)

        # Pop any remaining operators from the stack onto the output queue
        while operatorStack:
            outputQueue.append(operatorStack.pop())

        # Logging
        self.log.info(f"Computed Output Queue: {outputQueue}")

        return outputQueue


    def getPostfix(self, diffEquation):
        # Logging
        self.log.info(f"Computing postfix of {diffEquation}")

        # Remove spaces and tokenize the differential equation
        diffEquation = diffEquation.replace(" ", "")
        diffEquation = self.tokenize(diffEquation)

        # Initialize output queue and operator stack
        outputQueue = []
        operatorStack = []

        # Iterate through each token in the differential equation
        for value in diffEquation:
            # If the token is a float or 'x', add it to the output queue
            if self.isfloat(value) or value == "x":
                outputQueue.append(value)
                # If the token is '(', push it onto the operator stack
            elif value == "(":
                operatorStack.append(value)
                # If the token is ')', pop operators from the stack onto the output queue until '(' is encountered
            elif value == ")":
                while operatorStack[-1] != "(":
                    assert (len(operatorStack) != 0)
                    outputQueue.append(operatorStack.pop())
                assert (operatorStack[-1] == "(")
                operatorStack.pop()

                # If the next token on the stack is a function, pop it onto the output queue
                if len(operatorStack) != 0:
                    if self.isFunction(operatorStack[-1]) == True:
                        outputQueue.append(operatorStack.pop())
                # If the token is a function, push it onto the operator stack
            elif self.isFunction(value) == True:
                operatorStack.append(value)
                # If the token is an operator, pop operators from the stack onto the output queue
                # until the stack is empty, '(' is encountered, or the precedence of the operator
                # at the top of the stack is lower than the current operator
            elif value in self.operations:
                while (operatorStack and operatorStack[-1] != "("
                       and self.precedence(operatorStack[-1]) >= self.precedence(value)):
                    outputQueue.append(operatorStack.pop())
                operatorStack.append(value)
                # If the token is a function, push it onto the operator stack
            elif self.isFunction(value) == True:
                operatorStack.append(value)

        # Pop any remaining operators from the stack onto the output queue
        while operatorStack:
            outputQueue.append(operatorStack.pop())

        # Logging
        self.log.info(f"Computed Output Queue: {outputQueue}")

        return outputQueue


class ASTGraph:
    def __init__(self):
        self.operations = ["+", "-", "/", "*", "^", "sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid", "sqrt"] # List of operations
        self.unary = ["sin", "cos", "tan", "ln", "log", "arcsin", "arccos", "arctan", "cot", "csc", "sec", "sinh", "cosh", "tanh", "arccsc", "arcsec", "arccot", "sigmoid", "sqrt"] # List of unary operations
        root_log = MainLogger() # Creating a MainLogger instance
        self.log = root_log.StandardLogger("ASTGraph")  # Create a script specific logging instance


    def isValue(self, number): # Function to check if a number is a float or 'x'
        return self.isfloat(number) or number == 'x' or isinstance(number, str)

    def isfloat(self, number): # Function to check if a number is a float
        try:
            float(number)
            return True
        except:
            return False

    def checkForOperators(self, queue): # Function to check if there are any operators in the queue
        for q in queue:
            if q in self.operations:
                return True
        return False

    def returnOperatorName(self, operator, name=""): # Function to return the operator name
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
            case "sqrt":
                return OpType.SQRT
        return "UNK"

    def getAST(self, shuntyardresult): # Function to get the AST from the Shunt Yard result
        if len(shuntyardresult) <= 1:
            raise EquationTooShort
        self.log.info(f"Running AST compute from the Shunt Yard: {shuntyardresult}")
        graph = nx.MultiDiGraph() # Creating a MultiDiGraph

        opDict = {} # Dictionary to store the operator nodes

        while self.checkForOperators(shuntyardresult): # While there are operators in the queue
            counter = 0 # Counter to keep track of the position in the queue
            while shuntyardresult[counter] not in self.operations: # While the current element is not an operator
                counter += 1 # Increment the counter
            # print(f"Stopped @: {shuntyardresult[counter]}")

            if shuntyardresult[counter] in self.unary: # If the operator is unary
                if (counter - 1 >= 0 and self.isValue(shuntyardresult[counter - 1])): # If the previous element is a value
                    node_name = self.returnOperatorName(shuntyardresult[counter]).name + "_" + ''.join(
                        random.choices(string.ascii_uppercase +
                            string.digits, k=3)) # Generate a random node name

                    #else:
                    #    raise RuntimeError(f"Couldn't classify counter-2: {shuntyardresult[counter-2]}")
                    graph.add_edge(str(shuntyardresult[counter - 1]), node_name) # Add an edge from the previous element to the current node
                    if str(shuntyardresult[counter - 1]) == 'x': # If the previous element is 'x'
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": OpType.VAR.value}}) # Set the node attribute to 'x'
                    elif self.isfloat(shuntyardresult[counter - 1]): # If the previous element is a float
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": Const("CONST", float(shuntyardresult[counter - 1]))}}) # Set the node attribute to the float
                    #else:
                    #    raise RuntimeError("Couldn't classify counter-1")
                    self.log.info(f"{str(shuntyardresult[counter - 2])} --> {node_name}")
                    self.log.info(f"{str(shuntyardresult[counter - 1])} --> {node_name}")

                    nx.set_node_attributes(graph, {node_name: {"Op": self.returnOperatorName(shuntyardresult[counter]).value}}) # Set the node attribute to the operator

                    for _ in range(2): # Pop the previous element
                        shuntyardresult.pop(counter - 1) # Pop the previous element
                    shuntyardresult.insert(counter - 1, node_name) # Insert the current node

            else: # If the operator is binary
                if (counter - 2 >= 0 and self.isValue(shuntyardresult[counter - 1]) and self.isValue(shuntyardresult[counter - 2])): # If the previous two elements are values
                    node_name = self.returnOperatorName(shuntyardresult[counter]).name + "_" + ''.join(
                        random.choices(string.ascii_uppercase +
                            string.digits, k=3)) # Generate a random node name
                    print(f"Nodes: {shuntyardresult[counter - 2]} --> {node_name} --> {shuntyardresult[counter - 1]}") 
                    if shuntyardresult[counter - 2] == shuntyardresult[counter - 1]: # If the previous two elements are the same
                        shuntyardresult[counter - 2] = shuntyardresult[counter - 2] + ''.join(random.choices(string.digits, k=3)) # Add a random number to the previous element
                    graph.add_edge(str(shuntyardresult[counter - 2]), node_name) # Add an edge from the previous two elements to the current node
                    if 'x' in str(shuntyardresult[counter - 2]): # If the previous element is 'x'
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 2]): {"Op": OpType.VAR.value}}) # Set the node attribute to 'x'
                    elif self.isfloat(shuntyardresult[counter - 2]): # If the previous element is a float
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 2]): {"Op": Const("CONST", float(shuntyardresult[counter - 2]))}}) # Set the node attribute to the float
                    #else:
                    #    raise RuntimeError(f"Couldn't classify counter-2: {shuntyardresult[counter-2]}")
                    graph.add_edge(str(shuntyardresult[counter - 1]), node_name) # Add an edge from the previous element to the current node
                    if 'x' in str(shuntyardresult[counter - 1]): # If the previous element is 'x'
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": OpType.VAR.value}})    # Set the node attribute to 'x'
                    elif self.isfloat(shuntyardresult[counter - 1]): # If the previous element is a float
                        nx.set_node_attributes(graph, {str(shuntyardresult[counter - 1]): {"Op": Const("CONST", float(shuntyardresult[counter - 1]))}}) # Set the node attribute to the float
                    #else:
                    #    raise RuntimeError("Couldn't classify counter-1")
                    self.log.info(f"{str(shuntyardresult[counter - 2])} --> {node_name}")
                    self.log.info(f"{str(shuntyardresult[counter - 1])} --> {node_name}")

                    nx.set_node_attributes(graph, {node_name: {"Op": self.returnOperatorName(shuntyardresult[counter]).value}}) # Set the node attribute to the operator

                    for _ in range(3): # Pop the previous two elements
                        shuntyardresult.pop(counter - 2) 
                    shuntyardresult.insert(counter - 2, node_name)


        return graph

    def saveGraph(self, graph, filename):   # Function to save the graph
        self.log.info(f"Saving graph to {filename}")
        pos = nx.planar_layout(graph, scale=40)
        nx.draw_networkx(graph, pos=pos, with_labels=True)
        plt.savefig(filename)
    def getFinalNode(self, graph): # Function to get the final node
        for n in graph.nodes:
            #print(graph.degree[n])
            if graph.out_degree[n] <= 0:
                self.log.info(f"Got final node called {n}")
                return n
            else:
                pass
    def getNodes(self, graph): # Function to get the nodes
        return (list(nx.all_simple_paths(graph, source='x', target=self.getFinalNode(graph)))) # Return the nodes
    def displayGraph(self, graph): # Function to display the graph
        pos = nx.planar_layout(graph, scale=40)
        nx.draw_networkx(graph, pos=pos, with_labels=True)
        plt.show(bbox_inches='tight')

    def get_image_array(self, graph):
        buf = io.BytesIO()
        fig = plt.figure()

        pos = nx.spring_layout(graph)

        nx.draw(graph, pos=pos, with_labels=True)

        fig.savefig(buf, format='png')

        buf.seek(0)
        img = Image.open(buf)

        img_array = np.array(img)

        buf.close()
        fig.clear()
        return img_array
#class AutoDiff:

