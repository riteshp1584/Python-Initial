# Exercises in NumPy

import numpy as np

new1 = np.logspace(1, 10, 4)

print(new1)

new2 = np.logspace(2, 6, num=3, base=10)

print(new2)

new3 = np.logspace(1, 10, num=10, endpoint=True, base=3, dtype=int)

print(new3)

# Works correctly until here

'''
-> start    : [float] start(base ** start) of interval range.
-> stop     : [float] end(base ** stop) of interval range
-> endpoint : [boolean, optional]If True, stop is the last sample. By default, True
-> num      : [int, optional] No. of samples to generate
-> base     : [float, optional] Base of log scale. By default, equals 10.0
-> dtype    : type of output array
'''
