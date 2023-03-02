import os
os.system("cls")

import random

eleccion = input("Ingrese su opción perro hp: ")

computador = 1

while (computador != 4):
    computador = random.randrange(1,4)

    print(computador)


