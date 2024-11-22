class Menu:
    def __init__(self):
        # Inicializa el diccionario de productos
        self.productos = {}

    def mostrar_productos(self):
        # Muestra los productos del menú
        for clave, datos in self.productos.items():
            print(f"Clave: {clave}, Nombre: {datos['nombre']}, Precio: ${datos['precio']:.2f}")

    def agregar_producto(self, clave, nombre, precio):
        # Función para agregar un producto
        pass

    def eliminar_producto(self, clave):
        # Función para eliminar un producto
        pass

    def actualizar_producto(self, clave, nombre=None, precio=None):
        # Función para actualizar los datos de un producto
        pass
