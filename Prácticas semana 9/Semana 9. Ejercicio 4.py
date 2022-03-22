import os
os.system("cls")


jugadores = {1 : "Casillas", 15 : "Ramos",
3 : "Pique", 5 : "Puyol",
11 : "Capdevila", 14 : "Xabi Alonso",
16 : "Busquets", 8 : "Xavi Hernandez",
18 : "Pedrito", 6 : "Iniesta",
7 : "Villa"}

print ("Ingrese el # de un jugador.")
numero = int (input ())

if numero in jugadores.keys(): 
    print ()
    print (f"El nombre del jugador número {numero} es {jugadores.get(numero)}")

else: 
    print ()
    print ("Este jugador no se encuentra en la lista.")
