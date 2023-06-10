# Crear un arreglo aleatorio de tamaño entre 10 a 30
# Imprimir el arreglo creado y luego solicitar por consola la busqueda de un elemento
# en específico del arreglo creado
# esto utilizando array.

import random
import array

Número = random.randint(10,30) #Genera un número entre 10 y 30
arr = array.array('i',[]) # Crea un arreglo vacío de enteros
for i in range(Número):
    arr.append(random.randint(1,30)) #Agrega un número aleatorio entre 1 y 30 al arreglo
print(arr)


Busqueda_Num = int(input("¿Qué número desea buscar?: "))
num = arr.count(Busqueda_Num)

print ("El número que escogió sale un total de: ",num,"veces")

