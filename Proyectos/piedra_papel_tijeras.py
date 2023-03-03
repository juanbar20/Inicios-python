import os
os.system("cls")

import random

print("Wenas")



eleccion = int(input(" 1: Piedra \n 2: Papel \n 3: Tijeras   \nIngrese su opción perro hp: "))



if eleccion ==  1:
    eleccion = "Piedra"
    operador_eleccion = 1
elif eleccion == 2:
    eleccion = "Papel"
    operador_eleccion = 2
elif eleccion ==  3:
    eleccion = "Tijeras"
    operador_eleccion = 3
else:
    print("Su eleccion no esta en las opciones dadas, por favor elija de nuevo")

computador = random.randrange(1,4)

if computador == 1:
    computador = "Piedra"
    operador_computador = 1
elif computador == 2:
    computador = "Papel"
    operador_computador = 2
else:
    computador = "Tijeras"
    operador_computador = 3



while (operador_computador != 4):
    
    if eleccion == computador:
        print(f"Elegiste {eleccion} y el computador saco {computador} es empate. ")
        break
    else:

        if operador_eleccion == 1 :
            if operador_computador == 3:
                print(f"Felicidades tu sacaste {eleccion} y la maquina saco {computador}. ¡Tu ganas!")
                break
            else:
                print(f"Lo siento tu sacaste {eleccion} y la maquina saco {computador}. ¡Perdiste!")
                break
        elif operador_eleccion == 2:
            if operador_computador == 1:
                print(f"Felicidades tu sacaste {eleccion} y la maquina saco {computador}. ¡Tu ganas!")
                break
            else:
                print(f"Lo siento tu sacaste {eleccion} y la maquina saco {computador}. ¡Perdiste!")
                break
        else:
            if operador_computador == 2:
                print(f"Felicidades tu sacaste {eleccion} y la maquina saco {computador}. ¡Tu ganas!")
                break
            else:
                print(f"Lo siento tu sacaste {eleccion} y la maquina saco {computador}. ¡Perdiste!")
                break


