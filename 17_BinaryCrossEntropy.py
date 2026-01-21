import numpy as np

def BinaryCrossEntropy(actual, predicted):
    # Clipping predicted values to avoid log(0)
    predicted = np.clip(predicted, 1e-15, 1 - 1e-15)
    bce = - (actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))
    return np.mean(bce)

# Example usage
actual = np.array([1, 0, 1, 1, 0])
predicted = np.array([0.9, 0.1, 0.8, 0.7, 0.2])
print("Actual:", actual)
print("Predicted:", predicted)
print("Binary Cross Entropy Loss:", BinaryCrossEntropy(actual, predicted))
