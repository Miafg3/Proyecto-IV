import json
import os

class Inventario:
    """
    Maneja los productos del sistema.
    """

    def __init__(self):
        self.productos = []
        self.archivo = "datos/productos.json"
        self.cargar_productos()

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_productos()

    def mostrar_productos(self):
        return self.productos

    def guardar_productos(self):
        """
        Guarda todos los productos en productos.json.
        """
        datos = []

        for producto in self.productos:
            datos.append(producto.to_dict())

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar_productos(self):
        """
        Carga los productos desde productos.json.
        """
        if not os.path.exists(self.archivo):
            return

        with open(
            self.archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)

        from modelos.producto import Producto

        for producto in datos:

            nuevo_producto = Producto(
                producto["nombre"],
                producto["marca"],
                producto["sku"],
                producto["precio"],
                producto["cantidad"]
            )

            self.productos.append(nuevo_producto)