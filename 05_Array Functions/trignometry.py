import numpy as np

a1 = np.random.random((3,3))
a1 = np.round(a1*100)

sin_values = np.sin(a1)
sin_value = np.sin(np.deg2rad(a1))
cos_values = np.cos(np.deg2rad(a1))
tan_values = np.tan(np.deg2rad(a1))
print("Array:\n", a1)
print("Sine Values:\n", sin_values)
print("Sine Values:\n", sin_value)
print("Cosine Values:\n", cos_values)
print("Tangent Values:\n", tan_values)