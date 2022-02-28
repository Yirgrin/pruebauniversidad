print ("Ingrese dos números")
num1 = input ()
num2 = input ()


if num1 == num2: 
    print ("Ambos números son iguales")
else: 
    print ("Ambos números son diferentes")

if num1 > num2:
    print ("El número 1 es mayor que el numero 2")
elif num1 < num2: 
    print ("El número 2 es mayor o igual que el numero 1")

if(num1 >= '0' and num1 <= '9'):
    print(num1,":Es un numero")
else:
    print(num1,":No es un numero")

if(num2 >= '0' and num2 <= '9'):
    print(num2,":Es un numero")
else:
    print(num2,":No es un numero")
