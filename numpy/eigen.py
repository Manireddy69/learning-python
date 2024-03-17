import numpy as np 
a = np.array([[1,2],[3,4]])

eigenvalues , eigenvectors = np.linalg.eig(a)
b = eigenvectors[:,0]* eigenvalues[0]
print(eigenvalues)
print(eigenvectors)
print(b)