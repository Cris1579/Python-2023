#Algoritmo para conseguir n° primos entre 1 y 500

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(rango_inicio, rango_fin):
    primos = []
    for numero in range(rango_inicio, rango_fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Ejemplo de uso
inicio = 1
fin = 500
primos_encontrados = encontrar_primos(inicio, fin)
print("Números primos encontrados:", primos_encontrados)
