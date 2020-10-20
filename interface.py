from calculation.gauss import *
import numpy as np

class interface_handler:
    def __init__(self):
        pass
    def getMatrix(self,a,b):
        matrix = np.zeros((a,b))
        print("Please define the input matrix (format: [y][x]):")
        for i in range(a):
            for j in range(b):
                pos = "Matrix[" + str(i) + "][" + str(j) + "] = "
                matrix[i][j] = input(pos)
        print("Input matrix:")
        print(matrix)
        return matrix
    def getDims(self):
        print("Please specify dimensions of the input matrix:")
        x = input("X dimension = ")
        y = input("Y dimension = ")
        return int(x),int(y)
    

