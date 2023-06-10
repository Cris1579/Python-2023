# filas = 3
# columnas = 3
# import numpy as np
#
# matriz = np.random.randint(1, 6, size=(filas, columnas))
#
# # Calcular la inversa de la matriz
# inversa = np.linalg.inv(matriz)
# # Multiplicar las matrices
# res= np.dot(matriz,inversa)
# print("Matriz original:")
# print(matriz)
# print("Inversa de la matriz:")
# print(np.around(inversa,decimals=2))
# print("mxi:")
# print(np.around(res,decimals=2))

# import numpy as np
#
# # Crear una matriz aleatoria de 3x3 con valores del 1 al 10
# A = np.random.randint(1, 11, size=(3, 3))
#
# # Calcular la inversa de A
# A_inv = np.linalg.inv(A)
#
# # Redondear ambas matrices a 2 decimales
# A_rounded = np.around(A, decimals=2)
# print("Matriz original:")
# for fila in A_rounded:
#     print(fila)
#
# A_inv_rounded = np.around(A_inv, decimals=2)
# print("\nInversa de la matriz:")
# for fila in A_inv_rounded:
#     print(fila)
#
#
# # Calcular el resultado de multiplicar A por su inversa
# result_rounded = np.around(np.dot(A, A_inv), decimals=2)
# print("\nMultiplicacion REDONDEADA de la matriz por su inversa:")
# for fila in result_rounded:
#     print(fila)
#
# # Comprobar si el resultado es igual a la matriz identidad
# identity = np.identity(3)
# if np.allclose(result_rounded, identity):
#     print("\nEl resultado es igual a la matriz identidad"
#           "\nPor lo tanto se comprueba que A x A^-1 = I, siendo I = Matriz identidad")
# else:
#     print("El resultado no es igual a la matriz identidad")


