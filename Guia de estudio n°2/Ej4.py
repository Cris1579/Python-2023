# Integrantes:
# Antoine Briones - Cristopher González


# Un supermercado necesita un programa para el manejo de un almacén de productos en una
# de sus sucursales. Los productos se reciben en una pila y se despachan en una cola para su
# entrega a los clientes. Se solicita implementar un algoritmo que incluya tanto el uso de pila y
# cola. Debe realizarse las siguientes operaciones:
# A. Agregar producto: Permite ingresar un nuevo producto al almacén. El producto se
# agrega a la pila de productos recibidos.
# B. Despachar producto: Remueve el producto más antiguo de la cola y lo entrega al
# cliente. Si la cola está vacía, muestra un mensaje indicando que no hay productos
# disponibles para despachar.
# C. Verificar si la pila de productos recibidos está vacía: Devuelve un mensaje que
# indica si la pila de productos recibidos está vacía.
# D. Verificar si la cola de productos para despachar está vacía: Devuelve un mensaje
# que indica si la cola de productos para despachar está vacía.
# E. Imprimir lista de productos recibidos: Muestra en consola los productos
# almacenados en la pila de productos recibidos.
# F. Imprimir lista de productos para despachar: Muestra en consola los productos
# almacenados en la cola de productos para despachar.
# G. Mostrar cantidad total de productos en el almacén: Muestra en consola la
# cantidad total de productos que hay en el almacén, sumando la cantidad de
# productos recibidos en la pila y la cantidad de productos para despachar en la cola.


class PilaYCola:
    def __init__(self):
        self.top = None
        self.productoPila = []
        self.productoCola = []
        self.eliminado = []
    def push(self,item):
        self.top = item
        self.productoPila.append(item)
        return self.top

    def pop(self):
        if self.is_empty():
            return None
        return self.productoPila.pop(0)

    def __str__(self):
        return str(self.productoPila)

    def is_empty(self):
        return len(self.productoPila) == 0

    def size(self):
        return len(self.productoPila)


    def encolar(self,x):
        self.productoCola.append(x)

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            eliminado = self.productoCola.pop(0)
            self.eliminado.append(eliminado)
            return eliminado

    def list_eliminados(self):
        print(self.eliminado)
    def esta_vacia(self):
        return len(self.productoCola) == 0

    def tamaño(self):
        return self.productoCola


def menu():
    print("\n********** MENÚ **********")
    print("[1] Agregar producto")
    print("[2] Despachar producto")
    print("[3] Verificar si hay productos")
    print("[4] Verificar si hay productos para despachar")
    print("[5] Imprimir lista productos recibidos")
    print("[6] Imprimir lista productos despachados")
    print("[7] Imprimir todos los productos")
    print("[8] Salir")
    print("***************************")

    opcion =input("Seleccione su opción: ")

    if opcion == "1":
        producto = str(input("Ingrese un producto: "))
        lista.push(producto)
        lista.encolar(producto)
        menu()

    elif opcion == "2":
        despachar = lista.desencolar()
        if despachar is None:
            print("No quedan productos a despachar")
        else:
            print("Se ha retirado un producto")
            lista.pop()
        menu()

    elif opcion == "3":
        if lista.is_empty():
            print("No hay productos en el almacén")
        else:
            print("Si hay/quedan productos en el almacén")
        menu()

    elif opcion == "4":
        if lista.esta_vacia():
            print("No hay elementos a despachar")
        else:
            print("Hay/quedan productos a despachar")
        menu()

    elif opcion == "5":
        productos = lista.__str__()
        print(productos)
        menu()
    elif opcion == "6":
        productos = lista.eliminado
        print(productos)
        menu()
    elif opcion == "7":
        productosAlm = lista.__str__()
        productosDesp = lista.eliminado
        print("Productos en el almacén: ",productosAlm)
        print("Productos despachados: ",productosDesp)
        menu()

    elif opcion == "8":
        print("Saliendo...")
    else:
        print("Opción inválida.")
        menu()


lista = PilaYCola()
menu()