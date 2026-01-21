import numpy as np

a = np.array([1,2,3,4,np.nan,6])

print("Array with missing value:", a)
print("Is NaN:", np.isnan(a))

b = a[~np.isnan(a)]
print("Array without missing value:", b)
