#############################################
# Ejercicio 5 — “Escape Room:"La Arena del  #
#                       Gladiador"          #
#############################################
# variables establecidas de la partida
Vida_Gladiador = 100
Vida_Enemigo = 100
PocionesDeVida = 3
AtaquePesado = 15
DanoBaseDelEnemigo = 12
TurnoGladiador = True
print("            BIENVENIDO AL COLISEO")
gladiador = input("dime tu nombre esclavo!\n").replace(" ", "")
while gladiador.isalpha() == False:
    gladiador = input("aarghhh ingresa un nombre real.").replace(" ", "")
print("\npreparate para la batalla!\n")
# el juego corre hasta que uno de los dos quede sin vida
while (Vida_Enemigo > 0) and (Vida_Gladiador > 0):
    while TurnoGladiador == True:  # turno activo del gladiador, finaliza luego de cada accion. se controla con variable especificada
        print(f"""
            gladiador: {gladiador}  vida: {Vida_Gladiador}
            pociones disponibles: {PocionesDeVida}
            vida del gladiador enemigo: {Vida_Enemigo}""")
        # menu de opciones:
        turnoActivo = input(""" 
                tu turno!
                1. Ataque Pesado
                2. Ráfaga Veloz
                3. Curar
                seleccion: """)
        # validacion de datos ingresados por el jugador:
        while turnoActivo.isdigit() == False or turnoActivo != "1" and turnoActivo != "2" and turnoActivo != "3":
            turnoActivo = input("""
                error: ingresaste un dato no valido.
                ingresa un numero entre 1 y 3:                 
                1. Ataque Pesado
                2. Ráfaga Veloz
                3. Curar
                seleccion: """)
        match turnoActivo:
            case "1":
                print("""
                        ATAQUE PESADO!""")
                if Vida_Enemigo > 20:
                    Vida_Enemigo -= AtaquePesado
                    print(
                        f"   atacaste al enemigo con {AtaquePesado} puntos de daño!!")
                    TurnoGladiador = False
                else:  # caso especial vida del enemigo menor a 20
                    Vida_Enemigo -= AtaquePesado*1.5
                    print(
                        f"  Golpe critico: {AtaquePesado} puntos de daño!!")
                    TurnoGladiador = False
            case "2":
                print("\n   ataque rapido\n")
                for x in range(3):
                    Vida_Enemigo -= 5
                    print("Golpe conectado por 5 de daño")
                TurnoGladiador = False
            case "3":
                if PocionesDeVida > 0:
                    Vida_Gladiador += 30
                    PocionesDeVida -= 1
                    print("recuperaste puntos 30 de vida")
                    TurnoGladiador = False
                else:
                    print("te quedaste sin pociones!")
                    TurnoGladiador = False
    # turno enemigo:
    Vida_Gladiador -= 12
    TurnoGladiador = True  # devuelve el turno al jugador
if Vida_Gladiador >= 0:
    print(f"Victoria!! {gladiador} gano la batalla.")
elif Vida_Gladiador <= 0:
    print(f"Derrota. caiste en combate")
