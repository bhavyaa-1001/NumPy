import sys
a = [i for i in range(10000000)]

b=sys.getsizeof(a)
print(b)