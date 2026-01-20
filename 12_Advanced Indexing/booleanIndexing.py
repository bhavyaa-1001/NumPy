import numpy as np


a = np.random.randint(1,100,24).reshape(6,4)
boolean_index = a > 50
number2 = a[(a > 50) & (a % 2 == 0)]
print("Original array:\n", a)
print("Boolean Indexing (elements > 50):\n", a[boolean_index])
print("Elements greater than 50 and even:\n", number2)