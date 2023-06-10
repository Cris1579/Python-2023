# Escribir un programa que pida al usuario una palabra
# y muestre por consola el n° de veces que contiene cada vocal

def leer_frase():
    global palabra
    palabra = input("Ingrese alguna palabra para contar las vocales: ").lower()


def contar_vocales():
    Letra_a = ["a", "á"]
    cont = 0
    for x in Letra_a:
        for y in palabra:
            if x == y:
                cont += 1
    print("El n° de veces que sale la a es de: ", cont)

    Letra_e = ["e", "é"]
    cont = 0
    for x in Letra_e:
        for y in palabra:
            if x == y:
                cont += 1
    print("El n° de veces que sale la e es de: ", cont)
    Letra_i = ["i", "í"]
    cont = 0
    for x in Letra_i:
        for y in palabra:
            if x == y:
                cont += 1
    print("El n° de veces que sale la i es de: ", cont)
    Letra_o = ["o", "ó"]
    cont = 0
    for x in Letra_o:
        for y in palabra:
            if x == y:
                cont += 1
    print("El n° de veces que sale la o es de: ", cont)
    Letra_u = ["u", "ú"]
    cont = 0
    for x in Letra_u:
        for y in palabra:
            if x == y:
                cont += 1
    print("El n° de veces que sale la u es de: ", cont)



leer_frase()
contar_vocales()
