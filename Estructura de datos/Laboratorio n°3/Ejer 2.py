def Capitales():
    ziti = dict(
        capital = input("Ingrese el nombre de la capital: "),
        Región = input("Ingrese el nombre de la región: "),
        comunas = list(input("Ingrese las comunas,separados por un guión (-): ").split("-")),
        coordenas_capital = tuple(str(input("Ingrese las coordenadas de la capital,separados por un guión bajo (_):").split("_")))
    )
    return ziti

c1 = Capitales()
print(f"La primera ciudad es: {c1}")
c2 = Capitales()
print(f"La primera ciudad es: {c2}")
c3 = Capitales()
print(f"La primera ciudad es: {c3}")
