# main.py

# Importamos el archivo mechanical_workshop.py desde la carpeta src
from src import mechanical_workshop

# Ejecutamos el código dentro de mechanical_workshop.py
if __name__ == "__main__":
    # Llamamos a la función que contiene el código en mechanical_workshop.py
    # En este caso, solo ejecutamos todo el contenido del archivo
    exec(open("src/mechanical_workshop.py").read())
