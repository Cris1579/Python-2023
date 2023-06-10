# Crear un algoritmo donde se solicite dos matrices
# Se deben ingresar las columnas y las filas
# Los elementos de las matrices deben ser generados de forma aleatoria (0 a 5)
# Se deben sumar estas matrices, luego se solicita una tercer matriz
# Debe poseer las mismas caracteristicas que las otras dos
# Esta última debe restar a matriz resultante de la suma

import random
def matriz_random_(filas, columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(0, 5)
            fila.append(elem)
        m.append(fila)
    return m
# Resta de matrices:
def resta_matrices(m2b, m3):
    matriz_final = []
    for i in range(len(m2b)):
        fila = []
        for j in range(len(m2b[0])):
            resta = m2b[i][j] - m3[i][j]
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
m1 = matriz_random_(filas, columnas)
print(m1, "\n")
print("Segunda matriz aleatoria: ")
m2 = matriz_random_(filas, columnas)
print(m2, "\n")


# Suma de las 2 primeras matrices y se imprime la matriz resultante
matriz_final = suma_matrices(m1, m2)
print("La suma de las matrices da como resultado la siguiente matriz: ")
for fila in matriz_final:
    print(fila,"\n")
m2b = matriz_final
#Se pide una tercera matriz
m3 = matriz_random_(filas,columnas)
print("Tercera matriz aleatoria: ")
print(m3,"\n")

# Resta de la matriz resultante con la tercer matriz y se imprime la matriz resultante
matriz_final = resta_matrices(m2b,m3)
print("La resta de las matrices da como resultado la siguiente matriz: ")
for fila in matriz_final:
   print(fila)