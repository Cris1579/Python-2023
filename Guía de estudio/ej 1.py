# Crear una lista de diccionarios llamada pacientes
# donde cada dicc representa a un paciente con su info personal
# Se solicita crear una lista de 4 diccionarios
# Info que se solicita: Nombre (String), Edad (int), Peso (Float), Sintomas (Str)
# ADEMÁS realizar una busqueda en la lista de pacientes para encontrar
# un paciente en especifico por nombre y mostrar su ficha

dicc_1 = dict(
    nombre = str(input("Ingrese el nombre del paciente: ")),
    Edad = int(input("Ingrese la edad del paciente: ")),
    Peso = float(input("Ingrese el peso del paciente en kg: " )),
    Sintomas = str(input("Ingrese los sintomas del paciente: "))
)

dicc_2 = dict(
    nombre = str(input("\nIngrese el nombre del paciente: ")),
    Edad = int(input("Ingrese la edad del paciente: ")),
    Peso = float(input("Ingrese el peso del paciente en kg: ")),
    Sintomas = str(input("Ingrese los sintomas del paciente: "))
)
dicc_3 = dict(
    nombre = str(input("\nIngrese el nombre del paciente: ")),
    Edad = int(input("Ingrese la edad del paciente: ")),
    Peso = float(input("Ingrese el peso del paciente en kg: ")),
    Sintomas = str(input("Ingrese los sintomas del paciente: "))
)
dicc_4 = dict(
    nombre = str(input("\nIngrese el nombre del paciente: ")),
    Edad = int(input("Ingrese la edad del paciente: ")),
    Peso = float(input("Ingrese el peso del paciente en kg: ")),
    Sintomas = str(input("Ingrese los sintomas del paciente: "))
)

Lista_Pacientes = [dicc_1,dicc_2,dicc_3,dicc_4]
for x in Lista_Pacientes:
    print(x)

Busqueda_Paciente = str(input("\n Ingrese el nombre del paciente a buscar: "))

for diccionario in Lista_Pacientes:
    if diccionario['nombre'] == Busqueda_Paciente:
        print("Paciente encontrado:",diccionario)
        break
    else:
        print("No hay resultados")
        break