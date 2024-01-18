from abc import ABC, abstractmethod
from enum import Enum

class Generic_Op(ABC):
    def __init__(self, name):
        self.name = name
        self.differentiable = True
        self.numerical_value = None
        self.unary = False

    def getName(self):
        return self.name

    @abstractmethod
    def getDerivative(self, *args, **kwargs):
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

