# Área y perímetro de un triángulo
# Solicitando los tres lados al usuario
# a,b,c --> float

a = float(input("Ingrese valor para cateto a: "))
b = float(input("Ingrese valor para cateto b: "))
c = float(input("Ingrese valor para cateto c: "))
if a<=0 or b<=0 or c<=0:
    print("Uno o más valores son incorrectos, ingrese un valor superior a cero")
else:
    s = (a + b + c) / 2
    Area = (s * (s - a)*(s - b)*(s - c)) ** (1 / 2)
    Perimetro = int(a + b + c)
    print("El área sin redondear es : ", Area)
    print("El área redondeado es: ","{0:.3f}".format(Area))
    print("El perimetro es: ", Perimetro)
