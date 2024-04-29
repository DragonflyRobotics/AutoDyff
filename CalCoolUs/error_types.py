class ParenthesisMulError(Exception):
    def __init__(self, message="ParenthesisMul: Multiplication signs needed in between parenthesis and other operations or values"):
        self.message = message
        super().__init__(self.message)

class DNE(Exception):
    def __init__(self, message="DNE: The value does not exist at the given x value"):
        self.message = message
        super().__init__(self.message)

class DomainError(Exception):
    def __init__(self, message="DomainError: The value is outside the domain of the function"):
        self.message = message
        super().__init__(self.message)

class ParenthesisError(Exception):
    def __init__(self, message="BalanceParenthesis: Parenthesis are not balanced"):
        self.message = message
        super().__init__(self.message)
class ZeroDivisionError(Exception):
    def __init__(self, message="ZeroDivisionError: Division by zero"):
        self.message = message
        super().__init__(self.message)
class ImaginaryNumberError(Exception):
    def __init__(self, message="ImaginaryNumberError: Imaginary number"):
        self.message = message
        super().__init__(self.message)
class EmptyExpression(Exception):
    def __init__(self, message="EmptyExpression: Expressions like parenthesis sets and exponents can't be empty"):
        self.message = message
        super().__init__(self.message)

class UndefinedArguments(Exception):
    def __init__(self, message="UndefinedArguments: Arguments not provided for operation"):
        self.message = message
        super().__init__(self.message)

class EquationTooShort(Exception):
    def __init__(self, message="EquationTooShort: Equation is too short"):
        self.message = message
        super().__init__(self.message)
