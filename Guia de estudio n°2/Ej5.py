# Integrantes:
# Antoine Briones - Cristopher González


# Se requiere gestionar una jerarquía de empleados en una empresa. Cada empleado tiene un
# cargo específico y puede tener uno o varios subordinados. Utilizando un árbol, elaborar el
# programa con las siguientes funcionalidades:
# A. Agregar empleado: Permite ingresar un nuevo empleado a la jerarquía. El
# empleado se agrega como subordinado de un empleado existente, especificando su
# cargo.
# B. Eliminar empleado: Elimina un empleado de la jerarquía, junto con todos sus
# subordinados. Al eliminar un empleado, todos sus subordinados pasan a ser
# subordinados del empleado superior.
# C. Mostrar la jerarquía: Muestra en consola la estructura jerárquica completa de la
# empresa, mostrando los empleados y sus respectivos subordinados en forma de
# árbol.
# D. Buscar empleado: Permite buscar un empleado en la jerarquía por su nombre y
# muestra su cargo y subordinados directos, si los tiene.
# E. Obtener jefe directo: Dado un empleado, muestra en pantalla el nombre y cargo de
# su jefe directo.

class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

class Empresa:
    def __init__(self):
        self.empleados = []

    def addEmpleado(self, nombre, cargo, directBoss=None):
        empleado = Empleado(nombre, cargo)
        if directBoss:
            directBoss.subordinados.append(empleado)
        else:
            self.empleados.append(empleado)

    def deleteEmpleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
        else:
            directBoss = self.searchDirectBoss(empleado)
            if directBoss:
                directBoss.subordinados.remove(empleado)
                directBoss.subordinados.extend(empleado.subordinados)

    def showJerarquia(self):
        for empleado in self.empleados:
            self.showEmpleado(empleado)

    def showEmpleado(self, empleado, nivel=0):
        print("  " * nivel + "- " + empleado.nombre + " (" + empleado.cargo + ")")
        for subordinado in empleado.subordinados:
            self.showEmpleado(subordinado, nivel + 1)

    def searchEmpleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                return empleado
            else:
                subordinado = self.searchEmpleadoInSubordinados(empleado, nombre)
                if subordinado:
                    return subordinado
        return None

    def searchEmpleadoInSubordinados(self, empleado, nombre):
        for subordinado in empleado.subordinados:
            if subordinado.nombre == nombre:
                return subordinado
            else:
                subordinadoInSubordinados = self.searchEmpleadoInSubordinados(subordinado, nombre)
                if subordinadoInSubordinados:
                    return subordinadoInSubordinados
        return None

    def searchDirectBoss(self, empleado):
        for e in self.empleados:
            if empleado in e.subordinados:
                return e
            else:
                directBoss = self.searchDirectBossInSubordinados(e, empleado)
                if directBoss:
                    return directBoss
        return None

    def searchDirectBossInSubordinados(self, empleado, subordinado):
        for e in empleado.subordinados:
            if subordinado in e.subordinados:
                return e
            else:
                directBoss = self.searchDirectBossInSubordinados(e, subordinado)
                if directBoss:
                    return directBoss
        return None


def menu():
    print("\nMenú de opciones:")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Mostrar jerarquía")
    print("4. Buscar empleado")
    print("5. Obtener jefe directo")
    print("6. Salir\n")

    opcion = input("Seleccione una opción: ")
    print() #Espacio vacio

    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        cargo = input("Ingrese el cargo del empleado: ")
        directBoss = input("Ingrese el nombre del jefe directo (opcional): ")
        if not directBoss:
            directBoss = None
        else:
            directBoss = empresa.searchEmpleado(directBoss)
            while not directBoss and directBoss != "":
                print("El jefe directo no existe")
                directBoss = input("Ingrese el nombre del jefe directo (opcional): ")
                if directBoss:
                    directBoss = empresa.searchEmpleado(directBoss)
        empresa.addEmpleado(nombre, cargo, directBoss)
        menu()

    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado que desea eliminar: ")
        empleado = empresa.searchEmpleado(nombre)
        if empleado:
            empresa.deleteEmpleado(empleado)
        else:
            print("El empleado no existe")
        menu()

    elif opcion == "3":
        empresa.showJerarquia()
        menu()

    elif opcion == "4":
        nombre = input("Ingrese el nombre del empleado que desea buscar: ")
        empleado = empresa.searchEmpleado(nombre)
        if empleado:
            print(empleado.cargo)
            if empleado.subordinados:
                print("Subordinados: " + ", ".join(subordinado.nombre for subordinado in empleado.subordinados))
            else:
                print("Subordinados: No aplica")
        else:
            print("El empleado no existe")
        menu()

    elif opcion == "5":
        nombre = input("Ingrese el nombre del empleado del que desea obtener el jefe directo: ")
        empleado = empresa.searchEmpleado(nombre)
        if empleado:
            directBoss = empresa.searchDirectBoss(empleado)
            if directBoss:
                print(directBoss.nombre)
                print(directBoss.cargo)
            else:
                print("El empleado no tiene jefe directo")
        else:
            print("El empleado no existe")
        menu()

    elif opcion == "6":
        print("Saliendo...")

    else:
        print("Opción inválida")
        menu()

empresa = Empresa()
menu()