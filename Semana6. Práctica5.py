
num = int (input ("Digite un número  "))

resultado = 1

for i in range (2, num+1): 
    resultado = resultado * 1

print (resultado)

#Lo mismo pero en while 

contador = 2
while contador <= num: 
    resultado = resultado * contador 
    contador = contador + 1 
print (resultado)