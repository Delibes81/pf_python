import sqlite3

class Cliente:
    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono


    def guardar(self):
        # Guarda los datos del cliente en la base de datos
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clientes (clave, nombre, direccion, correo_electronico, telefono)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.clave, self.nombre, self.direccion, self.correo_electronico, self.telefono))
            conn.commit()

    @staticmethod
    def eliminar_cliente(clave):
        # Elimina un cliente de la base de datos
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM clientes WHERE clave = ?', (clave,))
            conn.commit()

    @staticmethod
    def actualizar_cliente(clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        # Actualiza los datos de un cliente en la base de datos
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            if nombre:
                cursor.execute('UPDATE clientes SET nombre = ? WHERE clave = ?', (nombre, clave))
            if direccion:
                cursor.execute('UPDATE clientes SET direccion = ? WHERE clave = ?', (direccion, clave))
            if correo_electronico:
                cursor.execute('UPDATE clientes SET correo_electronico = ? WHERE clave = ?', (correo_electronico, clave))
            if telefono:
                cursor.execute('UPDATE clientes SET telefono = ? WHERE clave = ?', (telefono, clave))
            conn.commit()

    @staticmethod
    def mostrar_datos(clave):
        # Muestra los datos de un cliente
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clientes WHERE clave = ?', (clave,))
            cliente = cursor.fetchone()
            if cliente:
                print(f"Clave: {cliente[0]}")
                print(f"Nombre: {cliente[1]}")
                print(f"Dirección: {cliente[2]}")
                print(f"Correo Electrónico: {cliente[3]}")
                print(f"Teléfono: {cliente[4]}")
            else:
                print("El cliente no existe.")
                