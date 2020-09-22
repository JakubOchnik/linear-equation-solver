from main_handler import *
import numpy as np
test = main_handler()
test.start()

#test = np.matrix('1 2; 3 4')
#print(test)
#row = np.copy(test[1])
#row = np.multiply(row, 2)
#print(row)
#row = np.subtract(test[1],row)
#print(row)
#test[1,:] = row[0,:]
#print(test)

#macierz = np.random.rand(5,5)
#for i in range(5):
##    macierz[0][i] = 0
#for i in range(5):
#    macierz[3][i] = 0
#print(macierz)
#ile = np.sum(~macierz.any(1))
#print(ile)
#t = macierz[~np.all(macierz==0,axis=1)]
#print(t)