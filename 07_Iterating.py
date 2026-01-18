import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

for i in a1:
    print("Element in a1:", i)  
print()
for row in a2:
    print("Row in a2:", row)
print()
for row in a3:
    print("2D Slice in a3:\n", row)
    print()


for i in np.nditer(a3):
    print("Element in a3 using nditer:", i)
print()