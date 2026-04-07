# Resolucion Actividad 11
#
# creamos la lista con los 10 estudiantes como se solicito:
Estudiantes = ["Micaela", "Sebastian", "Raul", "Julieta",
               "Sofia", "Adrian", "Daniel", "Paola", "Pablo", "Mayra"]
# utilizamos un bucle para mantener la busqueda activa hasta que el usuario indique que desea salir
while True:
    BusquedaEstudiante = input(
        "Ingresa el nombre del estudiante que buscas o Salir para finalizar.\n   nombre : ").replace(" ", "").capitalize()
    while BusquedaEstudiante.isalpha() == False:
        BusquedaEstudiante = input(
            "no ingreses caracteres especiales o numeros.\ningresa el nombre del estudiante que buscas: ").replace(" ", "").capitalize()
    # con la ayuda de un bucle for recorremos la lista para ver en que lugar se encuentra el nombre
    for i in range(len(Estudiantes)):
        if BusquedaEstudiante == Estudiantes[i]:
            posicion = i+1
            print(
                f"se encontro a {BusquedaEstudiante} en la lista.\nse encuentra en la posicion: {posicion} de la lista Estudiantes")
    # cuando el usuario desee salir:
    if BusquedaEstudiante == "Salir":
        break
    # si el nombre no se encuentra lo notificamos:
    else:
        print("el nombre no se encuentra en la lista.")
