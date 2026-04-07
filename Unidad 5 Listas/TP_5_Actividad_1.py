# Resolucion Actividad 1: #
# creamos la lista con la nota de 10 estudiantes
Notas = [3, 8, 5, 10, 1, 2, 4, 6, 7, 9]
print("notas sin organizar: ")
for i in Notas:
    if i == Notas[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
sumaNotas = 0
promedio = 0
# sacamos el promedio de las notas#
# realizo la suma de las notas utilizando un for, tambien existe la funcion nativa sum() para calcularlo.
for i in Notas:
    sumaNotas += i
# luego de realizar la suma guardada en la variable sumaNotas #
# realizamos sacamos la cantidad de notas guardadas en la lista utilizando la funcion len()#
cantidadNotas = len(Notas)
# dividimos sumaNotas por la cantidad de notas guardadas en la funcion a la q se hace referencia cantidadNotas#
promedio = sumaNotas/cantidadNotas
# creamos un bucle para organizar la lista existente y asi sacar la nota mas alta y la mas baja.#
for primerIndice in range(cantidadNotas-1):
    for segundoIndice in range(cantidadNotas-1-primerIndice):
        if Notas[segundoIndice] > Notas[segundoIndice+1]:
            Notas[segundoIndice], Notas[segundoIndice +
                                        1] = Notas[segundoIndice+1], Notas[segundoIndice]
# luego de ordenar la lista seleccionamos el ultimo elemento de la lista con indice -1
notaMasAlta = Notas[-1]
# el primer elemento de la lista que es la nota mas baja:
notaMasBaja = Notas[0]
# imprimimos todo lo solicitado en pantalla:
print("\nnotas organizadas de menor a mayor: ")
for i in Notas:
    if i == Notas[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
print(
    f"\nnota mas alta: {notaMasAlta}\nnota mas baja: {notaMasBaja}\npromedio de las notas: {promedio}")
