
class inventario:
    def __init__(self):
        self.productos = {
            "laptop"    : 10,
            "Mouse"     : 25,
            "Teclado"   : 15
            }
    def mostrar_inventario(self):
        print("\n--- Inventario ---")

        for producto, stock in self.productos.items():
            print(f"{producto.capitalize()}: {stock}")

    def vender_producto(self):

        producto = input("Producto vendido: ").lower()

        if producto not in self.productos:
            print("Producto no encontrado")
            return

        cantidad = int(input("Cantidad vendido"))
        if cantidad > self.productos[producto]:
            print("Stock infuciente")
            return

        self.productos[producto] -= cantidad
        print("Venta registrada")

    def agragar_stock(self):
        contador = 0
        for producto, stock in self.productos.items():
            contador += 1
            print(f"\n Producto {contador}: {producto.capitalize()}: Stock {stock}")

        producto = input("Agregar producto: ").capitalize()

        if producto not in self.productos:
            print("Producto no encontrado")
            return

        cantidad = int(input("Cantidad a agregar: "))
        self.productos[producto] += cantidad
        print("Stock actualizado")

while True:
    print("\n1. Ver inventario")
    print("2. Vender producto")
    print("3. Agregar stock")
    print("4. Salir")

    try:
        opcion = int(input("Opcion: "))

        match opcion:
            case 1:
                inventario.mostrar_inventario()

            case 2:
                inventario.vender_producto()

            case 3:
                inventario.agragar_stock()

            case 4:
                print("Programa finalizado")
                break

            case _:
                print("opcion invalida")

    except ValueError:
        print("Ingresa un numero valido unicamente")


