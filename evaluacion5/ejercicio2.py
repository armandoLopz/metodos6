def volumen_carga(capacidad, pesos, valores):
    n = len(pesos)
    # Crear matriz de programación dinámica
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    # Llenar la matriz
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(valores[i-1] + dp[i][w-pesos[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Encontrar los objetos seleccionados
    w = capacidad
    seleccionados = [0] * n
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            seleccionados[i-1] += 1
            w -= pesos[i-1]
            # Permitir múltiples unidades del mismo objeto
            while w >= pesos[i-1] and dp[i][w] == dp[i][w-pesos[i-1]] + valores[i-1]:
                seleccionados[i-1] += 1
                w -= pesos[i-1]
    
    return dp[n][capacidad], seleccionados

# Datos del problema
espacios = [1, 2, 3, 4]  # Espacios ocupados por cada objeto
valores = [50, 80, 30,20]  # Valor en miles de monedas
capacidad = 4  # Capacidad total del inventario

# Ejecutar el algoritmo
valor_maximo, objetos_seleccionados = volumen_carga(capacidad, espacios, valores)

print("Resultados del algoritmo VolumenCarga:")
print(f"Valor máximo obtenido: {valor_maximo}k monedas")
print("\nObjetos seleccionados:")
nombres = ["Espada", "Casco", "Botas", "Pocion"]
for i, cantidad in enumerate(objetos_seleccionados):
    print(f"{nombres[i]}: {cantidad} unidad(es)")

print("\nVerificación de restricciones:")
espacio_usado = sum(espacios[i] * objetos_seleccionados[i] for i in range(len(espacios)))
print(f"Espacio total usado: {espacio_usado}/{capacidad}")