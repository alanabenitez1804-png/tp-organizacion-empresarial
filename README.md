# TP Organización Empresarial - Escenario B: Análisis de Ventas

## Integrantes
* **Alan Benítez** (Líder y Organizador - Rol: Hugo)
* **Ramiro Acevedo** (Desarrollador Técnico - Rol: Paco)
* **Dario Nuñez** (Revisor y QA - Rol: Luis)

## Escenario Elegido
**Escenario B - Análisis de Ventas de una Pequeña Empresa**
El objetivo principal de este proyecto es procesar un conjunto de datos comerciales simulados para generar indicadores clave de rendimiento, permitiendo interpretar de manera clara el desempeño de la estructura comercial.

## Descripción del Dataset
El dataset de análisis se encuentra almacenado dentro de la carpeta `/datos` y cuenta con la siguiente información estructurada:
* **Producto:** Nombre o identificador del artículo comercializado.
* **Cantidad vendida:** Volumen de unidades despachadas en la transacción.
* **Precio:** Valor monetario unitario del producto.
* **Fecha de venta:** Registro temporal de la operación.
* link de acceso al dataset: https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset

## Estructura del Proyecto
* `/datos`: Carpeta destinada a almacenar los archivos de datos (CSV/Excel).
* `/scripts`: Contiene el código fuente algorítmico para el procesamiento de los datos.
* `/resultados`: Almacenamiento de reportes, tablas y gráficos exportados.

## Instrucciones de Ejecución
* ** Clonar el repositorio: git clone https://github.com/alanabenitez1804-png/tp-organizacion-empresarial.git
* ** Ingresar a la carpeta del proyecto: cd tp-organizacion-empresarial
* ** Ejecutar  python3 scripts/menu.py

    El mismo generará un Menú interactivo en el cual el usuario podrá generar distintos tipos de
    reportes por pantalla y también se podrá generar un gráfico, un archivo .txt y uno .csv con los datos de ventas totales
    y mensuales.

## Requisitos
* ** Python 3
* ** pandas
* ** matplotlib
