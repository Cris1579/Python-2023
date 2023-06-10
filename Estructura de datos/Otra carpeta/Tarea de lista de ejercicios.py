class Datos:
    def __init__(self, Nombre, Fecha_nac):
        self.nombre = Nombre
        self.fecha_nac = Fecha_nac

    def getNombre(self):
        return self.nombre
        pass

    def getFecha(self):
        return self.fecha_nac
        pass

    def __int__(self):
        return "Nombre: " + str(self.nombre) + ", Fecha de nacimiento: " + str(self.fecha_nac)

    pass
class Mascota(Datos):
    pass

    def __init__(self,Nombre ,Fecha_nac ,raza, especie):
        super().__init__(Nombre,Fecha_nac)
        self.raza = raza
        self.especie = especie
    def getRaza(self):
        return self.raza

    def getEspecie(self):
        return self.especie

    def __str__(self):
        return ("Raza: " + self.raza + ", Especie: " + self.especie)




A = Mascota("Carlos","19/08/2003","Bengalí", "Gato")
assert A.fecha_nac == "19/08/2003"
print(A)

# class Dueño(Mascota):
#   def __init__(self, Nombre, Fecha_nac, Ciudad, mascota):
#      super().__init__(Nombre, Fecha_nac)
#     self.ciudad = Ciudad
#    self.mascota = mascota

# def GetCiudad(self):
#   return self.ciudad
