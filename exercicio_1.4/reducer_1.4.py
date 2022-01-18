#!/usr/bin/python3

import sys

lista=[]   #lista donde iremos almacenando las ventas con el valor máximo, si es que hay más de una con valor máximo repetido
maxValor = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 4:  #atención que en este caso tenemos que recibir 4 no 2
        # Something has gone wrong. Skip this line.
        continue
    
    actualFecha = data_mapped[0]
    actualHora = data_mapped[1]
    actualStore = data_mapped[2]
    actualValor = float(data_mapped[3])
    
    if actualValor > maxValor:   #si el valor de la venta actual es mayor que el máximo almacenado
        maxValor=actualValor     #actualizamos el valor máximo almacenado
        lista=[]                 #vaciamos la lista de ventas con valor máximo      
        lista.append({'fecha':actualFecha, 'hora':actualHora, 'tienda':actualStore, 'valor':actualValor}) #añadimos la primera venta con el nuevo valor máximo a la lista
    
    elif actualValor == maxValor:    #si aparece otra venta con el mismo valor máximo
        lista.append({'fecha':actualFecha, 'hora':actualHora, 'tienda':actualStore, 'valor':actualValor}) #añadimos la venta a la lista de ventas con valor máximo


#una vez recorrido todo el fichero sacamos el resultado de ventas con valor máximo repetido
#usando como clave la concatenación con guión bajo de fecha_hora_tienda para identificar cada venta
for dicc in lista:
    print(f"{dicc['fecha']}_{dicc['hora']}_{dicc['tienda']}\t{dicc['valor']}")


