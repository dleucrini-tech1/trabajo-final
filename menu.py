# menu.py  —  CLASE 3 (y plan B si falla Streamlit)
# Ejecutá con:  python menu.py
# Completá agregar_producto(). Lo demás ya está hecho: leelo y entendelo.
# PLAN B: la misma aplicación, pero en la terminal (con gráficos en ventana).
import matplotlib.pyplot as plt

from modelos import Producto, Proyecto
from almacenamiento import guardar, cargar
from estadisticas import resumen
from graficos import graficar


def pedir_numero(texto, entero=False):
    while True:
        try:
            numero = float(input(texto))
            if numero < 0:
                print("No puede ser negativo")
            else:
                if entero:
                    return int(numero)
                return numero
        except ValueError:
            print("Ingresá un número válido")


def elegir_proyecto(proyectos):
    if len(proyectos) == 0:
        print("Todavía no hay proyectos")
        return None
    for i, p in enumerate(proyectos, 1):
        print(f"{i}. {p.nombre}")
    try:
        opcion = int(input("Elegí un proyecto: "))
        return proyectos[opcion - 1]
    except (ValueError, IndexError):
        print("Opción inválida")
        return None


def agregar_producto(proyecto):
    # TODO (Clase 3): pedir nombre (que no esté vacío), stock, costo, precio y ventas
    # con pedir_numero(...), crear el Producto y agregarlo con proyecto.agregar_producto(...)
    # Mostrar "Producto agregado" o "Ya existe un producto con ese nombre".
    print("Esta opción todavía no está hecha")


def editar_producto(proyecto):
    nombre = input("Nombre del producto a editar: ").strip()
    producto = proyecto.buscar(nombre)
    if producto is None:
        print("No existe ese producto")
        return
    print(f"Valores actuales -> stock: {producto.stock}, costo: {producto.costo}, "
          f"precio: {producto.precio}, ventas: {producto.ventas}")
    stock = pedir_numero("Nuevo stock: ", True)
    costo = pedir_numero("Nuevo costo: ")
    precio = pedir_numero("Nuevo precio de venta: ")
    ventas = pedir_numero("Nuevas ventas (unidades): ", True)
    proyecto.editar_producto(nombre, stock, costo, precio, ventas)
    print("Producto actualizado")


def ver_graficos(proyecto):
    if len(proyecto.productos) == 0:
        print("El proyecto no tiene productos")
        return
    propiedades = proyecto.nombres_propiedades()
    print("Propiedades:", ", ".join(propiedades))
    elegidas = input("¿Cuáles querés ver? (separadas por coma, o 'todas'): ").strip()
    if elegidas == "todas":
        lista = propiedades
    else:
        lista = []
        for nombre in elegidas.split(","):
            if nombre.strip() in propiedades:
                lista.append(nombre.strip())
    if len(lista) == 0:
        print("No elegiste propiedades válidas")
        return
    graficar(proyecto.productos, lista)
    plt.show()


def menu_proyecto(proyecto, proyectos):
    while True:
        print(f"\n--- Proyecto: {proyecto.nombre} ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Eliminar producto")
        print("4. Ver resumen")
        print("5. Ver gráficos")
        print("6. Editar producto")
        print("0. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_producto(proyecto)
            guardar(proyectos)
        elif opcion == "2":
            for producto in proyecto.productos:
                print("-", producto)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            print("Eliminado" if proyecto.eliminar_producto(nombre) else "No existe")
            guardar(proyectos)
        elif opcion == "4":
            for fila in resumen(proyecto.productos, proyecto.nombres_propiedades()):
                print(fila)
        elif opcion == "5":
            ver_graficos(proyecto)
        elif opcion == "6":
            editar_producto(proyecto)
            guardar(proyectos)
        elif opcion == "0":
            return
        else:
            print("Opción inválida")


def main():
    proyectos = cargar()
    while True:
        print("\n=== GESTOR DE PROYECTOS ===")
        print("1. Crear proyecto")
        print("2. Abrir proyecto")
        print("0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre del proyecto: ").strip()
            if nombre != "":
                proyectos.append(Proyecto(nombre))
                guardar(proyectos)
        elif opcion == "2":
            proyecto = elegir_proyecto(proyectos)
            if proyecto is not None:
                menu_proyecto(proyecto, proyectos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


main()
