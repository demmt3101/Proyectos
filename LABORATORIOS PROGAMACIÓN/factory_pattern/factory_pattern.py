# Clase base (interfaz en este caso)
class Productos:
    def operacion(self):
        pass

# Clases concretas que heredan de la clase base
class ProductoA(Productos):
    def operacion(self):
        print("Producto A")

class ProductoB(Productos):
    def operacion(self):
        print("Producto B")

class ProductoC(Productos):
    def operacion(self):
        print("Producto C")

# Clase fábrica
class FabricaProductos:
    @staticmethod
    def crear_producto(tipo):
        if tipo == "A":
            return ProductoA()
        elif tipo == "B":
            return ProductoB()
        elif tipo == "C":
            return ProductoC()        
        else:
            raise ValueError("Tipo de producto desconocido")

# Uso del patrón Factory
producto1 = FabricaProductos.crear_producto("A")
producto1.operacion()  # Salida: "Operación del Producto A"

producto2 = FabricaProductos.crear_producto("B")
producto2.operacion()  # Salida: "Operación del Producto B"

producto3 = FabricaProductos.crear_producto("C")
producto3.operacion()