# Exercises in NumPy

import numpy as np

arr1 = np.arange(0, 10).reshape(5, 2)

print(arr1)

arr2 = np.transpose(arr1)

print('\n', arr2)

arr3 = arr2.T

print('\n', arr3)

# Works correctly until here
