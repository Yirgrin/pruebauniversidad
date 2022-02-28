#Sabemos que las cadenas son datos alfanumericos 

cadena= "Programando python"

#esto es para descomponer una cadena, entonces sólo me estaría mostrando la letra que está en la poscición que estoy indicando

print (cadena[3])
print (cadena [0:21])

#Si le agrego un : más me estaría mostrando las letras de tres en tres
print (cadena [0:21:3])

print (cadena [::])

#Esto es para que vaya de derecha a izquierda
print (cadena [:: -1])

#mostrar los 4 ultimos caracteres de input

cadena= input()
print (cadena [-4 : ])