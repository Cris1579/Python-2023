# PT1: Crear dos matrices solicitando n° de filas y columnas
# Los elementos deben ser generados aleatoriamente (de 1 a 5)
# Luego se suman las matrices (Sin uso de librerias)
# PT2: La matriz resultante se debe multiplicar por un escalar
# del 1 al 10 (Se ingresa por teclado), se puede usar numpy
# PT3: La matriz resultante de PT2 se debe multiplicar por una nueva matriz
# Tanto el n° de filas y columnas como los elementos deben ser ingresados manual
# Se permite uso de numpy
import random
import numpy as np

#Parte 1
fila = int(input("Ingrese el n° de filas: "))
columna = int(input("Ingrese el n° de columnas: "))
def matriz_rdm (fila,columna):
    M = []
    for i in range(fila):
        fila = []
        for j in range(columna):
            elem = random.randint(1,5)
            fila.append(elem)
        M.append(fila)
    return M
def suma_matrices (m1,m2):
    ms = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        ms.append(fila)
    return ms
# Parte 2
def mult_matriz_escalar (ms,x):
    x = int(input("Ingrese algún n° entre 1 y 10: "))
    matriz_mult = []
    if x < 1 or x > 10:
        print("Por favor, ingrese un n° en el rango mencionado")
        return x
    else:
        for i in range(len(ms)):        #Agregado luego del laboratorio
            fila =[]
            for j in range(len(ms[0])):
                mult = ms[i][j] * x
                fila.append(mult)
            matriz_mult.append(fila)
        return matriz_mult              #fin
# Parte 3
fil = int(input("Ingrese el n° de filas: "))
colum = int(input("Ingrese el n° de columnas: "))
print("Ingrese los elementos para su tercera matriz: ")
mM = np.zeros((fil, colum))
for i in range(fil):
    for j in range(colum):
        elem = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        mM[i][j] = elem


m1 = matriz_rdm(fila,columna)
print("La matriz 1 es: ")
print(m1)
m2 = matriz_rdm(fila,columna)
print("La matriz 2 es: ")
print(m2)
sum_M = suma_matrices(m1, m2)
print("La suma de matrices resultante es: ")
print(sum_M)
#mul_escalar = mult_matriz_escalar(ms,x)
# m3 = matriz_manual(fila,columna)
