import numpy as np


def power_method(x, a, old):
    old_eigenvalue = old
    y = np.dot(a, x)
    eigenvalue = np.max(y)
    eigenvector = y / eigenvalue
    dif = abs(eigenvalue - old_eigenvalue)
    if dif <= 0.000000000000001:
        print("Eigenvalue:", eigenvalue)
        print("Eigenvector:", eigenvector, "\n")
    else:
        old_eigenvalue = eigenvalue
        x = eigenvector
        power_method(x, a, old_eigenvalue)


x = np.array([1, 1])
a = np.array([[0, 2], [2, 3]])
print(f"x = np.array({np.ndarray.tolist(x)})")
print(f"a = np.array({np.ndarray.tolist(a)})", "\n")
power_method(x, a, 0)

x = np.array([1, 1])
a = np.array([[2, 4], [3, 6]])
print(f"x = np.array({np.ndarray.tolist(x)})")
print(f"a = np.array({np.ndarray.tolist(a)})", "\n")
power_method(x, a, 0)
