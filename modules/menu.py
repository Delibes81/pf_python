import sqlite3
class Menu:
    def __init__(self):
        # Inicializa el diccionario de productos
        self.productos = {}

    def mostrar_productos(self):
        # Muestra los productos del menú
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()
            for producto in productos:
                print(f"Clave: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")

    def agregar_producto(self, clave, nombre, precio):
        # Función para agregar un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO productos (clave, nombre, precio)
                VALUES (?, ?, ?)
            ''', (clave, nombre, precio))
            conn.commit()
            print("Producto agregado exitosamente.")


    def eliminar_producto(self, clave):
        # Función para eliminar un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM productos WHERE clave = ?', (clave,))
            conn.commit()
            print("Producto eliminado exitosamente.")

    def actualizar_producto(self, clave, nombre=None, precio=None):
        # Función para actualizar los datos de un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            if nombre:
                cursor.execute('UPDATE productos SET nombre = ? WHERE clave = ?', (nombre, clave))
            if precio:
                cursor.execute('UPDATE productos SET precio = ? WHERE clave = ?', (precio, clave))
            conn.commit()
            print("Producto actualizado exitosamente.")
