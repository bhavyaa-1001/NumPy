import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

transposed_a2 = np.transpose(a2)
reshaped_a3 = a3.reshape(9,3)
print("Original a2:\n", a2)
print("Transposed a2:\n", transposed_a2)
print("Original a3:\n", a3)
print("Reshaped a3 (9x3):\n", reshaped_a3)

rraveled_a3 = a3.ravel()
print("Raveled a3:\n", rraveled_a3)