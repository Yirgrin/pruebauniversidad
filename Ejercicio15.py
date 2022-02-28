
print ("Ingrese su edad")
edad = int (input ())

print ("Ingrese su salario mensual")
salario= int (input ())

edadnecesaria = 16
ingresos = 1000

if edad >= edadnecesaria and salario >= ingresos: 
    print ("Usted debe tributar")
else: 
    print ("Usted no debe tributar")