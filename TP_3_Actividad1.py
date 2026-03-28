##################################
# Actividad 1 - “Caja del Kiosco”#
##################################
# Objetivos:  Simular una compra con validaciones y cálculo de total #
# durante el trabajo se utiliza una lista: variable carrito, para el ingreso de los items que determine comprar el cliente
# sin la lista el cliente tendria un limite de items a comprar que lo determinaria la cantidad de variables establecidas
nombre = input("""Bienvenido!
para iniciar tu compra te solicitamos ingreses 
un nombre de cliente valido
no se aceptan numeros ni caracteres especiales.
    ingrese su nombre: """)
# validando con .isalpha en while
while nombre.isalpha() == False:
    print("el nombre que ingresaste es invalido\npor favor no utilices numeros ni caracteres especiales")
    nombre = input("  ingrese un nombre valido: ")
# se solicita una cantidad de items
items = input("ingresa la cantidad de productos que vas a comprar\ntenga en cuenta que solo aceptamos numeros enteros y positivos\n  cantidad de productos: ")
# se utiliza metodo solicitado validando con .isdigit en while
while items.isdigit() == False:
    items = input(
        "por favor ingrese un numero entero, positivo y mayor a 0\ningrese la cantidad de productos: ")
# luego de validar como fue solicitado se vuelve a entero la variable#
items = int(items)
while items <= 0:  # nos aseguramos de que sea mayor a 0
    items = int(input(
        "veo q tu carrito esta vacio, por favor ingresa por lo menos 1 item al carrito para realizar una compra\n items: "))
# creamos un contenedor para los items a comprar y contadores para la suma#
carrito = []
total_descuento = 0
total_sin_descuentos = 0
total = 0
total_a_pagar = 0
promedio = 0
for i in range(items):
    precio = input(f"ingrese el precio del producto {i+1}: ")
    while precio.isdigit() == False:
        precio = input("ingrese un valor entero y positivo: ")
# luego de validar el precio utilizando .isdigit se vuelve entero la variable
    precio = int(precio)
# verificamos si existe o no un descuento#
    descuento = input(
        "tiene un cupon de descuento para el producto?\ningrese s en caso de tenerlo o n en caso de no tener el cupon: ")
    while descuento not in ["S", "s", "N", "n"]:
        descuento = input(
            "ingreso un valor incorrecto, por favor ingrese S en caso de tener el cupon\no N en caso de no tener un cupon de descuento: ")
    descuento = descuento.lower()
# realizamos el descuento si es necesario#
    if descuento == "s":
        carrito.append((i, precio, descuento))
        promedio += precio
        total += total_descuento
        precio -= precio / 10
        total_descuento += precio
        # introducimos objetos a la lista
    elif descuento == "n":
        carrito.append((i, precio, descuento))
        promedio += precio
        total_sin_descuentos += precio
        total += total_sin_descuentos

# verificamos la suma para que el valor ahorro nos de un numero positivo#
if total_descuento > total_sin_descuentos:
    ahorro = total_descuento - total_sin_descuentos
elif total_descuento < total_sin_descuentos:
    ahorro = total_sin_descuentos-total_descuento
promedio /= items
if total_sin_descuentos == 0:
    ahorro = promedio - total_descuento
    promedio = total_descuento / items
total_a_pagar = total_descuento + total_sin_descuentos
# realizamos la impresion de la compra#
print("    cliente: ", nombre)
print("\n    cantidad de productos: ", items)
for i, precio, descuento in carrito:
    print(f"    producto: {i+1} - precio: {precio} - descuento: {descuento}")
print(f"""
    valor total de productos sin descuentos: {total_sin_descuentos:.2f}
    valor total de productos con descuentos: {total_descuento:.2f}
    promedio por producto: {promedio:.2f}
    ahorro: {ahorro:.2f}
    total a pagar: {total_a_pagar:.2f}""")
