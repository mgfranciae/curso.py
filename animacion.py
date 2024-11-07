import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2 * np.pi * i / 100, 100)
    y = np.sin(x)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)
plt.show()