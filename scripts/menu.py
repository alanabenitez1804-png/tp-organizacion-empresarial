from analisis_ventas import *

def mostrar_menu():
    print("-"*30)
    print("    CONSULTAS DE VENTAS")
    print("-"*30)
    print("MENU")
    print(" 1- Búsqueda")
    print(" 2- Ventas Totales (por categoría)")
    print(" 3- Producto más vendido")
    print(" 4- Ventas mensuales")
    print(" 5- Generar archivo .txt + gráficos + tablas")
    print(" 6- Salir")

while True:
    """utiliza la funcion menu principal, para ser mas modular"""
    mostrar_menu()
    opcion = input('\nIngrese una opción del menú: ')
    match opcion:
        case "1":
            buscador()
        case "2":
            ventas_totales_por_categoria()
        case "3":
            ventas_producto = producto_mas_vendido()
            mayor_vendido = max(ventas_producto, key=ventas_producto.get)
            print(f"\nEl producto más vendido es {mayor_vendido}, con {ventas_producto[mayor_vendido]} unidades vendidas.")
        case "4":
            imprimir_ventas_por_mes(ventas_por_mes())
        case "5":
            generar_archivos()
        case "6":
            print('\nGracias por visitarnos!! Nos vemos la próxima\n')
            break
        case _:
            print("Opción inválida. Intente nuevamente")