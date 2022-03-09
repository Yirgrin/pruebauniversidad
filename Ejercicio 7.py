import os 
os.system("cls")

estudiantes = int (input ("¿Cuántos estudiantes harán uso del servicio del autobús?   "))


if estudiantes >= 100: 
    print ("El costo por cada alumno es de 65.00 dólares")
    autobus = 65.00
    rentaAutobus= autobus * estudiantes
    print (f"El costo de la renta del autobus es de {rentaAutobus} dólares")
elif estudiantes in range (50,100):
    print ("El costo por cada alumno es de 70.00 dólares")
    autobus = 70.00 
    rentaAutobus= autobus * estudiantes
    print (f"El costo de la renta del autobus es de {rentaAutobus} dólares")
elif estudiantes in range (30,50):
    print ("El costo por cada alumno es de 95.00 dólares")
    autobus = 95.00 
    rentaAutobus= autobus * estudiantes
    print (f"El costo de la renta del autobus es de {rentaAutobus} dólares")
    
else:  
    print ("El costo de la renta del autobús es de 4000.00 dólares")