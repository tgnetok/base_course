import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (-1, 1, 0.000666)
e = 2.718

def diff_func (hehe, t) : 
    x, y = hehe

    dx_dt = 3 * x - 2 * y + ((e ** (3 * t)) / ((e ** t) + 1))
    dy_dt = x - ((e ** (3 * t)) / ((e ** t) + 1))

    return dx_dt, dy_dt

x0 = 5 
y0 = -7
hehe0 = x0, y0

sol = odeint (diff_func, hehe0, t)

plt.plot (t, sol [:, 0], 'teal', label = 'hahaha')

plt.legend ()
plt.savefig ('task_2.png')