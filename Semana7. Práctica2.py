import os
os.system("cls")

lista = []

#lista = input ("Digite cualquier cosa     ")

#agrega un nuev valor al final 

lista.append ("Raul")
lista.append ("María")
lista.append ("Sofía")

print (lista)

#Inserta valor en una posicion en especifico 

lista.insert (0,"Ronald")
print (lista)

lista.insert (100,"Ronald")
print (lista)

#Borrar un valor de la lista

lista.remove ("María")
print (lista)

lista.remove ("Ronald")
print (lista)

#Ordenar la lista
lista.sort()
print (lista)

#Ordenar la lista al revés
lista.sort(reverse=True)
print (lista)

#Retorna lo que eliminó
print (lista.pop(0))
print (lista)

#Muestra cuantas veces aparece un dato en la lista 
#print lista.count ("Sofía")
print (lista)

indice = lista.index ("Ronald ")
print (lista [indice])

