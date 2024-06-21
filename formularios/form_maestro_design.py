import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import datetime
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
import random

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Profesores: {self.nombre} {self.apellido}"

class Categoria:
    def __init__(self, nombre, apellido, salon):
        self.nombre = nombre
        self.apellido= apellido
        self.salon = salon

    def mostrar_info(self):
        return f"Asignaturas: {self.nombre , self.apellido, self.salon}"

class Libro:
    def __init__(self, titulo, autor, hora, isbn):
        self.titulo = titulo
        self.autor = autor
        self.hora = hora
        self.isbn = isbn

    def mostrar_info(self):
        return (f"Curso: {self.titulo}, Docente: {self.autor}, Horario: {self.hora} , ID: {self.isbn}")

class Usuario:
    def __init__(self, nombre,apellido, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.apellido =apellido

    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, ID: {self.id_usuario}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo - Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre} {self.usuario.apellido}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def registrar_profesor(self, autor):
        self.autor.append(autor)

    def devolver_libro(self, libro, usuario, fecha_devolucion):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario and prestamo.fecha_devolucion is None:
                prestamo.fecha_devolucion = fecha_devolucion
                return
    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        self.prestamos.append({
            "libro": libro,
            "usuario": usuario,
            "fecha_prestamo": fecha_prestamo
        })
    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join(libro.mostrar_info() for libro in self.libros)

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(usuario.mostrar_info() for usuario in self.usuarios)

    def mostrar_prestamos(self):
        if not self.autor:
            return "No se han asignado profesores."
        return "\n".join(autor.mostrar_info() for autor in self.autor)

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.init_data()
        self.logo = util_img.leer_imagen("./UML_2/imagenes/logo.png", (360, 460))
        self.perfil = util_img.leer_imagen("./UML_2/imagenes/Perfil.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def init_data(self):
        autores = [
            Autor("Jane", "Austen"),
            Autor("Mark", "Twain"),
            Autor("George", "Orwell"),
            Autor("Virginia", "Woolf"),
            Autor("F. Scott", "Fitzgerald"),
            Autor("J.K.", "Rowling"),
            Autor("J.R.R.", "Tolkien"),
            Autor("Agatha", "Christie"),
            Autor("Stephen", "King"),
            Autor("Haruki", "Murakami")
            
        ]

        categorias = [
            Categoria("Lucía", "Ramos", "001"),
            Categoria("Pablo", "Torres", "002"),
            Categoria("Claudia", "Vargas", "003"),
            Categoria("Francisco", "Vanegas", "004"),
            Categoria("Miguel", "Possada", "005")
        ]

        libros = [
            Libro("Física", "Jane", "6:00 - 9:00", "01"),
            Libro("Matemáticas", "Mark", "7:00 - 10:00", "02"),
            Libro("Química", "George", "8:00 - 11:00", "03"),
            Libro("Biología", "Virginia", "9:00 - 12:00", "04"),
            Libro("Historia", "F. Scott", "10:00 - 13:00", "05"),
            Libro("Geografía", "J.K.", "11:00 - 14:00", "06"),
            Libro("Literatura", "J.R.R.", "12:00 - 15:00", "07"),
            Libro("Arte", "Agatha", "13:00 - 16:00", "08"),
            Libro("Música", "Stephen", "14:00 - 17:00", "09"),
            Libro("Deporte", "Haruki", "15:00 - 18:00", "10")
        ]

        for libro in libros:
            self.biblioteca.registrar_libro(libro)

        usuarios = [
            Usuario("Carlos","Rodriguez" , 1),
            Usuario("Elena","Martinez" ,  2),
            Usuario("Pablo","Morales" , 3),
            Usuario("Laura", "Almeida" , 4),
            Usuario("Andrés", "Acuña" , 5),
            Usuario("Claudia", "Cardenas" ,  6),
            Usuario("Diego", "Florez" , 7),
            Usuario("Lucía", "Aveiro" , 8),
            Usuario("Javier", "Parada" , 9),
            Usuario("Natalia", "Gamboa" , 10)
        ]
        for usuario in usuarios:
            self.biblioteca.registrar_usuario(usuario)
    def on_enter(self, e):
        e.widget['background'] = COLOR_MENU_CURSOR_ENCIMA

    def on_leave(self, e):
        e.widget['background'] = COLOR_MENU_LATERAL
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("./UML_2/imagenes/logo.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="¡MENÚ GESTIÓN DE CURSOS!")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, wraplength=200)
        self.labelTitulo.pack(side=tk.LEFT, padx=(10, 0))

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                        command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelInfo = tk.Label(self.barra_superior, text="POOUP@unipamplona.co")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10)
        self.labelInfo.pack(side=tk.RIGHT, padx=(0, 10))
    def toggle_panel(self):
        # Alternar la visibilidad del menú lateral
        if self.menu_lateral.winfo_viewable():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        self.menuLateralBtns = []

        botones_info = [
            ("Inicio", self.mostrar_inicio),
            ("Cursos", self.mostrar_libros),
            ("Estudiantes", self.mostrar_usuarios),
            ("Profesores", self.mostrar_prestamos),
            ("Registrar un Curso", self.registrar_libro),
            ("Registrar un Estudiante", self.registrar_usuario),
            ("Asignar Estudiante", self.realizar_prestamo),
            ("Salir", self.destroy)
        ]

        for (text, command) in botones_info:
            btn = tk.Button(self.menu_lateral, text=text, bg=COLOR_MENU_LATERAL, fg="white", 
                            font=("Roboto", 13, "bold"), bd=0, padx=10, pady=10, width=ancho_menu, height=alto_menu,
                            command=command)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.pack()
            self.menuLateralBtns.append(btn)

    def controles_cuerpo(self):
        # Controles del cuerpo principal
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def mostrar_inicio(self):
        self.limpiar_cuerpo()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_libros(self):
        self.limpiar_cuerpo()
        info_libros = self.biblioteca.mostrar_libros()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_libros, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_usuarios(self):
        self.limpiar_cuerpo()
        info_usuarios = self.biblioteca.mostrar_usuarios()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_usuarios, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def mostrar_prestamos(self):
        self.limpiar_cuerpo()
        info_prestamos = self.biblioteca.mostrar_prestamos()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_prestamos, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def registrar_libro(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del Curso:", bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 14)).pack(pady=(10, 5))
        titulo_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        titulo_entry.pack()

        tk.Label(self.cuerpo_principal, text="Profesor:", bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 14)).pack(pady=(10, 5))
        autor_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        autor_entry.pack()

        tk.Label(self.cuerpo_principal, text="Horario:", bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 14)).pack(pady=(10, 5))
        hora_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        hora_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID:", bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        def submit():
            titulo = titulo_entry.get()
            autor = autor_entry.get()
            hora = hora_entry.get()
            isbn = isbn_entry.get()

            if titulo and autor and hora and isbn:
                nuevo_libro = Libro(titulo, autor, hora, isbn)
                self.biblioteca.registrar_libro(nuevo_libro)
                messagebox.showinfo("Éxito", "Curso registrado con éxito")
                self.mostrar_libros()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)



    def registrar_usuario(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del Estudiante:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="Apellido del Estudiante:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        apellido_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        apellido_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del Estudiante:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            id_usuario = int(id_entry.get())

            nuevo_usuario = Usuario(nombre, apellido, id_usuario)
            self.biblioteca.registrar_usuario(nuevo_usuario)
            messagebox.showinfo("Éxito", "Estudiante registrado con éxito")
            self.mostrar_usuarios()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)


    def realizar_prestamo(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="ID de la Asignatura:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        isbn_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        isbn_entry.pack()

        tk.Label(self.cuerpo_principal, text="ID del Estudiante:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        id_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        id_entry.pack()

        def submit():
            isbn = isbn_entry.get()
            id_usuario = int(id_entry.get())

            libro = next((l for l in self.biblioteca.libros if l.isbn == isbn), None)
            usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == id_usuario), None)

            if libro and usuario:
                fecha_prestamo = datetime.date.today().strftime("%Y-%m-%d")
                self.biblioteca.realizar_prestamo(libro, usuario, fecha_prestamo)
                messagebox.showinfo("Éxito", "Asignatura asignada  con éxito")
                self.mostrar_prestamos()
            else:
                messagebox.showerror("Error", "Curso o estudiante no encontrado")

        tk.Button(self.cuerpo_principal, text="Realizar Préstamo", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)


    def mostrar_prestamos(self):
        prestamos_info = self.biblioteca.mostrar_prestamos()
        self.limpiar_cuerpo()
        tk.Label(self.cuerpo_principal, text=prestamos_info, bg=COLOR_CUERPO_PRINCIPAL, font=("Roboto", 12)).pack(pady=10)




