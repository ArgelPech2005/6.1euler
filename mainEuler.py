#   Codigo que implementa el metodo de Euler
#   para resolver una ecuacion diferencial
#   
#
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/04/2025
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definición de la EDO: dy/dx = f(x, y)
def f(x, y):
    return x + y

# Condiciones iniciales
x0 = 0
y0 = 1
xf = 2
n = 10

# Paso
h = (xf - x0) / n

# Inicialización de listas para almacenar resultados
x_vals = [x0]
y_vals = [y0]

# Método de Euler
x = x0
y = y0
for i in range(n):
    y = y + h * f(x, y)
    x = x + h
    x_vals.append(x)
    y_vals.append(y)

# Guardar resultados en archivo CSV
data = {
    "x": x_vals,
    "y_aproximada": y_vals
}
df = pd.DataFrame(data)
csv_path = "euler_resultados.csv"
df.to_csv(csv_path, index=False)

# Graficar la solución aproximada
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, 'o-', label='Solución aproximada (Euler)', color='blue')
plt.title('Método de Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
image_path = "euler_solucion.png"
plt.savefig(image_path)
plt.show()

