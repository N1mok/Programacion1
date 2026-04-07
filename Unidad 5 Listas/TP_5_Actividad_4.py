# Resolucion Actividad 4
#
# utilizamos la lista de la actividad
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datosSinRepetir = []
# primero ordenamos la lista:
for primeraPasada in range(len(datos)-1):
    for segundaPasada in range(len(datos)-1-primeraPasada):
        if datos[segundaPasada] > datos[segundaPasada+1]:
            datos[segundaPasada], datos[segundaPasada +
                                        1] = datos[segundaPasada+1], datos[segundaPasada]
# ahora ingresamos los datos a la lista solo si no se repiten
for i in datos:
    if i not in datosSinRepetir:
        datosSinRepetir.append(i)
# mostramos la lista original y el resultado
print("datos originales: ")
for i in datos:
    if i == datos[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
print("datos sin repetir: ")
for i in datosSinRepetir:
    if i == datosSinRepetir[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
