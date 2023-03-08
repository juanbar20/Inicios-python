import os
os.system("cls")

def run():
    """"repeticiones = int(input("Ingresa hasta que numero quieres ver al cuadrado: "))

    for i in range (1, repeticiones + 1):
        operacion = i ** 2
        print(f"El numero {i} al cuadrado tiene como resultado {operacion} ")"""
#    squares = [i**2 for i in range(1, 101) if i % 3 != 0 and i % 2 == 0]
    squares = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(squares)

if __name__ == "__main__":
    run()