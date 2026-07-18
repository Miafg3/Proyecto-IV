import customtkinter as ctk
from tema import *

class VentanaPrincipal:

    def __init__(self):
        self.ventana = ctk.CTk()
        self.configurar_ventana()
        self.crear_componentes()

    def configurar_ventana(self):
        self.ventana.title("Inventario")
        self.ventana.geometry("1000x650")
        self.ventana.configure(fg_color=COLOR_FONDO)

    def crear_componentes(self):

        self.sidebar = ctk.CTkFrame(
            self.ventana,
            width=220,
            fg_color=COLOR_PANEL,
            corner_radius=0
        )

        self.sidebar.pack(side="left", fill="y")
        
        # Título
        
        titulo = ctk.CTkLabel(
            self.sidebar,
            text="Inventario",
            font=(FUENTE, 24, "bold"),
            text_color=COLOR_TEXTO
        )

        titulo.pack(pady=(30, 10))
        
        # Subtítulo
        
        subtitulo = ctk.CTkLabel(
            self.sidebar,
            text="Sistema de Inventario",
            font=(FUENTE, 13),
            text_color="#BFC9D9"
        )

        subtitulo.pack(pady=(0, 30))
        
        # Botón Agregar Producto
        
        self.boton_agregar = ctk.CTkButton(
            self.sidebar,
            text="➕ Agregar producto",
            width=180,
            height=40,
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="black"
        )

        self.boton_agregar.pack(pady=10)
    
        self.area_principal = ctk.CTkFrame(
            self.ventana,
            fg_color=COLOR_FONDO,
            corner_radius=0
        )

        self.area_principal.pack(
            side="right",
            fill="both",
            expand=True
        )

    def iniciar(self):
        self.ventana.mainloop()