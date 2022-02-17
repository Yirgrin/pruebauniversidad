Algoritmo usuario_contraseña
	Definir nombreusuario,contraseña Como Caracter
	Escribir 'Ingrese su nombre de usuario'
	Leer usuario
	Escribir 'Ingrese su contraseña'
	Leer contraseña
	nombreusuario <- 'pepe'
	contraseñausuario <- 'supercontraseña'
	Si usuario=nombreusuario Y contraseña=contraseñausuario Entonces
		Escribir 'Usuario y contraseña correctos. Puede ingresar al sistema súper'
	SiNo
		Escribir 'Acceso denegado. Intente de nuevo'
		Escribir 'Ingrese su nombre de usuario'
		Leer usuario
		Escribir 'Ingrese su contraseña'
		Leer contraseña
		Si usuario=nombreusuario Y contraseña=contraseñausuario Entonces
			Escribir 'Usuario y contraseña correctos. Puede ingresar al sistema súper'
		SiNo
			Escribir 'Acceso denegado. Intente de nuevo'
			Escribir 'Ingrese su nombre de usuario'
			Leer usuario
			Escribir 'Ingrese su contraseña'
			Leer contraseña
			Si usuario=nombreusuario Y contraseña=contraseñausuario Entonces
				Escribir 'Usuario y contraseña correctos. Puede ingresar al sistema súper'
			SiNo
				Escribir 'Sistema bloqueado, consulte con el administrador'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
