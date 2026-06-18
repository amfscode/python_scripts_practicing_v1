# Base de datos
import os
import sqlite3

conexion = sqlite3.connect("EmpresaAMFS.db")
cursor = conexion.cursor()

# Ejecuta una consulta SQL en CRUD
cursor.execute("""
CREATE TABLE IF NOT EXISTS Empleados(
               id INTEGER PRIMARY KEY,
               nombre TEXT,
               salario REAL
               )
""")

# agrega informacion
cursor.execute(
    "INSERT INTO Empleados(nombre, salario) VALUES (?, ?)",
    ("Fiorela", 4500)
)

conexion.commit()       # Guarda los cambios

 # imprime la ruta del archivo .db
print(os.path.abspath("EmpresaAMFS.db"))

cursor.execute("SELECT * FROM Empleados") #imprime datos
for fila in cursor.fetchall(): # Obtiene todas las filas
    print(fila)
conexion.close()