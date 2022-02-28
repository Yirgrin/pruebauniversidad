
print ("Ingrese el monto a cancelar por su compra")
cancelar= int (input())

if cancelar>=10000 and cancelar<=20000: 
    descuento1 = cancelar * 0.1 
    total1 = cancelar - descuento1
    print ("El monto a cancelar con un descuento del 10% aplicado es de" , total1)
elif cancelar>=20001 and cancelar<=50000: 
    descuento2 = cancelar * 0.3 
    total2 = cancelar - descuento2
    print ("El monto a cancelar con un descuento del 30% aplicado es de" , total2)
elif cancelar>50000: 
    descuento3 = cancelar * 0.5
    total3 = cancelar - descuento3
    print ("El monto a cancelar con un descuento del 50% aplicado es de" , total3)
else: 
    print ("El monto a cancelar es de" , cancelar)