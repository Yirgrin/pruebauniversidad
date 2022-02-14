Algoritmo sumar_o_multiplicar
	definir num1, num2 como enteros
	Escribir 'Digite el valor de num1 y num2'
	Leer num1
	Leer num2
	Escribir 'Especifique si desea la suma o la multiplicación de ambos valores'
	Leer operacion
	Si suma o multiplicacion Entonces
		sumar = num1+num2
		Escribir 'la suma de estos dos valores es de:' , sumar
	SiNo
		multiplicar = num1 * num2
		Escribir 'la multiplicación de estos dos valores es de:' , multiplicar
	FinSi
FinAlgoritmo
