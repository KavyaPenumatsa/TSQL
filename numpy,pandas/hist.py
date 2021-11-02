import numpy as np
from matplotlib import pyplot as plt


a = np.array([20,87,4,40,53,74,56,51,11,20,40,15,79,25,27])
plt.hist(a,bins = [0,20,40,60,80,100])
plt.title("histogram")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y= np.sin(x)
plt.plot(x,y)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
z=np.zeros((6,6),dtype=int)
z[1::2,::2] = 1
z[::2,1::2] = 1
z