# Crea un archivo datos.json con un proyecto de ejemplo (para probar rápido).
from modelos import Producto, Proyecto
from almacenamiento import guardar

kiosco = Proyecto("Kiosco")
kiosco.agregar_producto(Producto("Alfajor", 120, 300, 500, 80))
kiosco.agregar_producto(Producto("Gaseosa", 60, 800, 1200, 45))
kiosco.agregar_producto(Producto("Chicle", 200, 50, 100, 150, {"devoluciones": 4}))
kiosco.agregar_producto(Producto("Galletitas", 90, 600, 900, 60))

libreria = Proyecto("Librería")
libreria.agregar_producto(Producto("Cuaderno", 40, 1500, 2500, 30))
libreria.agregar_producto(Producto("Lapicera", 300, 100, 250, 220))

guardar([kiosco, libreria])
print("datos.json creado")
