import numpy as np

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

changed_a1 = a1.astype(np.float64)
changed_a2 = a2.astype(np.int16)
changed_a3 = a3.astype(np.complex128)
print("Original a1 dtype:", a1.dtype, "Changed a1 dtype:", changed_a1.dtype)
print("Original a2 dtype:", a2.dtype, "Changed a2 dtype:", changed_a2.dtype)
print("Original a3 dtype:", a3.dtype, "Changed a3 dtype:", changed_a3.dtype)