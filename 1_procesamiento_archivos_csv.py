# CSV-Comma-Separated Values (Valores Separados por Comas)
# Es uno de los formatos más utilizados para intercambiar datos entre sistemas, hojas de cálculo (o excel) y bases de datos.


import csv
acu_ventas_totales = 0
#apertura y cierre del archivo.
with open("ventas_amfs.csv","r", encoding = "utf-8") as archivo: # "r"=read
# with open(r"E:\Datos\ventas.csv", "r", encoding="utf-8") as archivo: # r=raw strins
    lector = csv.DictReader(archivo)
    for fila in lector:
        acu_ventas_totales += float(fila["monto"])
print(f"Total vendido: {acu_ventas_totales}")
