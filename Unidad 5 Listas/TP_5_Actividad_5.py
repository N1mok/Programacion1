# Resolucion Actividad 5
#
print("estos son los 8 estudiantes presentes en clase:")
# creamos la lista con los alumnos y la imprimimos para que el usuario pueda verla
alumnos = ["Mayra", "Lupe", "Zacarias", "Natalia",
           "Sonia", "Micaela", "Pablo", "Daniel"]
for i in alumnos:
    if i == alumnos[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
# pedimos al usuario que seleccione agregar o eliminar a alguien.
print("parece que falta o hay un alumno de mas, agrega o elimina algun nombre\n    1.- agregar.\n    2.-eliminar.\n")
while True:
    select = input("seleccion: ").replace(" ", "")
    match select:
        # en caso de que quiera agregar un nuevo alumno a la lista:
        case "1":
            nombre = input(
                "ingrese el nombre para agregarlo a la lista: ").capitalize()
            while nombre.isalpha() == False:
                nombre = input("error: ingresaste un valor incorrecto.\n no utilices caracteres especiales o numeros.\n   nombre del alumno: ").capitalize(
                ).replace(" ", "")
            alumnos.append(nombre)
            break
            # en caso de que quiera eliminar a alguien de la lista:
        case "2":
            for i in alumnos:
                if i == alumnos[-1]:
                    print(i, end=" \n")
                else:
                    print(i, end=", ")
            borrarNombre = input(
                "ingrese el nombre del alumno que desea eliminar de la lista \n").capitalize().replace(" ", "")
            # validamos el dato ingresado:
            while borrarNombre.isalpha() == False and borrarNombre not in alumnos:
                if borrarNombre.isalpha() == False:
                    borrarNombre = input(
                        "ingresaste datos no validos. recuerda que no puedes utilizar caracteres especiales o numeros\ningresa el nombre del alumno a eliminar de la lista: ").capitalize().replace(" ", "")
                elif borrarNombre not in alumnos:
                    print(
                        "ingresaste un nombre que no se encuentra en la lista\nrevisa la siguiente lista, luego ingrese el nombre correctamente")
                    for i in alumnos:
                        if i == alumnos[-1]:
                            print(i, end=" \n")
                        else:
                            print(i, end=", ")
                    borrarNombre = input(
                        "nombre del alumno a eliminar de la lista: ").capitalize().replace(" ", "")
            alumnos.remove(borrarNombre)
            print("\nnombre eliminado con exito.\n")
            break
        case _:
            print("\nsolo puedes ingresar 1 o 2 para seleccionar la opcion.\n 1.- agregar un nombre a la lista\n 2.- ")
# finalizada la accion mostramos la lista actualizada:
print("lista actualizada: ")
for i in alumnos:
    if i == alumnos[-1]:
        print(i, end=" \n")
    else:
        print(i, end=", ")
