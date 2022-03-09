import os
os.system("cls")

CantidadEmpleados = int (input("Ingrese la cantidad de sueldos de sus empleados que desea evaluar    "))

sueldosMenores = 0
sueldosMayores = 0
GastosSalarios = 0

for i in range(1, CantidadEmpleados + 1):
    sueldo = int (input(f"Escriba el sueldo del empleado {i}: "))
    GastosSalarios = GastosSalarios + sueldo
    if sueldo <= 1500:
        sueldosMenores += 1
        
    elif sueldo > 1500: 
        sueldosMayores += 1
        
else:
    print (f"{sueldosMenores} empleados cobran menos de 1500 dólares.")
    print (f"{sueldosMayores} empleados cobran más de 1500 dólares.")

print (f"El gasto total de la empresa en sueldos es de {GastosSalarios} dólares.")