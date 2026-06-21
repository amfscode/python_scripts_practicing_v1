# Contexto real - Un usuario puede tener varios roles
usuario = {
    1: {
        "nombre":"Fiorela",
        "roles":["admin","editor"]
        },
    2: {
        "nombre":"ALex",
        "roles":["viewer"]
        },
    3: {
        "nombre": "Kiara",
        "roles": "editor"
        }
}

permisos = {
    "admin":{
        "crear",
        "editar",
        "eliminar",
        "ver"
        },
    "editor":{
        "Editar",
        "ver"
        },
    "viewer":{
        "ver"
        }
}

for id_user,datos in usuario.items():
    print(datos["nombre"], ">>>", datos["roles"])

