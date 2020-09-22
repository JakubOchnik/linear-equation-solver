from interface import *
from calculation.gauss import *
import numpy as np

class main_handler:
    def __init__(self):
        print("New main handler!")
        self.ui = interface_handler()
        self.calc = None
        self.x = None
        self.y = None
        self.results = []
    def start(self):
        self.x, self.y = 5, 4 #self.ui.getDims()
        print("matrix dims: ", self.x, "x", self.y)
        self.matrix = self.ui.getMatrix(self.y, self.x)
        self.calc = gauss_jordan()
        self.results = self.calc.solve(self.x, self.y, self.matrix)
        print(self.results)