# Pruebas de la CLASE 4 (estadisticas.py y graficos.py).  Ejecutar:  python pruebas_clase4.py
from _ayuda import chequear, resumen_final
from modelos import Producto
from estadisticas import total, promedio, producto_maximo, resumen
from graficos import graficar

productos = [Producto("Alfajor", 120, 300, 500, 80),
             Producto("Gaseosa", 60, 800, 1200, 45),
             Producto("Chicle", 200, 50, 100, 150)]

chequear("TODO 1: total de ventas", lambda: total(productos, "ventas") == 275)
chequear("TODO 1: total de ganancia", lambda: total(productos, "ganancia") == 41500)
chequear("TODO 2: promedio de stock", lambda: promedio(productos, "stock") == (120 + 60 + 200) / 3)
chequear("TODO 2: promedio sin productos es 0", lambda: promedio([], "stock") == 0)
chequear("TODO 3: producto con más ventas", lambda: producto_maximo(productos, "ventas").nombre == "Chicle")
chequear("TODO 3: producto con más ganancia", lambda: producto_maximo(productos, "ganancia").nombre == "Gaseosa")
chequear("TODO 3: sin productos devuelve None", lambda: producto_maximo([], "ventas") is None)
chequear("resumen devuelve una fila por propiedad", lambda: len(resumen(productos, ["ventas", "stock"])) == 2)


def prueba_grafico():
    fig = graficar(productos, ["ventas", "ganancia"])
    ejes = fig.axes
    return len(ejes) == 2 and len(ejes[0].patches) == 3


chequear("graficos TODO 1-2: 2 gráficos, 3 barras cada uno", prueba_grafico)

resumen_final()
