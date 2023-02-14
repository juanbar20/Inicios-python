
import os

os.system("cls")

USD = 1
ARS = 290
COP = 4600
MXN = 20

print("Bienvenido al conversor de monedas definitivo")
print("Elige una de las siguientes opciones de conversión: ")
print("1. Dolar a Pesos ")
print("2. Pesos a Dolar ")
conversor = int(input("Elija la opcion que prefieras"))

if conversor == 1:
    print("Elige una de las siguientes opciones de conversión: ")
    print("1. Dolar Estadounidense a pesos argentinos ")
    print("2. Dolar Estadounidense a pesos colombianos ")
    print("3. Dolar Estadounidense a pesos mexicanos ")
    opcion = input("¿Cual es tu opción?: ")
    opcion = int(opcion)

    if opcion == 1:
        
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = dolares * ARS
        print(f"Tienes {dolares} pesos argentinos")
    elif opcion == 2:
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = dolares * COP
        print(f"Tienes {dolares} pesos colombianos")
    elif opcion == 3:
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = dolares * MXN
        print(f"Tienes {dolares} pesos mexicanos")
    else:
        print("Elige una opción correcta")

elif conversor == 2:
    print("Elige una de las siguientes opciones de conversión: ")
    print("1. Pesos argentinos Estadounidense a dolares ")
    print("2. Pesos colombianos Estadounidense a dolares ")
    print("3. Pesos mexicanos Estadounidense a dolares ")
    
    opcion = input("¿Cual es tu opción?: ")
    opcion = int(opcion)

    if opcion == 1:
        
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = ARS / dolares
        print(f"Tienes {pesos} pesos argentinos")
    elif opcion == 2:
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = dolares * COP
        print(f"Tienes {dolares} pesos colombianos")
    elif opcion == 3:
        dolares = int(input("¿Cuantos dolares tienes?: "))
        pesos = dolares * MXN
        print(f"Tienes {dolares} pesos mexicanos")
    else:
        print("Elige una opción correcta")
else:
    print("Elige una opción valida")
