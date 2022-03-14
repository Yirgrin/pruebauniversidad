import os, random 

os.system ("cls")

intentos = 0 
numeroAdivinar = random.randint(0,10)

while intentos <= 2: 
    print ("Digite un número a adivinar")
    numeroDigitado = int(input())

    if numeroDigitado == numeroAdivinar: 
        print ("Usted ha acertado el número")
        break
    else: 
        print ("Siga intentando")

    intentos = intentos + 1

    if numeroDigitado < numeroAdivinar: 
        print ("El número debe ser más alto")
    else: 
        print ("El número debe ser más bajo")