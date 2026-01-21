import numpy as np

a = np.random.randint(1,100,15)
print("Original array:", a)

items = [20, 30, 40]
print(np.isin(a, items))