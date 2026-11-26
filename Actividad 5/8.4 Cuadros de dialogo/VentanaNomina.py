
import tkinter as tki
from tkinter import ttk, font


class VentanaNomina(tki.Toplevel):
    def __init__(self, principal, lista):
        super().__init__(principal)
        self.lista = lista
        self.inicio()
        self.title("Nómina de Empleados")
        self.geometry("650x300")

    def inicio(self):
        negrita = font.Font(family="Helvetica", size=10, weight="bold")
        cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight="bold")
        lblListaemp=tki.Label(self, text="  Lista de empleados   ", anchor="w",borderwidth="1", relief = "solid", font = cursiva)
        lblListaemp.place(x=255, y=10, width=135,height=23)
        datos = self.lista.obtenerMatriz()
        titulos = ("Nombre", "Apellidos", "Sueldo")
        tabla = ttk.Treeview(self, columns=titulos, show="headings")
        for t in titulos:
            tabla.heading(t, text=t)
            tabla.column(t, width=103, anchor="w")
        for r in datos:
            tabla.insert("", tki.END, values=r)
        scroll = ttk.Scrollbar(self, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scroll.set)

        tabla.place(x=49, y=50, width=550, height=200)
        scroll.place(x=599, y=50, width=18, height=200)
        total = self.lista.calcularTotalNomina()
        totalMiles = f"{total:,.0f}".replace(",", ".")

        lblnomina =tki.Label(self, text=f"Total nomina mensual: $ {totalMiles}", anchor="w", font = negrita)
        lblnomina.place(x=300, y=257, width=250, height=23)