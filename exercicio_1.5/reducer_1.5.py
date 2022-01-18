#!/usr/bin/python3

import sys

# Loop around the data
# It will be in the format key\tval
# Where key is a counter, val is the sale amount

totalVentas = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    valorActual = data_mapped[1]
    valorActual = float(valorActual)    #parseamos a float
    valorActual = round(valorActual,2)  #redondeamos a 2 decimales
    
    totalVentas += valorActual
    totalVentas = round(totalVentas,2)


# una vez finalizada la iteración devolvemos la salida:
print("total_ventas\t", totalVentas)
