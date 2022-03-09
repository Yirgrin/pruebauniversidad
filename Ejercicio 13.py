import os
os.system("cls")


LimiteMeses = 20
mes = 1
sumameses = 10

while mes <= LimiteMeses:
    print (f"El mes {mes} canceló una cuota de ${sumameses} ")
    cuotaMensual = sumameses * 2
    sumameses = cuotaMensual
    mes += 1
    Total = sumameses  

print (f"El total cancelado por las 20 cuotas es de ${Total}")