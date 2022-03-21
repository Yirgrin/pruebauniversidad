import os
os.system("cls")

estudiantes = []

for i in range (0,5):
    nombre = input ("Por favor digite un nombre     ")
    estudiantes.append (nombre)

for i in estudiantes: 
    print (f"El nombre del estudiante es {i}")