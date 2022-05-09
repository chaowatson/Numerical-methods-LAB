import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


def my_RK4(f, t_span, s0):
    s = np.zeros(len(t_span))
    t =np.zeros(len(t_span))
    s[0] = s0
    h = (2*np.pi)/9
    for i in range(len(t_span)):
        t[i] = t_span[i]
    for j in range(len(t)-1):
        k1 = f(t[j], s[j])
        k2 = f(t[j]+h/2, s[j]+(1/2)*k1*h)
        k3 = f(t[j]+h/2, s[j]+(1/2)*k2*h)
        k4 = f(t[j]+h, s[j]+(1/2)*k3*h)
        s[j+1] = s[j]+(h/6)*(k1+2*k2+2*k3+k4)
    return t, s

f = lambda t, s: np.sin(np.exp(s))/(t+1)
t_span = np.linspace(0, 2*np.pi, 10)
s0 = 0
# Runge-Kutta method
t, s = my_RK4(f, t_span, s0)
solution = solve_ivp(f, [0, 2*np.pi], [s0], t_eval=t_span)

plt.figure(figsize = (12, 8))
plt.plot(t, s,"r-",label="RK4")
plt.plot(solution.t, solution.y[0],"b--",label="Python Solver")
plt.grid()
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.show()