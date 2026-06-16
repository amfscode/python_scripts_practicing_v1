
import re       ##re (Regular Expressions)

# correo = input("ingrese su correo: ")
correo = "juan.perez@gmail.com"

patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"    #expresión regular (Regex)

print("Correo válido" if re.match(patron, correo) else "Correo inválido")

# if re.match(patron, correo):
#     print("correo valido")
# else:
#     print("correo invalido")

# Con Regex puedes definir exactamente qué estructura debe tener el texto.

texto = "hola"
print("Cuencide" if re.match(r"ho", texto) else "Sin cuencidencia")

# __________________________
# re.search() Busca el patrón en cualquier parte del texto
texto = "mi correo es juan@gmail.com"
if re.search(r"gmail", texto):
    print("Encontrado")

# re.findall() Devuelve todas las coincidencias.
texto = "Python 3 Java 8 C++ 20"
numeros = re.findall(r"\d+", texto)
print(numeros)

# re.sub() Reemplaza texto
texto = "Hola Juan"
nuevo = re.sub(r"Juan", "Pedro", texto)
print(nuevo)