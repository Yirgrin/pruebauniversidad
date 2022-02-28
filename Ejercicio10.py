

voto = (input ("""¿Por cuál partido desea votar?
A = Partido Rojo
B = Partido Verde
C = Partido Azul
Indique A, B o C"
""")).upper()


if voto == "A":
    print ("USted ha votado por el Partido Rojo")
elif voto == "B":
    print ("USted ha votado por el Partido Verde")
elif voto == "C":
    print ("USted ha votado por el Partido Azul")
else: 
    print ("Opción errónea")