Algoritmo tipo_cliente
//10.	El dueño de una pulpería tiene a la venta artículos y depende del tipo de cliente se le realiza un descuento con las siguientes condiciones:
//Sí el cliente es de tipo A se le descuenta 40%
//Sí el cliente es de tipo B se le descuenta 30%
//Sí el cliente es de tipo C se le descuenta 5%
//Escribir un algoritmo que lea el nombre del cliente, tipo de cliente, precio. Calcule el pago final.
	Escribir "Ingrese el nombre el usuario"
	Leer cliente
	Escribir 'Ingrese el precio del producto'
	Leer precio
	tipocliente<-""
	Repetir
		Escribir 'Especifique si el tipo de cliente es de tipo A,B,C'
		Leer tipocliente
		Si tipocliente='A' Entonces
			Escribir 'Se le aplicará un descuento del 40%'
			descuento<-(precio*40)/100
			preciofinal<-precio-descuento
			
		SiNo
			Si tipocliente='B' Entonces
				Escribir 'Se le aplicará un descuento del 30%'
				descuento<-(precio*30)/100
				preciofinal<-precio-descuento
			SiNo
				Si tipocliente='C' Entonces
					Escribir 'Se le aplicará un descuento del 5%'
					descuento<-(precio*5)/100
					preciofinal<-precio-descuento
				SiNo
					Escribir 'El dato ingresado es inválido, especifique A,B,C'
				Fin Si
			Fin Si
		Fin Si
	Hasta Que tipocliente='A' o tipocliente='B' o tipocliente='C'
	Escribir 'El nombre del cliente es: ' , cliente
	Escribir 'El cliente es de tipo: ' , tipocliente
	Escribir 'El precio sin descuento aplicado es de: ' , precio
	Escribir 'El monto a cancelar es de: ' preciofinal
	

FinAlgoritmo
