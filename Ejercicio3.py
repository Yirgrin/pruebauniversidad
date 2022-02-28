
 #omo entradas el salario diario y el número de días trabajados. 
 #Tenga en cuenta que al empleado se le debe descontar el 10%
  #por concepto de pensión y 15% por concepto de salud.

print ("Ingrese su salario diario")
salario = int (input ())

print ("Ingrese los días laborados")
diastrabajados = int (input ())

total = salario * diastrabajados
pension = total * 0.1
salud = total * 0.15

salariototal = total - pension - salud 

print ("El salario que recibirá el empleado es de:" , salariototal)
