# import the random module
"""""
import random

# declare a list
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
"""""
import numpy as np
matriz_1 = [
    [5,2],
    [8,3]
]
Minv = np.linalg.inv(matriz_1)
print (matriz_1)
print(Minv)