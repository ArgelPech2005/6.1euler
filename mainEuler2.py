#   Codigo que implementa el metodo de Euler
#   para resolver una ecuacion diferencial
#   

#           Autor:
#   Argel Jesus Pech Manrique
#   argelpech098@gmail.com  
#   Version 1.01 : 31/04/2025
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definición de la EDO: dv/dt = g - (k/m) * v
def f(x, y):
    g = 9.81      # Aceleración de la gravedad (m/s²)
    m = 2         # Masa del objeto (kg)
    k = 0.5       # Coeficiente de fricción (kg/s)
    return g - (k / m) * y

# Condiciones iniciales
x0 = 0     # Tiempo inicial (s)
y0 = 0     # Velocidad inicial (v(0) = 0)
xf = 10    # Tiempo final (s)
n = 50     # Número de pasos

# Paso de integración
h = (xf - x0) / n  # Tamaño de paso (Δt)

# Inicialización de listas
x_vals = [x0]      # Lista de tiempos
y_vals = [y0]      # Lista de velocidades aproximadas

# Método de Euler
x = x0
y = y0
for i in range(n):
    y = y + h * f(x, y)  # Estimación de la velocidad
    x = x + h            # Avance en el tiempo
    x_vals.append(x)
    y_vals.append(y)

# Solución exacta para comparar
g = 9.81
m = 2
k = 0.5
x_exact = np.linspace(x0, xf, 200)
y_exact = (m * g / k) * (1 - np.exp(-(k / m) * x_exact))

# Guardar resultados en CSV
data = {
    "Tiempo (s)": x_vals,
    "v_aproximada (m/s)": y_vals
}
df = pd.DataFrame(data)
df.to_csv("caida_libre_euler.csv", index=False)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, 'o-', label='Euler (aproximado)', color='blue')
plt.plot(x_exact, y_exact, '-', label='Solución exacta', color='red')
plt.title('Caída Libre con Resistencia del Aire - Método de Euler')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()
plt.savefig("caida_libre_euler.png")
plt.show()


