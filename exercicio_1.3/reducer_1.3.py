#!/usr/bin/python3

import sys

diccionario={} #para poder dejar almacenado el valor mayor de cada clave

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    actualClave = data_mapped[0]
    actualValor = float(data_mapped[1])
    
    if actualClave in diccionario:                       # si la clave ya está en el diccionario
    	if (actualValor) > (diccionario[actualClave]):   # si el valor actual es mayor que el mayor almacenado para esta clave
            diccionario[actualClave]=actualValor         # actualiza el valor almacenado para esta clave con el nuevo mayor   

    else:                                              # si la clave no está en el diccionario
        diccionario[actualClave]=actualValor             # la añade con el valor actual


#una vez acaba de recorrer todas las líneas tenemos almacenado en el diccionario el mayor valor para cada tipo de pago
#recorremos el diccionario imprimiendo clave tabulador valor 	
for key in diccionario:
	print(key, "\t", diccionario[key])
