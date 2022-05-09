import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-poster")


def my_central_diff(f, h):
    central_diff = []
    for i in range(5, 96):
        central_diff.append((f[i+1] - f[i-1]) / (2*h))
    return central_diff


def my_num_diff_w_smoothing(x, y, n):
    y_smoothed = np.zeros(len(y))
    h = (2 * np.pi) / 100
    for i in range(4, len(x) - 3):
        y_smoothed[i] = np.mean(y[i-n:i+n])
    dy_cent_diff = my_central_diff(y_smoothed, h)
    X = x[5:96:]
    return dy_cent_diff, X


np.random.seed(42)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + np.random.randn(len(x)) / 100
[dy, X] = my_num_diff_w_smoothing(x, y, 4)

h = (2 * np.pi) / 100
dy_real = np.cos(x)
dy_for_diff = np.diff(y) / h
x_diff = x[:-1:]


plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Noisy Sine Function")

plt.show()

plt.plot(x,dy_real ,"b-",label="cosine")
plt.plot(x_diff,dy_for_diff ,"g-",label="unsmoothed forward diff")
plt.plot(X, dy,"r-",label="smoothed")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Analytic Derivative and Smoothed Derivative")
plt.legend()

plt.show()