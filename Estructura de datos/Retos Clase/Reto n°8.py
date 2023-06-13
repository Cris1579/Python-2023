# Algoritmo que permita insertar elementos en un diccionario
# Información de 3 estudiantes
# Se debe ingresar: Nombre estudiantes, Nombre asignatura
# Nota Lab N°1 y Lab N°2
# Lab N°1: 30%, Lab N°2: 70%
# El algoritmo debe entregar toda la información ingresada más el promedio final

dicc = dict(
    nombre = input("Ingrese el nombre del primer estudiante: "),
    asig = input("Ingrese el nombre de la asignatura: "),
    nota_1 = float(input("Ingrese nota lab 1: ")),
    nota_2 = float(input("Ingrese nota lab 2: "))
)

promedio = dicc["nota_1"] * 0.3 + dicc["nota_2"] * 0.7
dicc['promedio'] = promedio


dicc2 = dict(
    nombre = input("Ingrese el nombre del segundo estudiante: "),
    asig = input("Ingrese el nombre de la asignatura: "),
    nota_1 = float(input("Ingrese nota lab 1: ")),
    nota_2 = float(input("Ingrese nota lab 2: "))
)
promedio = dicc2["nota_1"] * 0.3 + dicc2["nota_2"] * 0.7
dicc2['promedio'] = promedio

dicc3 = dict(
    nombre = input("Ingrese el nombre del tercer estudiante: "),
    asig = input("Ingrese el nombre de la asignatura: "),
    nota_1 = float(input("Ingrese nota lab 1: ")),
    nota_2 = float(input("Ingrese nota lab 2: "))
)
promedio = dicc3["nota_1"] * 0.3 + dicc3["nota_2"] * 0.7
dicc3['promedio'] = promedio

print("Información primer estudiante: ")
for x,y in dicc.items():
    print(x,'=',y)

print("\nInformación Segundo estudiante: ")
for x,y in dicc2.items():
    print(x,'=',y)

print("\nInformación Tercer estudiante: ")
for x,y in dicc3.items():
    print(x,'=',y)