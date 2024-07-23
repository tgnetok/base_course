import numpy as baigashov
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_big (R, angle_vel, time):
    alpha = angle_vel * baigashov.pi / 180 * time
    x = R * baigashov.cos(alpha)
    y = R * baigashov.sin(alpha)
    return x, y













fig, ax = plt.subplots() 

anim_object, = plt.plot([], [], '-', lw=2) 

xdata, ydata = [], [] 

ax.set_xlim(-4, 4) 
ax.set_ylim(-4, 4) 