import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

# Definimos la variable simbólica x
x = sp.Symbol('x')

# Definimos la función y = 4x + 5
y = 4*x + 5

# Creamos un arreglo de 10 valores de x entre -2 y 2
x_values = np.linspace(-2, 2, 10)

# Evaluamos la función y para cada valor de x
y_values = [y.subs(x, value) for value in x_values]

# Imprimimos los puntos (x, y)
for x, y in zip(x_values, y_values):
    print(f"({x:.2f}, {y:.2f})")
plt.plot(x_values, y_values, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y = 4x + 5')
plt.grid(True)
plt.show()