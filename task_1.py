import numpy as baigashov
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = baigashov.arange (-5, 5, 0.000666)

def diff_func (ses, x) : 
    y, z = ses

    dy_dx = y ** 2 * z
    dz_dx = (z / x) - y * (z ** 2)

    return dy_dx, dz_dx

y0 = 1 
z0 = -3
ses0 = y0, z0

sol = odeint (diff_func, ses0, x)

plt.plot (x, sol [:, 0], 'g', label = 'ddd')

plt.legend ()
plt.savefig ('task_1.png')