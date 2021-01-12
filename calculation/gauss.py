import numpy as np
class gauss_jordan:
    def __init__(self):
        #print("Gauss-Jordan class!")
        pass
    def checkZeros(self, matrix):
        zeroCount = np.sum(~matrix.any(1))
        newMatrix = matrix[~np.all(matrix==0,axis=1)]
        return zeroCount, newMatrix
    def find_parameters(self, x, y, matrix, finish=False):
        #looking for a column which contains only one non-zero value
        columns_x = []
        rows_y=[]
        for i in range(x-1):
            temp_ctr = 0
            for j in range(y):
                if matrix[j][i] != 0:
                    temp_ctr+=1
                    temp_nonzero_y = j
            if temp_ctr < 2:
                if finish==True and temp_nonzero_y in rows_y:
                        continue
                columns_x.append(i)
                rows_y.append(temp_nonzero_y)
        return columns_x,rows_y
    def find_nonsingle_y(self,x,y,matrix, col_x, rows_y):
        considered_x = []
        considered_y = []
        for i in range(y):
            if not i in col_x:
                considered_x.append(i)
        tempMatrix = matrix[0:y,:x-1]
        print(tempMatrix)
        print(matrix)
        for i in range(y):
            counter = np.count_nonzero(tempMatrix[i])
            for j in considered_x:
                if counter < x-1 and matrix[i][j] != 0:
                    considered_y.append(i)
        return considered_x, considered_y
    def parameter_cleanup(self,x,y, matrix):# columns):
        col_x,rows_y = self.find_parameters(x,y,matrix)
        considered_x, considered_y = self.find_nonsingle_y(x,y,matrix, col_x, rows_y)
        #szukaj wartości pod lub nad nimi
        #dla kazdego ze znalezionych iksow:
        for i in considered_x:
            k = 0
            for j in range(y):
                if j!=considered_y[k] and matrix[j][i]!=0:
                    #consider it
                    coeff = matrix[j][i] / matrix[considered_y[k]][i]
                    row = np.copy(matrix[considered_y[k]])
                    row = np.multiply(row,coeff)
                    for l in range(x):
                        matrix[j][l] = matrix[j][l] - row[l]
                zeroCount, matrix = self.checkZeros(matrix)
                if zeroCount!=0:
                    y = y - zeroCount
                    zeroCount = 0
                print(matrix)
                if j == y - 1:
                    break
            k+=1
        return matrix

    def solve(self,x,y,matrix):
        #sprawdz czy rownan nie jest wiecej niz zmiennych
        if y > x-1:
            drop = y - (x-1)
            matrix = matrix[:-drop,:]
            y = y - drop
        #glowna petla, tyle iteracji ile jest rownan
        for i in range(y):
            #!!! i odpowiada za wspolrzedna x przekatnej
            #matrix[0][0]
            #matrix[y_index][i]

            #petla powtarzajaca operacje dla kazdego z rownan nizej
            for j in range(i+1,y):
                #glowna petla, kazdy ponizej
                #1. sprawdz wspolczynnik pomnozenia
                if matrix[i][i]!=0:
                    coeff = matrix[j][i]/matrix[i][i]
                    #2. multiply row of the matrix
                    row = np.copy(matrix[i])
                    row = np.multiply(row,coeff)
                    #3. subtract row
                    for k in range(x):
                        matrix[j][k] = matrix[j][k] - row[k]
                else:
                    zeroCount, matrix = self.checkZeros(matrix)
                    if zeroCount!=0:
                        y = y - zeroCount
                        zeroCount = 0
                    continue
                zeroCount, matrix = self.checkZeros(matrix)
                if zeroCount!=0:
                    y = y - zeroCount
                    zeroCount = 0
                print(matrix)
                if j == y - 1:
                    break
        #na odwrot
        i_countup = 1
        for i in reversed(range(y)):
            #!!! i odpowiada za wspolrzedna x przekatnej
            #matrix[0][0]
            #matrix[y_index][i]

            #petla powtarzajaca operacje dla kazdego z rownan nizej
            for j in reversed(range(y-i_countup)):
                #glowna petla, kazdy ponizej
                #1. sprawdz wspolczynnik pomnozenia
                if matrix[i][i] != 0:
                    coeff = matrix[j][i]/matrix[i][i]
                    #2. multiply row of the matrix
                    row = np.copy(matrix[i])
                    row = np.multiply(row,coeff)
                    #3. subtract row
                    for k in range(x):
                        matrix[j][k] = matrix[j][k] - row[k]
                else:
                    continue
                zeroCount, matrix = self.checkZeros(matrix)
                if zeroCount!=0:
                    y = y - zeroCount
                    zeroCount = 0
                print(matrix)
                if j == y - 1:
                    break
            i_countup = i_countup + 1
        #test = self.findParameters(x, y, matrix)
        #print(test)
        results = []
        if y < x-1:
            matrix = self.parameter_cleanup(x,y,matrix)
            print(matrix)
            #przetwarzanie
            coeffs = np.zeros((y,x))
            col_x, row_y = self.find_parameters(x,y,matrix, finish=True)
            for i in range(y):
                divisor = matrix[row_y[i]][col_x[i]]
                for j in range(x):
                    if j == col_x[i]:
                        continue
                    if j == x-1:
                        coeffs[i][j] = matrix[i][j]/divisor
                    else:
                        coeffs[i][j] = -(matrix[i][j]/divisor)
            print(coeffs)
        else:
            for i in range(y):
                if matrix[i][i] != 1:
                    temp = matrix[i][x-1]/matrix[i][i]
                else:
                    temp = matrix[i][x-1]
                results.append(temp)
        return results
            