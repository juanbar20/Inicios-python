import os
os.system("cls")

def run():
    repeticiones = int(input("Ingresa hasta que numero quieres ver al cuadrado"))

    for i in range (1, repeticiones + 1):
        operacion = i ** 2
        print(f"El numero {i} al cuadrado tiene como resultado {repeticiones}")


if __name__ == "__main__":
    run()