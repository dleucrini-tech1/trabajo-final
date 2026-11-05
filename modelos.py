# modelos.py  —  CLASES 1 y 3
# Las dos clases del proyecto: Producto y Proyecto.
# Completá cada parte marcada con TODO. Probá con:  python pruebas_clase1.py


class Producto:
    def __init__(self, nombre, stock, costo, precio, ventas, extras=None):
        self.nombre = nombre
        self.stock = stock
        self.costo = costo
        self.precio = precio
        self.ventas = ventas
        # EXTRA (desafío final): propiedades inventadas a mano. Por ahora, vacío.
        if extras is None:
            extras = {}
        self.extras = extras

    def ganancia(self):
        return  (self.precio - self.costo)  * self.ventas 
        
    

    def propiedades(self):
        """Devuelve un diccionario con todos los datos numéricos del producto."""
        props = {
            "stock": self.stock,
            "costo": self.costo,
            "precio": self.precio,
            "ventas": self.ventas,
            "ganancia": self.ganancia(),
        }
        for clave, valor in self.extras.items():
            props[clave] = valor
        return props

    def a_diccionario(self):
        """Convierte el producto en un diccionario (para guardarlo en JSON)."""
        # TODO 2: devolver un diccionario con las claves
        # "nombre", "stock", "costo", "precio", "ventas" y "extras"
        pass

    def __str__(self):
        # TODO 3: devolver un texto como  "Alfajor (stock: 120, ganancia: $16000)"
        pass


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []   # lista de objetos Producto

    def buscar(self, nombre):
        """Devuelve el producto con ese nombre, o None si no existe."""
        # TODO 4: recorrer self.productos con un for y comparar producto.nombre
        pass

    def agregar_producto(self, producto):
        """Agrega el producto. Devuelve True si se pudo, False si el nombre ya existe."""
        # TODO 5: usar self.buscar(...) para ver si ya existe. Si no existe, agregarlo.
        pass

    def eliminar_producto(self, nombre):
        """Elimina el producto. Devuelve True si existía, False si no."""
        # TODO 6: buscar el producto y, si existe, sacarlo con self.productos.remove(...)
        pass

    def editar_producto(self, nombre, stock, costo, precio, ventas):
        """Cambia los valores de un producto existente. Devuelve True si existía, False si no."""
        # TODO 9: buscar el producto. Si no existe, devolver False.
        # Si existe, cambiarle stock, costo, precio y ventas por los valores nuevos y devolver True.
        pass

    def nombres_productos(self):
        """Lista con los nombres de todos los productos."""
        # TODO 7: armar y devolver una lista con los nombres
        pass

    def nombres_propiedades(self):
        """Lista de todas las propiedades numéricas que existen en el proyecto."""
        nombres = ["stock", "costo", "precio", "ventas", "ganancia"]
        for producto in self.productos:
            for clave in producto.extras:
                if clave not in nombres:
                    nombres.append(clave)
        return nombres

    def a_diccionario(self):
        # TODO 8: devolver {"nombre": ..., "productos": [lista de diccionarios]}
        # Pista: usá producto.a_diccionario() para cada producto
        pass
