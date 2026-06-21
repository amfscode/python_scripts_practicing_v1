import csv
acumilador_total = 0
with open("ventas_amfs.csv","r",encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        acumilador_total += float(fila["monto"])

print(f"\nTotal_vendido:{acumilador_total}\n")
