import csv
import os

# Programa de análisis de ventas usando el dataset de Kaggle:
# https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset
# Funcionalidades:
# 1. Buscar coincidencias de productos por categoría
# 2. Calcular ventas totales por categoría
# 3. Encontrar el producto más vendido
# 4. Calcular ventas por mes y detectar el mes con más ventas
# 5. Guardar los datos en un archivo .txt

ARCHIVO_CSV = "../datos/retail_sales_dataset.csv"
CARPETA_SALIDA = "../resultados"
ARCHIVO_SALIDA = os.path.join(CARPETA_SALIDA, "resumen_ventas.txt")

def lectura():
    try:
        """Lee el archivo CSV y devuelve un diccionario."""
        with open(ARCHIVO_CSV, "r", encoding="utf-8-sig") as archivo:
            """Guardamos los datos en una list(), ya que al llegar al return la funcion, el archivo se cierra"""
            return list(csv.DictReader(archivo))

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después


def ventas_totales_por_categoria():
    """Calcula el total de ventas de una categoría ingresada por el usuario."""
    categoria = input("\nIngrese una categoría (Beauty, Clothing o Electronics): ").capitalize()
    venta_total = 0
   
    """LLamamos a la funcion lectura() y guardamos los datos en una variable"""
    lector = lectura()

    for fila in lector:
        if fila["Product Category"] == categoria:
            cantidad = int(fila["Quantity"])
            precio = float(fila["Price per Unit"])
            subtotal = cantidad * precio
            venta_total += subtotal
    
    print(f"\nLas ventas totales de {categoria} fueron: ${venta_total:,.2f}")

def producto_mas_vendido():
    """Encuentra la categoría de producto con mayor cantidad de ventas."""
    ventas_producto = {}
    
    lector = lectura()

    for fila in lector:
        producto = fila["Product Category"]
        if producto not in ventas_producto:
            ventas_producto[producto] = 0
        ventas_producto[producto] += int(fila["Quantity"])

    return ventas_producto

def ventas_por_mes():
    """Calcula las ventas totales por mes y muestra el mes con más ventas."""
    venta_mes = {}
   
    lector = lectura()

    for fila in lector:
        fecha = fila["Date"]   # formato YYYY-MM-DD
        mes = fecha[:7]        # toma YYYY-MM
        cantidad = int(fila["Quantity"])
        precio = float(fila["Price per Unit"])
        subtotal = cantidad * precio
        
        if mes not in venta_mes:
            venta_mes[mes] = 0
        venta_mes[mes] += subtotal
    
    return venta_mes

def imprimir_ventas_por_mes(venta_mes):

    print("-"*20)
    print("\nVENTAS POR MES\n")
    print("-"*20)

    for mes, total in sorted(venta_mes.items()):
        print(f"{mes}, se vendió ${total:,.2f}")
   
    mes_mas_vendido = max(venta_mes, key=venta_mes.get)
    
    print("-"*20)   
    print("\nMES CON MÁS VENTAS\n")
    print("-"*20)

    print(f"El mes con más ventas fue {mes_mas_vendido}, con ${venta_mes[mes_mas_vendido]:,.2f}")


def buscador():
    """Cuenta cuántas coincidencias hay de una categoría iventas_por_mesngresada por el usuario."""
    buscar = input("\nIngrese una categoría a buscar (Beauty, Clothing o Electronics): ").capitalize()
    contador = 0
    
    lector = lectura()

    for fila in lector:
        if fila["Product Category"] == buscar:
            contador += 1
    
    print("\nRESULTADOS:")
    print(f"Se encontraron {contador} coincidencias de la categoría {buscar}.")


def generar_archivo():
    """Genera un archivo .txt con todos los datos"""
    try:
        """inicializamos la variable vacia"""
        ventas_total = 0

        """Abrimos el archivo para leer los datos"""
        lector = lectura()

        for fila in lector:
            """Como usamos DictReader, accedemos al nombre de la columna directamente"""
            precio_total = float(fila["Total Amount"])

            """Calculamos las ventas totales"""
            ventas_total += precio_total

        """Llamamos a las funciones para obtener los datos ya calculados y no tener que repetir código"""
        total_por_mes = ventas_por_mes()
        ventas_producto = producto_mas_vendido()
         
        mayor_vendido = max(ventas_producto, key=ventas_producto.get)

        """Guardamos los resultados obtenitdos en un archivo .txt"""
        with open (ARCHIVO_SALIDA, "w", encoding="utf-8") as arch_out:
            arch_out.write("=== REPORTE ===\n")
            arch_out.write(f"VENTAS TOTALES:\n ${ventas_total:,.2f}\n")
            arch_out.write(f"\nEl producto más vendido es {mayor_vendido}, con {ventas_producto[mayor_vendido]} unidades vendidas.\n")
            arch_out.write("\nVENTAS POR MES\n")

            for mes, total in sorted(total_por_mes.items()):
                arch_out.write(f"{mes}, se vendió ${total:,.2f}\n")

        print("BIEN! El archivo se generó exitosamente")


    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta: {ARCHIVO_CSV}")

    except ValueError as e:
        print(f"Error con el formato de los datos o columnas: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")




# Menú principal
print("-"*30)
print("    CONSULTAS DE VENTAS")
print("-"*30)
print("MENU")
print(" 1- Búsqueda\n 2- Ventas Totales (por categoría)\n 3- Producto más vendido\n 4- Ventas mensuales\n 5- Generar archivo .txt\n 6- Salir")

while True:
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
            generar_archivo()
        case "6":
            print('\nGracias por visitarnos!! Nos vemos la proxima\n')
            break
        case _:
            print("Opción inválida. Intente nuevamente")
