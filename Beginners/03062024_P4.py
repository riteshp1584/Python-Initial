# Exercises in NumPy

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr3 = np.concatenate((arr1, arr2), axis=0)

print(arr3)

arr4 = np.concatenate((arr1, arr2), axis=1)

print('\n', arr4)

# Works correctly until here