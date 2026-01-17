import numpy as np

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print("Number of dimensions of a1:", a1.shape)
print("Number of dimensions of a2:", a2.shape)
print("Number of dimensions of a3:", a3.shape)