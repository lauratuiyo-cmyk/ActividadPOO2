class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self.precio -= self.precio * (porcentaje / 100)
        else:
            print("Descuento no válido")

    def mostrar_informacion(self):
        print("Producto:", self.nombre)
        print("Precio: $", self.precio)


# Programa principal
producto1 = Producto("Laptop", 15000)

print("ANTES:")
producto1.mostrar_informacion()

producto1.aplicar_descuento(20)

print("\nDESPUÉS:")
producto1.mostrar_informacion()
