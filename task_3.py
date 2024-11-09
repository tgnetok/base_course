import numpy as baigashov
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = baigashov.arange (-5, 5, 0.00666)

def diff_func (hehe, t) : 
    y, z = hehe 

    dy_dt = z
    dz_dt = np.sin(x) * np.cos(x)

    return dy_dt, dz_dt

y0 = 3
dy_dt0 = 0

hehe0 = y0, dy_dt0

x = 8

sol = odeint (diff_func, hehe0, t)

plt.plot (t, sol [:, 0], 'gainsboro', label = 'memeeeeee')

plt.legend ()
plt.savefig ('task_3.png')