import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)

print("Original 1D array:", a)
print("Sumulative sum of 1D array:", np.cumsum(a))
print("Original 2D array:\n", b)
print("Sumulative sum of 2D array along columns:\n", np.cumsum(b, axis=0))
print("Sumulative sum of 2D array along rows:\n", np.cumsum(b, axis=1))

print("product cumulative of 1D array:", np.cumprod(a))