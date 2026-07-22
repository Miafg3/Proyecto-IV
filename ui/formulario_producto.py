import customtkinter as ctk
from tema import *

class FormularioProducto(ctk.CTkFrame):
    """Formulario para agregar productos."""

    def __init__(self, master):
        super().__init__(master,fg_color=COLOR_FONDO)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.crear_componentes()

    def crear_componentes(self):

        # Tarjeta centrada

        self.tarjeta = ctk.CTkFrame(
            self,
            fg_color=COLOR_PANEL,
            corner_radius=15
        )

        self.tarjeta.grid(
            row=0,
            column=0,
            padx=50,
            pady=50
        )

        # Título

        titulo = ctk.CTkLabel(
            self.tarjeta,
            text="Agregar producto",
            font=(FUENTE, 26, "bold"),
            text_color=COLOR_TEXTO
        )

        titulo.pack(
            pady=(35, 30)
        )

        # Nombre

        ctk.CTkLabel(
            self.tarjeta,
            text="Nombre",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_nombre = ctk.CTkEntry(
            self.tarjeta,
            width=450,
            height=40
        )

        self.entry_nombre.pack(
            padx=35,
            pady=(6, 20)
        )

        # Marca

        ctk.CTkLabel(
            self.tarjeta,
            text="Marca",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_marca = ctk.CTkEntry(
            self.tarjeta,
            width=450,
            height=40
        )

        self.entry_marca.pack(
            padx=35,
            pady=(6, 20)
        )

        # SKU

        ctk.CTkLabel(
            self.tarjeta,
            text="SKU",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_sku = ctk.CTkEntry(
            self.tarjeta,
            width=450,
            height=40
        )

        self.entry_sku.pack(
            padx=35,
            pady=(6, 20)
        )

        # Precio

        ctk.CTkLabel(
            self.tarjeta,
            text="Precio",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_precio = ctk.CTkEntry(
            self.tarjeta,
            width=450,
            height=40
        )

        self.entry_precio.pack(
            padx=35,
            pady=(6, 20)
        )

        # Cantidad

        ctk.CTkLabel(
            self.tarjeta,
            text="Cantidad",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_cantidad = ctk.CTkEntry(
            self.tarjeta,
            width=450,
            height=40
        )

        self.entry_cantidad.pack(
            padx=35,
            pady=(6, 30)
        )

        # Botón

        self.boton_guardar = ctk.CTkButton(
            self.tarjeta,
            text="Guardar producto",
            height=45,
            width=450,
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="black",
            corner_radius=8
        )

        self.boton_guardar.pack(
            padx=35,
            pady=(0, 35)
        )