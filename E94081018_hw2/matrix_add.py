import numpy as np


def matrix_add(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        a = np.array(a)
        b = np.array(b)
        c = a + b
        c = np.ndarray.tolist(c)
        return True, c
    else:
        return True, "Matrix dimensions are not compatible for addition"


a = [[2, 3, 1], [4, 6, 2]]
b = [[1, 2, 3], [3, 4, 5]]
addible, c = matrix_add(a, b)
if addible: print(c)

a = [[2, 3, 1], [4, 6, 2]]
b = [[1, 2], [3, 4]]
addible, c = matrix_add(a, b)
if addible: print(c)

a = [[2, 3, 1], [4, 6, 2]]
b = [[1, 2], [3, 4], [3, 4]]
addible, c = matrix_add(a, b)
if addible: print(c)
