import numpy as np


def gauss(a, y):
    print(f"a = np.array({np.ndarray.tolist(a)})")
    print(f"y = np.array({np.ndarray.tolist(y)})", "\n")
    a_row = np.size(a, 0)
    a_col = np.size(a, 1)
    a = a.astype(float)
    y = np.reshape(y, (-1, 1))
    a = np.concatenate((a, y), axis=1)

    for i in range(a_col-1):
        for j in range(a_row-1):
            a[i + j + 1] = a[i] * (-a[i + j + 1, i] / a[i, i]) + a[i + j + 1]
        a_row -= 1

    a_row = np.size(a, 0)
    a_col = np.size(a, 1)
    x = np.zeros(a_row)
    numerator = 0

    for i in range(a_row):
        for j in range(a_col-1):
            numerator = x[j]*a[a_row-1-i,j] + numerator
        numerator = a[a_row-1-i, a_col-1] - numerator
        x[a_row-1-i] = numerator/a[a_row-1-i, a_col-2-i]
        numerator = 0

    print("upper triangular matrix:")
    print(a, "\n")
    print("x:")
    print(np.array2string(x, separator=','), "\n")


a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = np.array([2, 2, 5])
gauss(a, y)

a = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y = np.array([4, 8, 5, 6])
gauss(a, y)
