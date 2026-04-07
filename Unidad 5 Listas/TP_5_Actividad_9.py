# Resolucion Actividad 9 #
#
print("juguemos Ta-Te-Ti")
# creamos el tablero que se utilizara para el juego:
TaTeTi = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# iniciamos el juego y lo mantenemos en funcionamiento hasta que se llene el tablero
# o alguien gane la partida con un bucle while:
while True:
    # para garantizar el correcto funcionamiento se verifican una a una todas las variables dentro de la matriz
    if "-" not in TaTeTi[0][0] and "-" not in TaTeTi[0][1] and "-" not in TaTeTi[0][2] and "-" not in TaTeTi[1][0] and "-" not in TaTeTi[1][1] and "-" not in TaTeTi[1][2] and "-" not in TaTeTi[2][0] and "-" not in TaTeTi[2][1] and "-" not in TaTeTi[2][2]:
        break
    else:
        TurnoX = True
    # se imprime el tablero cuando inicia y finaliza cada turno utilizando un bucle for doble
    for i in range(len(TaTeTi)):
        for x in range(len(TaTeTi[i])):
            if x == len(TaTeTi[i]) - 1:
                print(TaTeTi[i][x], end=" ")
            else:
                print(TaTeTi[i][x], end=" | ")
        print()
    # inicia turno del jugador con la marca X:
    while TurnoX == True:
        # instruimos que datos ingresar para facilitar la comprencion del funcionamiento:
        print("""
        Turno X
        para marcar el tablero primero selecciona la fila luego la columna:
                 1  2  3 <<-- Columnas
               1 -  -  - 
               2 -  -  - 
               3 -  -  - 
               ^
              filas             """)
        # solicitamos primero la fila:
        fila = input("ingresa la fila: ")
        # validamos informacion en caso de dato invalido:
        while fila != "1" and fila != "2" and fila != "3":
            fila = input("ingresa 1 2 o 3 para determinar la fila: ")
        # se cambia el string por un numero entero para facilitar el uso de la variable dado que utilizamos numeros
        fila = int(fila)
        # se resta el valor para poder pasarlo a los valores dentro de la matriz
        fila -= 1
        # solicitamos la columna a ocupar y realizamos el mismo procedimiento que cuando se solicito la fila:
        columna = input("ingresa la columna: ")
        while columna != "1" and columna != "2" and columna != "3":
            columna = input("ingresa 1 2 o 3 para determinar la columna: ")
        columna = int(columna)
        columna -= 1
        # en caso de que la posicion elegida este ocupada por un jugador:
        while TaTeTi[fila][columna] != "-":
            print("lugar ocupado. Ingresa otro lugar")
            fila = input("ingresa la fila: ")
            while fila != "1" and fila != "2" and fila != "3":
                fila = input("ingresa 1 2 o 3 para determinar la fila: ")
            fila = int(fila)
            fila -= 1
            columna = input("ingresa la columna: ")
            while columna != "1" and columna != "2" and columna != "3":
                columna = input("ingresa 1 2 o 3 para determinar la columna: ")
            columna = int(columna)
            columna -= 1
        TaTeTi[fila][columna] = "X"
        # finalizamos el turno:
        TurnoX = False
    # en caso de que las X Ganen el juego se definen los requisitos:
    if "X" in TaTeTi[0][0] and "X" in TaTeTi[0][1] and "X" in TaTeTi[0][2]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[1][0] and "X" in TaTeTi[1][1] and "X" in TaTeTi[1][2]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[2][0] and "X" in TaTeTi[2][1] and "X" in TaTeTi[2][2]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[0][0] and "X" in TaTeTi[1][0] and "X" in TaTeTi[2][0]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[0][1] and "X" in TaTeTi[1][1] and "X" in TaTeTi[2][1]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[0][2] and "X" in TaTeTi[1][2] and "X" in TaTeTi[2][2]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[0][0] and "X" in TaTeTi[1][1] and "X" in TaTeTi[2][2]:
        print("X GANAN!!")
        break
    if "X" in TaTeTi[0][2] and "X" in TaTeTi[1][1] and "X" in TaTeTi[2][0]:
        print("X GANAN!!")
        break
    if "-" not in TaTeTi[0][0] and "-" not in TaTeTi[0][1] and "-" not in TaTeTi[0][2] and "-" not in TaTeTi[1][0] and "-" not in TaTeTi[1][1] and "-" not in TaTeTi[1][2] and "-" not in TaTeTi[2][0] and "-" not in TaTeTi[2][1] and "-" not in TaTeTi[2][2]:
        break
    else:
        TurnoO = True
    # imprimimos el tablero para el turno rival:
    for i in range(len(TaTeTi)):
        for x in range(len(TaTeTi[i])):
            if x == len(TaTeTi[i]) - 1:
                print(TaTeTi[i][x], end=" ")
            else:
                print(TaTeTi[i][x], end=" | ")
        print()
    # inicia el turno del jugador con la marca O:
    while TurnoO == True:
        print("""
        Turno O
        para marcar el tablero primero selecciona la fila luego la columna:
                1  2  3  <<- columnas
              1 -  -  - 
              2 -  -  - 
              3 -  -  - 
              ^
            filas            """)
        # al igual que con la X se piden los mismos valores y se utilizan las mismas variables:
        fila = input("ingresa la fila: ")
        while fila != "1" and fila != "2" and fila != "3":
            fila = input("ingresa 1 2 o 3 para determinar la fila: ")
        fila = int(fila)
        fila -= 1
        columna = input("ingresa la columna: ")
        while columna != "1" and columna != "2" and columna != "3":
            columna = input("ingresa 1 2 o 3 para determinar la columna: ")
        columna = int(columna)
        columna -= 1
        while TaTeTi[fila][columna] != "-":
            print("lugar ocupado. Ingresa otro lugar")
            fila = input("ingresa la fila: ")
            while fila != "1" and fila != "2" and fila != "3":
                fila = input("ingresa 1 2 o 3 para determinar la fila: ")
            fila = int(fila)
            fila -= 1
            columna = input("ingresa la columna: ")
            while columna != "1" and columna != "2" and columna != "3":
                columna = input("ingresa 1 2 o 3 para determinar la columna: ")
            columna = int(columna)
            columna -= 1
        TaTeTi[fila][columna] = "O"
        TurnoO = False
    # en caso de que las O ganen el juego se definen los parametros:
    if "O" in TaTeTi[0][0] and "O" in TaTeTi[0][1] and "O" in TaTeTi[0][2]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[1][0] and "O" in TaTeTi[1][1] and "O" in TaTeTi[1][2]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[2][0] and "O" in TaTeTi[2][1] and "O" in TaTeTi[2][2]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[0][0] and "O" in TaTeTi[1][0] and "O" in TaTeTi[2][0]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[0][1] and "O" in TaTeTi[1][1] and "O" in TaTeTi[2][1]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[0][2] and "O" in TaTeTi[1][2] and "O" in TaTeTi[2][2]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[0][0] and "O" in TaTeTi[1][1] and "O" in TaTeTi[2][2]:
        print("O GANAN!!")
        break
    if "O" in TaTeTi[0][2] and "O" in TaTeTi[1][1] and "O" in TaTeTi[2][0]:
        print("O GANAN!!")
        break
# la partida llega a su fin.
print("Termino la partida")
for i in range(len(TaTeTi)):
    for x in range(len(TaTeTi[i])):
        if x == len(TaTeTi[i]) - 1:
            print(TaTeTi[i][x], end=" ")
        else:
            print(TaTeTi[i][x], end=" | ")
    print()
