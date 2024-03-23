class ParenthesisMulError(Exception):
    "Multiplication signs needed in between parntehsis and other operations or values"
    pass
class DNE(Exception):
    "The value does not exist at the given x value"
    pass
class DomainError(Exception):
    "The value is outside the domain of the function"