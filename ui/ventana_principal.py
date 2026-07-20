import customtkinter as ctk
from tema import *
from ui.formulario_producto import FormularioProducto

class VentanaPrincipal:
    """Ventana principal del sistema."""

    def __init__(self):
        self.ventana = ctk.CTk()

        self.configurar_ventana()
        self.crear_componentes()

    def configurar_ventana(self):
        """Configura la ventana principal."""
        self.ventana.title("Proyecto - IV")
        self.ventana.geometry("1000x650")
        self.ventana.configure(fg_color=COLOR_FONDO)

    def crear_componentes(self):
        """Crea todos los componentes de la ventana."""
        self.crear_sidebar()
        self.crear_area_principal()

    def crear_sidebar(self):
        """Crea el menú lateral."""
        self.sidebar = ctk.CTkFrame(
            self.ventana,
            width=240,
            fg_color=COLOR_PANEL,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Título

        self.titulo = ctk.CTkLabel(
            self.sidebar,
            text="Proyecto - IV",
            font=(FUENTE, 24, "bold"),
            text_color=COLOR_TEXTO
        )

        self.titulo.pack(
            pady=(30, 5)
        )

        # Subtítulo

        self.subtitulo = ctk.CTkLabel(
            self.sidebar,
            text="Sistema de Inventario",
            font=(FUENTE, 13),
            text_color="#BFC9D9"
        )

        self.subtitulo.pack(
            pady=(0, 35)
        )

        # Botones

        opciones = [
            ("➕ Agregar producto", self.mostrar_formulario_producto),
            ("📦 Inventario", None),
            ("🔍 Buscar", None),
            ("✏️ Editar producto", None),
            ("🗑️ Eliminar producto", None)
        ]

        for texto, comando in opciones:

            boton = ctk.CTkButton(
                self.sidebar,
                text=texto,
                height=42,
                corner_radius=8,
                fg_color=COLOR_BOTON,
                hover_color=COLOR_BOTON_HOVER,
                text_color="black",
                command=comando
            )

            boton.pack(
                fill="x",
                padx=20,
                pady=8
            )

    def crear_area_principal(self):
        """Crea el área principal."""
        self.area_principal = ctk.CTkFrame(
            self.ventana,
            fg_color=COLOR_FONDO,
            corner_radius=0
        )

        self.area_principal.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Header

        self.header = ctk.CTkFrame(
            self.area_principal,
            height=80,
            fg_color=COLOR_PANEL,
            corner_radius=0
        )

        self.header.pack(
            fill="x"
        )

        self.titulo_header = ctk.CTkLabel(
            self.header,
            text="Bienvenido",
            font=(FUENTE, 26, "bold"),
            text_color=COLOR_TEXTO
        )

        self.titulo_header.pack(
            padx=25,
            pady=20,
            anchor="w"
        )

        # Contenido

        self.contenido = ctk.CTkFrame(
            self.area_principal,
            fg_color=COLOR_FONDO
        )

        self.contenido.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        self.descripcion = ctk.CTkLabel(
            self.contenido,
            text="Selecciona una opción del menú para comenzar.",
            font=(FUENTE, 16),
            text_color="#BFC9D9"
        )

        self.descripcion.pack()

    def limpiar_contenido(self):
        """Elimina todo el contenido del área principal."""
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_formulario_producto(self):
        """Muestra el formulario para agregar productos."""
        self.limpiar_contenido()

        formulario = FormularioProducto(
            self.contenido
        )

        formulario.pack(
            fill="both",
            expand=True
        )

    def iniciar(self):
        """Inicia la aplicación."""
        self.ventana.mainloop()