# Resolucion actividad 7 #
#
# utilizo una lista para los dias
dia = ["Lunes", "Martes", "Miercoles",
       "Jueves", "Viernes", "Sabado", "Domingo"]
# utilizo una matriz para las temperaturas respetando el orden  #
# para que se encuentren en la misma posicion que el dia        #
temperaturas = [[31, 13], [20, 9], [21, 10],
                [30, 19], [25, 15], [24, 12], [26, 17]]
# las variables a continuacion contendran las sumas que se utilizaran para el promedio: #
promedioTemperaturaMaxima = 0
promedioTemperaturaMinima = 0
# en esta lista se va a guardar la amplitud termica de cada dia
AmplitudXDia = []
# se realiza la suma de temperaturas maximas recorriendo las filas
#  manteniendo la misma columna a la que se le asigno el valor
for fila in range(len(temperaturas)):
    promedioTemperaturaMaxima += temperaturas[fila][0]
# se realiza la suma de temperaturas minimas recorriendo las filas
#  manteniendo la misma columna a la que se le asigno el valor
for fila in range(len(temperaturas)):
    promedioTemperaturaMinima += temperaturas[fila][1]
# una vez obtenidas las sumas se realiza la division por la cantidad de dias para obtener el promedio:
promedioTemperaturaMaxima = promedioTemperaturaMaxima / len(temperaturas)
promedioTemperaturaMinima = promedioTemperaturaMinima / len(temperaturas)
# ahora realizamos la resta entre temperatura maxima y minima para obtener la amplitud termica
# el valor de la resta se guarda en la variable AmplitudXDia
for fila in range(len(temperaturas)):
    rangoTemperatura = temperaturas[fila][0]-temperaturas[fila][1]
    AmplitudXDia.append(rangoTemperatura)
# abuscamos el valor mas alto:
amplitudTermica = max(AmplitudXDia)
# ahora buscamos la posicion en la que se encuentra dentro de la lista
# como se respeto el indice de los dias y de las temperaturas registradas
# el resultado indicara la ubicacion del dia
amplitudTermica = AmplitudXDia.index(amplitudTermica)
print(f"promedio temperatura maxima: {promedioTemperaturaMaxima:.1f}")
print(f"promedio temperatura minima: {promedioTemperaturaMinima:.1f}")
print(f"dia que se registro mayor amplitud termica: {dia[amplitudTermica]}")
