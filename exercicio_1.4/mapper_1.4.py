#!/usr/bin/python3

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# Como vamos a buscar la venta de máximo valor
# y seguramente haya varias ventas con ese valor máximo repetido
# obtendremos varios resultados y para diferenciarlos necesitaremos
# varios campos para que identifiquen de manera única cada venta
# una clave única candidata podría ser fecha+hora+tienda
# no creo que en una misma tienda se hagan 2 ventas simultaneas


import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len (data) != 6:     #añadimos esta condición para que en vez de dar error continue con la siguiente línea si encuentra alguna línea que no cumpla las características
        continue
    date, time, store, item, cost, payment = data
    # preparamos la salida para luego trabajar con (fecha, hora, tienda) y valor
    print(f'{date}\t{time}\t{store}\t{cost}')
