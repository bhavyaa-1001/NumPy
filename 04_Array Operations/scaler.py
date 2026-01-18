import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

scaled_a1 = a1 * 2.5
scaled_a2 = a2 + 10

print("Original a1:\n", a1)
print("Scaled a1 (multiplied by 2.5):\n", scaled_a1)
print("Original a2:\n", a2) 
print("Scaled a2 (added 10):\n", scaled_a2)