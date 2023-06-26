# Integrantes:
# Antoine Briones - Cristopher González


# Desarrollar un programa para realizar operaciones estadísticas básicas sobre una serie de
# datos. Implementar una lista enlazada simple para almacenar los datos y proporciona las
# siguientes funcionalidades:
# A. Agregar datos: Permite ingresar un nuevo dato a la lista.
# B. Calcular media: Calcula y devuelve la media (promedio) de los datos almacenados
# en la lista.
# C. Calcular desviación estándar: Calcula y devuelve la desviación estándar de los
# datos almacenados en la lista.
# D. Imprimir lista: Muestra en pantalla los datos almacenados en la lista.
# E. Verificar si la lista está vacía: Devuelve un valor booleano que indica si la lista está
# vacía.
# El programa debe utilizar una clase Nodo para representar cada dato de la lista enlazada y
# una clase ListaEnlazada que administre la lista y contenga las funcionalidades
# mencionadas. La desviación estándar debe calcularse utilizando la fórmula estadística
# adecuada

import math
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
        self.longitud += 1

    def promedio(self):
        if self.longitud == 0:
            return None
        suma = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            suma += nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
        return suma / self.longitud

    def desviacion_estandar(self):
        if self.longitud == 0:
            return None
        suma = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            suma += nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
        media = suma / self.longitud
        suma_cuadrados = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            suma_cuadrados += (nodo_actual.valor - media) ** 2
            nodo_actual = nodo_actual.siguiente
        varianza = suma_cuadrados / self.longitud
        desviacion_estandar = math.sqrt(varianza)
        return desviacion_estandar

    def imprimir(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        print(f"Los números son : ({', '.join(valores)})")

    def revisar(self):
        act = self.cabeza
        while act:
            print(type(act.valor), end=" - ")
            act = act.siguiente
        return None

    def isEmpty(self):
        return f"¿La lista está vacía?   R: {self.cabeza is None}"


def menu():
    print("\n1. Agregar número")
    print("2. Calcular promedio")
    print("3. Calcular desviación estándar")
    print("4. Imprimir lista de números")
    print("5. Revisar si hay números en lista")
    print("6. Salir\n")
    opcion = input("Opción: ")
    print() #Espacio vacio

    if opcion == "1":
        numero = float(input("Ingrese un número: "))
        lista.agregar(numero)
        menu()

    elif opcion == "2":
        promedio = lista.promedio()
        if promedio is None:
            print("La lista está vacía.")
        else:
            print("El promedio es:", round(promedio, 4))
        menu()

    elif opcion == "3":
        desviacion = lista.desviacion_estandar()
        if desviacion is None:
            print("La lista está vacía.")
        else:
            print("La desviación estándar es:", round(desviacion, 4))
        menu()

    elif opcion == "4":
        lista.imprimir()
        menu()

    elif opcion == "5":
        print(lista.isEmpty())
        menu()

    elif opcion == "6":
        print("Saliendo...")

    else:
        print("Opción inválida.")
        menu()

lista = ListaEnlazada()
menu()