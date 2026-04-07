# Resolucion Actividad 3 #
#
# generamos una lista al azar con 15 numeros entre 1 y 100
numeros = [15, 20, 39, 41, 8, 32, 11, 2, 4, 96, 21, 74, 81, 99, 33]
numerosPares = []
numerosImpares = []
# creamos un bucle para discriminar numeros pares de impares:
for i in numeros:
    if i % 2 == 0:
        numerosPares.append(i)
    else:
        numerosImpares.append(i)
# imprimimos todo en pantalla con sus respectivos bucles:
print("lista de numeros al azar: ")
for i in numeros:
    if i == numeros[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
# cantidad de numeros pares:
print("numeros pares: ")
for i in numerosPares:
    if i == numerosPares[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
print(f"tiene: {len(numerosPares)} numeros pares")
# cantidad de numeros impares:
print("numeros impares: ")
for i in numerosImpares:
    if i == numerosImpares[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
print(f"tiene: {len(numerosImpares)} numeros impares")
