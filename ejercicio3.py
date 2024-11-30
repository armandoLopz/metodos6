import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    return x**2 + y**2 + z**2 - 2*x*y + 3*z

def gradient(x, y, z):
    dx = 2*x - 2*y
    dy = 2*y - 2*x
    dz = 2*z + 3
    return np.array([dx, dy, dz])

def gradient_descent(start_point, learning_rate, num_iterations):
    point = np.array(start_point)
    f_values = []
    
    for _ in range(num_iterations):
        grad = gradient(*point)
        point = point - learning_rate * grad
        f_values.append(f(*point))
    
    return point, f_values

# Parámetros iniciales
start = np.array([1, 1, 1])
alpha = 0.1
iterations = 15

# Ejecutar el descenso del gradiente
final_point, f_history = gradient_descent(start, alpha, iterations)

# Imprimir resultados
print(f"Punto final después de {iterations} iteraciones: {final_point}")
print(f"Valor mínimo de la función: {f(*final_point)}")

# Graficar la evolución del valor de la función
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), f_history, marker='o')
plt.title('Evolución del valor de la función durante el descenso del gradiente')
plt.xlabel('Iteración')
plt.ylabel('f(x, y, z)')
plt.grid(True)
plt.show()