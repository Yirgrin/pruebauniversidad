import os
os.system("cls")

continuar = input ("¿Desea iniciar a ingresar datos?    ").upper()

positivo = "SI"
negativo = "NO"
contador = 1
n = 0
Suma = 0

while continuar == positivo:
    Notas = int (input (f"Ingrese la nota del estudiante {contador}:  "))
    n += 1
    Suma= Suma + Notas
    continuar = input ("¿Desea continuar ingresando datos?    ").upper()
    contador += 1
if continuar == negativo: 
    promedio = Suma / n
    print (f"El promedio total de las notas ingresadas es de:  {promedio}")
else: 
    print ("Indique 'Si o No'")
