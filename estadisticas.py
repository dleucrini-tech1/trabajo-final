# estadisticas.py  —  CLASE 4
# Cálculos con los datos de un proyecto, en Python puro.
# Probá con:  python pruebas_clase4.py


def valores(productos, propiedad):
    """Lista con el valor de una propiedad para cada producto (0 si no la tiene)."""
    lista = []
    for producto in productos:
        lista.append(producto.propiedades().get(propiedad, 0))
    return lista


def total(productos, propiedad):
    # TODO 1: devolver la suma de los valores de esa propiedad (usá valores(...))
    pass


def promedio(productos, propiedad):
    # TODO 2: devolver el promedio. Si no hay productos, devolver 0.
    pass


def producto_maximo(productos, propiedad):
    """Devuelve el producto con el valor más alto de esa propiedad (o None)."""
    # TODO 3: recorrer los productos y quedarte con el de mayor valor.
    # Pista: empezá con mejor = None y comparalo con cada producto.
    pass


def resumen(productos, propiedades):
    """Lista de filas (diccionarios) con total, promedio y máximo por propiedad."""
    filas = []
    for propiedad in propiedades:
        mejor = producto_maximo(productos, propiedad)
        filas.append({
            "propiedad": propiedad,
            "total": round(total(productos, propiedad), 2),
            "promedio": round(promedio(productos, propiedad), 2),
            "máximo": mejor.nombre if mejor else "-",
        })
    return filas
