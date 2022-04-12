import numpy as np


def gauss_seidel(a,y):
    print(f"a = np.array({np.ndarray.tolist(a)})")
    print(f"y = np.array({np.ndarray.tolist(y)})", "\n")

    # set init value
    x1 = 0
    x2 = 0
    x3 = 0
    epsilon = 0.0001
    converged = False

    x_old = np.array([x1, x2, x3])

    print("Iteration results")
    print("k,	 x1,	  x2,	  x3 ")
    # do the iteration
    for k in range(1, 50):
        # gauss_seidel method
        x1 = (y[0]-(a[0][1]*x2+a[0][2]*x3))/a[0][0]
        x2 = (y[1]-(a[1][0]*x1+a[1][2]*x3))/a[1][1]
        x3 = (y[2]-(a[2][0]*x1+a[2][1]*x2))/a[2][2]
        x = np.array([x1, x2, x3])
        # check if it is smaller than threshold
        dx = np.sqrt(np.dot(x-x_old, x-x_old))

        print("%d  %.4f  %.4f  %.4f" % (k, x1, x2, x3))
        # if smaller than threshold
        if dx < epsilon:
            converged = True
            print("Converged!", "\n")
            break

        # assign the latest x value to the old value
        x_old = x

    if not converged:
        print("Not converged, increase the # of iterations", "\n")


# exec
a = np.array([[8, 4, -3], [-2, -8, 5], [3, 5, 10]])
y = np.array([14, 5, -8])
gauss_seidel(a, y)

a = np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]])
y = np.array([10, 6, 3])
gauss_seidel(a, y)
