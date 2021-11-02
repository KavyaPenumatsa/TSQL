import numpy as np

a=np.arange(20)
a
a[:4]
a[4]

s = slice(2,12,3)
a[s]

b=np.arange(0,45,5)
b=b.reshape(3,3)
print(b)

for x in np.nditer(b):
    print(x)

for x in np.nditer(b, order ="c"):
    print(x)
for x in np.nditer(b, order = "f"):
    print(x)
