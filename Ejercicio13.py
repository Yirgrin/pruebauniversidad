#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = int (input ("Ingrese las medidas del lado A del triángulo: "))
b = int (input ("Ingrese las medidas del lado B del triángulo: "))
c = int (input ("Ingrese las medidas del lado C del triángulo: "))

x=(a**2)+(b**2)
y=c**2

if x == y:
    print("Es un triangulo rectangulo")
if a == b or a == c or b == c: 
    print ("El triángulo es isóceles")
elif a == b and a and c and b == c:
    print ("El triángulo es equilátero")
else: 
    print ("El triángulo es escaleno")