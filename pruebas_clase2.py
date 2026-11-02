# Pruebas de la CLASE 2 (almacenamiento.py).  Ejecutar:  python pruebas_clase2.py
import os
from _ayuda import chequear, resumen_final
from modelos import Producto, Proyecto
from almacenamiento import guardar, cargar

ARCHIVO_PRUEBA = "datos_prueba.json"
if os.path.exists(ARCHIVO_PRUEBA):
    os.remove(ARCHIVO_PRUEBA)

chequear("TODO 3: cargar un archivo inexistente devuelve []", lambda: cargar(ARCHIVO_PRUEBA) == [])

k = Proyecto("Kiosco")
k.agregar_producto(Producto("Alfajor", 120, 300, 500, 80))
k.agregar_producto(Producto("Chicle", 200, 50, 100, 150, {"devoluciones": 4}))
l = Proyecto("Librería")

guardar([k, l], ARCHIVO_PRUEBA)
chequear("TODO 1-2: guardar crea el archivo", lambda: os.path.exists(ARCHIVO_PRUEBA))

leidos = cargar(ARCHIVO_PRUEBA)
chequear("TODO 4: se cargan 2 proyectos", lambda: len(leidos) == 2)
chequear("TODO 4: nombres de los proyectos", lambda: [p.nombre for p in leidos] == ["Kiosco", "Librería"])
chequear("TODO 4: se cargan los productos", lambda: leidos[0].nombres_productos() == ["Alfajor", "Chicle"])
chequear("TODO 4: los datos son correctos", lambda: leidos[0].buscar("Alfajor").ganancia() == 16000)
chequear("TODO 4: se cargan las propiedades extra", lambda: leidos[0].buscar("Chicle").extras == {"devoluciones": 4})
chequear("TODO 4: proyecto sin productos", lambda: leidos[1].productos == [])

if os.path.exists(ARCHIVO_PRUEBA):
    os.remove(ARCHIVO_PRUEBA)
resumen_final()
