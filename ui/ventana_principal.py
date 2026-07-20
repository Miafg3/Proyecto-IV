import customtkinter as ctk
from tema import *

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
        """Crea todos los componentes."""
        self.crear_sidebar()
        self.crear_area_principal()

    def crear_sidebar(self):
        """Crea el panel lateral."""
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
            "➕ Agregar producto",
            "📦 Inventario",
            "🔍 Buscar",
            "✏️ Editar producto",
            "🗑️ Eliminar producto"
        ]

        for opcion in opciones:

            boton = ctk.CTkButton(
                self.sidebar,
                text=opcion,
                height=42,
                fg_color=COLOR_BOTON,
                hover_color=COLOR_BOTON_HOVER,
                text_color="black",
                corner_radius=8
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

        self.titulo_principal = ctk.CTkLabel(
            self.area_principal,
            text="Bienvenido",
            font=(FUENTE, 30, "bold"),
            text_color=COLOR_TEXTO
        )

        self.titulo_principal.pack(
            pady=(50, 10)
        )

        self.descripcion = ctk.CTkLabel(
            self.area_principal,
            text="Selecciona una opción del menú para comenzar.",
            font=(FUENTE, 15),
            text_color="#BFC9D9"
        )

        self.descripcion.pack()

    def iniciar(self):
        """Inicia la aplicación."""
        self.ventana.mainloop()