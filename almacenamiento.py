# almacenamiento.py  —  CLASE 2
# Guardar y cargar los proyectos en un archivo JSON.
# Probá con:  python pruebas_clase2.py
import json
from modelos import Producto, Proyecto

ARCHIVO = "datos.json"


def guardar(proyectos, archivo=ARCHIVO):
    # TODO 1: armar una lista "datos" con proyecto.a_diccionario() de cada proyecto
    # TODO 2: abrir el archivo en modo "w" (encoding="utf-8") y escribir con
    #         json.dump(datos, f, indent=2, ensure_ascii=False)
    pass


def cargar(archivo=ARCHIVO):
    """Lee el archivo y devuelve una lista de Proyecto. Si no existe, lista vacía."""
    # TODO 3: abrir el archivo en modo "r" y leerlo con json.load(f).
    #         Usá try/except FileNotFoundError: si no existe, devolver [].
    # TODO 4: por cada diccionario d de la lista:
    #         - crear Proyecto(d["nombre"])
    #         - por cada p en d["productos"] crear un Producto(...) y agregarlo
    #           (el último dato, extras, se obtiene con p.get("extras", {}))
    #         - agregar el proyecto a la lista que vas a devolver
    return []
