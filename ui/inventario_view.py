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
        self.productos = self.inventario.mostrar_productos()
        self.crear_componentes()

    # COMPONENTES PRINCIPALES

    def crear_componentes(self):
        self.crear_header()
        self.crear_barra_acciones()
        self.crear_lista_productos()

    # HEADER

    def crear_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=40,
            pady=(30, 10)
        )

        titulo = ctk.CTkLabel(
            header,
            text="📦 Inventario",
            font=(FUENTE, 30, "bold"),
            text_color=COLOR_TEXTO
        )

        titulo.pack(
            anchor="w"
        )

        descripcion = ctk.CTkLabel(
            header,
            text="Gestiona todos los productos registrados.",
            font=(FUENTE, 15),
            text_color="#BFC9D9"
        )

        descripcion.pack(
            anchor="w",
            pady=(5, 10)
        )

        contador = ctk.CTkLabel(
            header,
            text=f"{len(self.productos)} producto(s) registrado(s)",
            font=(FUENTE, 15, "bold"),
            text_color=COLOR_BOTON
        )

        contador.pack(
            anchor="w"
        )
        
    # BARRA DE ACCIONES

    def crear_barra_acciones(self):

        acciones = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        acciones.pack(
            fill="x",
            padx=40,
            pady=(10, 20)
        )

        buscar = ctk.CTkEntry(
            acciones,
            placeholder_text="🔍 Buscar producto...",
            height=40,
            width=400
        )

        buscar.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        actualizar = ctk.CTkButton(
            acciones,
            text="Actualizar",
            width=140,
            height=40,
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="white"
        )

        actualizar.pack(
            side="right"
        )
        
    # LISTA DE PRODUCTOS

    def crear_lista_productos(self):

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

        if not self.productos:

            mensaje = ctk.CTkLabel(
                contenedor,
                text="No hay productos registrados.",
                font=(FUENTE, 18),
                text_color=COLOR_TEXTO
            )

            mensaje.pack(
                pady=20
            )

            return

        for producto in self.productos:

            self.crear_tarjeta(
                contenedor,
                producto
            )
            
    # TARJETA DE PRODUCTO

    def crear_tarjeta(self, contenedor, producto):

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

        # TITULO

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

        # INFORMACION

        informacion = ctk.CTkFrame(
            tarjeta,
            fg_color="transparent"
        )

        informacion.pack(
            fill="x",
            padx=20
        )

        informacion.grid_columnconfigure(
            0,
            weight=0
        )

        informacion.grid_columnconfigure(
            1,
            weight=1
        )

        datos = [
            ("Marca", producto.marca),
            ("SKU", producto.sku),
            ("Precio", f"${producto.precio}"),
            ("Cantidad", producto.cantidad)
        ]

        for fila, (nombre, valor) in enumerate(datos):

            etiqueta = ctk.CTkLabel(
                informacion,
                text=nombre,
                font=(FUENTE, 15, "bold"),
                text_color=COLOR_TEXTO
            )

            etiqueta.grid(
                row=fila,
                column=0,
                sticky="w",
                padx=(0, 30),
                pady=6
            )

            dato = ctk.CTkLabel(
                informacion,
                text=str(valor),
                font=(FUENTE, 15)
            )

            dato.grid(
                row=fila,
                column=1,
                sticky="w",
                pady=6
            )

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
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
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