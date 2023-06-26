
pi = 3.1416
radio = float(input("Inserte el radio de su círculo: "))

if radio > 0:
    circun = (2*pi*radio)
    area = (pi*(radio**2))
    print("La circunferencia y el área del círculo son, respectivamente: ")
    print("{0:.3f}".format(circun),"{0:.3f}".format(area))
else:
    print("Ingrese un valor válido")
