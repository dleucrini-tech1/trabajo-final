# Pruebas de la CLASE 1 (modelos.py).  Ejecutar:  python pruebas_clase1.py
from _ayuda import chequear, resumen_final
from modelos import Producto, Proyecto

a = Producto("Alfajor", 120, 300, 500, 80)

chequear("TODO 1: ganancia = (precio - costo) * ventas", lambda: a.ganancia() == 16000)
chequear("TODO 2: a_diccionario tiene nombre y ventas",
         lambda: a.a_diccionario()["nombre"] == "Alfajor" and a.a_diccionario()["ventas"] == 80)
chequear("TODO 2: a_diccionario tiene las 6 claves",
         lambda: sorted(a.a_diccionario().keys()) == ["costo", "extras", "nombre", "precio", "stock", "ventas"])
chequear("TODO 3: __str__", lambda: str(a) == "Alfajor (stock: 120, ganancia: $16000)")

p = Proyecto("Kiosco")
chequear("TODO 5: agregar_producto devuelve True la primera vez", lambda: p.agregar_producto(a) is True)
chequear("TODO 5: agregar_producto devuelve False si el nombre está repetido",
         lambda: p.agregar_producto(Producto("Alfajor", 1, 1, 1, 1)) is False)
chequear("TODO 5: no se duplicó el producto", lambda: len(p.productos) == 1)
chequear("TODO 4: buscar encuentra un producto", lambda: p.buscar("Alfajor") is a)
chequear("TODO 4: buscar devuelve None si no existe", lambda: p.buscar("Nada") is None)
p.agregar_producto(Producto("Gaseosa", 60, 800, 1200, 45))
chequear("TODO 7: nombres_productos", lambda: p.nombres_productos() == ["Alfajor", "Gaseosa"])
chequear("TODO 6: eliminar_producto devuelve True", lambda: p.eliminar_producto("Gaseosa") is True)
chequear("TODO 6: eliminar_producto devuelve False si no existe", lambda: p.eliminar_producto("Gaseosa") is False)
chequear("TODO 6: el producto ya no está", lambda: p.nombres_productos() == ["Alfajor"])
chequear("TODO 8: Proyecto.a_diccionario",
         lambda: p.a_diccionario()["nombre"] == "Kiosco" and p.a_diccionario()["productos"][0]["nombre"] == "Alfajor")

q = Proyecto("Tienda")
q.agregar_producto(Producto("Remera", 10, 500, 900, 30))
chequear("TODO 9: editar_producto devuelve True si existe", lambda: q.editar_producto("Remera", 25, 500, 1000, 40) is True)
chequear("TODO 9: cambia los valores", lambda: (q.buscar("Remera").stock, q.buscar("Remera").precio, q.buscar("Remera").ventas) == (25, 1000, 40))
chequear("TODO 9: la ganancia se recalcula", lambda: q.buscar("Remera").ganancia() == 20000)
chequear("TODO 9: devuelve False si no existe", lambda: q.editar_producto("Nada", 1, 1, 1, 1) is False)

resumen_final()
