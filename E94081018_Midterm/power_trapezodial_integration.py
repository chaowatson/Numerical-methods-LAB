import numpy as np

f = np.zeros(7)
f[0] = 1.0/4700
f[1] = 1.8/12200
f[2] = 2.4/19000
f[3] = 3.5/31800
f[4] = 4.4/40100
f[5] = 5.1/43800
f[6] = 6.0/43200

h = (6-1)/6
x = np.linspace(1, 6, 7)
int_val = 0

for i in range(6):
    int_val += h*(f[i] + f[[i+1]])/2
t = 2000*int_val

delt_t = np.array2string(t)
print(delt_t[1:-1])