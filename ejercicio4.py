import numpy as np
from scipy.optimize import minimize

# Función objetivo
def objective(x):
    return x**2 + 4*x + 5

# Restricciones
def constraint1(x):
    return x - 2

def constraint2(x):
    return 5 - x

# Configuración de las restricciones
cons = ({'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2})

# Punto inicial
x0 = [3.5]  # Un punto inicial que satisface ambas restricciones

# Optimización
sol = minimize(objective, x0, method='SLSQP', constraints=cons)

# Resultados
print("Solución óptima:")
print(f"x = {sol.x[0]:.4f}")
print(f"Valor mínimo de la función = {sol.fun:.4f}")
print(f"Éxito: {sol.success}")
print(f"Mensaje: {sol.message}")

# Verificación de las restricciones
print("\nVerificación de restricciones:")
print(f"g1(x) = {constraint1(sol.x[0]):.4f} >= 0")
print(f"g2(x) = {constraint2(sol.x[0]):.4f} >= 0")

# Gráfica de la función y la solución
import matplotlib.pyplot as plt

x = np.linspace(1, 6, 100)
y = objective(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x² + 4x + 5')
plt.axvline(x=2, color='r', linestyle='--', label='x = 2')
plt.axvline(x=5, color='g', linestyle='--', label='x = 5')
plt.plot(sol.x[0], sol.fun, 'ro', label='Punto óptimo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función objetivo y punto óptimo')
plt.legend()
plt.grid(True)
plt.show()