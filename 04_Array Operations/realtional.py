import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

greater_mask = a1 > 5
equal_mask = a2 == 15
print("a1 > 5:\n", greater_mask)
print("a2 == 15:\n", equal_mask)