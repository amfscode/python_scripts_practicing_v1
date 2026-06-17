#
import os
import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

# Ejecuta una consulta SQL
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
print(os.path.abspath("empresa.db"))

cursor.execute("SELECT * FROM Empleados") #imprime datos
for fila in cursor.fetchall(): # Obtiene todas las filas
    print(fila)
conexion.close()