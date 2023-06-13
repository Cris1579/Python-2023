# Algoritmo donde se simule el proceso de apilar libros en una biblioteca
# Para luego ir sacandolos utilizando el principio de pilas.
# Utilizar clases y funciones

class stack:
    def __init__(self):
        self.top = None
        self.stack = []
    def push(self,item):
        self.top = item
        self.stack.append(item)
        return self.top
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

    def tope(self):
        if self.is_empty():
            return None
        return self.stack[-1]

#Para usarlo
pila_libros = stack()
# Agregando elementos
pila_libros.push("Libro_1")
pila_libros.push("Libro_2")
pila_libros.push("Libro_3")
pila_libros.push("Libro_4")
print("La pila es: ")
print(pila_libros)
#Verificando si la pila esta vacía
if pila_libros.is_empty():
    print("Esta vacía")

# Obtener el libro en la parte superior
ultimo_libro = pila_libros.tope()
print("\nEl libro en la parte superior es: ",ultimo_libro)

# Sacando un libro
while pila_libros.size() > 0:
    libro_sacado = pila_libros.pop()
    print("\nSacando de la parte superior al libro:",libro_sacado,",la pila queda:")
    print(pila_libros)
if pila_libros.is_empty():
    print("Ahora la pila esta vacía")


