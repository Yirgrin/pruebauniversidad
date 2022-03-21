import os
os.system("cls")


colores = {"amarillo" : "yellow", 
            "verde" : "green", 
            "rojo" : "red"}

for i in colores: 
    print (f"EL color en español es {i}, El color es ingles es {colores.get(i)}")

print ("___________________________")

for keys, values in colores.items():
    print (f"EL color en español es {keys}, El color es ingles es {values}")