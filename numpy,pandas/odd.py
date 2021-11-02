import numpy as np

a = np.arange(10)
print(a)
b = (a%2 == 1)
a[b] = -1
print(a)
