import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
arr2 = np.array([[[1, 2, 3], ['John', 'Kalil', 'Randy']], [[1, 2, 3], ['John', 'Kalil', 'Randy']]])
print(arr2.ndim)
