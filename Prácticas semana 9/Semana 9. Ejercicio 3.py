import os
os.system("cls")

paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", 
"Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", 
"Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
"Venezuela": "Caracas", "España": "Madrid"}

dato = input ("Ingrese el país del cuál desea saber su cápital:     ").title()

if dato in paises.keys():
    print (f"La capital del país {dato} es {paises.get(dato)}")

else: 
    print ("Este país no se encuentra en la lista.")
    
