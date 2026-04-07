# actividad 10
#
# creamos una lista con los dias de la semana, la posicion de los mismos es correlativa
# a la lista que contiene las ventas de cada dia
#
diasSemana = ["Lunes", "Martes", "Miercoles",
              "Jueves", "Viernes", "Sabado", "Domingo"]
# la siguiente lista contiene las ventas realizadas cada dia de la semana
ventas = [["sv", "sv", "cigarros", "aceite"], ["alfajor", "alfajor", "paty", "fideos"], ["paty", "paty", "leche", "sv"], [
    "cigarros", "sv", "sv", "pan"], ["alfajor", "alfajor", "sv", "sv"], ["pan", "leche", "huevos", "sv"], ["sv", "sv", "sv", "sv"]]
# las variables conteoVentas_x se utilizan para ver el total de ventas de cada producto en la semana
ArticuloMasVendido = 0
conteoVentas_cigarros = 0
conteoVentas_aceite = 0
conteoVentas_alfajor = 0
conteoVentas_paty = 0
conteoVentas_fideos = 0
conteoVentas_leche = 0
conteoVentas_pan = 0
conteoVentas_Huevos = 0
conteoMasVentas = 0
DiaMasVentas = 0
productoDeLaSemana = ""
# se utiliza el bucle for para contar cada articulo vendido en la semana
# dentro del mismo se ejecuta un contador para verificar cual articulo fue el mas vendido en la semana
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "cigarros":
            conteoVentas_cigarros += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "aceite":
            conteoVentas_aceite += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "alfajor":
            conteoVentas_alfajor += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "paty":
            conteoVentas_paty += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "fideos":
            conteoVentas_fideos += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "leche":
            conteoVentas_leche += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "pan":
            conteoVentas_pan += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador
for i in ventas:
    contadorArticulo = 0
    for contador in i:
        if contador == "huevos":
            conteoVentas_Huevos += 1
            contadorArticulo += 1
            if contadorArticulo > ArticuloMasVendido:
                ArticuloMasVendido = contadorArticulo
                productoDeLaSemana = contador

# el siguiente bucle busca el dia con mayor cantidad de ventas:
for i in range(len(ventas)):
    MasVentas = 0
    for x in range(len(ventas[i])):
        if "sv" != ventas[i][x]:
            MasVentas += 1
            if MasVentas > conteoMasVentas:
                DiaMasVentas = i
                conteoMasVentas = MasVentas
# pasamos a imprimir los resultados:
print(f"""
articulos vendidos en la semana: 

paquetes de cigarrillos: {conteoVentas_cigarros}
cajas de aceite: {conteoVentas_aceite}
cajas de alfajor: {conteoVentas_alfajor}
cajas de paty: {conteoVentas_paty}
paquetes de fideo: {conteoVentas_fideos}
cartones de leche: {conteoVentas_leche}
bolsas de pan x 20kg: {conteoVentas_pan}
maples de huevos: {conteoVentas_Huevos}

mejor dia de la semana: {diasSemana[DiaMasVentas]}
producto mas vendido en la semana : {productoDeLaSemana}
""")
