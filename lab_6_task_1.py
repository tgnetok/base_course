import matplotlib.pyplot as plt

x = (1, 1, 5, 5, 1)
y = (1, 5, 5, 1, 1)

plt.plot (x, y)
plt.axis('equal')
plt.savefig ('square')