# Actividad 1 #
edad = int(input("por favor ingresa tu edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("eres menor")

# Actividad 2 #
nota = int(input("por favor ingresa tu nota: "))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")

# Actividad 3 #
par = int(input("por favor ingresa un numero para verificar si es par: "))
x = par % 2
if x == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# Actividad 4 #
edad = int(input(
    "por favor ingresa tu edad para ver a que categoria perteneces\n    edad: "))
if edad < 12:
    print("* niño/a: menor de 12 años de edad")
elif edad >= 12 and edad < 18:
    print("* adolescente: tenes entre 12 y 18 años de edad")
elif edad >= 18 and edad < 30:
    print("* adulto/a joven: tenes entre 18 y 30 años de edad")
else:
    print("* adulto/a: tenes 30 o mas años de edad")

# Actividad 5 #
passw = input(
    "crea una contraseña que tenga entre 8 y 14 caracteres\n    contraseña: ")
if len(passw) >= 8 and len(passw) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("por favor, ingrese una contraseña entre 8 y 14 caracteres")

# Actividad 6 #
kWh = int(input(
    "ingrese su consumo mensual de energía eléctrica en kilovatios (kWh)\n     consumo en kWh: "))
if kWh >= 500:
    print("Considere medidas de ahorro energético")
elif kWh > 300:
    print("Consumo alto")
elif kWh > 150 and kWh <= 300:
    print("Consumo medio")
else:
    print("consumo bajo")


# Actividad 7 #
vocal = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")
palabra = input("por favor introduce una frase o palabra: ")
palabra = palabra.lower()
if palabra.endswith(vocal):
    print(f"{palabra}!")
else:
    print(palabra)

# Actividad 8 #
nombre = input("por favor ingresa tu nombre: ")
x = int(input("""
    a continuacion ingrese: 
        1 Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
        2 Si quiere su nombre en minúsculas. Por ejemplo: pedro.
        3 Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
            ingreso: """))
if x == 1:
    nombre = nombre.upper()
elif x == 2:
    nombre = nombre.lower()
elif x == 3:
    nombre = nombre.title()
print(nombre)

# Actividad 9 #
t = float(input("ingrese un numero entre 1 y 10 para ver la magnitud de un terremoto\ny su categoria según la escala de Richter: "))
if t >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
elif t >= 6:
    print("Muy Fuerte (puede causar daños significativos)")
elif t >= 5:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif t >= 4:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif t >= 3:
    print("Leve (ligeramente perceptible)")
else:
    print("Muy leve (imperceptible).")

# Actividad 10 #
print("queres saber en que estacion del año te encuentras?")
H = input("para eso necesitamos saber en que hemisferio te encuentras\ningresa una n para el hemisferio norte\no una s para el hemisferio sur\n   n/s: ")
H = H.lower()
if H == "n":
    mes = int(
        input("ahora por favor ingresa el mes utilizando los numeros del 1 al 12: "))
    dia = int(
        input("para finalizar ingresa el dia utilizando los numeros del 1 al 31: "))
    if mes == 1 or mes == 2 or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
        print("estas en invierno")
    elif mes == 4 or mes == 5 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        print("estas en primavera")
    elif mes == 7 or mes == 8 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("estas en verano")
    elif mes == 10 or mes == 11 or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        print("estas en otoño")
elif H == "s":
    mes = int(
        input("ahora por favor ingresa el mes utilizando los numeros del 1 al 12: "))
    dia = int(
        input("para finalizar ingresa el dia utilizando los numeros del 1 al 31: "))
    if mes == 1 or mes == 2 or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
        print("estas en verano")
    elif mes == 4 or mes == 5 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        print("estas en otoño")
    elif mes == 7 or mes == 8 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("estas en invierno")
    elif mes == 10 or mes == 11 or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        print("estas en primavera")
