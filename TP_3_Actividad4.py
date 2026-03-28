##########################################
# Ejercicio 4 — “Escape Room: La Bóveda” #
##########################################
# definimos variables del juego
# utilizo una unica lista para las "cerraduras" de la boveda
#
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
forzar_seguidas = 3
cerraduras = ["sabado", "horoscopo", "0987654321"]
codigo_parcial = ""
print("""
        Bienvenido agente!
te estabamos esperando, para iniciar
necesitamos tu nombre clave.
solo puedes usar letras
(*no se permiten numeros)
(*no se permiten caracteres especiales)""")
jugador = input("\n ingresa tu nick: ")
while jugador.isalpha() == False:  # validacion del nombre de jugador con isalpha
    jugador = input("""por favor ingresa un nombre valido
    recuerda que no puedes usar numeros ni caracteres especiales
    nombre del agente: """)
print(f"""\nagente: {jugador}
tiene el deber de traernos la informacion que se encuentra en la boveda,
esta solo podra ser abierta si descubre la combinacion de 3 cerraduras
distintas, cuenta con las siguientes herramientas:
* tablet de hackeo para el panel de acceso a cada cerradura:
    la utilizara para ingresar las palabras o digitos necesarios para
    abrir las cerraduras:
        cada intento cuesta -10 de energia y -3 de tiempo
* un kit de Ganzua para intentar forzar cada cerradura:
        cuesta -20 de energia y -2 de tiempo (puede activar la alarma)
* un inhibidor de camaras:
    te permitira descansar y te dara +15 puntos de energia -1 de tiempo mientras las alarmas no esten activas
    si la alarma esta activada y lo utilizas perderas -10 puntos de energia
\n""")
verificar_inicio = False
# verificacion en caso de querer salir del juego sin iniciar partida o error al ingresar caracter
while verificar_inicio == False:
    jugador_inicio = input(
        "estas listo para iniciar?\n        si / no :").replace(" ", "")
    if jugador_inicio == "si":
        verificar_inicio = True
        print(f"""
        llegaste a la base, pudiste infiltrarte sin activar las alarmas
        en este momento tienes:
            energia: {energia}
            tiempo: {tiempo}
        recuerda utilizar el inhibidor para descansar y recuperar algo de energia.""")
    elif jugador_inicio == "no":  # decide salir del juego se solicita confirmacion
        print("buena suerte en tus futuras misiones! adios.")
        break
    else:
        print(
            "error: solo puedes ingresar\n        si / no \n si para iniciar\n no para salir ")
    while energia >= 0 and tiempo >= 0 and cerraduras_abiertas < 3:
        if alarma == True and tiempo <= 3:
            print("fallaste! una alarma fantasma bloqueo el sistema")
            break
        seleccion_menu_partida = input(f"""       
        estado del agente: {jugador}
        energia: {energia}  tiempo: {tiempo}
        cerraduras abiertas: {cerraduras_abiertas}
        opciones: 
            1.- forzar cerradura (costo: -20 energia, -2 tiempo) 
            2.- hackear panel (costo: -10 energia, -3 tiempo)
            3.- descansar activa inhibidor de camaras ( +15 energia (max 100). -1 tiempo)
                seleccionaste: """).replace(" ", "")
        while seleccion_menu_partida.isdigit() == False:
            seleccion_menu_partida = input("""ingresa un numero para seleccionar la opcion :
        1.- forzar cerradura (costo: -20 energia, -2 tiempo) 
        2.- hackear panel (costo: -10 energia, -3 tiempo)
        3.- activa inhibidor de camaras ( +15 energia (max 100). -1 tiempo)
            seleccionaste: """).replace(" ", "")
        match seleccion_menu_partida:
            case "1":
                energia -= 20
                tiempo -= 2
                forzar_seguidas -= 1
                if forzar_seguidas == 0:  # regla anti-spam
                    break
                if energia < 40:        # se activa caso especial de forzado
                    print("                 riesgo de alarma!")
                    posible_alarma_activa = input("""
                            encontraste una puerta trasera, selecciona:
                                    | 1 | 2 | 3 | 
                            para intentar abrir la cerradura : """).replace(" ", "")
                    while posible_alarma_activa.isdigit() == False and posible_alarma_activa <= 0 and posible_alarma_activa > 3:
                        posible_alarma_activa = input(
                            "solo puedes ingresar: 1, 2 o 3 : ")
                    if posible_alarma_activa == "1" or posible_alarma_activa == "2":
                        print("abriste la cerradura!")
                        cerraduras_abiertas += 1
                    elif posible_alarma_activa == "3":
                        print("fallaste! se activo la alarma.\nwiuwiuwiu")
                        alarma = True
            case "2":
                forzar_seguidas = 3  # cortamos racha de "forzar_seguidas"
                if cerraduras_abiertas == 0:
                    for x in range(4):  # accion de hackeo opcion 2 de linea 527 a 586
                        print("sexto dia de la semana")
                        print(f"""estado del agente: {jugador}
                        energia: {energia}  tiempo: {tiempo}
                        cerraduras abiertas: {cerraduras_abiertas}""")
                        energia -= 10  # en cada ronda pierde 10 de energia
                        tiempo -= 0.75  # cuando finaliza el for pierde 3 de tiempo
                        llave = input(
                            "cual es el primer codigo?\n codigo: ").replace(" ", "").lower()
                        codigo_parcial += "*"
                        if len(codigo_parcial) >= 8:
                            codigo_parcial = ""
                            cerraduras_abiertas += 1
                            print(
                                "forzaste el codigo y pasaste el primero")
                            break
                        if llave == cerraduras[0]:
                            cerraduras_abiertas += 1
                            print(
                                "correcto! abriste la primera cerradura")
                            break
                elif cerraduras_abiertas == 1:  # activa 2da cerradura
                    for x in range(4):
                        print("pista: los chinos usan 12 animales en el")
                        print(f"""estado del agente: {jugador}
                        energia: {energia}  tiempo: {tiempo}
                        cerraduras abiertas: {cerraduras_abiertas}""")
                        energia -= 10
                        tiempo -= 0.75
                        llave = input(
                            "cual es el segundo codigo?\n codigo: ").replace(" ", "").lower()
                        codigo_parcial += "*"
                        if len(codigo_parcial) >= 8:
                            codigo_parcial = ""
                            cerraduras_abiertas += 1
                            print(
                                "forzaste el codigo y pasaste el segundo")
                            break
                        if llave == cerraduras[1]:
                            cerraduras_abiertas += 1
                            print(
                                "correcto! abriste la segunda cerradura")
                            break
                elif cerraduras_abiertas == 2:  # activa 3er cerradura
                    for x in range(4):
                        print("pista: ingresa numeros en orden de 0 a 1")
                        print(f"""estado del agente: {jugador}
                        energia: {energia}  tiempo: {tiempo}
                        cerraduras abiertas: {cerraduras_abiertas}""")
                        energia -= 10
                        tiempo -= 0.75
                        llave = input(
                            "cual es el tercer codigo?\n codigo: ").replace(" ", "")
                        if llave == cerraduras[2]:
                            cerraduras_abiertas += 1
                            print("correcto! abriste la tercer cerradura")
                            break
            case "3":
                # descanso el jugador debe recuperar energia y perder tiempo
                forzar_seguidas = 3  # corto racha de refrescar cerraduras
                tiempo -= 1
                if alarma == False and energia <= 96:
                    print(
                        "pudiste activar el inhibidor de camaras, descansa ,recupera el aliento y continua")
                    energia = 100
                elif alarma == False and energia <= 95:
                    energia += 15
                elif alarma == True:  # caso si alarma = on
                    print(
                        "el personal esta alerta! el inhibidor no va a cubrirte esta vez\n   pierdes -10 de energia")
                    energia -= 10
                else:
                    print("energia al maximo, estas gastando tiempo")
            case _:
                print("\nerror: ingresaste un valor fuera del rango\n")
    if cerraduras_abiertas == 3:
        print(
            "VICTORIA!!! conseguiste ingresar a la boveda sin ser detectado")
        break
    if energia <= 0:
        print("Derrotado: te quedaste sin energia")
        break
    if tiempo <= 0:
        print("Derrota: te quedaste sin tiempo")
        break
    if forzar_seguidas == 0:
        print("Derrota: Forzaste mas de 3 veces seguidas, bloqueaste la boveda!")
        break
