#Algoritmo que guarde el RUT de 5 personas y el nombre
#Luego ordenar de forma Ascendente y Alfabeticamente


nombres = []
ruts = []
while True:
    nombre = input(str("Ingrese el nombre: "))
    rut = input(str("Ingrese el rut: "))
    if nombre == "":
        break
    else:
        nombres.append(nombre)
        ruts.append(rut)

print("\nLos nombres registrados son: ")
for nom in nombres:
    print (nom)

print ("\nLos Ruts registrados son: ")
for rt in ruts:
    print(rt)



print("La lista con los nombres ordenados alfabeticamente queda: ")
nombres.sort()
print(nombres)

print("La lista con los ruts ordenados de forma ascendente queda: ")
ruts.sort()
print(ruts)