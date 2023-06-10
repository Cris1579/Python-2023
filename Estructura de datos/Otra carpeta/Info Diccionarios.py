# get() nos entrega el value para un key determinado
# Si añado un parametro y su valor, ese devuelve si no se encuentra la key
# print (d1.get('Nombre'))
# print (d1.get('Avion', 'no encontrado'))

# Para imprimir los key del diccionario
# for x in d1:
#    print(x)

# Para imprimir los value del diccionario
# for x in d1:
#    print(d1[x])

# El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

# El método popitem() elimina de manera aleatoria un elemento del diccionario.

d = {'a': 1, 'b': 2}
d.popitem()
print(d)
#{'a': 1}