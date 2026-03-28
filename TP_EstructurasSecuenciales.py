# actividad 1#
print("hola mundo!")

# actividad 2#
nombre = input(
    "bienvenido al trabajo practico de estructuras secuenciales\npor favor ingresa tu nombre: ")
print(f"hola {nombre}!")

# actividad 3#
nombre = input("por favor ingresa nuevamente tu nombre para confirmarlo: ")
apellido = input("ingresa tu apellido: ")
edad = input("ingresa tu edad: ")
pais = input("por favor ingresa el pais donde vivis: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

# actividad 4#
radioC = int(input("A continuacion por favor ingresa el radio de un circulo \npara calcular el area y perimetro del mismo\nradio del circulo: "))
perimetro = 2*3.1416*radioC
area = 3.1416*(radioC)**2
print(
    f"perimetro del circulo: {perimetro:.2f}\narea del circulo: {area:.2f}")

# actividad 5#
segundos = int(input(
    "por favor ingresa una gran cantidad de segundos\npara transformarlas en horas: "))
horas = segundos/3600
print(f"los segundos ingresados equivalen a: {horas:.2f}")

# actividad 6#
x = int(input("ingresa un numero para que creemos su tabla de multiplicacion: "))
x0 = x*0
x1 = x*1
x2 = x*2
x3 = x*3
x4 = x*4
x5 = x*5
x6 = x*6
x7 = x*7
x8 = x*8
x9 = x*9
x10 = x*10
print(f"""
        {x} x 0 = {x0}
        {x} x 1 = {x1}
        {x} x 2 = {x2}
        {x} x 3 = {x3}
        {x} x 4 = {x4}
        {x} x 5 = {x5}
        {x} x 6 = {x6}
        {x} x 7 = {x7}
        {x} x 8 = {x8}
        {x} x 9 = {x9}
        {x} x 10 = {x10}
        """)

# actividad 7#
n1 = int(input("por favor ingresa 2 numeros enteros distintos a 0\npara realizar una suma, resta, division y multiplicacion.\nprimer numero: "))
n2 = int(input("segundo numero: "))
if n1 > n2:
    mult = n1*n2
    div = n1/n2
    rest = n1-n2
    sum = n1+n2
else:
    mult = n2*n1
    div = n2/n1
    rest = n2-n1
    sum = n2+n1
print(f"""
        resultado de la suma: {sum}
        resultado de la resta: {rest}
        resultado de la multiplicacion: {mult}
        resultado de la division: {div}
        """)

# actividad 8 #
peso = float(input(
    "a continuacion te daremos tu indice de masa corporal\npor favor ingresa tu peso: "))
altura = float(input("ahora por favor ingresa tu altura: "))
IMC = peso/altura**2
print(f"tu indice de masa corporal es: {IMC:.1f}")

# actividad 9 #
gradosC = int(input(
    "vamos a convertir una temperatura en grados Celsius a grados Fahrenheit\npor favor ingresa una temperatura en grados celsius: "))
gradosF = (gradosC * 9/5) + 32
print(
    f"ingresaste: {gradosC} grados Celsius\nequivale a: {gradosF} grados Fahrenheit.")

# actividad 10 #
p1 = int(input(
    "vamos a sacar el promedio de 3 numeros\npor favor ingresa el primer numero: "))
p2 = int(input("ingresa el segundo: "))
p3 = int(input("ingresa el tercer y ultimo numero: "))
pT = (p1+p2+p3)/3
print(f"ingresaste: {p1}, {p2} y {p3} el promedio es: {pT:.1f}")
