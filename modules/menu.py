import sqlite3

class Menu:
    @staticmethod
    def agregar_producto(clave, nombre, precio):
        # Función para agregar un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO menu (clave, nombre, precio)
                VALUES (?, ?, ?)
            ''', (clave, nombre, precio))
            conn.commit()
            print("Producto agregado exitosamente.")

    @staticmethod
    def eliminar_producto(clave):
        # Función para eliminar un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM menu WHERE clave = ?', (clave,))
            conn.commit()
            print("Producto eliminado exitosamente.")

    @staticmethod
    def actualizar_producto(clave, nombre=None, precio=None):
        # Función para actualizar los datos de un producto
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            if nombre and precio:
                cursor.execute('''
                    UPDATE menu
                    SET nombre = ?, precio = ?
                    WHERE clave = ?
                ''', (nombre, precio, clave))
            elif nombre:
                cursor.execute('''
                    UPDATE menu
                    SET nombre = ?
                    WHERE clave = ?
                ''', (nombre, clave))
            elif precio:
                cursor.execute('''
                    UPDATE menu
                    SET precio = ?
                    WHERE clave = ?
                ''', (precio, clave))
            conn.commit()
            print("Producto actualizado exitosamente.")

    @staticmethod
    def mostrar_productos():
        # Función para mostrar todos los productos
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM menu')
            productos = cursor.fetchall()
            for producto in productos:
                print(producto)