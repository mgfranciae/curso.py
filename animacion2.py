import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros iniciales (ejemplo)
v0 = 10  # Velocidad inicial (m/s)
theta = np.pi/4  # Ángulo de lanzamiento (radianes)
g = 9.81  # Aceleración debido a la gravedad (m/s^2)
t_max = 2  # Tiempo máximo de la simulación (s)

# Ecuaciones de movimiento
def x(t):
    return v0 * np.cos(theta) * t
def y(t):
    return v0 * np.sin(theta) * t - 0.5 * g * t**2

# Generar datos
t = np.linspace(0, t_max, 100)
x_values = x(t)
y_values = y(t)

# Crear la figura y el eje
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-')

# Función de actualización para la animación
def animate(i):
    line.set_data(x_values[:i], y_values[:i])
    return line,

# Crear la animación y asignarla a la variable anim
anim = FuncAnimation(fig, animate, frames=len(x_values), interval=10)

# Mostrar la animación
plt.show()