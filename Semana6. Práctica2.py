import os 
os.system("cls")

#ciclo while 

contador = 1 
while contador <= 10: 
    print (contador)
    contador += 1 

#ciclo for
for i in range(1,11): 
    print (i)

for vuelta in "Ronald": 
    print (vuelta)


#Uasando el for sería lo mismo que hacer esto con el while
nombre = "Yirgrin"
contador = 0 
while contador < len(nombre): 
    print (nombre [contador])
    contador += 1