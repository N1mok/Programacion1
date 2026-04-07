# Resolucion actividad 12
#
# creamos un contenedor para los numeros que va a ingresar el usuario
ListaNumerosEnteros = []
print("a continuacion necesitamos que ingreses 8 numeros enteros")
# mediante un bucle for obtenemos los valores uno a uno que va ingresando el usuario
for i in range(8):
    numeroEntero = input(f"ingresa el {i+1} numero: ")
    # en caso de error al ingresar los datos:
    while numeroEntero.isdigit() == False:
        numeroEntero = input(
            f"solo puedes ingresar numeros enteros.\n ingresa el {i+1} numero: ")
    # pasamos los datos obtenidos de string a numeros enteros:
    numeroEntero = int(numeroEntero)
    # guardamos los enteros en la lista para poder trabajarlos:
    ListaNumerosEnteros.append(numeroEntero)
# se utiliza el metodo sorted para crear una lista nueva con los numeros que ingreso el usuario
# la funcion sorted por si sola ordena los numeros de Menor a Mayor
# si utilizamos el parametro reverse = True de la funcion sorted
# el orden se invierte y la lista pasa a ordenarse de Mayor a Menor
listaMayorMenor = sorted(ListaNumerosEnteros, reverse=True)
listaMenorMayor = sorted(ListaNumerosEnteros)
print("\nlista original:")
for i in ListaNumerosEnteros:
    if i == ListaNumerosEnteros[-1]:
        print(i, end=" ")
    else:
        print(i, end=", ")
print("\nLista ordenada de menor a mayor:")
for i in listaMenorMayor:
    if i == listaMenorMayor[-1]:
        print(i, end=" ")
    else:
        print(i, end=", ")
print("\nLista ordenada de mayor a menor:")
for i in listaMayorMenor:
    if i == listaMayorMenor[-1]:
        print(i, end=" ")
    else:
        print(i, end=", ")
