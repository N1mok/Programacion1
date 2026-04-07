# Resolucion Actividad 2 #
#
print("en esta actividad te solicitamos que ingreses 5 productos\nlos cuales seran guardados en una lista para organizarlos alfabeticamente")
# creamos un contenedor de lista
producto = []
# creamos un bucle para que el usuario ingrese los elementos uno a uno#
for i in range(5):
    ingresoProducto = input(
        f"ingresa el producto nº {i+1}: ").replace(" ", "").lower()
    # en caso de que ingrese un valor incorrecto validamos#
    while ingresoProducto.isalpha() == False:
        ingresoProducto = input(
            f"por favor solo ingresa letras.\nno estan permitidos los numeros o caracteres especiales\n   producto nº {i+1}: ").replace(" ", "").lower()
    producto.append(ingresoProducto)
# ordenamos la lista:
productoOrdenado = sorted(producto)
# imprimimos la lista utilizando un bucle
print("organizamos la lista con los productos que nos diste:")
for i in productoOrdenado:
    if i in productoOrdenado[-1]:
        print(i, end=" ")
    else:
        print(i, end=", ")
# solicitamos que elimine un producto
restProducto = input(
    "\ningresa un producto a eliminar de la lista: ").replace(" ", "").lower()
# verificamos que este en la lista
while restProducto not in productoOrdenado:
    print("lo que ingresaste no se encuentra en la lista a continuacion: ")
    for i in productoOrdenado:
        if i in productoOrdenado[-1]:
            print(i, end=" ")
        else:
            print(i, end=", ")
    restProducto = input(
        "\ningresa un producto dentro de la lista actual: ").replace(" ", "").lower()
# eliminamos el producto:
productoOrdenado.remove(restProducto)
# imprimimos la lista actualizada.
print("se actualizo la lista: ")
for i in sorted(productoOrdenado):
    if i in productoOrdenado[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
