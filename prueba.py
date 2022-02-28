
nombre = input ("")
edad = int (input())

print ("El nombre es {}" .format (nombre))
print ("La edad es {}" .format (edad))


#otra forma de hacerlo 

nombre = "Yirgrin"
edad = 18

if type(nombre) == str: 
    print ("El nombre es una cadena de caracteres")
else: 
    print ("El nombre no es cadena de caracteres")

if type(edad) == int: 
    print ("El número es un entero")
else: 
    print ("El número no es entero")