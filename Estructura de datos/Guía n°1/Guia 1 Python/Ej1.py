# Crear una matriz 5x5 y sumar los elementos de cada columna
# imprimiendo la suma más alta entre todas las columnas
# Se incluye sumar los elementos de todas las filas
# y la suma más baja de todas las filas
# No usar numpy
import random

filas = 5
columnas = 5

def Cmr(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(0, 5)
            fila.append(elem)
        matriz.append(fila)
    return matriz

def suma_col(matriz):
    # Lo siguente es para recorrer una columna
    i = 0
    suma = 0
    columna_1 = []
    for fila in matriz:
        columna_1.append(fila[i])
    for elemnt in columna_1:
        suma += elemnt
    return suma

def suma_col2(matriz):
    i = 1
    suma = 0
    columna_2 = []
    for fila in matriz:
        columna_2.append(fila[i])
    for elemnt in columna_2:
        suma += elemnt
    return suma

def suma_col3(matriz):
    i = 2
    suma = 0
    columna_3 = []
    for fila in matriz:
        columna_3.append(fila[i])
    for elemnt in columna_3:
        suma += elemnt
    return suma

def suma_col4(matriz):
    i = 3
    suma = 0
    columna_4 = []
    for fila in matriz:
        columna_4.append(fila[i])
    for elemnt in columna_4:
        suma += elemnt
    return suma

def suma_col5(matriz):
    suma = 0
    i = 4
    columna_5 = []
    for fila in matriz:
        columna_5.append(fila[i])
    for elemnt in columna_5:
        suma += elemnt
    return suma

def suma_fil(filas):
    suma = 0
    for filas in matriz:
        for elemnt in filas:
            suma += elemnt
    return suma

def suma_bajaFil(matriz):
    suma = 0
    i = 0
    fila_1 = []
    for columna in matriz:
        fila_1.append(columna[i])
    for elemnt in fila_1:
        suma += elemnt

    return suma


def suma_bajaFil2(matriz):
    suma = 0
    i = 1
    fila_2 = []
    for columna in matriz:
        fila_2.append(columna[i])

    for elemnt in fila_2:
        suma += elemnt

    return suma


def suma_bajaFil3(matriz):
    suma = 0
    i = 2
    fila_3 = []
    for columna in matriz:
        fila_3.append(columna[i])

    for elemnt in fila_3:
        suma += elemnt

    return suma


def suma_bajaFil4(matriz):
    suma = 0
    i = 3
    fila_4 = []
    for columna in matriz:
        fila_4.append(columna[i])

    for elemnt in fila_4:
        suma += elemnt

    return suma


def suma_bajaFil5(matriz):
    suma = 0
    i = 4
    fila_5 = []
    for columna in matriz:
        fila_5.append(columna[i])
    for elemnt in fila_5:
        suma += elemnt

    return suma


matriz = Cmr(filas, columnas)
print("La matriz resultante es: ")
for fila in matriz:
    print(fila)

Stf = suma_fil(5)
print("\nLa suma de todas las filas es: ", Stf)
col1 = suma_col(matriz)
col2 = suma_col2(matriz)
col3 = suma_col3(matriz)
col4 = suma_col4(matriz)
col5 = suma_col5(matriz)
fila1 = suma_bajaFil(matriz)
fila2 = suma_bajaFil2(matriz)
fila3 = suma_bajaFil3(matriz)
fila4 = suma_bajaFil4(matriz)
fila5 = suma_bajaFil5(matriz)
cmd = max(col1, col2, col3, col4, col5)
fcm = min(fila1, fila2, fila3, fila4, fila5)
print("\nLa suma más baja entre las filas es: ", fcm)
print("\nLa suma más alta entre las columnas es: ", cmd)
