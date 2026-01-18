import numpy as np
a1 = np.random.random((3,3))
a1 = np.round(a1*100)

max_value = np.max(a1, axis=1)
min_value = np.min(a1)
sum_value = np.sum(a1)
product_value = np.prod(a1)

print("Array:\n", a1)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Sum of All Elements:", sum_value)
print("Product of All Elements:", product_value)