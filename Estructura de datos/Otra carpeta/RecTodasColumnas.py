# Este algoritmo recorre todas las columnas y las imprime verticalmente

def recorrer_columnas(matriz):
    num_columnas = len(matriz[0])  # Obtener el número de columnas

    for columna_deseada in range(num_columnas):
        for fila in matriz:
            elemento = fila[columna_deseada]
            # Aquí puedes hacer algo con el elemento de la columna, como imprimirlo
            print(elemento)
        # Agregar una línea en blanco entre columnas
        print()

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
recorrer_columnas(matriz)
