#!/usr/bin/python3

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 4 (cost) and any anotherone
# We need to write them out to standard output, separated by a tab

import sys

conta=0 #para clave de cada línea de salida usaremos por ejemplo un contador
for line in sys.stdin:
    data = line.strip().split("\t")
    if len (data) != 6: continue   #añadimos esta condición para que en vez de dar error continue con la siguiente línea si encuentra alguna línea que no cumpla las características
    date, time, store, item, cost, payment = data
    print(f'{conta}\t{cost}')  # ahora preparamos la salida para luego trabajar con ventas por tipo de pago
    conta+=1
    
