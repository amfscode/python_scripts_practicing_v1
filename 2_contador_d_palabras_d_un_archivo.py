from collections import Counter # Counter, contar cuántas veces aparece cada elemento.

with open("frases_amfs.txt","r",  encoding = "utf-8") as archivo:
    contenido = archivo.read().lower()  # lee y minusculas
palabras = contenido.split()            #['python', 'es', 'genial.', 'python'....
print(palabras)
contador = Counter(palabras)            # {'python': 2,'es': 2,.....
for palabra, frecuencia in contador.most_common(): # (10) = las 10 mas repetitivas
    print(palabra, frecuencia)          # palabra =  pythony y frecuencia = 2