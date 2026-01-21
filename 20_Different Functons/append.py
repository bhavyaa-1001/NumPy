import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print("Original 1D array:", a)
print("Appended 1D array:", np.append(a, [101,102,103]))
print("Original 2D array:\n", b)    
print("Appended 2D array (adding a row):\n", np.append(b, [[101,102,103,104]], axis=0))