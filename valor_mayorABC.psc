Algoritmo valor_mayorabc
	definir A,B,C como entero 
	Escribir 'defina valores de A,B,C'
	Leer A
	Leer B
	Leer C
	Si A>B&A>C Entonces
		Escribir 'A es el valor mayor'
	SiNo
		Si A<B&C<B Entonces
			Escribir 'B es el valor mayor'
		SiNo
			Escribir 'C  es el valor mayor'
		FinSi
	FinSi
FinAlgoritmo
