# Conceptos  APIs JSON HTTP requests

import requests         #para hacer peticiones HTTP a APIs y sitios web
url = "https://jsonplaceholder.typicode.com/users" # # URL de la API que queremos consultar.
respuesta = requests.get(url)       # # Realiza una petición GET a la URL.
####print(respuesta.text)
if respuesta.status_code == 200:    #Verificar si la petición fue exitosa.# El código 200 significa "OK".
                                    # Conviertir el JSON recibido en objetos Python.
    usuarios = respuesta.json()     # En este caso será una lista de diccionarios.
    for usario in usuarios:
        print(usario["name"])
# ___________________________________
# v2
try:
    respuesta = requests.get(url, timeout=5)  # # Realiza una petición GET a la URL.

    respuesta.raise_for_status()  # Verificar si la petición fue exitosa.
    usuarios = respuesta.json()   # Conviertir el JSON recibido en objetos Python.
    for usario in usuarios:
        print(
            f"ID: {usario["id"]} | "
            f"Nombre: {usario["name"]} | "
            f"Email: {usario["email"]}"
        )
except requests.exceptions.RequestException as e  :
    print(f"Error: {e} {type(e)}")