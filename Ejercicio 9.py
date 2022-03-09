import os 
os.system("cls")

numeroCita = int (input ("Contando este número de cita, ¿Cuántas veces a consultado con el Dr. Mata Sanos?     "))

if numeroCita in range (1,4): 
    print ("Usted debe cancelar un monto de $200.00 por la consulta")
    Cancelado = 200.00 * numeroCita
    print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
elif numeroCita in range (4,6): 
    print ("Usted debe cancelar un monto de $150.00 por la consulta")
    if numeroCita == 4: 
        Cancelado = 600.00 + 150.00
        print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
    else: 
        Cancelado = 600.00 + 150.00 * 2
        print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
elif numeroCita in range (6,9):
    print ("Usted debe cancelar un monto de $100.00 por la consulta")
    if numeroCita == 6: 
        Cancelado = 900.00 + 100.00
        print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
    elif numeroCita == 7: 
        Cancelado = 900.00 + 100.00 * 2
        print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
    else:
        Cancelado = 900.00 + 100.00 * 3
        print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")
else: 
    print ("Usted debe cancelar un monto de $50.00 por la consulta")
    contador = numeroCita - 8
    Cancelado = 1200.0 + (50.00 * contador)
    print (f"El total cancelado del tratamiento hasta ahora es de {Cancelado} dólares.")