import numpy as np
a1 = np.random.random((3,3))
a1 = np.round(a1*100)

log_values = np.log(a1) 

exp_values = np.exp(a1)
print("Array:\n", a1)
print("Logarithm:\n", log_values)
print("Exponential:\n", exp_values)