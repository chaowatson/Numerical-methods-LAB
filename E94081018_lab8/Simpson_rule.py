import numpy as np
import matplotlib.pyplot as plt


def function(x):
    f = (x**3) + (x**2)
    return f


def error(n):
    a = -2
    b = 4
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    f = function(x)
    simpson = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
    err = 84 - simpson
    return err


grid_points = np.arange(11, 171, 2).tolist()
error_out = []
for x in grid_points:
    error_out.append(error(x))
print(f"minimum error: {min(error_out)}")

plt.plot(grid_points, error_out, linewidth=1.5)
plt.xlabel('grid points')
plt.ylabel('error')
plt.show()



