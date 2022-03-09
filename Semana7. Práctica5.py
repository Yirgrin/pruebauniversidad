import os
os.system("cls")

lista = []

for item in range (1,6): 
    lista.append (input (f"Digite el dato {item}:    "))

for i in lista: 
    print (i)

#otro ejemplo 
numeropersonas = int (input (f"Digite la cantidad de nombres que desea ingresar:    "))
for item in range (1, numeropersonas + 1): 
    lista.append (input (f"Digite el dato {item}:    "))
    


#personas con edades correspondientes
for item in range (0, numeropersonas): 
    nombre = input("nombre      ")
    edad = input ("Edad     ")
    p = [nombre, edad]
    print (p)
    lista.append (p)
    print (lista)