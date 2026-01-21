import numpy as np

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
  return np.mean((actual - predicted)**2)

print("Actual:", actual)
print("Predicted:", predicted)
print(mse(actual,predicted))