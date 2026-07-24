import customtkinter as ctk

from tema import *

from modelos.producto import Producto
from modelos.inventario import Inventario

class FormularioProducto(ctk.CTkFrame):
    """Formulario para agregar productos."""
    
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=COLOR_FONDO
        )

        self.inventario = Inventario()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.crear_componentes()

    def crear_componentes(self):

        # Tarjeta

        self.tarjeta = ctk.CTkFrame(
            self,
            fg_color=COLOR_PANEL,
            corner_radius=15,
            width=620
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

        titulo.pack(pady=(35, 30))

        # Nombre

        ctk.CTkLabel(
            self.tarjeta,
            text="Nombre",
            anchor="w"
        ).pack(fill="x", padx=35)

        self.entry_nombre = ctk.CTkEntry(
            self.tarjeta,
            width=500,
            height=40,
            corner_radius=8
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
            width=500,
            height=40,
            corner_radius=8
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
            width=500,
            height=40,
            corner_radius=8
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
            width=500,
            height=40,
            corner_radius=8
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
            width=500,
            height=40,
            corner_radius=8
        )

        self.entry_cantidad.pack(
            padx=35,
            pady=(6, 30)
        )

        # Botón

        self.boton_guardar = ctk.CTkButton(
            self.tarjeta,
            text="Guardar producto",
            width=500,
            height=45,
            corner_radius=8,
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="white",
            command=self.guardar_producto
        )

        self.boton_guardar.pack(
            padx=35,
            pady=(0, 35)
        )

    def guardar_producto(self):
        """Guarda un producto en el inventario."""

        producto = Producto(
            self.entry_nombre.get(),
            self.entry_marca.get(),
            self.entry_sku.get(),
            self.entry_precio.get(),
            self.entry_cantidad.get()
        )

        self.inventario.agregar_producto(producto)
        print("Producto guardado correctamente")