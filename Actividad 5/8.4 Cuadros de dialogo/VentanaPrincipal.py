import tkinter as tki
from tkinter import filedialog, messagebox, font

from ListaEmpleados import ListaEmpleados
from VentanaAgregarEmpleado import VentanaAgregarEmpleado
from VentanaNomina import VentanaNomina


class VentanaPrincipal(tki.Tk):
    def __init__(self):
        super().__init__()
        self.empleados = ListaEmpleados()
        self.inicio()
        self.title("Nomina")
        self.geometry("300x200")

    def inicio(self):
        barraMenu = tki.Menu(self)
        menuOpciones = tki.Menu(barraMenu, tearoff=False)
        menuOpciones.add_command(label="Agregar empleado", command=lambda: self.actionPerformed(1))
        menuOpciones.add_command(label="Calcular nómina", command=lambda: self.actionPerformed(2))
        menuOpciones.add_separator()
        menuOpciones.add_command(label="Guardar archivo", command=lambda: self.actionPerformed(3))
        barraMenu.add_cascade(label="Menú", menu=menuOpciones)
        self.config(menu=barraMenu)

        cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight="bold")
        titulo = tki.Label(text= "  Opciones de Nomina  " ,anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        titulo.place(x=82,y=10)
        btn1 = tki.Button(self, text="Agregar empleado",command=lambda: self.actionPerformed(1), width=25)
        btn1.place(x=62, y=50)

        btn2 = tki.Button(self, text="Calcular nómina",command=lambda: self.actionPerformed(2), width=25)
        btn2.place(x=62, y=90)

        btn3 = tki.Button(self, text="Guardar archivo",command=lambda: self.actionPerformed(3), width=25)
        btn3.place(x=62, y=130)

    def actionPerformed(self, op):
        if op == 1:
            VentanaAgregarEmpleado(self, self.empleados)
        elif op == 2:
            VentanaNomina(self, self.empleados)
        elif op == 3:
            carpeta = filedialog.askdirectory(parent=self, mustexist=True)
            if not carpeta:
                return

            ruta = f"{carpeta}/ArchivoNomina.txt"
            try:
                texto = self.empleados.convertirTexto()
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(texto)
            except OSError as error:
                messagebox.showerror("Error al guardar", str(error), parent=self)
                return

            messagebox.showinfo("Archivo guardado", ruta, parent=self)