import json
import os

class Inventario:
    """
    Maneja los productos del sistema.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        return self.productos