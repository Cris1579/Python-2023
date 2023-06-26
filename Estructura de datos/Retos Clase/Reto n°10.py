# Algoritmo que simule una lista de frutas
# por lista enlazada
# Se debe crear un menú:
# A) Agregar una fruta al final de la lista
# B) Agregar una fruta al inicio
# C) Eliminar una fruta
# D) Imprimir la lista actual
# E) Obtener cabecera
# F) Obtener cola
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None
class ListaEnlazada:
    def __init__(self):
        self.tope = None

    def agregar_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.tope is None:
            self.tope = nuevo_nodo
        else:
            actual = self.tope
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def agregar_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.next = self.tope
        self.tope = nuevo_nodo

    def imprimir_lista(self):
        actual = self.tope
        while actual:
            print(actual.dato,end=" -> ")
            actual = actual.next
        return None

    def obtener_top(self):
        return self.tope

    def obtener_cola(self):
        temporal = self.tope
        while temporal.next:
            temporal = temporal.next
        return temporal

    def existe(self,dato):
        actual = self.tope
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.next
        return False

    def eliminar(self,dato):
        actual = self.tope
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.next
        if actual:
            if anterior:
                anterior.next = actual.next
            else:
                self.tope = actual.next

def menu():
    print("\n********** MENÚ **********")
    print("¿Qué deseas hacer?")
    print("[1] Agregar una fruta al final de la lista")
    print("[2] Agregar una fruta al inicio de la lista")
    print("[3] Eliminar una fruta")
    print("[4] Imprimir lista")
    print("[5] Obtener tope")
    print("[6] Obtener cola")
    print("[7] Salir")
    print("***************************")
    print()
    opcion = str(input("Selecciona una opción: "))
    if opcion == "1":
        dato = input("\nIngrese una fruta: ")
        frutas.agregar_final(dato)
        menu()
    elif opcion == "2":
        dato = input("Ingrese una fruta: ")
        frutas.agregar_inicio(dato)
        menu()
    elif opcion == "3":
        dato = input("Fruta a eliminar: ")
        if frutas.existe(dato):
            print(f'La fruta"{dato}" fue eliminada de la lista.')
            frutas.eliminar(dato)
        else:
            print(f'La fruta"{dato}" no se encuentra en la lista')
        menu()
    elif opcion == "4":
        frutas.imprimir_lista()
        menu()
    elif opcion == "5":
        tope = frutas.obtener_top()
        print(tope)
        menu()
    elif opcion == "6":
        cola = frutas.obtener_cola()
        print(cola)
        menu()
    elif opcion == "7":
        print("Hasta luego :)")

    else:
        print("Ingrese un valor válido")
        menu()

frutas = ListaEnlazada()
menu()
