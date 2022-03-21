import os
os.system("cls")

#Recordemos 

lista = []
tuplas = ()
diccionarios = {}

#Diccionarios
#Su acrónimo es dict

diccionarios = {"Dato1" : 1, 
                "Dato2" : 2,
                "Dato3" : 3
}

#Para acceder a una posicion en memoria lo hago por medio de [] y dentro las claves

print ("Dato num 1" , {diccionarios["Dato1"]})
print ("___________________________")

#Para agregar otro dato al diccionario. Sólo asignamos la clave con el valor
#Diccionarios son mutables
#Si ya hay un dato especificado entonces lo sobreescribre, sino entonces sólo lo asigna

diccionarios ["Dato4"] = 44
print (diccionarios)

#Métodos de los diccionarios


#.get para extraer info desde una posicion en memoria
print (diccionarios.get ("Dato1")) #con metodo
print (diccionarios ["Dato1"]) #sin metodo


#.items para mostrar todo el contenido del dict
print (diccionarios.items()) #con metodo

#.keys para mostrar las claves
print ("muestra las llaves", diccionarios.keys()) 

#.values para mostrar los valores
print ("muestra los valores", diccionarios.values()) 

#.pop borra y devuelve un dato
print ("Pop" , diccionarios.pop("Dato1"))