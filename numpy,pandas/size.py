import numpy as np
import time
import sys

b=range(1000)
print(sys.getsizeof(5)*len(b))

c = np.arange(1000)
print(c.size*c.itemsize)

size = 100000
L1 = print(range(size))
L2 = print(range(size))
A1 = print(np.arange(size))
