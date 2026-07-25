import customtkinter as ctk

from tema import *
from modelos.inventario import Inventario

class InventarioView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=COLOR_FONDO
        )

        self.inventario = Inventario()
        self.crear_componentes()

    def crear_componentes(self):
        titulo = ctk.CTkLabel(
            self,
            text="Inventario",
            font=(FUENTE, 28, "bold"),
            text_color=COLOR_TEXTO
        )

        titulo.pack(
            pady=(30, 20)
        )

        contenedor = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 30)
        )

        productos = self.inventario.mostrar_productos()

        if not productos:

            mensaje = ctk.CTkLabel(
                contenedor,
                text="No hay productos registrados.",
                font=(FUENTE, 18)
            )

            mensaje.pack(pady=20)

            return

        for producto in productos:

            tarjeta = ctk.CTkFrame(
                contenedor,
                fg_color=COLOR_PANEL,
                corner_radius=12
            )

            tarjeta.pack(
                fill="x",
                pady=10,
                padx=10
            )

            ctk.CTkLabel(
                tarjeta,
                text=producto.nombre,
                font=(FUENTE, 20, "bold"),
                text_color=COLOR_TEXTO
            ).pack(anchor="w", padx=20, pady=(15, 5))

            ctk.CTkLabel(
                tarjeta,
                text=f"Marca: {producto.marca}"
            ).pack(anchor="w", padx=20)

            ctk.CTkLabel(
                tarjeta,
                text=f"SKU: {producto.sku}"
            ).pack(anchor="w", padx=20)

            ctk.CTkLabel(
                tarjeta,
                text=f"Precio: ${producto.precio}"
            ).pack(anchor="w", padx=20)

            ctk.CTkLabel(
                tarjeta,
                text=f"Cantidad: {producto.cantidad}"
            ).pack(anchor="w", padx=20, pady=(0, 15))