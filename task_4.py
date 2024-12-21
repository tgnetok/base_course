import numpy as baigashov
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = baigashov.arange (0, 60, 0.0666)
frames = 500

def mayatnik (z, t):

    y, vy = z

    dy_dt = (l * baigashov.sqrt (k)) / baigashov.sqrt (m)

    return dy_dt
 
x0 = 0
vx0 = v * baigashov.cos(alpha)
y0 = 0
vy0 = v * baigashov.sin(alpha)

z0 = x0, vx0, y0, vy0

 
sol = odeint(myachik_letet, z0, t)
x = sol[:,0]
y = sol[:,2]

fig, ax = plt.subplots()
 
ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
 
 
def animate(i):
    ball.set_data([x[i]], [y[i]])
    ball_line.set_data([x[:i]], [y[:i]])
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge = 36
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
 
ani.save('ball_1.gif') 