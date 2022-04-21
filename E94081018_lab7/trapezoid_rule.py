import numpy as np
import matplotlib.pyplot as plt
import math


def func(x):
    f = 4 * (x ** 2) + (1 / 3) * x + 5
    return f

def trapezoid_rule(n):
    start = - 2
    stop = 4
    height = (stop - start) / (n - 1)
    x = np.linspace(start, stop, n)
    y = func(x)
    I_trap = 0.5*height*(y[0]+2*sum(y[1:n-1])+y[n-1])
    err_trap = I_trap - 128

    print("I_trap:", math.floor(I_trap * 1000) / 1000.0)
    print("err_trap:", -math.floor(err_trap * 1000) / 1000.0)

    x_curve = np.linspace(start, stop, 1000)
    plt.plot(x_curve, func(x_curve), linewidth=2, c='r')
    for i in range(len(x) - 1):
        if i % 3 == 0:
            area_color = 'darkorange'
        elif i % 2 == 1:
            area_color = 'forestgreen'
        else:
            area_color = 'royalblue'
        plt.fill_between([x[i], x[i + 1]], [func(x[i]), func(x[i + 1])], color=area_color, alpha=0.5,
                         interpolate=True)
    plt.show()

trapezoid_rule(3)
trapezoid_rule(11)
trapezoid_rule(21)
