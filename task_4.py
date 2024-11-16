import numpy as baigashov
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = baigashov.arange (-5, 5, 0.00666)

def diff_func (z, t) : 
    y, omega = z 

    dy_dt = omega
    domega_dt = - 4 * omega - 5 * y

    return dy_dt, domega_dt

y0 = 4
dy_dt0 = - 1

z0 = y0, dy_dt0

sol = odeint (diff_func, z0, t)

plt.plot (t, sol [:, 0], 'b', label = 'wewe')

plt.legend ()
plt.savefig ('fig_4.png')