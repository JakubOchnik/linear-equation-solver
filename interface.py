from calculation.gauss import *
import numpy as np

class interface_handler:
    def __init__(self):
        print("New interface!")
    def getMatrix(self,a,b):
        matrix = np.zeros((a,b))
        for i in range(a):
            for j in range(b):
                pos = str(i) + " " + str(j)
                matrix[i][j] = input(pos)
        print(matrix)
        return matrix
    def getDims(self):
        print("Please specify dimensions of the input matrix:")
        x = input("x dimension:")
        y = input("y dimension:")
        return int(x),int(y)
    

