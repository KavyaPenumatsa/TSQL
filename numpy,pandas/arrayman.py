import numpy as np

a = np.arange(9)
print("the original array")
print(a)
print()

b=a.reshape(3,3)
print("the modified array:")
print(b)

print(b.flatten())

print(b.flatten(order='F'))

