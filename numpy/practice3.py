import numpy as np
a = np.array([[1,3,5,7,9],[2,4,6,8,10]])#make sure that both the array arguments should be equal
print(a)
print(a.sum(axis=1))#caluclates sum in coloumns
print(a.sum(axis=0))#calculate sum of rows 