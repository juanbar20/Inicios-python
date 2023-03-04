import os
os.system("cls")

import random

"""numero = random.randint(1, 100)
intentos = 5

while(intentos > 0):
    eleccion = int(input("Elige el numero: "))
    if eleccion > numero:
        print("Ell numero es mas pequeño")
        intenos = intentos - 1
    elif eleccion < numero:
        print("El numero es mas grande")
        intenos = intentos - 1
    else:
        print("Ganaste")
        break

print("Se acabaron los intentos")"""


def run ():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un numero del 1 al 100"))
    while numero_elegido != numero_aleatorio:
        pass
    print("Ganaste")




if __name__ == "__main__":
    run()