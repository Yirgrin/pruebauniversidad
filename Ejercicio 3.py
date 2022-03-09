import os
from string import octdigits 
os.system("cls")

PrimerAño= int (input ("Ingrese un año   "))
SegundoAño= int (input ("Ingrese otro año    "))

if PrimerAño < SegundoAño: 
    for i in range (PrimerAño, SegundoAño + 1): 
        print (i)
else: 
    print ("El dato del primero año ingresado debe ser menor que el dato del segundo año.")