

print ("Ingrese dos números")
num1 = int (input ("Numero 1: "))
num2 = int (input ("Numero 2: "))

opcion1 = num1 + num2 
opcion2 = num1 - num2
opcion3 = num1 * num2

respuesta = int (input ("""
Opción 1: Mostrar la suma de estos dos números
Opción 2: Mostrar la resta de estos dos números
Opción 3: Mostrar la multiplicación de estos dos números
Digite 1, 2 o 3
"""))

if respuesta == 1:
    print ("La suma de estos dos numeros es de:" , opcion1)
elif respuesta == 2:
    print ("La resta de estos dos numeros es de:" , opcion2)
elif respuesta == 3:
   print ("La multiplicación de estos dos numeros es de:" , opcion3)
