import os 
os.system("cls")

EdadCliente = int (input ("Ingrese su edad"   ))

if EdadCliente < 4: 
    print ("Su entrada es gratis")
elif EdadCliente >= 4 and EdadCliente <=18:
    print ("El costo de su entrada es de 5 dólares")
else: 
    print ("El costo de su entrada es de 10 dólares")