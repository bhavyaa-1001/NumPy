import numpy as np

a = np.random.randint(1,100,15)
print("Original array:", a)
print("Indices of elements greater than 50:", np.where(a > 50))
print("Indices of elements greater than 50 , replace with 0:", np.where(a > 50,0,a))

