import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
b = a > 1
print(a)
print(b)# gives us in boolean expression
print(a[a>3])

c= np.where(a>3,a,0)#replace less than 3 with 0
#this can help us to  replace the values of array which are not satisfying our condition with another value
print("after replacing with less than 3 :" ,c)

x = np.array([10,19,30,41,50,78])
even = np.argwhere(x %2==0).flatten()
even1 = np.argwhere(x %2==0).reshape(-1)
print(x[even1])
print(x[even])

