import customtkinter as ctk
from tema import *

class FormularioProducto(ctk.CTkFrame):
    """Formulario para agregar productos."""

    def __init__(self, master):
        super().__init__(master, fg_color=COLOR_FONDO)

        self.crear_componentes()

    def crear_componentes(self):

        # Título

        titulo = ctk.CTkLabel(
            self,
            text="Agregar producto",
            font=(FUENTE, 24, "bold"),
            text_color=COLOR_TEXTO
        )

        titulo.pack(anchor="w", pady=(0, 25))

        # Nombre

        ctk.CTkLabel(
            self,
            text="Nombre"
        ).pack(anchor="w")

        self.entry_nombre = ctk.CTkEntry(
            self,
            width=350
        )

        self.entry_nombre.pack(pady=(5, 15))

        # Marca

        ctk.CTkLabel(
            self,
            text="Marca"
        ).pack(anchor="w")

        self.entry_marca = ctk.CTkEntry(
            self,
            width=350
        )

        self.entry_marca.pack(pady=(5, 15))

        # SKU

        ctk.CTkLabel(
            self,
            text="SKU"
        ).pack(anchor="w")

        self.entry_sku = ctk.CTkEntry(
            self,
            width=350
        )

        self.entry_sku.pack(pady=(5, 15))

        # Precio

        ctk.CTkLabel(
            self,
            text="Precio"
        ).pack(anchor="w")

        self.entry_precio = ctk.CTkEntry(
            self,
            width=350
        )

        self.entry_precio.pack(pady=(5, 15))

        # Cantidad

        ctk.CTkLabel(
            self,
            text="Cantidad"
        ).pack(anchor="w")

        self.entry_cantidad = ctk.CTkEntry(
            self,
            width=350
        )

        self.entry_cantidad.pack(pady=(5, 25))

        # Botón

        self.boton_guardar = ctk.CTkButton(
            self,
            text="Guardar producto",
            width=180,
            height=40,
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="black"
        )

        self.boton_guardar.pack(anchor="w")