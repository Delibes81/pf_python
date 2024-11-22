class Pedido:
    def __init__(self):
        # Inicializa el diccionario de pedidos
        self.pedidos = {}

    def mostrar_pedidos(self):
        # Muestra los pedidos
        for pedido_id, datos in self.pedidos.items():
            print(f"Pedido ID: {pedido_id}, Cliente: {datos['cliente']}, Producto: {datos['producto']}, Precio: ${datos['precio']:.2f}")

    def crear_pedido(self, pedido_id, cliente, producto, precio):
        # Función para crear un pedido
        pass

    def cancelar_pedido(self, pedido_id):
        # Función para cancelar un pedido
        pass

