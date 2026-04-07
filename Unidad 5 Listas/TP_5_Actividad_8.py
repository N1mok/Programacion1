# Actividad 8 #
#
# la matriz contiene las notas de cada estudiante
notasEstudiantes = [[5, 8, 7], [9, 3, 6], [6, 8, 7], [7, 7, 7], [8, 4, 1]]
# la siguiente lista contiene el promedio de cada alumno
promedioEstudiantes = []
# cada variable a continuacion contiene la suma para realizar el promedio de cada nota
promedioMate = 0
promedioHistoria = 0
promedioFisica = 0
# realizamos la suma y division para obtener el promedio de cada estudiante
for i in range(len(notasEstudiantes)):
    promedio = (notasEstudiantes[i][0] +
                notasEstudiantes[i][1]+notasEstudiantes[i][2])/3
    promedio = round(promedio, 2)
    promedioEstudiantes.append(promedio)
# realizamos la suma de las notas obtenidas en matematica por cada alumno
for i in range(len(notasEstudiantes)):
    promedioMate += notasEstudiantes[i][0]
# realizamos la suma de las notas obtenidas en historia por cada alumno
for i in range(len(notasEstudiantes)):
    promedioHistoria += notasEstudiantes[i][1]
# realizamos la suma de las notas obtenidas en fisica por cada alumno
for i in range(len(notasEstudiantes)):
    promedioFisica += notasEstudiantes[i][2]
# imprimimos en pantalla los promedios de cada estudiante:
print("promedio de cada estudiante del curso: ")
for i in promedioEstudiantes:
    if i == promedioEstudiantes[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
# realizamos la division para obtener el promedio de cada materia
promedioMate /= 5
promedioHistoria /= 5
promedioFisica /= 5
# imprimimos en pantalla cada resultado:
print(f"\npromedio del curso en la materia matematica: {promedioMate}\n")
print(f"promedio del curso en la materia historia: {promedioHistoria}\n")
print(f"promedio del curso en la materia fisica: {promedioFisica}\n")
