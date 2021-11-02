import numpy as np
import time
import sys


size = 100000
L1 = range(size)
L2 = range(size)
A1 = print(np.arange(size))


start =time.time()
result = [(x+y) for x,y in zip(L1,L2)]
result = [(x+y) for x,y in zip(L1,L2)]
print(result)
print("python list took:",(time.time() - start)*1000)