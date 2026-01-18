import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print("a1:", a1)
print("a2:\n", a2)
print("a3:\n", a3)

print(a1[2:5])
print(a2[0:2,1:3])
print(a2[0,:])
print(a2[1:,1:3])
print(a2[::2,::3])

print(a3[0:2,1:,1:])
print(a3[:,::2,::2])