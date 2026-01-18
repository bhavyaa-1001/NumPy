import numpy    as np

a1 = np.random.random((2,3))*100
round_values = np.round(a1)
floor_values = np.floor(a1)
ceil_values = np.ceil(a1)

print("Array:\n", a1)
print("Rounded Values:\n", round_values)
print("Floor Values:\n", floor_values)
print("Ceil Values:\n", ceil_values)