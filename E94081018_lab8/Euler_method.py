import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

f = lambda t, s: np.exp(-2*t)
h = 0.1
t = np.arange(0, 1 + h, h)
init = -1/2
s = np.zeros(len(t))
s[0] = init

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s,  label='Approximate')
plt.plot(t, -1/2*np.exp(-2*t), '--', label='Exact', color='red')
plt.title('Euler v.s. Exact')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

