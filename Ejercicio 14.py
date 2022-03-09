import os
os.system("cls")

Lote = int (input ("Indique cuántos focos quiere ingresar al sistema    "))
focoverde = "verde"
focorojo = "rojo"
focoblanco = "blanco"
sumaverdes = 0
sumarojos = 0
sumablancos = 0

for i in range (1, Lote + 1): 
    foco = input (f"Indique el color del foco número {i}:    ").lower
    if foco == focoverde: 
        sumaverdes += 1
    elif foco == focorojo: 
        sumarojos += 1
    elif foco == focoblanco: 
        sumablancos += 1
else:
    print (f"Hay {sumaverdes} focos verdes en existencia")
    print (f"Hay {sumarojos} focos rojo en existencia")
    print (f"Hay {sumablancos} focos blanco en existencia")
