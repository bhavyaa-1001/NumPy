import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)

print("Original 1D array:", a)
print("Indices of maximum value in 1D array:", np.argmax(a))
print("Original 2D array:\n", b)
print("Indices of maximum values in each column of 2D array:", np.argmax(b, axis=0))
print("Indices of maximum values in each row of 2D array:", np.argmax(b, axis=1))