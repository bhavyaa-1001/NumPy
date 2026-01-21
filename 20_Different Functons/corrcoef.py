import numpy as np

salary = np.array([20000,40000,35000,60000])
experience = np.array([1,2,3,4])

print("Correlation coefficient matrix:")
print(np.corrcoef(salary, experience))