
#           Autor:
#   Argel Jesus Pech Manrique
#   argelpech098@gmail.com  
#   Version 1.01 : 25/04/2025
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Definición de la EDO del capacitor: dV/dt = (1 / RC) * (V_fuente - V)
def f(t, V):
    R = 1000           # Resistencia en ohmios (Ω)
    C = 0.001          # Capacitancia en faradios (F)
    V_fuente = 5       # Voltaje de la fuente en voltios (V)
    return (1 / (R * C)) * (V_fuente - V)

# Condiciones iniciales y parámetros
x0 = 0      # Tiempo inicial (s)
y0 = 0      # Voltaje inicial (V)
xf = 5      # Tiempo final (s)
n = 20      # Número de pasos

h = (xf - x0) / n  # Tamaño del paso (Δt)

# Inicialización de listas
x_vals = [x0]         # Lista de tiempos
y_vals = [y0]         # Lista de voltajes aproximados
y_exact = [0]         # Lista de voltajes exactos
errores = [0]         # Lista de errores absolutos

# Valores constantes para la solución exacta
R = 1000
C = 0.001
V_fuente = 5

# Método de Euler + comparación con la solución exacta
x = x0
y = y0
for i in range(n):
    y = y + h * f(x, y)            # Euler: nuevo valor de voltaje
    x = x + h                      # Avanza en el tiempo
    y_real = V_fuente * (1 - np.exp(-x / (R * C)))  # Solución analítica
    error = abs(y_real - y)        # Error absoluto
    
    # Guardar valores
    x_vals.append(x)
    y_vals.append(y)
    y_exact.append(y_real)
    errores.append(error)

# Guardar resultados en archivo CSV
df = pd.DataFrame({
    "Tiempo (s)": x_vals,
    "V_aproximada (V)": y_vals,
    "V_exacta (V)": y_exact,
    "Error_absoluto (V)": errores
})
df.to_csv("carga_capacitor_comparacion.csv", index=False)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, 'o-', label='Solución aproximada (Euler)', color='blue')
plt.plot(x_vals, y_exact, '-', label='Solución exacta', color='red')
plt.title('Carga de un Capacitor - Comparación Euler vs Exacta')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.savefig("carga_capacitor_comparacion.png")
plt.show()


