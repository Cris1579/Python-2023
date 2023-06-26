# Integrantes:
# Antoine Briones - Cristopher González


# Se está implementando un programa para administrar una cola de atención al cliente en
# una farmacia. Cada cliente tiene un número de ticket y un número de caja para que pueda
# ser atendido. Se solicita implementar un algoritmo que contenga una lista circular para
# manejar la cola de atención de tres cajas: Caja 1, Caja 2 y Caja 3.


class Cliente:
    def __init__(self, ticket, nCaja):
        self.ticket = ticket
        self.nCaja = nCaja

class Nodo:
    def __init__(self, cliente=None):
        self.cliente = cliente
        self.next = None

class ListaCircular:
    def __init__(self):
        self.first = None
        self.count = 0

    def add(self, cliente):
        newNode = Nodo(cliente)
        if self.first is None:
            self.first = newNode
            newNode.next = self.first
        else:
            actual = self.first
            while actual.next != self.first:
                actual = actual.next
            actual.next = newNode
            newNode.next = self.first
        self.count += 1
        if self.count == 3:
            self.count = 0

    def imprimir(self):
        if self.first is None:
            print("La lista está vacía")
        else:
            actual = self.first
            while True:
                print(f"Ticket N°{actual.cliente.ticket}    -   Caja N°{actual.cliente.nCaja}")
                actual = actual.next
                if actual == self.first:
                    break


lista = ListaCircular()
lista.add(Cliente(1, 1))
lista.add(Cliente(2, 2))
lista.add(Cliente(3, 3))
lista.add(Cliente(4, 1))
lista.add(Cliente(5, 2))
lista.imprimir()