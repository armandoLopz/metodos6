import numpy as np
from scipy.optimize import minimize

# Función objetivo
def objective(x):
    return -0.1 * x[0] - 0.08 * x[1]  # Negativo porque minimize busca el mínimo

# Restricciones
def constraint1(x):
    return x[0] + x[1] - 1

def constraint2(x):
    return 0.05 - (0.02 * x[0]**2 + 0.03 * x[1]**2)

# Configuración de las restricciones
con1 = {'type': 'eq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
cons = [con1, con2]

# Punto inicial
x0 = [0.5, 0.5]

# Optimización
sol = minimize(objective, x0, method='SLSQP', constraints=cons)

# Resultados
print("Solución óptima:")
print(f"x = {sol.x[0]:.4f}")
print(f"y = {sol.x[1]:.4f}")
print(f"Rendimiento máximo = {-sol.fun:.4f}")
print(f"Éxito: {sol.success}")
print(f"Mensaje: {sol.message}")