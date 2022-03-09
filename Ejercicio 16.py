import os
os.system("cls")

altura = int (input ("Indique de que tamaño desea la escalera    "))
inicio = 1

for espacios in range (altura, 0, -1): 
    for i in range (espacios):
        print ("  ", end="")
    
    for i in range (inicio):
        print ("* ", end="")

    print ()
    inicio += 2