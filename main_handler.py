from interface import *
from calculation.gauss import gauss_jordan
import numpy as np

class main_handler:
    def __init__(self):
        #print("New main handler!")
        self.ui = interface_handler()
        self.calc = None
        self.x = None
        self.y = None
        self.results = []
    def start(self):
        self.x, self.y = self.ui.getDims()
        print("Matrix dimensions: ", self.x, "x", self.y)
        print("Specify the matrix (coordinates are shown in format: 'y x')")
        self.matrix = self.ui.getMatrix(self.y, self.x)
        self.calc = gauss_jordan()
        self.results = self.calc.solve(self.x, self.y, self.matrix)
        print(self.results)