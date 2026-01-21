import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)

print("Original 1D array:", a)
print("Sorted 1D array:", np.sort(a))
print(np.sort(a)[::-1])
print("Original 2D array:\n", b)
print("Sorted 2D array along columns:\n", np.sort(b, axis=0))