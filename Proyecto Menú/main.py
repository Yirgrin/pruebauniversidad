from ast import Delete
from operator import truediv
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox 
import tkinter.ttk as ttk
import os
os.system("cls")

#===================Funciones===================================
def validate_entry(text):
    return text.isnumeric()

def insertar_en_tabla():
    global contador2
    tabla.insert(parent="",index="end",iid=contador2,text="",values=(dato1,dato2,dato3,total_unidades))
    contador2+=1

def añadir():
    global total_a_pagar
    global dato1
    global dato2
    global dato3
    global total_unidades
    dato1=lista_de_nombres[opcion]
    dato2=int(cantidad_deseada.get())
    dato3=lista_de_precios[opcion]
    total_unidades=dato2*dato3
    lista_de_totales.append(total_unidades)
    total_a_pagar=sum(lista_de_totales)
    insertar_en_tabla()
    cantidad_deseada.delete(0, tk.END)
    descripcion.destroy()
    for a in frame_derechaS2.winfo_children():
        a.destroy()
    

def cantidad():
    global opcion
    global cantidad_deseada
    global descripcion
    global foto
    global foto_del_producto
    global pregunta
    opcion=eleccion.get()
    frame_descripcion=Frame(frame_derechaS2)
    frame_descripcion.grid(column=0,row=0)
    descripcion = Label(frame_descripcion,text=descripciones[opcion],font=(font_style,font_size))
    descripcion.grid(column=0,row=0)
    foto_del_producto=Frame(frame_derechaS2)
    foto_del_producto.grid(column=0,row=1)
    Label(foto_del_producto,text=lista_de_nombres[opcion],font=(font_style,font_size),image=imagenes[opcion],compound=BOTTOM).grid(column=0,row=0)
    cantidad_del_producto=Frame(frame_derechaS2)
    cantidad_del_producto.grid(column=0,row=2)
    pregunta = Label(cantidad_del_producto,text="Digite cuantos quiere",font=(font_style,font_size)).grid(column=0,row=0)
    cantidad_deseada= Entry(cantidad_del_producto,font=(font_style,font_size),validate="key",validatecommand=(cantidad_del_producto.register(validate_entry), "%S"))
    cantidad_deseada.grid(column=0,row=1)
    Button(cantidad_del_producto,text="Añadir al Carrito",font=(font_style,font_size),command=añadir).grid(column=0,row=2)


def cancelar_pedido():
    global cancelar
    cancelar=Toplevel ()
    cancelar.geometry ("250x70")
    Label (cancelar, text= "Total a cancelar ₡", font=(font_style,font_size)).grid(column=0,row=0)
    cuenta= Label (cancelar, text=total_a_pagar, font=(font_style,font_size)).grid(column=1,row=0)
    Button (cancelar, text= "Cancelar",font=(font_style,font_size),command=finalizar).grid(column=6,row=2)
    frame_derechaS2.grid_forget()


#=========================Root y Variables=============================
root=Tk()
root.title("Extreme Magic")

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "azure-light")
style = ttk.Style()
style.theme_use ("clam")
root.geometry ("940x660")
root.resizable (0,0)
font_style="Candara"
font_size=12


contador2=1
lista_de_totales=[]
total_a_pagar=0
contador1=0
eleccion=IntVar()

#=====================Información de los productos=================================
imagen1=PhotoImage(file = r"Imagenes\extreme burger.png")
imagen2=PhotoImage(file = r"Imagenes\the mistress.png")
imagen3=PhotoImage(file = r"Imagenes\the witcher.png")
imagen4=PhotoImage(file = r"Imagenes\the crow.png")
imagen5=PhotoImage(file = r"Imagenes\the wand.png")
imagen6=PhotoImage(file = r"Imagenes\the swamp.png")
imagen7=PhotoImage(file = r"Imagenes\fairy dust.png")
imagen8=PhotoImage(file = r"Imagenes\the cure.png")
imagen9=PhotoImage(file = r"Imagenes\the enchantment.png")
imagen10=PhotoImage(file = r"Imagenes\postre.png")
imagen11=PhotoImage(file = r"Imagenes\torta de cafe.png")
imagen12=PhotoImage(file = r"Imagenes\potion.png")
imagen13=PhotoImage(file = r"Imagenes\coca.png")
imagen14=PhotoImage(file = r"Imagenes\sprite.png")
imagen15=PhotoImage(file = r"Imagenes\fanta naranja.png")

imagenes=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7,imagen8,imagen9,imagen10,imagen11,imagen12,imagen13,imagen14,imagen15,]

lista_de_nombres=["Extreme Burger","The Mistress","The Witcher",
"The Crow","The Wand","The Swamp",
"Fairy Dust","The Cure","The Enchantment",
"Spells", "Charm", "Potion", 
"Coca Cola", "Sprite", "Fanta Naranja"]

lista_de_precios=[4000,3500,2500,2500,2500,2000,2800,2500,2300,1000,1200,1200,700,700,700]

descripciones=["""Pan artesanal, doble torta de carne, bacon,
aguacate, queso mozarella, lechuga, tomate.
(₡4000)""",
"""Pan artesanal, torta de pavo, huevo frito, aguacate.
(₡3500)""",
"""Pan artesanal, torta de carne, queso amarillo,
pepinillos, lechuga, tomate.
(₡2500)""",
"""Carne y pollo, salsa picante extreme,
papas fritas, verdura.
(₡2500)""",
"""Agucante, verduras, lechuga,
tomate, salsa especial
(₡2500)""",
"""Jamón, queso, pepino, salsa agria..
(₡2000)""",
"""Papas, frijoles, carne, aguacate,
salsa agria, magic polvo picante.
(₡2800)""",
"""Papas, bacon, pollo, frijoles,
lechuga, tomate, salsa de queso.
(₡2500)""",
"""Papas, carne, cebolla frita,
queso mozarella, huevo frito.
(₡2300)""",
"Canasta de rollos de canela. (₡1000)",
"Torta fría de café. (₡1200)",
"Volcán de crema pastelera. (₡1200)", 
"Gaseosas 250ml (₡700)",
"Gaseosas 250ml (₡700)",
"Gaseosas 250ml (₡700)"]

#========================Framnes==============================
frame_izquierda=Frame(root)
frame_izquierda.grid(column=0,row=0)
frame_derecha=Frame(root)
frame_derecha.grid(column=1,row=0)
frame_derecha_superior=Frame(frame_derecha)
frame_derecha_superior.grid(column=0,row=0)
frame_derechaS1= Frame (frame_derecha_superior)
frame_derechaS1.grid(column=0, row=0)
frame_derechaS2= Frame (frame_derecha_superior)
frame_derechaS2.grid(column=1, row=0)
frame_derecha_inferior=Frame(frame_derecha)
frame_derecha_inferior.grid(column=0,row=1)
frame_derecha_cancelar = Frame (frame_derecha)
frame_derecha_cancelar.grid(column=0,row=2)

#======================================================

for fila in range(0,5):
    for columna in range(3):
        Radiobutton(frame_izquierda, text=lista_de_nombres[contador1], font=(font_style,font_size), image=imagenes[contador1], compound=BOTTOM,variable=eleccion,value=contador1).grid(column=columna,row=fila)
        contador1+=1

#======================================================

Button(frame_derechaS1,text="Cantidad",font=(font_style,font_size),command=cantidad, relief="raised", borderwidth=10, anchor="nw").grid (row=0, column=0)

Button (frame_derecha_cancelar, text= "Continuar",font=(font_style,font_size), command= cancelar_pedido, relief="raised", borderwidth=10).grid(column=0,row=3)

#=======================Tabla===============================
tabla=ttk.Treeview(frame_derecha_inferior)
tabla["columns"]=("Producto","Unidades","Precio_Unitario", "Precio_Total")
tabla.column("#0",width=0,stretch=NO)
tabla.column("Producto",anchor=CENTER,width=200)
tabla.column("Unidades",anchor=CENTER,width=100)
tabla.column("Precio_Unitario",anchor=CENTER,width=100)
tabla.column("Precio_Total",anchor=CENTER,width=100)
tabla.heading("#0",text="",anchor=CENTER)
tabla.heading("Producto",text="Producto",anchor=CENTER)
tabla.heading("Unidades",text="Unidades",anchor=CENTER)
tabla.heading("Precio_Unitario",text="Precio Unitario",anchor=CENTER)
tabla.heading("Precio_Total",text="Precio Total",anchor=CENTER)
tabla.pack()


def borrar():
    seleccionado = tabla.selection()[0]
    tabla.delete(seleccionado)

Button (frame_derecha_cancelar, text= "Eliminar producto selecionado",font=(font_style,font_size),command=borrar, relief="raised", borderwidth=10).grid(column=0,row=0)


def finalizar ():
    respuesta = messagebox.askokcancel("Cancelar", "¿Está seguro de que desea cancelar su pedido?")
    if respuesta == "True": 
        for i in tabla.get_children(): 
            tabla.delete(i)
            cancelar.destroy()
            lista_de_totales=[]
            total_a_pagar=0
            frame_derechaS2.grid(column=1, row=0)
            for a in frame_derechaS2.winfo_children():
                a.destroy()
       

root.mainloop()