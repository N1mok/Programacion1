#################################################
# Ejercicio 3 (Alta) — “Agenda de Turnos con    #
#                        Nombres (sin listas)”  #
#################################################
# Durante el trabajo se utilizara .replace para reemplazar espacios vacios o cambiar valores en las strings
# establecemos los turnos
Lunes1 = "(libre)"
Lunes2 = "(libre)"
Lunes3 = "(libre)"
Lunes4 = "(libre)"
Martes1 = "(libre)"
Martes2 = "(libre)"
Martes3 = "(libre)"
# inicio de sesion del operador
operador = input("""
                        bienvenido

            para iniciar sesion debes ingresar tu nombre,
                solo debes ingresar letras.
                    operador: """).replace(" ", "")
while operador.isalpha() == False:  # validando con isalpha
    operador = input(
        "ingrese un nombre valido,recuerde que no puede usar caracteres especiales\nnombre del operador: ").replace(" ", "")
# ingreso al menu
while True:
    seleccion_menu = input("""
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema
    opcion: """)
    match seleccion_menu:
        case "1":  # ingreso a reservas
            dia = input(f"""    
                ingrese el dia que desea reservar
            tenga en cuenta los turnos disponibles a continuacion 
            ***si desea el primer turno libre seleccione el dia y turno 5
                Turnos agendados:
                    
                    Dia:   Lunes
                        1.-    {Lunes1}
                        2.-    {Lunes2}
                        3.-    {Lunes3}
                        4.-    {Lunes4}
                    Dia:   Martes    
                        1.-    {Martes1}
                        2.-    {Martes2}
                        3.-    {Martes3}
                    dia seleccionado: """).replace(" ", "").lower()
            while dia != "lunes" and dia != "martes":  # seleccion de dia
                dia = input(
                    "ingresa lunes o martes, de momento solo tenemos esos dias.\n     dia seleccionado:").replace(" ", "").lower()
            if dia == "martes":
                turno = input(  # seleccion turnos martes
                    "ingrese un turno a ocupar entre 1 y 3, ingrese 5 para primer turno libre \n          turno: ").replace(" ", "")
                while turno != "1" and turno != "2" and turno != "3" and turno != "5" or turno.isdigit() == False:
                    turno = input(
                        "los martes solo tenemos 3 turnos\n ingresa un numero entre 1 y 3, ingrese 5 para primer turno libre\n     turno: ").replace(" ", "")
            else:
                turno = input(  # seleccion turnos lunes
                    "ingrese un turno a ocupar entre 1 y 4, ingrese 5 para primer turno libre\n         turno: ").replace(" ", "")
                while turno != "1" and turno != "2" and turno != "3" and turno != "4" and turno != "5" or turno.isdigit() == False:
                    turno = input(
                        "por favor ingresa un numero entre 1 y 4, ingrese 5 para primer turno libre\n         turno: ").replace(" ", "")
            dia = dia+turno  # genero para comparar turnos libres
            paciente = input("ingresa el nombre del paciente (solo utilice letras) para reservar el turno: ").replace(
                " ", "").lower()
            while paciente.isalpha() == False:  # validando nombre de paciente solo con letras
                paciente = input(
                    "el nombre del paciente no puede tener caracteres especiales, solo use letras\n  nombre: ").replace(" ", "").lower()
            if paciente == Lunes1 or paciente == Lunes2 or paciente == Lunes3 or paciente == Lunes4 or paciente == Martes1 or paciente == Martes2 or paciente == Martes3:
                print("el paciente ya esta anotado, verifique la agenda.")
            elif dia == "lunes5" or dia == "martes5":  # toma de primer turno libre
                if dia == "lunes5" and Lunes1 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Lunes1 = Lunes1.replace(Lunes1, paciente)
                elif dia == "lunes5" and Lunes2 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Lunes2 = Lunes2.replace("(libre)", paciente)
                elif dia == "lunes5" and Lunes3 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Lunes3 = Lunes3.replace("(libre)", paciente)
                elif dia == "lunes5" and Lunes4 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Lunes4 = Lunes4.replace("(libre)", paciente)
                elif dia == "martes5" and Martes1 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Martes1 = Martes1.replace("(libre)", paciente)
                elif dia == "martes5" and Martes2 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Martes2 = Martes2.replace("(libre)", paciente)
                elif dia == "martes5" and Martes3 == "(libre)":
                    print("\nprimer turno libre asignado con exito.\n")
                    Martes3 = Martes3.replace("(libre)", paciente)
                else:
                    print("turno ocupado, revise la agenda")
            else:  # en caso de que seleccione dia y turno
                if dia == "lunes1" and Lunes1 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Lunes1 = Lunes1.replace("(libre)", paciente)
                elif dia == "lunes2" and Lunes2 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Lunes2 = Lunes2.replace("(libre)", paciente)
                elif dia == "lunes3" and Lunes3 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Lunes3 = Lunes3.replace("(libre)", paciente)
                elif dia == "lunes4" and Lunes4 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Lunes4 = Lunes4.replace("(libre)", paciente)
                elif dia == "martes1" and Martes1 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Martes1 = Martes1.replace("(libre)", paciente)
                elif dia == "martes2" and Martes2 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Martes2 = Martes2.replace("(libre)", paciente)
                elif dia == "martes3" and Martes3 == "(libre)":
                    print("\nTurno asignado con exito.\n")
                    Martes3 = Martes3.replace("(libre)", paciente)
                else:
                    print("turno ocupado, revise la agenda")
        case "2":  # cancelar turnos
            while True:
                print(f"""
                
                ingreso al panel de cancelacion de turnos
                
                    operador: {operador}
                            
                    Turnos agendados:
                    
                    Dia:   Lunes
                        1.-    {Lunes1}
                        2.-    {Lunes2}
                        3.-    {Lunes3}
                        4.-    {Lunes4}
                    Dia:   Martes    
                        1.-    {Martes1}
                        2.-    {Martes2}
                        3.-    {Martes3}
                
                primero se le solicitara el dia, luego el turno a cancelar.
                visualice la agenda que esta arriba antes de realizar cambios.
                si desea salir del panel ingrese salir
                            """)
                dia = input("por favor ingrese el dia: ").replace(
                    " ", "").lower()
                if dia == "salir":
                    break
                while dia != "lunes" and dia != "martes" and dia != "salir":
                    dia = input("si desea seleccionar un dia ingrese lunes o martes\nsi desea salir del panel ingrese salir.\n           ingreso: ").replace(
                        " ", "").lower()
                if dia == "salir":
                    break
                elif dia == "martes":
                    turno = input(
                        "ingrese un turno a ocupar entre 1 y 3 \n          turno: ").replace(" ", "")
                    while turno != "1" and turno != "2" and turno != "3" or turno.isdigit() == False:
                        turno = input(
                            "los martes solo tenemos 3 turnos\n ingresa un numero entre 1 y 3\n     turno: ")
                        print("por favor ingresa un numero entero entre 1 y 3.")
                else:
                    turno = input(
                        "por favor ingresa un numero entre 1 y 4\n         turno: ")
                    while turno != "1" and turno != "2" and turno != "3" and turno != "4" or turno.isdigit() == False:
                        turno = input(
                            "por favor ingresa un numero entre 1 y 4\n         turno: ").replace(" ", "")
                dia = dia+turno
                paciente = input(
                    "por favor ingrese el nombre del paciente a eliminar exactamente como esta en la lista\n paciente:").replace(" ", "").lower()
                if dia == "lunes1" and Lunes1 == (paciente):
                    Lunes1 = Lunes1.replace(paciente, "(libre)")
                    print("\nTurno libre con exito.\n")
                elif dia == "lunes2" and Lunes2 == (paciente):
                    Lunes2 = Lunes2.replace(paciente, "(libre)")
                    print("\nTurno libre con exito.\n")
                elif dia == "lunes3" and Lunes3 == (paciente):
                    print("\nTurno libre con exito.\n")
                    Lunes3 = Lunes3.replace(paciente, "(libre)")
                elif dia == "lunes4" and Lunes4 == (paciente):
                    print("\nTurno libre con exito.\n")
                    Lunes4 = Lunes4.replace(paciente, "(libre)")
                elif dia == "martes1" and Martes1 == (paciente):
                    print("\nTurno libre con exito.\n")
                    Martes1 = Martes1.replace(paciente, "(libre)")
                elif dia == "martes2" and Martes2 == (paciente):
                    print("\nTurno libre con exito.\n")
                    Martes2 = Martes2.replace(paciente, "(libre)")
                elif dia == "martes3" and Martes3 == (paciente):
                    print("\nTurno libre con exito.\n")
                    Martes3 = Martes3.replace(paciente, "(libre)")
                else:
                    print(
                        "turno o paciente inexistente, verifique la agenda.")
        case "3":  # agenda
            print(f"""
                    operador: {operador}
                            
                    Turnos agendados:
                    
                    Dia:   Lunes
                        1.-    {Lunes1}
                        2.-    {Lunes2}
                        3.-    {Lunes3}
                        4.-    {Lunes4}
                    Dia:   Martes    
                        1.-    {Martes1}
                        2.-    {Martes2}
                        3.-    {Martes3}
                
                            """)
        case "4":  # suma de turnos libres, ocupados y discriminamos dias para visualizar cual tiene mas turnos
            contador_turnos_libres = 0
            contador_turnos_ocupados = 0
            turnos_lunes = 0
            turnos_martes = 0
            if Lunes1 == ("(libre)"):
                contador_turnos_libres += 1
            if Lunes2 == ("(libre)"):
                contador_turnos_libres += 1
            if Lunes3 == ("(libre)"):
                contador_turnos_libres += 1
            if Lunes4 == ("(libre)"):
                contador_turnos_libres += 1
            if Martes1 == ("(libre)"):
                contador_turnos_libres += 1
            if Martes2 == ("(libre)"):
                contador_turnos_libres += 1
            if Martes3 == ("(libre)"):
                contador_turnos_libres += 1
            if Lunes1 != ("(libre)"):
                turnos_lunes += 1
                contador_turnos_ocupados += 1
            if Lunes2 != ("(libre)"):
                turnos_lunes += 1
                contador_turnos_ocupados += 1
            if Lunes3 != ("(libre)"):
                turnos_lunes += 1
                contador_turnos_ocupados += 1
            if Lunes4 != ("(libre)"):
                turnos_lunes += 1
                contador_turnos_ocupados += 1
            if Martes1 != ("(libre)"):
                turnos_martes += 1
                contador_turnos_ocupados += 1
            if Martes2 != ("(libre)"):
                turnos_martes += 1
                contador_turnos_ocupados += 1
            if Martes3 != ("(libre)"):
                turnos_martes += 1
                contador_turnos_ocupados += 1
            if turnos_lunes > turnos_martes:
                dia_mas_ocupado = "lunes"
            elif turnos_martes > turnos_lunes:
                dia_mas_ocupado = "martes"
            elif turnos_lunes == turnos_martes:
                dia_mas_ocupado = "empate"
            print(f"""
                    turnos libres: {contador_turnos_libres}
                    turnos ocupados: {contador_turnos_ocupados}
                    turnos del dia lunes: {turnos_lunes}
                    turnos del dia martes: {turnos_martes}
                    dia mas ocupado: {dia_mas_ocupado}""")
        case "5":  # salida del sistema
            break
        case _:
            print("ingrese una opcion valida")
