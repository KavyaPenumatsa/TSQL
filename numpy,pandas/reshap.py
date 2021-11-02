import numpy as np

a=np.arange(12).reshape(4,3)

print(np.transpose(a))

b=np.arange(8).reshape(2,4)

c=b.reshape(2,2,2)

np.rollaxis(c,2)

d=np.arange(9).reshape(3,3)
e=np.array([10,11,12])
f=np.multiply(d,e)
print(f)