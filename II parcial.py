import os
os.system("cls")


username = "josuemora"
password = "mora1997"

SaldoInicial = 0

IntentoUser = input ("¡Bienvenido! Por favor ingrese su usuario:    ").lower()
IntentoUser = IntentoUser.rstrip()


while IntentoUser != username:
    print ("Usuario incorrecto.")
    IntentoUser = input ("¡Bienvenido! Por favor ingrese su usuario:    ").lower()
    IntentoUser = IntentoUser.rstrip()

if IntentoUser == username: 
    IntentoPass = input ("Por favor ingrese su contraseña:    ")
    contador = 1 

    if IntentoPass != password:
        while contador <= 2: 
           print ("Su contraseña es incorrecta. Por favor intente de nuevo.")
           print() 
           IntentoPass = input ("Por favor ingrese su contraseña:    ")
           contador += 1
           if IntentoPass == password: break
           if contador == 3: 
               print ("Usuario bloqueado. Contacte con un agente de soporte")  
               break

print()

while IntentoPass == password: 
    options = (input ("""Menú de opciones. Marque la opción del trámite que desea realizar
1. Depositar dinero a la cuenta
2. Sacar dinero de la cuenta
3. Ver saldo
4. Salir    
    """))
    print()

    if options == "1": 
        deposito = input ("Indique la cantidad de dinero que desea depositar a su cuenta:     ")
        verificar = deposito.isdigit()
        print()
        if verificar == True:
            deposito=int(deposito)
            SaldoInicial = (SaldoInicial + deposito) 
            print ("Su transacción fue exitosa.")
            print (f"Usted ha ingresado a su cuenta un monto de: {deposito} colones.")
            print (f"Su saldo actual es de: {SaldoInicial} colones.")
            print ()
        else: 
            print ("Su transacción es incorrecta. Por favor ingrese un monto correcto.")
            print ()  

    elif options == "2":
        retiro = input ("Indique la cantidad de dinero que desea retirar de su cuenta:     ")
        verificar = retiro.isdigit()
        print ()

        if verificar == True:
            retiro = int(retiro)
            if retiro < SaldoInicial:
                if retiro % 1000 == 0:
                    SaldoInicial = (SaldoInicial - retiro)
                    print (f"Su transacción fue exitosa.")
                    print (f"Usted ha retirado de su cuenta un monto de: {retiro} colones.")
                    print (f"Su saldo actual es de: {SaldoInicial} colones.")
                    print ()
                else: 
                    print ("Su transacción es incorrecta. Por favor ingrese un monto correcto.")
                    print ()

            elif retiro > SaldoInicial:
                print ("Usted no cuenta con suficiente dinero para realizar esta transacción.")
                print ()
        else:
            print("Monto Invalido")

    elif options == "3":
        print (f"El saldo de su cuenta es de {SaldoInicial} colones.")
        print ()
    
    elif options == "4": 
        print ("¡Muchas gracias por preferir nuestro banco!")
        print ()
        exit()
