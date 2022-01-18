#!/usr/bin/python3

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 3 (item description) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len (data) != 6: continue  #añadimos esta condición para que en vez de dar error continue con la siguiente línea si encuentra alguna línea que no cumpla las características
    date, time, store, item, cost, payment = data
    print(f'{item}\t{cost}')  # ahora preparamos la salida para luego calcular el valor total por categoría (item description)
