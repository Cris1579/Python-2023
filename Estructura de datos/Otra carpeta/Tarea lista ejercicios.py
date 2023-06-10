class Asignaturas:
    def __init__(self, nombre_asig, fechaInicio):
        self.nombreasig = nombre_asig
        self.FechInic = fechaInicio

    def getNombreAsig(self):
        return self.nombreasig

    def getFech_Inicio(self):
        return self.FechInic

    def __str__(self):
        return "Nombre de la Asignatura: " + self.nombreasig + ", Fecha de inicio de clases : " + str(self.FechInic)


class Estudiante(Asignaturas):
    def __init__(self, nombre_asig, fechaInicio, nombre, fecha_nac, carrera, año_ingreso):
        super().__init__(nombre_asig, fechaInicio)
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.carrera = carrera
        self.año_ingreso = año_ingreso

    def getNombre(self):
        return self.nombre

    def getFechaNAc(self):
        return self.fecha_nac

    def getCarrera(self):
        return self.carrera

    def getAño_ingreso(self):
        return self.año_ingreso

    def __str__(self):
        return "Nombre Estudiante: " + self.nombre + ", Fecha de nacimiento: " + str(self.fecha_nac) + ", Carrera: " \
               + self.carrera + ", Año de ingreso: " + self.año_ingreso


Carlos = Estudiante("Historia", "14 de abril", "Carlos Sanhueza", "15/05/2004", "Ped.en Historia", "2020")
ramos = Asignaturas("Historia", "14 de abril")
print(Carlos)
print(ramos)
