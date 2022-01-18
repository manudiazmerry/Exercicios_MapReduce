#!/usr/bin/python3

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the method of payment, val is the sale amount
#
# All the sales for a particular method of payment will be presented,
# then the key will change and we'll be dealing with the next method of payment

#esto funciona porque el mapeo hace un sort
#es decir que el fichero que devuelve está ordenado por las claves
#va sumando para una clave y cuando encuentra línea con nueva clave reinicia el total

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)    #parseamos a float
    thisSale = round(thisSale,2)  #redondeamos a 2 decimales

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", salesTotal)
        #oldKey = thisKey;  # creo que sobra esta liña ... bien creido, no es necesaria *
        salesTotal = 0

    oldKey = thisKey # * porque ya actualiza aquí en cada iteración
    salesTotal += thisSale
    salesTotal = round(salesTotal,2)

# Escribe o último par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey, "\t", salesTotal)
