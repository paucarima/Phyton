from laptop_gaming import Lapto_Gaming
from laptop_Business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["D:\\Phyton\\class1\\img\\1.jpg",
                         "D:\\Phyton\\class1\\img\\2.jpg", "D:\\Phyton\\class1\\img\\3.jpg", "D:\\Phyton\\class1\\img\\4.jpg", "D:\\Phyton\\class1\\img\\5.jpg"]

        root.title("Ingresar Datos")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(
            row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(
            row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(
            row=2, column=1)

        ttk.Label(self.root, text="Tarjeta Gráfica").grid(row=3, column=0)
        self.tarj_graf = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarj_graf).grid(
            row=3, column=1)

        ttk.Label(self.root, text="Precio").grid(row=4, column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(
            row=4, column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=5, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(
            row=5, column=1)

        ttk.Label(self.root, text="Duración de Bateria").grid(row=6, column=0)
        self.duracion = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion).grid(
            row=6, column=1)

        ttk.Button(self.root, text="Agregar Laptop",
                   command=self.agregar_laptop).grid(row=7, column=0)

        self.mostrar_laptos = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptos.grid(row=8, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)

    def agregar_laptop(self):
        nueva_laptop = Lapto_Gaming(self.marca.get(), self.procesador.get(
        ), self.memoria.get(), self.tarj_graf.get(), self.precio.get())
        self.laptops.append(nueva_laptop)

        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(
        ), self.almacenamiento.get(), self.duracion.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptos.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aletorias()

    def mostrar_imagen_aletorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo
        pass


root = tk.Tk()
app = App(root)
root.mainloop()
