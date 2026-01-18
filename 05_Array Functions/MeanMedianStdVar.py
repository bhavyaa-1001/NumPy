import numpy as np

a1 = np.random.random((3,3))
a1 = np.round(a1*100)

mean_value = np.mean(a1)
median_value = np.median(a1)
std_value = np.std(a1)
var_value = np.var(a1)

print("Array:\n", a1)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)
print("Variance:", var_value)