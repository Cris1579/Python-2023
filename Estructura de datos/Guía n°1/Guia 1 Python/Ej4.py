#Aplicar el metodo de Gauss para invertir una matriz aleatoria de 3 a 5 de dimensión sin
#utilizar librerias (excepto el uso de la libreria Random). Imprimir la matriz original y luego
#la matriz inversa. Recordar que si una matriz A es una matriz cuadrada no-singular, es
#decir, tal que su determinante es distinto de cero se puede utilizar el Metodo de Eliminacion Gaussiana.
#El calculo de la inversa se realiza ampliando la matriz A adosando la
#matriz identidad a su lado derecho

import random
# dim = Dimension
def crearMtrx(dim):

    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            fila.append(random.randint(1, 9))
        matriz.append(fila)
    return matriz

def printMtrx(matriz):
    for fila in matriz:
        print(fila)

def intercambiarFilas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def multFilas(matriz, fila, escalar):
    for i in range(len(matriz[fila])):
        matriz[fila][i] *= escalar

def sumFilas(matriz, fila_destino, fila_origen, factor):
    for i in range(len(matriz[fila_destino])):
        matriz[fila_destino][i] += factor * matriz[fila_origen][i]

def mIdentidad(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def mInvert(matriz):
    dim = len(matriz)
    identidad = mIdentidad(dim)
    for i in range(dim):
        # buscar el mayor elemento en la columna
        vmax = abs(matriz[i][i])
        fmax = i
        for j in range(i + 1, dim):
            if abs(matriz[j][i]) > vmax:
                vmax = abs(matriz[j][i])
                max_row = j
        # Intercambiar filas de ser necesario
        if fmax != i:
            intercambiarFilas(matriz, i, fmax)
            intercambiarFilas(identidad, i, fmax)
        # Hacer ceros
        for j in range(i + 1, dim):
            factor = -matriz[j][i] / matriz[i][i]
            sumFilas(matriz, j, i, factor)
            sumFilas(identidad, j, i, factor)
    # Hacer unos
    for i in range(dim):
        escalar = 1 / matriz[i][i]
        multFilas(matriz, i, escalar)
        multFilas(identidad, i, escalar)
    return identidad

# Matriz de dim 3 a 5
dimension = random.randint(3, 5)
m = crearMtrx(dimension)


print("Matriz original:")
printMtrx(m)

# Invertir la matriz con Gauss
mInv = mInvert(m)


print("\nMatriz inversa (redondeada):")
for i in range(len(mInv)):
    for j in range(len(mInv[i])):
        mInv[i][j] = round(mInv[i][j], 2)
printMtrx(mInv)
