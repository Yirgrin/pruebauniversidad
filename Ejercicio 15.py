import os
os.system("cls")

tamaño = int (input ("Indique de que tamaño desea la escalera    "))

for altura in range (1, tamaño + 1): 
    for escalera in range (1, altura + 1): 
        print (escalera, end="")
    print ()