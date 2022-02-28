cadena ="goku123"

#el len lo utilizo para medir el tamaño de la cadena
size = len(cadena)
print (size)

#estoy preguntando si en la cadena está el signo de dolar
print ("$" in cadena)

if "$" in cadena: 
    print ("Si contiene el signo")
else: 
    print ("No contiene el signo")

#Mayusculas y minusculas

#con upper convierto en mayúscula
cadena = "hola como está"
print (cadena.upper())


#con lower conviero en minuscula
cadena = "HOLA COMO ESTÁ"
print (cadena.lower())

#con tittle convierto cada letra inicial en mayúscula
cadena= "mi nombre es yirgrin aguilar bermudez"
cadenatittle = cadena.title()
print (cadenatittle)


#validando datos
print ("Por favor digite si o no")
opcion = input ()
if opcion.lower() == "si":
    print ("Digitó que sí")

print ("Por favor digite si o no")
opcion = input ()
if opcion.upper() == "SI":
    print ("Digitó que sí")

   
#elimina los espacios del final
print ("Por favor digite su nombre")
opcion = input ()
if opcion.rstrip() == "Yirgrin":
    print ("Su nombre es Yirgrin")
else: 
    print ("Su nombre no es Yirgrin")


    #elimina los espacios del principio
print ("Por favor digite su nombre")
opcion = input ()
if opcion.lstrip () == "Yirgrin":
    print ("Su nombre es Yirgrin")
else: 
    print ("Su nombre no es Yirgrin")