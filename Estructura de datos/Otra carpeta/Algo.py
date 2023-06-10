import numpy as np
import random

m = random.randint(1, 10)
n = random.randint(1, 10)

arr = np.random.rand(m, n)

print(arr)

N = random.randint(1, 30)  # Genera un número aleatorio entre 1 y 30
Arr = []

for i in range(N):
    Arr.append(random.randint(1, 50))  # Agrega un número aleatorio entre 1 y 100 a la lista

print(Arr)