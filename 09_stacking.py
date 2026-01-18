import numpy as np

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

horizontal_stack = np.hstack((a4, a5))
vertical_stack = np.vstack((a4, a5))

print("Array a4:\n", a4)
print("Array a5:\n", a5)
print("Horizontal Stack of a4 and a5:\n", horizontal_stack)
print("Vertical Stack of a4 and a5:\n", vertical_stack)