#LIBRERIAS 
#CLASES 
#APIS 

#para limpiar la pantalla de comandos (mac)
#import os
#os.system("clear")

#para limpiar la pantalla de comandos (Windows)
import os
os.system("cls")



edad = int (input ("Digite su edad  "))

if edad >= 18: 
    print ("Es mayor de edad")
else: 
    print ("Es menor de edad")


#if de una sola línea
    
edad = int (input ("Digite su edad  "))

print ("Es mayor de edad" if (edad >= 18) else "Es menor de edad") 