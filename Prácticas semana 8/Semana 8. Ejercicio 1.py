import os
os.system("cls")


#listas y tuplas

#tuplas (No mutables)
dias = ("lunes", "martes", "miercoles", "jueves", "viernes")

#listas (mutables)

numeros = [1,2,3,4,5,6]
print (numeros [-1])
print ("___________________________")
#Recorrer listas

for i in numeros: 
    print (i)

print ("___________________________")

palabras = ("peine", "pelo", "refri", "plato")

for dato in palabras: 
    print (f"El dato de {dato} tiene un tamañpo de {len(dato)} letras")
