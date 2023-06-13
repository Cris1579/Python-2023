# Se tiene una tupla de frutas
# frutas = ("manzana","platano","pera","naranja","frutilla","manzana")
# Se pide:
# 1) Eliminar los repetidos
# 2) Agregar la palabra "mango"
# 3) Eliminar "platano"
# 4) Calcular la cantidad de frutas que existen
import collections

frutas = ("manzana","platano","pera","naranja","frutilla","manzana")
frutas_lista = list(frutas)
print("La lista original es: ")
print(frutas)

for fruta in frutas_lista:
    if frutas_lista.count(fruta) > 1:
        frutas_lista.remove(fruta)

print("\n Eliminando los repetidos, queda así: ")
print(frutas_lista)

frutas_lista.append("mango")
print("\n Añadiendo 'mango': ")
print(frutas_lista)

frutas_lista.remove("platano")
print("\n Removiendo platano: ")
print(frutas_lista)

Contador = collections.Counter(frutas_lista)
print("\n La cantidad de frutas es: ")
print(Contador)

