import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print("a1:", a1)
print("a2:\n", a2)
print("a3:\n", a3)

print("a1[-1]:", a1[-1])
print(" a2:", a2[1,0])
print(a2[1,2])
print(" a3:", a3[1,0,1])
print(a3[0,1,0])