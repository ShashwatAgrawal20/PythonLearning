# from abc import ABCMeta, abstractmethod  class shape(metaclass = ABCMeta):
from abc import ABC, abstractmethod
# ye jo abstract method hoti hai ye sb ke lye lagu kya kr na hai uss ke niche vo function likhna hota hai .. 
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectrangle(shape):
    type = "rectrangle"
    sides = 4

    def __init__(self):
        self.length = 34
        self.breadth = 3423


    def printarea(self):
        return self.length + self.breadth


rect = rectrangle()
print(rect)
# eno = shape()