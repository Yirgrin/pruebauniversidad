import os
os.system("cls")

agenda = {}

option = True

while option: 

    #Pedimos informacion
    nombre = input ("Digite el nombre   ")
    numero = input ("Digite el numero   ")

    if nombre in agenda: 
        print ("Ya existe el nombre")
    else:
        agenda = [nombre] = numero
        print ("Usuario agregado")

    respuesta = input ("Quiere salir digite S/N     ")
    if respuesta.upper() == "S": 
        option = False
print (agenda)