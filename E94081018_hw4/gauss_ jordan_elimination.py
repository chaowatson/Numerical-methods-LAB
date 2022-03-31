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

    for k in range(0, len(a)):
        a[k] = a[k] / a[k][k]
    for i in range(0, len(a)):
        for j in range(i, len(a) - 1):
            a[i] = a[i] - a[j + 1] * (a[i][j + 1] / a[j + 1][j + 1])
    x = a[:, len(a)]
    print("diagonal matrix:")
    print(np.array2string(a, separator=','), "\n")
    print("x:")
    print(np.array2string(x, separator=','), "\n")


a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = np.array([2, 2, 5])
gauss(a, y)

a = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y = np.array([4, 8, 5, 6])
gauss(a, y)
