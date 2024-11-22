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
            calcular_costo_producto()
        elif opcion == 'b':
            # Si el usuario selecciona 'b', se muestra un mensaje para Clientes
            print("Ha seleccionado Clientes.")
        elif opcion == 'c':
            # Si el usuario selecciona 'c', se muestra un mensaje para Menú
            print("Ha seleccionado Menú.")
        elif opcion == 'd':
            # Si el usuario selecciona 'd', se sale del programa
            print("Saliendo del programa.")
            break
        else:
            # Si el usuario ingresa una opción no válida, se muestra un mensaje de error
            print("Opción no válida. Por favor, intente de nuevo.")

# Llamada a la función para iniciar el programa
seleccionar_opcion()