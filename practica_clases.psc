Algoritmo practica_clases
	
	Definir contador,cantidad Como Entero
	Definir notas,promedio,totalNotas Como Real
	Definir condicional Como Caracter
	
	//aquí inicializamos las variables
	contador=0 
	cantidad=0
	promedio=0
	totalNotas=0
	condicional='si'
	
	Mientras condicional == 'si' Hacer
		Escribir 'Por favor digite la nota de un estudiante'
		Leer notas
		
		totalNotas = totalNotas+notas
		Escribir 'Desea continuar si o no'
		leer condicional
		
		contador= contador+1
		
	FinMientras
	Escribir 'El total de estudiantes es de: ' , contador 
	Escribir 'El promedio de notas es de: ' ,totalNotas/contador

FinAlgoritmo
