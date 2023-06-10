#Determinar la distancia entre dos puntos (x1,y1,z1) y (x2,y2,z2)
#Ambos puntos son reales
x1 = float(input("Ingrese su valor real para X1: "))
y1 = float(input("Ingrese su valor real para Y1: "))
z1 = float(input("Ingrese su valor real para Z1: "))
x2 = float(input("Ingrese su valor real para X2: "))
y2 = float(input("Ingrese su valor real para Y2: "))
z2 = float(input("Ingrese su valor real para Z2: "))
D = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**(1/2)
print("La distancia entre ambos puntos es de: ", "{0:.3f}".format(D))
Dx = x1-x2
Dy = y1-y2
Dz = z1-z2
Dt = (Dx,Dy,Dz)
print("La distancia entre ambos puntos como par ordenado: ", Dt)