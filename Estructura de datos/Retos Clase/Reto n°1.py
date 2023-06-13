# Ordenar de forma descendente, luego de forma aleatoria
import random

Numeros = [1, 3, 11, 7, 5, 9, 13]
Numeros.sort(key=None , reverse=True)

#Ahora con palabras
Palabras = ["Papa","Banana","Zapallo","Tomate"]
Palabras.sort(key=None , reverse=True)
print("Lista de palabras")
print(Palabras)

#Ahora de forma aleatoria
print("\n Lista original de números")
print(Numeros)
random.shuffle(Numeros)
print("\n Primera lista random")
print(Numeros)
random.shuffle(Palabras)
print("\n Segunda lista random")
print(Palabras)
