import os 
os.system("cls")

print ("Digite la cantidad de trabajdores que desea consultar")
cantidad = int (input ())
resultado = 0

for i in range (1, cantidad+1):
    print ("Digite el salario del trabajador" , i)
    salario = int (input ())
    resultado = resultado + salario 

print ("El total es de: " , resultado)