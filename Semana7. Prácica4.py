import os
os.system("cls")

listanumeros = [1,2,3,4,5,6,7,8,9]

indice = 0
while indice < 9: 
    print (listanumeros[indice])
    indice += 1

while indice < len (listanumeros): 
    print (listanumeros[indice])
    indice += 1

print ("______________________")

#Lo mismo pero con for
for i in listanumeros: 
    print (i)