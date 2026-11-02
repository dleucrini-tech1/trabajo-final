# graficos.py  —  CLASES 4 y 5
# Gráficos con matplotlib. Un gráfico de barras por cada propiedad elegida.
import matplotlib.pyplot as plt

from estadisticas import valores


def graficar(productos, propiedades):
    """Devuelve una figura con un gráfico de barras por propiedad.
    Cada barra es un producto."""
    # TODO 1: armar la lista "nombres" con el nombre de cada producto
    nombres = []

    cantidad = len(propiedades)
    fig, ejes = plt.subplots(1, cantidad, figsize=(5 * cantidad, 4), squeeze=False)

    for i in range(cantidad):
        propiedad = propiedades[i]
        eje = ejes[0][i]
        # TODO 2: dibujar las barras:  eje.bar(nombres, valores(productos, propiedad), color="#306998")
        eje.set_title(propiedad.capitalize())
        eje.set_xlim(-1, max(len(nombres), 3))
        eje.tick_params(axis="x", rotation=30)

    fig.tight_layout()
    return fig
