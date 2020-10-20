import numpy as np

class gauss_jordan:
    def __init__(self):
        print("Calculation started!\nSteps:")
    def checkZeros(self, matrix):
        zeroCount = np.sum(~matrix.any(1))
        newMatrix = matrix[~np.all(matrix==0,axis=1)]
        return zeroCount, newMatrix
    def findParameters(self, x, y, matrix):
        # looking for a column with only one value different from 0
        columns = []
        rows=[]
        for i in range(x-1):
            temp_ctr = 0
            for j in range(y):
                if matrix[j][i] != 0:
                    temp_ctr+=1
            if temp_ctr < 2:
                columns.append(i)
        return columns
    def parameterCleanup(self,x,y, matrix, columns):
        while counter!=y:
            for i in range(x-1):
                temp_ctr = 0
                for j in range(y):
                    if matrix[j][i] != 0:
                        temp_ctr+=1
                if temp_ctr > 1:
                    pass
                else:
                    columns.append(i)


    def solve(self,x,y,matrix):
        # check if there are more equations than variables
        if y > x-1:
            drop = y - (x-1)
            matrix = matrix[:-drop,:]
            y = y - drop
        # main loop, no of iterations equal to no of equations
        for i in range(y):
            #i corresponds to x diagonal coordinate
            #matrix[0][0]
            #matrix[y_index][i]

            # a loop which repeats operations for any equation below
            for j in range(i+1,y):
                #1. check the multiplication factor
                coeff = matrix[j][i]/matrix[i][i]
                #2. multiply row of the matrix
                row = np.copy(matrix[i])
                row = np.multiply(row,coeff)
                #3. subtract row
                for k in range(x):
                    matrix[j][k] = matrix[j][k] - row[k]
                zeroCount, matrix = self.checkZeros(matrix)
                if zeroCount!=0:
                    y = y - zeroCount
                    zeroCount = 0
                print(matrix)
                if j == y - 1:
                    break
        #the other way around
        i_countup = 1
        for i in reversed(range(y)):
            #i corresponds to x diagonal coordinate
            #matrix[0][0]
            #matrix[y_index][i]

            # a loop which repeats operations for any equation above
            for j in reversed(range(y-i_countup)):
                #1. check the multiplication factor
                coeff = matrix[j][i]/matrix[i][i]
                #2. multiply row of the matrix
                row = np.copy(matrix[i])
                row = np.multiply(row,coeff)
                #3. subtract row
                for k in range(x):
                    matrix[j][k] = matrix[j][k] - row[k]
                zeroCount, matrix = self.checkZeros(matrix)
                if zeroCount!=0:
                    y = y - zeroCount
                    zeroCount = 0
                print(matrix)
                if j == y - 1:
                    break
            i_countup = i_countup + 1
        results = []
        if y < x-1:
            pass
        else:
            for i in range(y):
                if matrix[i][i] != 1:
                    temp = matrix[i][x-1]/matrix[i][i]
                else:
                    temp = matrix[i][x-1]
                results.append(temp)
        return results
