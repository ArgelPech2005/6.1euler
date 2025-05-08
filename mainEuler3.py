#   Codigo que implementa el metodo de Euler
#   para resolver una ecuacion diferencial
#   
#
#           Autor:
#   Argel Jesus Pech Manrique
#   argelpech098@gmail.com  
#   Version 1.01 : 31/04/2025
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros del problema
T0 = 90           # Temperatura inicial (°C)
Tamb = 25         # Temperatura ambiente (°C)
k = 0.07          # Constante de enfriamiento
t0 = 0            # Tiempo inicial (minutos)
tf = 30           # Tiempo final (minutos)
n = 30            # Número de pasos

# Paso de tiempo
h = (tf - t0) / n

# Inicializar listas
t_vals = [t0]
T_euler = [T0]
T_exacta = [T0]  # La inicial es la misma

# Método de Euler
t = t0
T = T0
for i in range(n):
    T = T + h * (-k * (T - Tamb))
    t = t + h
    T_euler.append(T)
    t_vals.append(t)
    # Solución exacta en ese t
    T_ex = Tamb + (T0 - Tamb) * np.exp(-k * t)
    T_exacta.append(T_ex)

# Guardar en CSV
df = pd.DataFrame({
    "Tiempo (min)": t_vals,
    "T (Euler)": T_euler,
    "T (Exacta)": T_exacta
})
df.to_csv("enfriamiento_euler_vs_exacta.csv", index=False)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(t_vals, T_euler, 'o-', label="Euler", color='blue')
plt.plot(t_vals, T_exacta, '--', label="Exacta", color='red')
plt.title("Enfriamiento de un cuerpo - Método de Euler vs Exacta")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_enfriamiento.png")
plt.show()





