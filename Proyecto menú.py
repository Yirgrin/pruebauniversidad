import os
os.system("cls")

start = input ("¡Bienvenido a Extreme Magic! ¿Quieres hechar un vistazo a nuestro menú disponible? S/N      ").upper()
print ()

carrito = []
CancelarTotal = []
        
while start == "S":
    menu = int (input ("""Menú: 
    1) Hamburguesas
    2) Burritos 
    3) Papas 
    4) Postres 
    5) Combos 
    6) Refrescos
    7) Cancelar pedido
    8) Salir
Digite la opción de menú que desea consultar. 
    """))
    print ()

    if menu == 1: 
        print ("""Hamburguesas: 
        1. Extreme Burger: Pan artesanal, doble torta de carne, bacon, aguacate, queso mozarella, lechuga, tomate. (₡4000)
        2. The Mistress: Pan artesanal, torta de pavo, huevo frito, aguacate. (₡3500)
        3. The Witcher: Pan artesanal, torta de carne, queso amarillo, pepinillos, lechuga, tomate. (₡2500)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))

            if agregar == 1: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (4000 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append ("Extreme Burger")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Extreme Burger")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (3500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The Mistress")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Mistress")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The Witcher")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Witcher")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            else: 
                print ("Por favor ingrese una opción correcta.")

        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print ()


    if menu == 2: 
        print ("""Burritos: 
        1. The crow: Carne y pollo, salsa picante extreme, papas fritas, verdura. (₡2500)
        2. The Wand: Agucante, verduras, lechuga, tomate, salsa especial. (₡2500)
        3. The swamp: Jamón, queso, pepino, salsa agria. (₡2000)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))

            if agregar == 1: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append ("The crow")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The crow")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The Wand")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Wand")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2000 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The swamp")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The swamp")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            else: 
                print ("Por favor ingrese una opción correcta.")

        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print ()
    
    
    if menu == 3: 
        print ("""Papas Fritas: 
        1. Fairy Dust: Papas, frijoles, carne, aguacate, salsa agria, magic polvo picante.. (₡2800)
        2. The Cure: Papas, bacon, pollo, frijoles, lechuga, tomate, salsa de queso. (₡2500)
        3. The Enchantment: Papas, carne, cebolla frita, queso mozarella, huevo frito. (₡2300)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))

            if agregar == 1: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2800 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append ("Fairy Dust")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Fairy Dust")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The Cure")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Cure")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2300 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("The Enchantment")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Enchantment")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            else: 
                print ("Por favor ingrese una opción correcta.")

        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print ()


    if menu == 4: 
        print ("""Postres: 
        1. Spells: Canasta de rollos de canela. (₡1000)
        2. Charm: Torta fría de café. (₡1200)
        3. Potion: Volcan de crema pastelera. (₡1200)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))

            if agregar == 1: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (1000 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append ("Spells")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Spells")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (1200 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("Charm")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Charm")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (1200 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("Potion")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Potion")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            else: 
                print ("Por favor ingrese una opción correcta.")

        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print ()   
    
    if menu == 5: 
        print ("""Combos: 
        1. Combo 1: Hamburgesa The Mistress, burrito The Crow, postre Spells, refresco. (₡7000)
        2. Combo 2: Extreme Burger, 2 burritos The Crow, papas Fairy Dust, refresco 1L, postre Charm. (₡11500)
        3. Combo 3: Papas The Cure, hamburgesa The Wuitcher, 2 postres Potion, refresco. (₡6000)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))

            if agregar == 1: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (7000 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append ("Combo 1")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Combo 1")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (11500 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("Combo 2")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Combo 2")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (6000 * cantidad)
                CancelarTotal.append (sumacuenta)
                carrito.append("Combo 3")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Combo 3")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()

            else: 
                print ("Por favor ingrese una opción correcta.")

        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print () 
    

    if menu == 6: 
        print ("""Gaseosas 250ml (₡700): 
        1. Coca Cola
        2. Canada Dry
        3. Fanta Naranja
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            if agregar != 1 and agregar != 2 and agregar != 3: 
                print ("Por favor ingrese una opción correcta.")

            cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
            sumacuenta = (700 * cantidad)
            CancelarTotal.append (sumacuenta)
            carrito.append ("Gaseosa 250ml")
            print ()
            print (f"Usted ha agregado a su carrito {cantidad} Gaseosa 250ml")
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
            print ()
    
        elif continuar != "S" and continuar != "N": 
            print ("Entrada inválida.")

        else: 
            print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 8 para salir.")
            print () 
             

    if menu == 7: 
        MetodoCancelar = input ("¿Desea cancelar con efectivo o con tarjeta?    ").lower()
        print ()
        if MetodoCancelar == "tarjeta":
            #descuento = CancelarTotal - 0.12
            #CancelarTotal -= descuento
            #¿NO PUEDO HACER DESCUENTO?
            print (carrito)
            print (f"Monto total a cancelar por su compra {CancelarTotal}")
            print ()
            print ("¡Esperamos verte pronto!")
            exit()
        elif MetodoCancelar == "efectivo":
            print (carrito)
            print (f"Monto total a cancelar por su compra {CancelarTotal}")
            print ()
            print ("¡Esperamos verte pronto!")
            exit()
        else: 
            print ("Entrada inválida.")
        

    if menu == 8: 
        print ("¡Esperamos verte pronto!")
        exit()
    

