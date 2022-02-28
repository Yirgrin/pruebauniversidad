
print ("Ingrese su edad")
edadcliente = int (input ())

if edadcliente < 4: 
    print ("Su entrada es gratis")
elif edadcliente >= 4 and edadcliente <=18:
    print ("El costo de su entrada es de 5 euros")
else: 
    print ("El costo de su entrada es de 10 euros")