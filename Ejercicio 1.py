import os 
os.system("cls")

CantidadNumeros = int(input("¿Cuántos números desea intruducir en el programa?   "))

contadorNegativo = 0
contadorPositivo = 0

for i in range(1, CantidadNumeros + 1):
    numero = float(input(f"Escriba el número {i}: "))
    if numero < 0:
        contadorNegativo += 1
    elif numero > 0: 
        contadorPositivo += 1
else:
    print(f"Usted ha escrito {contadorNegativo} números negativos.")
    print(f"Usted ha escrito {contadorPositivo} números positivos.")