# Crear dos matrices solicitando datos (cantidad de filas y columnas)
# Los elementos de las matrices deben ser aleatorios (de 1 a 5)
# Luego en una función ser sumados y en otra función ser restados
# NO usar numpy.

# Cuenta propia: No resuelto
# Posible solución:

import random
def matriz_random(filas, columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(1, 5)
            fila.append(elem)
        m.append(fila)
    return m


# Resta de matrices:
def resta_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final


# Suma de matrices:
def suma_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final


filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
print("Primera matriz aleatoria: ")
m1 = matriz_random(filas, columnas)
print(m1, "\n")
print("Segunda matriz aleatoria: ")
m2 = matriz_random(filas, columnas)
print(m2, "\n")

# Resta de las 2 matrices y se imprime la matriz resultante
matriz_final = resta_matrices(m1, m2)
print("La resta de las matrices da como resultado la siguiente matriz: ")
for fila in matriz_final:
    print(fila, "\n")

# Suma de las 2 matrices y se imprime la matriz resultante
matriz_final = suma_matrices(m1, m2)
print("La suma de las matrices da como resultado la siguiente matriz: ")
for fila in matriz_final:
    print(fila)
