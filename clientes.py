class Cliente:
    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        # Inicializa los atributos del cliente
        self.datos = {
            'clave': clave,
            'nombre': nombre,
            'direccion': direccion,
            'correo_electronico': correo_electronico,
            'telefono': telefono
        }

    def mostrar_datos(self):
        # Muestra los datos del cliente
        for clave, valor in self.datos.items():
            print(f"{clave.capitalize()}: {valor}")

    def agregar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        # Función para agregar un cliente
        pass

    def eliminar_cliente(self, clave):
        # Función para eliminar un cliente
        pass

    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        # Función para actualizar los datos de un cliente
        pass