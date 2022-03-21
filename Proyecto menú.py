import os
os.system("cls")

start = input ("¡Bienvenido a Extreme Magic! ¿Quieres hechar un vistazo a nuestro menú disponible? S/N      ").upper()
print ()

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

    carrito = []

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
                carrito.append("Extreme Burger")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} Extreme Burger")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()
            elif agregar == 2: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (3500 * cantidad)
                carrito.append("The Mistress")
                print ()
                print (f"Usted ha agregado a su carrito {cantidad} The Mistress")
                print ("Si desea continuar comprando digite la opción de su preferencia. O bien digite 7 para cancelar su pedido.")
                print ()
            elif agregar == 3: 
                cantidad = int (input ("Ingrese cuantas unidades desea ordenar.     "))
                sumacuenta = (2500 * cantidad)
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


    if menu == 2: 
        print ("""Burritos: 
        1. The crow: Carne y pollo, salsa picante extreme, papas fritas, verdura. (₡2500)
        2. The Wand: Agucante, verduras, lechuga, tomate, salsa especial. (₡2500)
        3. The swamp: Jamón, queso, pepino, salsa agria. (₡2000)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            carrito.append(agregar)
            print (carrito)
    
    if menu == 3: 
        print ("""Papas Fritas: 
        1. Fairy Dust: Papas, frijoles, carne, aguacate, salsa agria, magic polvo picante.. (₡2800)
        2. The Cure: Papas, bacon, pollo, frijoles, lechuga, tomate, salsa de queso. (₡2500)
        3. The Enchantment: Papas, carne, cebolla frita, queso mozarella, huevo frito. (₡2300)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            carrito.append(agregar)
            print (carrito)

    if menu == 4: 
        print ("""Postres: 
        1. Spells: Canasta de rollos de canela. (₡1000)
        2. Charm: Torta fría de café. (₡1200)
        3. Potion: Volcan de crema pastelera. (₡2000)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            carrito.append(agregar)
            print (carrito)   
    
    if menu == 5: 
        print ("""Combos: 
        1. Combo 1: Hamburgesa The Mistress, burrito The Crow, postre Spells, refresco. (₡7000)
        2. Combo 2: Extreme Burger, 2 burritos The Crow, papas Fairy Dust, refresco 1L, postre Charm. (₡11500)
        3. Combo 3: Papas The Cure, hamburgesa The Wuitcher, 2 postres Potion, refresco. (₡6000)
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            carrito.append(agregar)
            print (carrito)  
    
    if menu == 6: 
        print ("""Gaseosas 250ml (₡700): 
        1. Coca Cola
        2. Canada Dry
        3. Fanta Naranja
        """)
        continuar = input ("¿Desea agregar alguna opción del menú al carrito? S/N     ").upper()
        
        if continuar == "S":
            agregar = int (input ("Digite la opción númerica del menú que desea agregar al carrito.     "))
            carrito.append(agregar)
            print (carrito)   

    if menu == 7: 
        print (carrito)
        print (sumacuenta)

    if menu == 8: 
        print ("¡Esperamos verte pronto!")
        exit()
    

