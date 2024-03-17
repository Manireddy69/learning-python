import numpy as np
a = np.arange(3,9)
print(a)#give 6  elements from 3 to 8
print(a.shape)#give us 6 
b = a.reshape(3,2)#we use multiples of 6 because of shape
c = a.reshape(2,3)
print(c)
print(b)