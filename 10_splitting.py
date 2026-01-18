import numpy as np

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

split_arrays = np.hsplit(a4, 2)
vertical_split_arrays = np.vsplit(a5, 3)
print("Array a4:\n", a4)
print("Array a5:\n", a5)    
print("Horizontally Split a4 into 2 parts:\n", split_arrays)
print("Vertically Split a5 into 3 parts:\n", vertical_split_arrays)
