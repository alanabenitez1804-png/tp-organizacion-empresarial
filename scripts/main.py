import os
from menu import mostrar_menu

def asegurar_estructura():
    carpetas = [
        "datos",
        "resultados"
    ]

    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)

def main():
    asegurar_estructura()
    mostrar_menu()

if __name__ == "__main__":
    main()