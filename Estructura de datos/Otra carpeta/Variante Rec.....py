#Variante 21/05 by ChatGPT
def suma_columnas(matriz):
    num_columnas = len(matriz[0])  # Obtener el número de columnas
    suma_columnas = [0] * num_columnas  # Lista para almacenar la suma de cada columna

    for fila in matriz:
        for columna_deseada in range(num_columnas):
            elemento = fila[columna_deseada]
            suma_columnas[columna_deseada] += elemento

    # Imprimir la suma de cada columna junto con su índice
    print("Suma de cada columna:")
    for indice, suma in enumerate(suma_columnas):
        columna = indice + 1  # Ajustar el índice de la columna (comenzando en 1 en lugar de 0)
        print("Columna", columna, ":", suma)

    # Encontrar el valor más alto
    maximo = max(suma_columnas)
    indice_maximo = suma_columnas.index(maximo) + 1  # Obtener el índice de la columna más alta
    print("Valor más alto en la columna", indice_maximo, ":", maximo)

# Ejemplo de uso
matriz = [
    [1, 7, 1],
    [4, 5, 6],
    [7, 8, 9]
]

suma_columnas(matriz)
