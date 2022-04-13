import numpy as np


def inverse_power_method(x, a):
    a = a.astype(float)
    eig_vec = x.astype(float)
    a_inv = np.linalg.inv(a)
    for i in range(100):
        eig_vec = np.dot(a_inv, eig_vec)
        if max(abs(eig_vec)) != max(eig_vec):
            eig_val_rec = -max(abs(eig_vec))
        else:
            eig_val_rec = max(abs(eig_vec))
        eig_vec = eig_vec / eig_val_rec
    print("The Minimum Eigenvalue: ", 1/eig_val_rec)
    print("Eigenvector:", eig_vec, "\n")


x = np.array([1, 1])
a = np.array([[0, 2], [2, 3]])
print(f"x = np.array({np.ndarray.tolist(x)})")
print(f"a = np.array({np.ndarray.tolist(a)})", "\n")
inverse_power_method(x, a)

x = np.array([1, 1, 1])
a = np.array([[1, 5, 2],[2, 4, 3],[2, 1, 6]])

print(f"x = np.array({np.ndarray.tolist(x)})")
print(f"a = np.array({np.ndarray.tolist(a)})", "\n")
inverse_power_method(x, a)
