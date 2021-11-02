import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print('\n')
b = np.resize(a,(3,2))
print(b)
print('\n')
print(b.shape)
b = np.resize(a,(3,3))
print(b)
print(b.shape)
