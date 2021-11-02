import numpy as np
import time
import sys


a=np.zeros([3,4])

b=np.arange(5)

print("concat example:")
print(np.char.add(['hello','hi'],['abc','xyz']))
print(np.char.center('hello',20,fillchar = '-'))
print(np.char.capitalize('hello world'))
print(np.char.lower('HELLO'))
print(np.char.upper('hello world'))
print(np.char.split('hello how are you doing'))
print(np.char.strip(['nina','admin'],'a'))
print(np.char.join([':','.'],['day','year']))