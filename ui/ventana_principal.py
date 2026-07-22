import customtkinter as ctk
from tema import *
from ui.formulario_producto import FormularioProducto

class VentanaPrincipal:

    def __init__(self):
        self.ventana = ctk.CTk()
        self.botones = {}
        self.configurar_ventana()
        self.crear_componentes()

    # CONFIGURACIÓN

    def configurar_ventana(self):
        self.ventana.title("Proyecto IV")
        self.ventana.state("zoomed")
        self.ventana.minsize(1100, 700)
        self.ventana.configure(
            fg_color=COLOR_FONDO
        )

    # COMPONENTES

    def crear_componentes(self):

        self.ventana.grid_columnconfigure(
            1,
            weight=1
        )

        self.ventana.grid_rowconfigure(
            0,
            weight=1
        )

        self.crear_sidebar()
        self.crear_area_principal()
        self.mostrar_formulario()

    # SIDEBAR

    def crear_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.ventana,
            width=270,
            fg_color=COLOR_PANEL,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.sidebar.grid_propagate(False)

        # TITULO

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="Sistema de\nInventario",
            font=(FUENTE, 24, "bold"),
            text_color=COLOR_TEXTO,
            justify="center"
        )

        titulo.pack(
            pady=(40, 20)
        )

        # LINEA

        separador = ctk.CTkFrame(
            self.sidebar,
            height=2,
            fg_color="#5F6B7A"
        )

        separador.pack(
            fill="x",
            padx=20,
            pady=(0, 25)
        )

        # MENU

        menu = ctk.CTkLabel(
            self.sidebar,
            text="MENÚ",
            font=(FUENTE, 13, "bold"),
            text_color="#BFC9D9"
        )

        menu.pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        self.crear_boton(
            "Agregar producto",
            "➕",
            self.mostrar_formulario
        )

        self.crear_boton(
            "Inventario",
            "📦",
            None
        )

        self.crear_boton(
            "Buscar",
            "🔍",
            None
        )

        self.crear_boton(
            "Editar",
            "✏️",
            None
        )

        self.crear_boton(
            "Eliminar",
            "🗑️",
            None
        )

    # BOTONES

    def crear_boton(self, nombre, icono, comando):

        boton = ctk.CTkButton(
            self.sidebar,
            text=f"{icono}  {nombre}",
            height=46,
            corner_radius=10,
            fg_color=COLOR_PANEL,
            hover_color="#243E73",
            anchor="w",
            font=(FUENTE, 15),
            
            command=lambda: self.accion_boton(
                nombre,
                comando
            )
        )

        boton.pack(
            fill="x",
            padx=20,
            pady=6
        )

        self.botones[nombre] = boton

    # AREA PRINCIPAL

    def crear_area_principal(self):

        self.contenido = ctk.CTkFrame(
            self.ventana,
            fg_color=COLOR_FONDO,
            corner_radius=0
        )

        self.contenido.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # CAMBIO DE VISTAS

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_formulario(self):
        self.limpiar_contenido()

        formulario = FormularioProducto(
            self.contenido
        )

        formulario.pack(
            expand=True
        )

    # BOTON ACTIVO

    def accion_boton(self, nombre, comando):
        self.seleccionar_boton(nombre)
        if comando:
            comando()  
           
    def seleccionar_boton(self, nombre):
        for boton in self.botones.values():
            boton.configure(
                fg_color=COLOR_PANEL,
                hover_color="#243E73",
                text_color="white"
            )

        self.botones[nombre].configure(
            fg_color=COLOR_BOTON,
            hover_color=COLOR_BOTON_HOVER,
            text_color="white"
        )
        
        # INICIAR

    def iniciar(self):
        self.seleccionar_boton(
            "Agregar producto"
        )

        self.ventana.mainloop()