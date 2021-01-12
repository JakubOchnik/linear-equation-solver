from calculation.gauss import gauss_jordan
import numpy as np

class interface_handler:
    def __init__(self):
        print("New interface!")
    def getMatrix(self,a,b):
        #matrix = np.array([[2.0,-3,-4,5,-13],[4,-6,1,-1,14],[6,-9,1,2,13],[2,-3,-2,-4,9]],dtype=float)
        matrix = np.array([[2,1,-1,1,0],[0,1,3,-3,0],[1,1,1,-1,0],[1,0,-2,2,0]],dtype=float)
        #matrix = np.zeros((a,b))
        #for i in range(a):
        #    for j in range(b):
        #        pos = str(i) + " " + str(j)
        #        matrix[i][j] = input(pos)
        print(matrix)
        return matrix
    def getDims(self):
        print("Please specify dimensions of the input matrix:")
        x = input("x dimension:")
        y = input("y dimension:")
        return int(x),int(y)
    

