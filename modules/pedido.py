import sqlite3
import os
import time

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
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            ticket_content = f"""
            Ticket de Pedido
            ----------------
            Cliente: {cliente_nombre}
            Producto: {producto_nombre}
            Precio: {precio}
            Hora: {timestamp}
            """
            # Crear la carpeta 'tickets' si no existe
            ticket_dir = os.path.join(os.getcwd(), 'tickets')
            if not os.path.exists(ticket_dir):
                os.makedirs(ticket_dir)

            # Obtener el número consecutivo para el nombre del archivo
            existing_files = [f for f in os.listdir(ticket_dir) if f.startswith(f'ticket_{cliente_id}_{producto_id}_') and f.endswith('.txt')]
            consecutive_number = len(existing_files) + 1

            ticket_path = os.path.join(ticket_dir, f'ticket_{cliente_id}_{producto_id}_{consecutive_number}.txt')
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

