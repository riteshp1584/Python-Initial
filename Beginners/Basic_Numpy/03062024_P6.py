# Exercises in NumPy

import numpy as np

arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([5, 6, 7, 8])

arr3 = np.hstack((arr1, arr2))

print(arr3)

arr4 = np.vstack((arr1, arr2))

print('\n', arr4)

# Works correctly until here
