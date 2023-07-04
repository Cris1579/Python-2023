class Pila:
    def __init__(self):
        self.top = None
        self.stack = ["Informe final", "Guía de estudio","Tesis 4","Seminario Osorno"]
    def push(self,x):
        self.top = x
        self.stack.append(x)
    def pop(self):
        if self.esta_vacio():
            return None
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def esta_vacio(self):
        return len(self.stack) == 0
    def __str__(self):
        print (str(self.stack))
    def tope(self):
        if self.esta_vacio():
            return None
        return self.stack[-1]

Documentos = Pila()
print("La lista original es: ")
Documentos.__str__()
print("Añadiendo 'Avance Tesis' queda: ")
Documentos.push("Avance Tesis")
Documentos.__str__()
print("Añadiendo 'Proyecto Integrador' queda: ")
Documentos.push("Proyecto Integrador")
Documentos.__str__()

print("\n El elemento que está en el tope es: ")
print(Documentos.tope())
Documentos.pop()
print("\n Eliminando el que esta en el tope, la lista queda: ")
Documentos.__str__()

if not Documentos.esta_vacio():
    print("\n La lista no está vacía")