import numpy as np

a = np.random.randint(1,100,15)

clipping = np.clip(a, a_min=30, a_max=70)
print("Original array:", a)
print("Clipped array (values limited between 30 and 70):", clipping)