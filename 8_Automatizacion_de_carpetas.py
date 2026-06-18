# Sistema de archivos, Automatización
# Encontrar archivo PDF
import os
ruta = "E:/"

for archivo in os.listdir(ruta):
    if archivo.endswith(".pdf"):
        print("PDF Encontrado: ", archivo)
