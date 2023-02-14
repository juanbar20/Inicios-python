import os
os.system("cls")


eleccion = input("Ingrese su opción perro hp: ")

if eleccion == "Papel" or eleccion == "papel":
    print("Computador elije Tijeras, gana computador :)")
elif eleccion == "Piedra" or eleccion == "piedra":
    print("Computadora elige Papel. Gana la computadora :) ")
elif eleccion == "Tijeras" or eleccion == "tijeras":
    print("Computadora elige Piedra. Gana la computadora :)")
else:
    print("Ingresa una opción correta")


variable = "5"
print(f"El numero de incidentes es {variable}")