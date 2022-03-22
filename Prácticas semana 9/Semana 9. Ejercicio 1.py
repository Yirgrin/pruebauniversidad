import os
os.system("cls")

diccionario = {"uno" : 1, "dos" : 2}
print (diccionario ["uno"])

print (diccionario.keys())
print (diccionario.values())

diccionario ["tres"] = 3

valor = "cien"
print (valor in diccionario)

valor = "dos"
print (valor in diccionario.values())
print (valor in diccionario.keys())

for i in diccionario: 
    print(i)

for clave, calor in diccionario.items (): 
    print(clave, "=>" , valor)
    