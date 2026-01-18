import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

product = a1 * a2
sum_result = a1 + a2

print("Element-wise Product of a1 and a2:\n", product)
print("Element-wise Sum of a1 and a2:\n", sum_result)