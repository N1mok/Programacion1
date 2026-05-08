booleano = [True, False]


def opcion():
    print("""
        menu de opciones.
        1- conjuncion
        2- disyuncion
        3- negacion
        """)


print("bienvenido al generador de tablas de verdad: ")
while True:
    opcion()
    seleccion = input(" opcion seleccionada:")
    while seleccion.isdigit() == False:
        print("error: no ingreso una opcion valida")
        opcion()
        seleccion = input(" opcion seleccionada:")
    if seleccion == "1":
        print(" conjuncion: tabla de verdad ")
        print("A\tB\tA and B")
        print("-"*25)
        for valor1 in booleano:
            for valor2 in booleano:
                print(f" {valor1}\t{valor2}\t{valor1 and valor2}")
    elif seleccion == "2":
        print(" disyuncion: tabla de verdad ")
        print("-"*25)
        for valor1 in booleano:
            for valor2 in booleano:
                print(f" {valor1} | {valor2} | {valor1 or valor2}")
    elif seleccion == "3":
        print(" tabla de verdad negando A")
        print("¬ A  |   B   | ¬A and B")
        for valor1 in booleano:
            for valor2 in booleano:
                print(f" {not valor1}\t{valor2}\t{valor1 or valor2}")
