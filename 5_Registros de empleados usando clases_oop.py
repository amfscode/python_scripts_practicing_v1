# OOP

class Empleado:         #class crea una clase
    def __init__(self,nombre,salario):  #self representa al objeto que se está creando
        self.nombre = nombre
        self.salario = salario
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")

Empleado1 = Empleado("Carlos", 3500)
Empleado1.mostrar_info()

# Conceptos:Clases, Objetos, Encapsulamiento
