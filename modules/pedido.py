import sqlite3
import os

class Pedido:
    @staticmethod
    def crear_pedido(cliente_id, producto_id):
        # Crea un pedido
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            
            # Obtener el nombre del cliente
            cursor.execute('SELECT nombre FROM clientes WHERE clave = ?', (cliente_id,))
            cliente = cursor.fetchone()
            if not cliente:
                print("Cliente no encontrado.")
                return
            cliente_nombre = cliente[0]
            
            # Obtener el nombre y precio del producto
            cursor.execute('SELECT nombre, precio FROM menu WHERE clave = ?', (producto_id,))
            producto = cursor.fetchone()
            if not producto:
                print("Producto no encontrado.")
                return
            producto_nombre, precio = producto
            
            # Insertar el registro en la tabla pedidos
            cursor.execute('''
                INSERT INTO pedidos (cliente, producto, precio)
                VALUES (?, ?, ?)
            ''', (cliente_nombre, producto_nombre, precio))
            conn.commit()
            print("Pedido creado exitosamente.")

             # Simular la impresión de un ticket
            ticket_content = f"""
            Ticket de Pedido
            ----------------
            Cliente: {cliente_nombre}
            Producto: {producto_nombre}
            Precio: {precio}
            """
            ticket_path = os.path.join(os.getcwd(), f'ticket_{cliente_id}_{producto_id}.txt')
            with open(ticket_path, 'w') as ticket_file:
                ticket_file.write(ticket_content)
            print(f"Ticket generado: {ticket_path}")


    @staticmethod
    def cancelar_pedido(pedido_id):
        # Cancela un pedido
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pedidos WHERE pedido = ?', (pedido_id,))
            conn.commit()
            print("Pedido cancelado exitosamente.")

