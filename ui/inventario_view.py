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
                corner_radius=15
            )

            tarjeta.pack(
                fill="x",
                padx=10,
                pady=12
            )

            # TÍTULO

            titulo = ctk.CTkLabel(
                tarjeta,
                text=f"📦 {producto.nombre}",
                font=(FUENTE, 22, "bold"),
                text_color=COLOR_TEXTO
            )

            titulo.pack(
                anchor="w",
                padx=20,
                pady=(18, 8)
            )

            # SEPARADOR

            separador = ctk.CTkFrame(
                tarjeta,
                height=2,
                fg_color="#5F6B7A"
            )

            separador.pack(
                fill="x",
                padx=20,
                pady=(0, 15)
            )

            # INFORMACIÓN

            informacion = ctk.CTkFrame(
                tarjeta,
                fg_color="transparent"
            )

            informacion.pack(
                fill="x",
                padx=20
            )

            ctk.CTkLabel(
                informacion,
                text=f"Marca:      {producto.marca}",
                font=(FUENTE, 15)
            ).pack(anchor="w", pady=3)

            ctk.CTkLabel(
                informacion,
                text=f"SKU:          {producto.sku}",
                font=(FUENTE, 15)
            ).pack(anchor="w", pady=3)

            ctk.CTkLabel(
                informacion,
                text=f"Precio:      ${producto.precio}",
                font=(FUENTE, 15)
            ).pack(anchor="w", pady=3)

            ctk.CTkLabel(
                informacion,
                text=f"Cantidad:  {producto.cantidad}",
                font=(FUENTE, 15)
            ).pack(anchor="w", pady=3)

            # BOTONES

            botones = ctk.CTkFrame(
                tarjeta,
                fg_color="transparent"
            )

            botones.pack(
                fill="x",
                padx=20,
                pady=(18, 18)
            )

            editar = ctk.CTkButton(
                botones,
                text="✏ Editar",
                width=110,
                fg_color="#D4A017",
                hover_color="#B8860B",
                text_color="white"
            )

            editar.pack(
                side="right",
                padx=(10, 0)
            )

            eliminar = ctk.CTkButton(
                botones,
                text="🗑 Eliminar",
                width=110,
                fg_color="#B22222",
                hover_color="#8B1A1A",
                text_color="white"
            )

            eliminar.pack(
                side="right"
            )