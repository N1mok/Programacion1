#                    -Parcial n°1 -
#            Sistema de Control de Inventario
#                -Contexto del Problema-
# Una ferretería local necesita digitalizar el control de sus productos
# para evitar pérdidas de stock. Actualmente, manejan sus datos de forma manual
# requieren un programa que permita gestionar las herramientas a la venta y sus unidades
# disponibles en tiempo real.
# Utilizo 2 listas vacias
# una contendra los articulos del inventario:
herramientas = []
# la otra contiene la cantidad del articulo antes ingresado:
existencias = []
# inicia el programa
print("Bienvenido!\n")
# mostramos el menu dentro de un bucle, el mismo se mantiene activo
# mientras el operador lo necesite:
while True:
    print("""
        -menu de inicio-
    ingrese:
    1.-Carga inicial de herramientas.
    2.-Carga de existencias.
    3.-visualizacion de inventario.
    4.-Consulta de stock (existencias)
    5.-Reporte de agotados
    6.-Alta de nuevo producto
    7.-Actualizacion de stock(venta/ingreso)
    8.-Salir
    """)
    # la variable seleccion se encargara de validar las opciones de menu:
    seleccion = input(
        "seleccione la opcion utilizando los numeros del 1 al 8\ncomo indica el menu: ").replace(" ", "")
    while seleccion.isdigit() == False:
        seleccion = input(
            "error: no puede ingresar letras o caracteres especiales.\ningrese un numero entre 1 y 8: ").replace(" ", "")
    # en caso de que el operador inicie la carga de herramientas:
    if seleccion == "1":
        # solo se permitira una carga inicial.
        if herramientas:
            print("\nya realizo la carga inicial.\npara agregar algun articulo ingrese la opcion 7 en el menu de inicio.\n")
        # en caso de que la carga inicial todavia no se haya realizado:
        else:
            print("\n- Carga Inicial de herramientas -\n\nrevise con atencion la cantidad de articulos que desea ingresar, luego de nombre a los items uno por uno.")
            # la variable cantidad_de_herramientas se utiliza para obtener
            # la cantidad de veces que se repetira el bucle for
            cantidad_de_herramientas = input(
                "cantidad de articulos: ").replace(" ", "")
            # si lo ingresado no es lo que se espera:
            while cantidad_de_herramientas.isdigit() == False or cantidad_de_herramientas == "0":
                print("\nError: Dato no valido.\n")
                cantidad_de_herramientas = input(
                    "ingrese un numero mayor a 0: ").replace(" ", "")
            # una vez que se cumplan los requisitos la variable pasa de str a int:
            cantidad_de_herramientas = int(cantidad_de_herramientas)
            # cada vez que el bucle se repite el operador ingresara un articulo nuevo a la lista:
            for i in range(cantidad_de_herramientas):
                # la variable nombre_herramientas contendra los articulos a cargar en la lista herramientas
                nombre_herramienta = input(
                    f"ingrese el nombre del articulo {i+1} a cargar: ").title().replace(" ", "")
                # si el operador ingresa un dato incorrecto:
                while nombre_herramienta.isalpha() == False:
                    print(
                        "\nError: Dato no valido.\npor favor no utilice caracteres especiales, solo se permiten letras.\n")
                    nombre_herramienta = input(
                        f"ingrese el nombre del articulo {i+1} a cargar: ").title().replace(" ", "")
                # en caso de que el articulo ingresado ya este dentro de la lista:
                while nombre_herramienta in herramientas:
                    nombre_herramienta = input(
                        "el articulo que ingreso ya se encuentra en la lista.\ningrese uno distinto o salir para cancelar el ingreso: ").lower()
                # en caso de se cumplan los requisitos se agrega el articulo a la lista:
                herramientas.append(nombre_herramienta)
    # en caso de que el operador ingrese a la carga de existencias
    elif seleccion == "2":
        # si todavia no realizo la carga de articulos (opcion 1)
        if not herramientas:
            print("primero ingresa un articulo a la lista opcion 1 del menu de inicio.")
        # la carga de cantidades solo se permitira una vez para no alterar la lista:
        elif existencias:
            print("error: ya realizo la carga inicial.\nsi quiere actualizar la lista ingrese la opcion 7 en el menu de inicio\n")
        # si es la primera vez que realiza la carga de existencias:
        else:
            print("a continuacion le pediremos que ingrese el stock de herramientas:")
            # se utiliza un bucle for para recorrer la lista de herramientas y ver cuantos articulos agrego el operador:
            for i in range(len(herramientas)):
                # la variable stock_herramientas contendra la cantidad de articulos disponibles de cada tipo:
                stock_herramientas = input(
                    f"ingrese la cantidad de {herramientas[i]} :").replace(" ", "")
                while stock_herramientas.isdigit() == False:
                    print("\nError: ingresa un numero\n")
                    stock_herramientas = input(
                        f"ingrese la cantidad de {herramientas[i]} :").replace(" ", "")
                # volvemos entero el string y enviamos la cantidad a la lista existencias:
                stock_herramientas = int(stock_herramientas)
                existencias.append(stock_herramientas)
    # en caso de que ingrese al inventario:
    elif seleccion == "3":
        print("- Inventario -")
        # si el inventario se encuentra vacio:
        if not herramientas or not existencias:
            print("primero realiza la carga inicial(opcion 1 en el menu)\nsi ya realizo la carga inicial ahora realice la carga de existencias(opcion 2 del menu)")
        # si tiene contenido lo imprime:
        else:
            print("listado completo de existencias:")
            for i in range(len(herramientas)):
                print(
                    f"herramienta: {herramientas[i]} cantidad: {existencias[i]}")
    # si ingresa a la Revision de stock:
    elif seleccion == "4":
        # si el inventario se encuentra vacio:
        if not herramientas or not existencias:
            print("primero realiza la carga inicial(opcion 1 en el menu)\nsi ya realizo la carga inicial ahora realice la carga de existencias(opcion 2 del menu)")
        # caso contrario:
        else:
            print("- revision de stock -")
            # primero se realiza la busqueda del articulo dentro de la lista herramientas:
            # la variable busqueda contendra el articulo a buscar:
            busqueda = input(
                "ingrese el articulo para buscarlo en el inventario : ").title().replace(" ", "")
            # en caso de que se encuentre en la lista:
            if busqueda in herramientas:
                for i in range(len(herramientas)):
                    if busqueda == herramientas[i]:
                        posicion = i
                print(
                    f"articulo: {herramientas[posicion]} cantidad: {existencias[posicion]}")
            # en caso de que no se encuentre en la lista:
            elif busqueda not in herramientas:
                print(
                    "el articulo no se encuentra en la lista.\nverifique existencia en la opcion 3 del menu de inicio")
    # en caso de que ingrese a la opcion de reporte de articulos agotados:
    elif seleccion == "5":
        # si todavia no se realizo la carga inicial de articulos (opcion 1 del menu):
        if not herramientas:
            print(
                "ingrese articulos al inventario con la opcion 1 en el menu de inicio.\n")
        # si todavia no se realizo la carga de stock de articulos en el inventario (opcion 2 del menu)
        elif not existencias:
            print("ingrese el stock del inventario, opcion 2 del menu de inicio.")
        # una vez cumplidos los requisitos:
        else:
            print("Reporte de articulos agotados: ")
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    sin_stock = []
                    sin_stock.append(herramientas[i])
                    for i in range(len(sin_stock)):
                        print(sin_stock[i])
            # en caso de que no hayan faltantes:
            if 0 not in existencias:
                print("articulos sin faltantes.")
    # si ingresa a la alta de nuevo producto:
    elif seleccion == "6":
        # si el inventario se encuentra vacio:
        if not herramientas or not existencias:
            print("primero realiza la carga inicial(opcion 1 en el menu)\nsi ya realizo la carga inicial ahora realice la carga de existencias(opcion 2 del menu)")
        # caso contrario:
        else:
            print(
                "- Alta de nuevo producto -\nsolo podra ingresar un articulo y el stock del mismo:")
            # alta_producto contendra el nuevo articulo a ingresar en la lista herramientas:
            alta_producto = input(
                "ingrese el articulo para agregarlo al inventario: ").title().replace(" ", "")
            while alta_producto.isalpha() == False or alta_producto in herramientas:
                if alta_producto.isalpha() == False:
                    alta_producto = input(
                        "no ingrese caracteres especiales o numeros.\n articulo: ").title().replace(" ", "")
                # en caso de que el articulo ya se encuentre en la lista:
                elif alta_producto in herramientas:
                    alta_producto = input(
                        "el articulo ya se encuentra en la lista, ingrese uno distinto.\narticulo: ").title().replace(" ", "")
            # una vez que se haya tomado el producto se solicita el ingreso de cantidad del mismo:
            cantidad_producto = input(
                f"ingrese la cantidad de {alta_producto} en existencia:").replace(" ", "")
            # si ingresa un simbolo negativo:
            if "-" in cantidad_producto:
                print("ingreso un simbolo negativo. ingrese un valor mayor a 0")
            # se mantendra en el bucle hasta que ingrese un valor correcto:
            while cantidad_producto.isdigit() == False:
                cantidad_producto = input(
                    f"\nsolo puede ingresar numeros.\ningrese la cantidad de: {alta_producto} en existencia: ")
            # luego de obtener lo solicitado de forma correcta se transforma el string a entero
            cantidad_producto = int(cantidad_producto)
            # una vez que las dos solicitudes al operador cumplen los requisitos
            #  se agregan a sus respectivas listas :
            herramientas.append(alta_producto)
            existencias.append(cantidad_producto)
            print("\nalta exitosa.\n")
    # si ingresa a actualizacion de stock:
    elif seleccion == "7":
        # si el inventario se encuentra vacio:
        if not herramientas or not existencias:
            print("primero realiza la carga inicial(opcion 1 en el menu)\nsi ya realizo la carga inicial ahora realice la carga de existencias(opcion 2 del menu)")
        # caso contrario
        else:
            # se crea un bucle para crear un "menu" dado caso de que se necesiten
            # para registrar mas de una venta o actualizacion:
            while True:
                print("""
                    - Menu de Actualizacion de stock - 
                ingrese:
                1.- Venta de articulo.
                2.- Actualizacion de articulo.
                3.- menu inicio.""")
                # la variable seleccion obtiene el ingreso del operador:
                seleccion = input("opcion: ")
                # en caso de que ingrese a la venta de articulos:
                if seleccion == "1":
                    print("\n- Seccion Ventas -\n")
                    # primero buscamos el articulo en la lista para ver si hay existencias:
                    busqueda = input(
                        "ingrese el articulo vendido: ").title().replace(" ", "")
                    # revisamos la lista con un bucle for:
                    if busqueda in herramientas:
                        for i in range(len(herramientas)):
                            if busqueda == herramientas[i]:
                                # guardamos su posicion en la lista:
                                posicion = i
                        # si no hay stock del producto:
                        if existencias[posicion] == 0:
                            print(
                                "\nel articulo no posee existencias, revise el inventario.\n")
                        # en caso de que haya stock disponible:
                        else:
                            # la variable cantidad_a_vender contendra la cantidad del articulo vendido:
                            cantidad_a_vender = input(
                                f"ingrese la cantidad de {herramientas[posicion]} vendidas: ").replace(" ", "")
                            while cantidad_a_vender.isdigit() == False:
                                print(
                                    "Error:solo puede ingresar un numero positivo: ")
                                cantidad_a_vender = input(
                                    f"ingrese la cantidad de {herramientas[posicion]} vendidas: ").replace(" ", "")
                            # pasamos la variable de str a int:
                            cantidad_a_vender = int(cantidad_a_vender)
                            # si hay suficiente existencia del articulo a vender:
                            if existencias[posicion] >= cantidad_a_vender:
                                existencias[posicion] -= cantidad_a_vender
                                print("venta exitosa.")
                            # si la demanda del articulo supera la existencia en stock:
                            elif cantidad_a_vender > existencias[posicion]:
                                print(
                                    f"no cuentas con esa cantidad de {herramientas[posicion]}\nverifica el inventario.")
                    # en caso de que exista el articulo dentro del inventario:
                    elif busqueda not in herramientas:
                        print(
                            "\narticulo ingresado no disponible, ingrese un articulo distinto.\n")
                # en caso de que desee actualizar el stock los articulos disponibles:
                elif seleccion == "2":
                    print("\n- Seccion Actualizacion de articulos -\n")
                    # primero buscamos el articulo a actualizar:
                    busqueda = input(
                        "ingrese el articulo a actualizar: ").title().replace(" ", "")
                    # el bucle identificara la posicion
                    if busqueda in herramientas:
                        for i in range(len(herramientas)):
                            if busqueda == herramientas[i]:
                                posicion = i
                        # una vez encontrado el articulo, la variable cantidad_a_actualizar contendra
                        # el monto que ingresa al stock del inventario
                        cantidad_a_actualizar = input(
                            f"ingrese la cantidad de {herramientas[posicion]} a ingresar al inventario: ").replace(" ", "")
                        while cantidad_a_actualizar.isdigit() == False:
                            cantidad_a_actualizar = input(
                                "solo puede ingresar numeros positivos o 0 en caso de no tener mas existencias.\n cantidad: ").replace(" ", "")
                        # pasamos la variable cantidad_a_actualizar de str a int y la sumamos a la posicion correspondiente
                        cantidad_a_actualizar = int(cantidad_a_actualizar)
                        existencias[posicion] += cantidad_a_actualizar
                        print("se actualizo el inventario.\n")
                    # si el articulo no se encuentra en la lista:
                    elif busqueda not in herramientas:
                        print(
                            "\narticulo ingresado no disponible, ingrese un articulo distinto.\n")
                # si el operador ya no necesita ingresar o vender items:
                elif seleccion == "3":
                    break
    # si el operador desea salir del programa:
    elif seleccion == "8":
        break
    # en caso de que el usuario ingrese un dato incorrecto en el menu de inicio:
    else:
        if seleccion != "1" and seleccion != "2" and seleccion != "3" and seleccion != "4" and seleccion != "5" and seleccion != "6" and seleccion != "7" and seleccion != "8":
            print("\nerror: dato no valido. solo puede ingresar numeros del 1 al 8.\n")
