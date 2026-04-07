# Resolucion actividad 6 #
#
# debemos rotar los numeros una posicion a la derecha
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
# para rotar la lista eliminamos el ultimo numero de la lista y lo guardamos en una variable
rotacion = lista.pop()
# luego insertamos el numero extraido de la lista al inicio de la misma
lista.insert(0, rotacion)
print(lista)
