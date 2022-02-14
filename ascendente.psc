Algoritmo ascendente
	definir num1,num2,num3 como entero 
	Escribir 'Ingrese el valor de num1,num2,num3'
	Leer num1
	Leer num2
	Leer num3
	Si num1<num2&num1<num3&num2<num3 Entonces
		Escribir num1
		Escribir num2
		Escribir num3
	SiNo
		Si num2<num1&num2<num3&num3<num1 Entonces
			Escribir num2
			Escribir num3
			Escribir num1
		SiNo
			Si num3<num2&num3<num1&num1<num2 Entonces
				Escribir num3
				Escribir num1
				Escribir num2
			SiNo
				Si num1<num3&num1<num2&num3<num2 Entonces
					Escribir num1
					Escribir num3
					Escribir num2
				SiNo
					Si num2<num1&num2<num3&num1<num3 Entonces
						Escribir num2
						Escribir num1
						Escribir num3
					SiNo
						Escribir num3
						Escribir num2
						Escribir num1
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
