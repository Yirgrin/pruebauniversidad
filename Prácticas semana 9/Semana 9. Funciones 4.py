import os
from pickle import FALSE, TRUE
os.system("cls")

def validar (ValidarCorreo):
    caracter = "@"
    correovalido = False
    for i in ValidarCorreo:
        if i == caracter:
            return True
    return False

correo = input ("Digite su correo:      ")
if validar (correo):
    print ("El correo es válido")
else: 
    print ("El correo es inválido.")