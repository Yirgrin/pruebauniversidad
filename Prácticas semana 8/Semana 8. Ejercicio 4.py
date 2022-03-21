import os
os.system("cls")

#Afirmar y devuelve resultado boolean
nombre = "Ronald"

print (nombre.startswith ("R"))

print ("___________________________")

lista = ("Ronald", "Marco", "Juan")

for i in lista: 
    if i.startswith("R"):
        print ("Comienza con una R")
    else:
        print ("No comienza con una R")