import os
os.system("cls")

#Sintaxis
#definir la función (el nombre)

#Las variables acá fuera son las variabes globales.
numero1 = 100
print ("ID de la variable" ,id(numero1))
print ("ID del numero" ,id(100))

def sumar (): 
    #las variables acá dentro son variables locales
    numero1 = 20
    print ("ID de la variable dentro" ,id(numero1))
    numero2 = 30
    sumar = numero1 + numero2
    print ("La suma es de" , sumar)

#para llamar una función lo hago con el nombre y los paréntesis. Y lo hago fuera de la función

sumar ()
print (numero1)


#Paython lenguaje Key sensitive 
