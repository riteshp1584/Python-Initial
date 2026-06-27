# Exercises in NumPy

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr,3)

print(newarr)

# Works correctly until here

print("\n")

for x in newarr:
    print(x)
