# Ejemplo de como hacer una transpuesta
# Definir una matriz de ejemplo
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Obtener las dimensiones de la matriz
filas = len(matriz)
columnas = len(matriz[0])

# Crear una nueva matriz para almacenar la transpuesta
transpuesta = []
for j in range(columnas):
    fila_transpuesta = []
    for i in range(filas):
        fila_transpuesta.append(matriz[i][j])
    transpuesta.append(fila_transpuesta)

# Imprimir la matriz transpuesta
for fila in transpuesta:
    print(fila)
