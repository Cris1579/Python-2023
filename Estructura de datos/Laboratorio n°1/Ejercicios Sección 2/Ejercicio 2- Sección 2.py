# Crear matriz solicitando filas y columnas
# Ingresar un escalar
# Elementos de la matriz deben ser aleatorios (0 al 10)
# Multiplicar la matriz con el escalar

import random

def matriz_random(filas, columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(0, 10)  # N° aleatorio entre 0 y 10
            fila.append(elem)
        m.append(fila)
    return m
def mult_matriz(m,escalar):
    matriz_final = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            mult = m[i][j] * escalar
            fila.append(mult)
        matriz_final.append(fila)
    return matriz_final



filas = int(input("Ingrese el n° de filas para la matriz:\n"))
columnas = int(input("Ingrese el n° de columnas para la matriz:\n"))
escalar = int(input("Ingrese algún número:\n"))

m = matriz_random(filas,columnas)
print("La matriz aleatoria resultante es: ")
print(m,"\n")
#Multiplicación entre la matriz y el escalar
matriz_final = mult_matriz(m,escalar)
print("La multiplicación da como resultado: ")
for fila in matriz_final:
    print(fila)
