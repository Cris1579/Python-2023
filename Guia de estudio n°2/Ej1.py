# Integrantes:
# Antoine Briones - Cristopher González


# Un equipo de desarrolladores tiene la misión de programar una aplicación de reproducción
# de música y se necesita implementar una lista enlazada doble para administrar la lista de
# reproducción de un usuario en específico. Cada nodo de la lista representa una canción, y
# cada canción tiene un título y un artista.
# Se solicita implementar una lista enlazada doble para una lista de reproducción de música.


class Node:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.back = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmptyForClassOnly(self):
        return self.first is None

    def isEmpty(self):
        if self.first is None:
            return "La Lista NO tiene canciones"
        else: return "La lista SI tiene canciones"

    def addLast(self, dato):
        newNode = Node(dato)
        if self.isEmptyForClassOnly():
            self.first = newNode
            self.last = newNode
        else:
            newNode.back = self.last
            self.last.next = newNode
            self.last = newNode

    def addFirst(self, dato):
        newNode = Node(dato)
        if self.isEmptyForClassOnly():
            self.first = newNode
            self.last = newNode
        else:
            newNode.next = self.first
            self.first.back = newNode
            self.first = newNode

    def imprimir(self):
        actual = self.first
        while actual:
            print(actual.dato)
            actual = actual.next

    def giveFirst(self):
        return self.first.dato if self.first else None

    def giveLast(self):
        return self.last.dato if self.last else None

    def exist(self, search):
        actual = self.first
        while actual:
            if actual.dato == search:
                return  True
            actual = actual.next
        return False

    def delete(self, search):
        actual = self.first
        while actual:
            if actual.dato == search:
                if actual.back:
                    actual.back.next = actual.next
                else: self.first = actual.next
                if actual.next:
                    actual.next.back = actual.back
                else: self.last = actual.back
                break
            actual = actual.next


def menu():
    print("\nSeleccione una opción:")
    print("1. Agregar canción al inicio")
    print("2. Agregar canción al final")
    print("3. Imprimir lista de canciones")
    print("4. Obtener primera canción")
    print("5. Obtener ultima canción")
    print("6. Buscar canción")
    print("7. Eliminar canción")
    print("8. Revisar si hay canciones en lista")
    print("9. Salir\n")

    opcion = input("Opción: ")
    print() #Espacio vacio
    if opcion == "1":
        dato = input("La canción agregada al inicio es: ")
        lista.addFirst(dato)
        menu()
    elif opcion == "2":
        dato = input("La canción agregada al final es: ")
        lista.addLast(dato)
        menu()
    elif opcion == "3":
        lista.imprimir()
        menu()
    elif opcion == "4":
        cabecera = lista.giveFirst()
        print("Primera canción:", cabecera)
        menu()
    elif opcion == "5":
        cola = lista.giveLast()
        print("Última canción:", cola)
        menu()
    elif opcion == "6":
        search = input("Ingrese la canción a buscar: ")
        if lista.exist(search):
            print(f'La canción "{search}" SI se encuentra en la lista.')
        else:
            print(f'La canción "{search}" NO se encuentra en la lista.')
        menu()
    elif opcion == "7":
        search = input("Ingrese la canción a eliminar: ")
        if lista.exist(search):
            print(f'La canción "{search}" fue eliminada de la lista.')
            lista.delete(search)
        else:
            print(f'La canción "{search}" NO se encuentra en la lista.')
        menu()
    elif opcion == "8":
        print(lista.isEmpty())
        menu()
    elif opcion == "9":
        print("Saliendo...")
    else:
        print("Opción inválida.")
        menu()

lista = ListaDoblementeEnlazada()
menu()