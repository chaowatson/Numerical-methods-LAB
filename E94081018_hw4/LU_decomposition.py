import numpy as np

def LU(a, y):
    print(f"a = np.array({np.ndarray.tolist(a)})")
    print(f"y = np.array({np.ndarray.tolist(y)})", "\n")
    a2 = a.astype(float)
    a = a.astype(float)
    L = np.identity(len(a)).astype(float)

    for i in range(0, len(a2)):
        for j in range(i+1, len(a2)):
            L[j][i] = a2[j][i] / a2[i][i]
            a2[j] = a2[j] - a2[i]*(a2[j][i]/a2[i][i])

    U = a2.astype(float)
    x = np.linalg.inv(U).dot(np.linalg.inv(L)).dot(y)

    print("u_matrix:")
    print(U, "\n")
    print("l_matrix:")
    print(L, "\n")
    print("x:")
    print(np.array2string(x, separator=','), "\n")


a1 = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y1 = np.array([2, 2, 5])
LU(a1, y1)


a2 = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y2 = np.array([4, 8, 5, 6])
LU(a2, y2)
