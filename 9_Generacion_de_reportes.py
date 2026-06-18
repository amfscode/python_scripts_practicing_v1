#
import csv
ventas = []
with open("ventas_amfs.csv", "r",encoding = "utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas.append(float(fila["venta"]))

# print(ventas)

print(f"Promedio: {sum(ventas)/ len(ventas)}")
print(f"Maximo: {max(ventas)}")
print(f"minimo: {min(ventas)}")
