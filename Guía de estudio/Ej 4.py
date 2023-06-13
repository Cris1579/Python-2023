# Desarrollar un algoritmo que contenga 6 productos de supermercado, utilizando colas
# Hacer un método que agregue un producto
# Crear un metodo para eliminar el primer producto de la cola
# Una función que muestre los productos, sin modificar la cola
# Metodo que invierta el orden de productos
# Función que elimine todos los productos

class Cola:
    def __init__(self):
        self.cola = ["Yoghurt","Mantequilla","Lentejas","Arroz","Tomates","Jabón"]
    def encolar(self,x):
        self.cola.append(x)
    def desencolar(self):
        if self.esta_vacio():
            return None
        return self.cola.pop()
    def esta_vacio(self):
        return len(self.cola) == 0
    def __str__(self):
        print (str(self.cola))
    def vaciar(self):
        if not self.esta_vacio():
            self.cola.clear()
        return None
    def invertir(self):
        return self.cola.reverse()

supermerk2 = Cola()
print("La lista original es: ")
supermerk2.__str__()
supermerk2.desencolar()
print("La lista eliminando un objeto queda: ")
supermerk2.__str__()
supermerk2.invertir()
print("\nLa lista invertida queda: ")
supermerk2.__str__()
print("\n Ahora eliminando todo contenido de esta fila: ")
supermerk2.vaciar()
supermerk2.__str__()