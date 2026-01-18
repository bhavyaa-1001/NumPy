import numpy as np

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

dot_product = np.dot(a2, a3)
print("Array a2:\n", a2)
print("Array a3:\n", a3)
print("Dot Product of a2 and a3:\n", dot_product)