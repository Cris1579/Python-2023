# from Sesion import Sesion
# que se yo, de ahí se ve si hereda de algo
class Asistencia:
    nombres = []
    while True:
        nombre = input(str("Ingrese el nombre del estudiante a guardar: "))
        if nombre == "":
            break
        else:
            nombres.append(nombre)
    print("Los nombres ingresados son:")
    for x in nombres:
        print(x)
