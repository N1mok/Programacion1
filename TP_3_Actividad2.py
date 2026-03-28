#############################################################################
#   Actividad 2 /// “Acceso al Campus y Menú Seguro”\\\                     #
# objetivo:  Login con intentos + menú de acciones con validación estricta. #
#############################################################################
#
# establecemos datos de usuario
usuario_correcto = "alumno"
clave_correcta = "python123"
estado_inscripcion = "inscripto"
intentosMaximos = 3
intentos = 0
print("""         Bienvenido!
para ingresar al campus debes ingresar correctamente
tu usuario y contraseña.
""")
# solicitamos los datos para permitir o denegar el ingreso
usuario = input("   por favor ingresa tu usuario: ")
clave = input("   por favor ingresa tu clave: ")
intentosMaximos -= 1
intentos += 1
while usuario_correcto != usuario and clave_correcta != clave:
    print(f"""
            intento {intentos}/3 -
            usuario: {usuario} - clave:xxxx
            error: credenciales invalidas
            si llegas a 3 intentos fallidos se bloqueara
        """)
    intentosMaximos -= 1
    intentos += 1
    usuario = input("   por favor ingresa tu usuario: ")
    clave = input("   por favor ingresa tu clave: ")
    # en caso de que falle 3 intentos
    if intentosMaximos == 0:
        print(f"""
            intento {intentos}/3 - 
            usuario: {usuario} - clave:xxxx
            Cuenta Bloqueada
            """)
        break


# ingreso exitoso

if usuario_correcto == usuario and clave_correcta == clave:
    print(f"""
    intento: {intentos}/3 - 
    usuario: {usuario} - clave : {clave}
    acceso concedido
    """)
    inicio_secion = True
# creamos el menu de inicio de sesion
while inicio_secion == True:
    seleccion_menu = input("""
        1.- Ver estado de inscripción
        2.- Realizar cambio de clave
        3.- Mostrar mensaje motivacional
        4.- Salir
            ingresa la opcion deseada: """)
    # validacion por isdigit
    while seleccion_menu.isdigit() == False:
        seleccion_menu = input("""
        ingresa un numero entre 1 y 4 para realizar la seleccion en el menu:
        1.- Ver estado de inscripción
        2.- Realizar cambio de clave
        3.- Mostrar mensaje motivacional
        4.- Salir
            ingresa la opcion deseada: """)
    seleccion_menu = int(seleccion_menu)
    match seleccion_menu:
        case 1:
            print(f"\n                 {estado_inscripcion}")
        case 2:
            # cambio de clave
            clave_nueva = input(
                "ingrese una clave con mas de 6 caracteres\n  clave:")
            # validacion de clave usando .len
            while len(clave_nueva) < 6:
                clave_nueva = input(
                    "por favor ingresa una clave mas larga: ")
            confirmar_clave = input(
                "vuelve a ingresar la misma clave para confirmar\n  clave: ")
            if confirmar_clave == clave_nueva:
                print("cambio de clave exitoso")
                confirmar_clave = clave_correcta
        case 3:
            print("arriba rocky! MICKY TE AMA!!")
        case 4:
            print("  adios!")
            inicio_secion = False
        case _:
            print("    error:Opcion fuera del rango")
