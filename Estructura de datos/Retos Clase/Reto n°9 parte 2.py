# Algoritmo donde se simule el proceso de atención de un banco
# Se debe crear una lista con los nombres de los clientes
# Utilizar Clase y funciones

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self,x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def __str__(self): # Tamaño
        return str(self.items)


atcClt = Cola()
if atcClt.esta_vacia():
    print("No hay nadie en la cola actualmente")

#Agregar personas
atcClt.encolar("Carlos")
print("Ha ingresado: ",atcClt)
atcClt.encolar("Rigo")
print("Ha ingresado alguien más, quedando la fila: ",atcClt)
atcClt.encolar("Rodri")
print("Ha ingresado alguien más, quedando la fila: ",atcClt)

#Sacando personas
if len(atcClt.__str__()) > 0:
    personaOut = atcClt.desencolar()
    print("Se ha retirado", personaOut ,",quedando la fila así: ")
    print(atcClt)
if atcClt.esta_vacia():
    print("No queda nadie en la fila")
