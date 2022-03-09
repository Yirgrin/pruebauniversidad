import os 
os.system("cls")

inversion = int (input ("¿Cuánta cantidad de dinero desea invertir?   "))
interes = int (input ("Ingrese el interés anual   "))
years = int (input ("¿Por cuántos años desea invertir este dinero?   "))


capital = ((inversion*interes)/100)*years
cadaaño = capital / years
print (f"El monto de cápital obtenido al final de cada año invertido será de: {cadaaño} dólares")
print (f"El monto de cápital obtenido al final de {years} años de inversión será de: {capital} dólares")