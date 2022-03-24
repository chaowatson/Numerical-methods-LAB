import numpy as np


def inverse_solve(a, y):
    print(f"a = np.array({np.ndarray.tolist(a)})")
    print(f"y = np.array({np.ndarray.tolist(y)})", "\n")
    a_row = np.size(a, 0)
    a_col = np.size(a, 1)
    a = a.astype(float)
    a_adj = np.zeros((a_row, a_col))

    for i in range(a_col):
        for j in range(a_row):
            det = np.delete(a, i, axis=0)
            det = np.delete(det, j, axis=1)
            det = np.linalg.det(det)
            a_adj[i][j] = det * (-1) ** (i + j)
    a_adj = a_adj.T
    a_inv = a_adj / np.linalg.det(a)
    x = np.dot(a_inv, y)

    print("adjugate matrix:")
    print(f"array({np.array2string(a_adj, separator=', ')})", "\n")
    print("x:")
    print(np.array2string(x, separator=','), "\n")


a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = np.array([2, 2, 5])
inverse_solve(a, y)

a = np.array([[1, 2], [3, 4]])
y = np.array([2, 5])
inverse_solve(a, y)
