from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
import pandas as pd

# Programa de análisis de ventas usando el dataset de Kaggle:
# https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset
# Funcionalidades:
# 1. Buscar coincidencias de productos por categoría
# 2. Calcular ventas totales por categoría
# 3. Encontrar el producto más vendido
# 4. Calcular ventas por mes y detectar el mes con más ventas
# 5. Guardar los datos en un archivo .txt

#AL utilizar pathlib evitamos problemas por lo que funciona en 
# windows y en linux por lo que hace el proyecto portable
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas
ARCHIVO_CSV = BASE_DIR / "datos" / "retail_sales_dataset.csv"
CARPETA_SALIDA = BASE_DIR / "resultados"
ARCHIVO_SALIDA = CARPETA_SALIDA / "resumen_ventas.txt"

def lectura():
    try:
        """Lee el archivo CSV y devuelve un diccionario."""
        with open(ARCHIVO_CSV, "r", encoding="utf-8-sig") as archivo:
            #Guardamos los datos en una list(), ya que al llegar al return la funcion, el archivo se cierra
            return list(csv.DictReader(archivo))

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}' en el directorio actual.")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return [] # Devolvemos una lista vacía para evitar que el programa rompa después


def ventas_totales_por_categoria():
    """Calcula el total de ventas de una categoría ingresada por el usuario."""
    try:
        categoria = input("\nIngrese una categoría (Beauty, Clothing o Electronics): ").capitalize()
        
        #Declaramos en una tupla las categorias permitidas
        cat_permitidas = ('Beauty', 'Clothing', 'Electronics')

        #Verificamos con una condición if que el valor ingresado sea válido
        if not categoria.isalpha() or categoria not in cat_permitidas:
            print('Error, debe ingresar una categoría válida')
            return
        
        venta_total = 0
    
        #LLamamos a la funcion lectura() y guardamos los datos en una variable
        lector = lectura()

        for fila in lector:
            if fila["Product Category"] == categoria:
                cantidad = int(fila["Quantity"])
                precio = float(fila["Price per Unit"])
                subtotal = cantidad * precio
                venta_total += subtotal
        
        print(f"\nLas ventas totales de {categoria} fueron: ${venta_total:,.2f}")
    
    except KeyError as e:
        print(f"Error: No existe la columna {e} en el archivo CSV.")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def producto_mas_vendido():
    """Encuentra la categoría de producto con mayor cantidad de ventas."""
    ventas_producto = {}
    
    #Abrimos el archivo para leer los datos
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
   
    #Abrimos el archivo para leer los datos
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
    """Cuenta cuántas coincidencias hay de una categoría ingresada por el usuario."""
    try:
        buscar = input("\nIngrese una categoría a buscar (Beauty, Clothing o Electronics): ").capitalize()
        
        #Declaramos en una tupla las categorias permitidas
        cat_permitidas = ('Beauty', 'Clothing', 'Electronics')

        #Verificamos con una condición if que el valor ingresado sea válido
        if not buscar.isalpha() or buscar not in cat_permitidas:
            print('Error, debe ingresar una categoría válida')
            return
        
        contador = 0
        
        #Abrimos el archivo para leer los datos
        lector = lectura()

        for fila in lector:
            if fila["Product Category"] == buscar:
                contador += 1
        
        print("\nRESULTADOS:")
        print(f"Se encontraron {contador} coincidencias de la categoría {buscar}.")

    except KeyError as e:
        print(f"Error: No existe la columna {e} en el archivo CSV.")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def generar_archivos():
    """Genera un archivo .txt con todos los datos"""
    try:
        #inicializamos la variable vacia
        ventas_total = 0

        #Abrimos el archivo para leer los datos
        lector = lectura()

        for fila in lector:
            #Como usamos DictReader, accedemos al nombre de la columna directamente
            precio_total = float(fila["Total Amount"])

            #Calculamos las ventas totales
            ventas_total += precio_total

        #Llamamos a las funciones para obtener los datos ya calculados y no tener que repetir código
        total_por_mes = ventas_por_mes()
        ventas_producto = producto_mas_vendido()
         
        mayor_vendido = max(ventas_producto, key=ventas_producto.get)

        #Guardamos los resultados obtenidos en un archivo .txt
        with open (ARCHIVO_SALIDA, "w", encoding="utf-8") as arch_out:
            arch_out.write("=== REPORTE ===\n")
            arch_out.write(f"VENTAS TOTALES:\n ${ventas_total:,.2f}\n")
            arch_out.write(f"\nEl producto más vendido es {mayor_vendido}, con {ventas_producto[mayor_vendido]} unidades vendidas.\n")
            arch_out.write("\nVENTAS POR MES\n")

            for mes, total in sorted(total_por_mes.items()):
                arch_out.write(f"{mes}, se vendió ${total:,.2f}\n")

        #Llamamos a las funciones para generar el gŕafico y el archivo .csv
        generar_grafico_ventas_por_mes(total_por_mes)
        generar_tabla_por_categoria()
        
        print("BIEN! El archivo y los resultados se generaron exitosamente")


    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta: {ARCHIVO_CSV}")

    except ValueError as e:
        print(f"Error con el formato de los datos o columnas: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def generar_grafico_ventas_por_mes(venta_mes):
    """Genera un gráfico tomando los valores totales de ventas de cada mes"""
    
    try:
        meses = list(venta_mes.keys())
        totales = list(venta_mes.values())
        
        plt.figure(figsize=(10,5))
        plt.plot(meses, totales, marker="o", color="blue")
        plt.title("Evolución de Ventas por Mes")
        plt.xlabel("Mes")
        plt.ylabel("Ventas ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(CARPETA_SALIDA, "ventas_por_mes.png"))
        plt.close()
        
        print("Gráfico generado en resultados/ventas_por_mes.png")

    except Exception as e:
        print(f"Error al generar el gráfico: {e}")

def generar_tabla_por_categoria():
    """Genera un archivo .csv con los valores de ventas de cada producto"""
    
    try:
        lector = lectura()
        
        if not lector:
            return
        
        df = pd.DataFrame(lector)
        df["Total Amount"] = df["Total Amount"].astype(float)
        tabla = df.groupby("Product Category")["Total Amount"].sum()
        tabla.to_csv(os.path.join(CARPETA_SALIDA, "tabla_ventas.csv"))
        
        print("Tabla generada en resultados/tabla_ventas.csv")
    
    except KeyError as e:
        print(f"Error: Falta la columna {e}.")

    except ValueError as e:
        print(f"Error en los datos: {e}")

    except Exception as e:
        print(f"Error al generar la tabla: {e}")