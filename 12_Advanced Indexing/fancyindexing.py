import numpy as np

a = np.arange(24).reshape(6,4)

fancy = a[:,[0,2,3]]

print("Original array:\n", a)
print(fancy)