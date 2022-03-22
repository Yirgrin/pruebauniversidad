import os
os.system("cls")

def sumar (): 
    numero1 = int (input ("Digite un número     "))
    numero2 = int (input ("Digite un número     "))
    suma = numero1 + numero2
    return suma, numero1, numero2

#Para manipular un valor de una función debo crear una variable para almacenar la función

valorsuma, valornum1, valornum2 = sumar ()
print ("Suma:" , valorsuma,     "Número1:" , valornum1,     "Número2:" , valornum2 )
