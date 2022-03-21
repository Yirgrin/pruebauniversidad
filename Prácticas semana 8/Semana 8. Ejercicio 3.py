import os
os.system("cls")

lista  =[20,65,12,2,8,65,48,1,5,8]
pares = []
impares = []

for i in lista:
    if i % 2 == 0: 
        pares.append (i)
        print (f"El número {i} es par")
    else: 
       impares.append (i)
       print (f"El número {i} es impar")

print (f"Los números pares son {pares}")
print (f"Los números pares son {impares}")