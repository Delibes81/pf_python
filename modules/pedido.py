import sqlite3
class Pedido:
    def __init__(self):
        # Inicializa el diccionario de pedidos
        self.pedidos = {}

    def mostrar_pedidos():
        # Muestra los pedidos
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM pedidos')
            pedidos = cursor.fetchall()
            for pedido in pedidos:
                print(f"Pedido ID: {pedido[0]}, Cliente: {pedido[1]}, Producto: {pedido[2]}, Precio: ${pedido[3]:.2f}")

    def crear_pedido(cliente, producto, precio):
        # Crea un pedido
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pedidos (cliente, producto, precio)
                VALUES (?, ?, ?)
            ''', (cliente, producto, precio))
            conn.commit()
            print("Pedido creado exitosamente.")

    def cancelar_pedido(pedido_id):
        # Cancela un pedido
        with sqlite3.connect('happyburger.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pedidos WHERE pedido_id = ?', (pedido_id,))
            conn.commit()
            print("Pedido cancelado exitosamente.")

