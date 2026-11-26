import tkinter as tki
from tkinter import messagebox, simpledialog, font

from VentanaHabitaciones import VentanaHabitaciones
from VentanaSalida import VentanaSalida


class VentanaPrincipal(tki.Tk):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.inicio()
        self.title("Hotel")
        self.geometry("300x200")

    def inicio(self):
        barraMenu = tki.Menu(self)
        menuOpciones = tki.Menu(barraMenu, tearoff=False)
        menuOpciones.add_command(label="Consultar habitaciones", command=lambda: self.actionPerformed(1))
        menuOpciones.add_command(label="Salida de huéspedes", command=lambda: self.actionPerformed(2))
        barraMenu.add_cascade(label="Menú", menu=menuOpciones)
        self.config(menu=barraMenu)


        cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight="bold")
        titulo = tki.Label(text= "  Sistema de habitaciones  " ,anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        titulo.place(x=75,y=10)

        btn2 = tki.Button(self, text="Consultar habitaciones",command=lambda: self.actionPerformed(1), width=25)
        btn2.place(x=62, y=70)

        btn3 = tki.Button(self, text="Salida de huéspedes",command=lambda: self.actionPerformed(2), width=25)
        btn3.place(x=62, y=110)

    def actionPerformed(self, opcion):
        if opcion == 1:
            VentanaHabitaciones(self, self.hotel)
        elif opcion == 2:
            numeroHabitacion = simpledialog.askstring(
                "Salida de huéspedes", "Ingrese número de habitación", parent=self)
            if numeroHabitacion is None:
                return
            try:
                numero = int(numeroHabitacion)
            except ValueError:
                messagebox.showerror("Error", "Campo nulo o error en formato de número", parent=self)
                return

            if numero < 1 or numero > 10:
                messagebox.showinfo("Mensaje", "El número de habitación debe estar entre 1 y 10", parent=self)
            elif self.hotel.buscarHabitacionOcupada(numero):
                VentanaSalida(self, self.hotel, numero)
            else:
                messagebox.showinfo("Mensaje", "La habitación ingresada no ha sido ocupada", parent=self)
