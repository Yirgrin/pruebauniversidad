Algoritmo n_camisas
	definir N,precio,preciototal,descuento como real
	Escribir 'Ingrese la cantidad de camisas que desea comprar'
	Leer N
	Escribir 'Ingrese el precio de las camisas'
	Leer precio
	Si N>=1&N<=5 Entonces
		preciototal = precio*N
		Escribir 'El precio total de las camisas sin descuento es de:' , preciototal
		Escribir 'El descuento de esta compra es de 12,5%'
		descuento = preciototal*0.125
		Escribir 'El monto descontado es de:' , descuento
		compra = preciototal-descuento
		Escribir 'El precio total a cancelar es de:' , compra
	SiNo
		Si N>=5&N<=8 Entonces
			preciototal = precio*N
			Escribir 'El precio total de las camisas sin descuento es de:' , preciototal
			Escribir 'El descuento de esta compra es de 20%'
			descuento = preciototal*0.2
			Escribir 'El monto descontado es de:' , descuento 
			compra = preciototal-descuento
			Escribir 'El monto total a cancelar es de:' , compra
		SiNo
			preciototal = precio*N
			Escribir 'El precio total de las camisas sin descuento es de:' ,preciototal
			Escribir 'El descuento aplicado en esta compra es de 31,5%'
			descuento = preciototal*0.315
			Escribir 'El monto descontado es de:' descuento
			compra = preciototal-descuento
			Escribir 'El monto total a cancelar es de:' , compra
		FinSi
	FinSi
FinAlgoritmo
