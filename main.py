from modules.__init__ import Cliente, Menu, Pedido


def imprimir_menu():
    # Esta función imprime el menú de opciones
    print("Seleccione una opción:")
    print("a. Pedidos")
    print("b. Clientes")
    print("c. Menú")
    print("d. Salir")

def calcular_costo_producto():
    # Esta función calcula el costo de un producto
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    unidades = int(input("Ingrese las unidades a solicitar: "))
    costo_total = precio * unidades
    # Imprime el costo total del producto
    print(f"El costo total para {unidades} unidades de {nombre_producto} es: ${costo_total:.2f}")

def seleccionar_opcion():
    # Esta función controla el flujo del programa basado en la opción seleccionada por el usuario
    while True:
        imprimir_menu()
        opcion = input("Ingrese su opción: ").lower()
        
        if opcion == 'a':
            # Si el usuario selecciona 'a', se calcula el costo del producto
            print("Ha seleccionado Pedidos.")
            mostrar_menu_pedidos()
            #calcular_costo_producto()
        elif opcion == 'b':
            # Si el usuario selecciona 'b', se muestra un mensaje para Clientes
            print("Ha seleccionado Clientes.")
            mostrar_clientes()
        elif opcion == 'c':
            # Si el usuario selecciona 'c', se muestra un mensaje para Menú
            print("Ha seleccionado Menú.")
            mostrar_menu_producto()
        elif opcion == 'd':
            # Si el usuario selecciona 'd', se sale del programa
            print("Saliendo del programa.")
            break
        else:
            # Si el usuario ingresa una opción no válida, se muestra un mensaje de error
            print("Opción no válida. Por favor, intente de nuevo.")

def mostrar_clientes():
        # Esta función muestra las opciones para Clientes
        while True:
            print("\nClientes")
            print("1. Agregar Cliente")
            print("2. Eliminar Cliente")
            print("3. Actualizar Cliente")
            print("4. Mostrar Cliente")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                # Si el usuario selecciona '1', se agrega un cliente
                clave = input("Clave: ")
                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                correo_electronico = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                cliente = Cliente(clave, nombre, direccion, correo_electronico, telefono)
                cliente.guardar()
                print("Cliente agregado exitosamente.")
            elif opcion == '2':
                # Si el usuario selecciona '2', se elimina un cliente
                clave = input("Clave: ")
                Cliente.eliminar_cliente(clave)
                print("Cliente eliminado exitosamente.")
            elif opcion == '3':
                # Si el usuario selecciona '3', se actualiza un cliente
                clave = input("Clave: ")
                nombre = input("Nombre (dejar en blanco para no cambiar): ")
                direccion = input("Dirección (dejar en blanco para no cambiar): ")
                correo_electronico = input("Correo Electrónico (dejar en blanco para no cambiar): ")
                telefono = input("Teléfono (dejar en blanco para no cambiar): ")
                Cliente.actualizar_cliente(clave, nombre or None, direccion or None, correo_electronico or None, telefono or None)
                print("Cliente actualizado exitosamente.")
            elif opcion == '4':
                # Si el usuario selecciona '4', se muestra un cliente
                clave = input("Clave: ")
                Cliente.mostrar_datos(clave)
            elif opcion == '5':
                # Si el usuario selecciona '5', se sale de la función
                break
            else:
                print("Opción no válida. Intente de nuevo.")
def mostrar_menu_pedidos():
    # Esta función muestra las opciones para Pedidos
    while True:
        print("\nMenú de Pedidos")
        print("1. Crear Pedido")
        print("2. Cancelar Pedido")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cliente_id = input("ID del Cliente: ")
            producto_id = input("ID del Producto: ")
            Pedido.crear_pedido(cliente_id, producto_id)
        elif opcion == '2':
            pedido_id = input("ID del Pedido: ")
            Pedido.cancelar_pedido(pedido_id)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
def mostrar_menu_producto():
        # Esta función muestra las opciones para Productos
        while True:
            print("\nMenú de Productos")
            print("1. Agregar Producto")
            print("2. Eliminar Producto")
            print("3. Actualizar Producto")
            print("4. Mostrar Productos")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                clave = input("Clave: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                Menu.agregar_producto(clave, nombre, precio)
            elif opcion == '2':
                clave = input("Clave: ")
                Menu.eliminar_producto(clave)
            elif opcion == '3':
                clave = input("Clave: ")
                nombre = input("Nombre (dejar en blanco para no cambiar): ")
                precio = input("Precio (dejar en blanco para no cambiar): ")
                Menu.actualizar_producto(clave, nombre or None, float(precio) if precio else None)
            elif opcion == '4':
                Menu.mostrar_productos()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
# Llamada a la función para iniciar el programa
seleccionar_opcion()