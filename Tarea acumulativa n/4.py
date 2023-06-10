#Dado un número real que representa una calificación de examen
#entregar una calificación cualitativa
x = float(input("Ingrese la nota de examen: "))
if x < 1.0 or x > 7.0:
       print("Error, ingrese una nota válida entre 1.0 a 7.0")
else:
    if x > 1.0 and x < 4.0:
        print("Reprobado")
    if x >= 4.0 and x < 5.0:
        print ("Aprobado")
    if x >= 5.0 and x < 6.0:
        print ("Notable")
    if x >=6.0 and x <= 7.0:
        print ("Sobresaliente")

