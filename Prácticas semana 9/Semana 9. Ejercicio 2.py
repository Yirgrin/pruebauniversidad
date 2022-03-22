import os
os.system("cls")

peliculas = {}

print ("Digite la pelicula y el genero que desea guardar en el inventario.")

for i in range (4): 
    pelicula = input ("Digite la pelicula:  ")
    genero = input ("Digite genero      ")
    peliculas [pelicula] = genero

for i, j in peliculas.items ():
    print (f"La pelicula {i} es de genero {j}")