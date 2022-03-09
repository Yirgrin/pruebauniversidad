import os 
os.system ("cls")

hamburguesas = (input ("""¡Bienvenido a Oso Hambriento!
Menú: 
a) Hamburguesa Sencilla por $20.00
b) Hamburguesa doble por $25.00
c) Hamburguesa Triple por $28.00
¿Qué desea llevar? Ingrese a,b o c

""")).lower()

sencilla = "a"
doble = "b"
triple = "c"

cantidad = int (input ("¿Cuántas hamburguesas desea comprar?    "))

if hamburguesas == sencilla:
    monto = 20.00 * cantidad 
    descuento = monto * 0.05
    montoCancelar = monto - descuento
    print (f"El monto a cancelar por su compra de hamburguesas sencillas es de {montoCancelar} dólares. ¡Muchas gracias!")
elif hamburguesas == doble: 
    monto = 25.00 * cantidad 
    descuento = monto * 0.05
    montoCancelar = monto - descuento
    print (f"El monto a cancelar por su compra de hamburguesas dobles es de {montoCancelar} dólares. ¡Muchas gracias!")
else: 
    monto = 28.00 * cantidad 
    descuento = monto * 0.05
    montoCancelar = monto - descuento
    print (f"El monto a cancelar por su compra de hamburguesas triples es de {montoCancelar} dólares.¡Muchas gracias!")