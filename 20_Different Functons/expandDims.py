import numpy as np

a = np.random.randint(1,100,15)
print("Original array:", a)
expanded_a = np.expand_dims(a, axis=1)
print("Expanded array (new axis at position 0):", expanded_a)