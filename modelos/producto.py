class Producto:
    """
    Representa un producto dentro del inventario.
    """

    def __init__(self, nombre, marca, sku, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.sku = sku
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        """
        Convierte el objeto Producto en un diccionario.
        Esto nos permitirá guardarlo fácilmente en un archivo JSON.
        """
        return {
            "nombre": self.nombre,
            "marca": self.marca,
            "sku": self.sku,
            "precio": self.precio,
            "cantidad": self.cantidad
        }