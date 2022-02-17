#Evaluar dos números

print("Digite dos números")

numero1= int(input("Digite número 1: "))
numero2= int(input("Digite número 2: "))
numero3= int(input("Digite número 3: "))

if (numero1>numero2) and (numero1>numero3): 
    print ("El número 1 es el mayor")
else:
    if (numero2>numero1) and (numero2>numero3): 
        print("El número 2 es el número mayor")
    else: 
        print("El número 3 es el mayor")