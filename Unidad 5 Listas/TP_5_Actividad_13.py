# Resolucion Actividad 13
#
# Creamos una lista para los puntajes:
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# Ordenamos la lista de puntajes dentro de la variable ranking:
ranking = sorted(puntajes, reverse=True)
# la variable posicionRanking tendra la ubicacion del puntaje 990
posicionRanking = 0
# recorremos la lista para encontrar la ubicacion con un bucle for
for i in range(len(ranking)):
    if ranking[i] == 990:
        posicionRanking = i
# luego de obtener la posicion imprimimos todo lo solicitado en pantalla
print(f"Puntaje mas alto: {ranking[0]}")
print(f"Puntaje mas bajo: {ranking[-1]}")
print("Ranking: ")
for i in ranking:
    print(i, end=" ")
print(f"\nel puntaje 990 se encuentra en la posicion: {posicionRanking+1}")
