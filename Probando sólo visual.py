
from tkinter import * 
from tkinter import ttk

carrito = []
CancelarTotal = []
Unidades = []

def inicio ():
    global root
    root= Tk()
    root.title ("Extreme Magic")
    root.geometry("615x600")

    Bienvenida = Label (root, text= "Menú Disponible",  bg= "burlywood3", font=("TkMenuFont",18))
    Bienvenida.pack(fill= X)
    hamburguesa = Button (root, text= "Hamburguesas", bg= "burlywood1", font=("TkMenuFont",10), width= 18, height= 8, command= hamburguesas).place (x= 20, y= 45)
    burrito = Button (root, text= "Burritos", bg= "burlywood4", font=("TkMenuFont",10), width= 18, height= 8, command= burritos).place (x= 230, y= 45)
    papa  = Button (root, text= "Papas", bg= "burlywood4", font=("TkMenuFont",10),  width= 18, height= 8, command= papas).place (x= 440, y= 45)
    postre = Button (root, text= "Postres", bg= "burlywood4", font=("TkMenuFont",10),  width= 18, height= 8, command= postres).place (x= 20, y= 230)
    combo = Button (root, text= "Combos", bg= "burlywood4", font=("TkMenuFont",10), width= 18, height= 8, command= combos).place (x= 230, y= 230)
    refrescos = Button (root, text= "Refrescos", bg= "burlywood4", font=("TkMenuFont",10),  width= 18, height= 8).place (x= 440, y= 230)
    root.mainloop()


def hamburguesas (): 
    ventana1 = Toplevel(root)
    ventana1.title ("Hamburguesas")
    ventana1.geometry("850x280")
    menu = Label (ventana1, text="""Hamburguesas: 
        1. Extreme Burger: Pan artesanal, doble torta de carne, bacon, aguacate, queso mozarella, lechuga, tomate. (₡4000)
        2. The Mistress: Pan artesanal, torta de pavo, huevo frito, aguacate. (₡3500)
        3. The Witcher: Pan artesanal, torta de carne, queso amarillo, pepinillos, lechuga, tomate. (₡2500)
        ¿Desea agregar algo al carrito?""", font=("candara",12)).place (x= 20, y= 45)
    opcion1 = Button (ventana1, text= "Agregar opción 1").place (x= 20, y= 200)
    opcion2 = Button (ventana1, text= "Agregar opción 2").place (x= 220, y= 200)
    opcion3 = Button (ventana1, text= "Agregar opción 3").place (x= 420, y= 200)
    

def burritos ():
    ventana2 = Toplevel(root)
    ventana2.title ("Burritos")
    ventana2.geometry("850x280")
    menu = Label (ventana2, text="""Burritos: 
        1. The crow: Carne y pollo, salsa picante extreme, papas fritas, verdura. (₡2500)
        2. The Wand: Agucante, verduras, lechuga, tomate, salsa especial. (₡2500)
        3. The swamp: Jamón, queso, pepino, salsa agria. (₡2000)
        ¿Desea agregar algo al carrito?""", font=("candara",12)).place (x= 20, y= 45)
    opcion1 = Button (ventana2, text= "Agregar opción 1").place (x= 20, y= 200)
    opcion2 = Button (ventana2, text= "Agregar opción 2").place (x= 220, y= 200)
    opcion3 = Button (ventana2, text= "Agregar opción 3").place (x= 420, y= 200)

def papas ():
    ventana3 = Toplevel(root)
    ventana3.title ("Papas")
    ventana3.geometry("850x280")
    menu = Label (ventana3, text="""Papas Fritas: 
        1. Fairy Dust: Papas, frijoles, carne, aguacate, salsa agria, magic polvo picante.. (₡2800)
        2. The Cure: Papas, bacon, pollo, frijoles, lechuga, tomate, salsa de queso. (₡2500)
        3. The Enchantment: Papas, carne, cebolla frita, queso mozarella, huevo frito. (₡2300)
        ¿Desea agregar algo al carrito?""", font=("candara",12)).place (x= 20, y= 45)
    opcion1 = Button (ventana3, text= "Agregar opción 1").place (x= 20, y= 200)
    opcion2 = Button (ventana3, text= "Agregar opción 2").place (x= 220, y= 200)
    opcion3 = Button (ventana3, text= "Agregar opción 3").place (x= 420, y= 200)

def postres ():
    ventana4 = Toplevel(root)
    ventana4.title ("Postres")
    ventana4.geometry("850x280")
    menu = Label (ventana4, text="""Postres: 
        1. Spells: Canasta de rollos de canela. (₡1000)
        2. Charm: Torta fría de café. (₡1200)
        3. Potion: Volcan de crema pastelera. (₡1200)
        ¿Desea agregar algo al carrito?""", font=("candara",12)).place (x= 20, y= 45)
    opcion1 = Button (ventana4, text= "Agregar opción 1").place (x= 20, y= 200)
    opcion2 = Button (ventana4, text= "Agregar opción 2").place (x= 220, y= 200)
    opcion3 = Button (ventana4, text= "Agregar opción 3").place (x= 420, y= 200)

def combos ():
    ventana5 = Toplevel(root)
    ventana5.title ("Combos")
    ventana5.geometry("850x280")
    menu = Label (ventana5, text="""Combos: 
        1. Combo 1: Hamburgesa The Mistress, burrito The Crow, postre Spells, refresco. (₡7000)
        2. Combo 2: Extreme Burger, 2 burritos The Crow, papas Fairy Dust, refresco 1L, postre Charm. (₡11500)
        3. Combo 3: Papas The Cure, hamburgesa The Wuitcher, 2 postres Potion, refresco. (₡6000)
        ¿Desea agregar algo al carrito?""", font=("candara",12)).place (x= 20, y= 45)
    opcion1 = Button (ventana5, text= "Agregar opción 1").place (x= 20, y= 200)
    opcion2 = Button (ventana5, text= "Agregar opción 2").place (x= 220, y= 200)
    opcion3 = Button (ventana5, text= "Agregar opción 3").place (x= 420, y= 200)
inicio()
