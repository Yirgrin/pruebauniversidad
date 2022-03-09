import os
os.system("cls")


antiguedad = int (input ("Especifique la cantidad de años trabajados   "))
if antiguedad >=2 and antiguedad <= 5:
    salario = int (input ("Especifique su salario   "))
    bonoantiguo = salario * 0.2
    print (f"Su bono mensual por antiguedad es de {bonoantiguo} dólares")
elif antiguedad >= 5: 
    salario = int (input ("Especifique su salario   "))
    bonoantiguo = salario * 0.3
    print (f"Su bono mensual por antiguedad es de {bonoantiguo} dólares")
else: 
    salario = int (input ("Especifique su salario   "))
    
if salario < 1000:
    bonosalario = salario * 0.25
    print (f"Su bono mensual por concepto de salario es de {bonosalario} dólares")
elif salario > 1000 and salario <= 3500: 
    bonosalario = salario * 0.15
    print (f"Su bono mensual por concepto de salario es de {bonosalario} dólares")
else: 
    bonosalario = salario * 0.1
    print (f"Su bono mensual por concepto de salario es de {bonosalario} dólares")

if bonoantiguo > bonosalario: 
    print (f"Usted recibirá el bono mensual de mayor cantidad ecónomica correspondiente a: {bonoantiguo} dólares")
else: 
    print (f"Usted recibirá el bono mensual de mayor cantidad ecónomica correspondiente a: {bonosalario} dólares")