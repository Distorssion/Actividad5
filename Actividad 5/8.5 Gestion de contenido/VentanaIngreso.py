import tkinter as tki
from datetime import date
from tkinter import messagebox, font

from Huesped import Huesped


class VentanaIngreso(tki.Toplevel):
    def __init__(self, principal, hotel, numeroHabitacionReservada):
        super().__init__(principal)
        self.hotel = hotel
        self.numeroHabitacionReservada = numeroHabitacionReservada
        self.inicio()
        self.title("Ingreso")
        self.geometry("310x250")

    def inicio(self):
        negrita = font.Font(family="Helvetica", size=10, weight="bold")
        lblhab= tki.Label(self, text=f"Habitación: {self.numeroHabitacionReservada}", anchor="w")
        lblhab.place(x=20, y=20, width=270, height=23)

        lbldate= tki.Label(self, text="Fecha (aaaa-mm-dd):", anchor="w")
        lbldate.place(x=20, y=50, width=140, height=23)
        self.campoFechaIngreso = tki.Entry(self)
        self.campoFechaIngreso.place(x=165, y=50, width=125, height=23)

        lblhuesped = tki.Label(self, text="Huésped:", anchor="w", font = negrita)
        lblhuesped.place(x=20, y=90, width=140, height=23)

        lblnombre = tki.Label(self, text="Nombre:", anchor="w")
        lblnombre.place(x=20, y=110, width=140, height=23)
        self.campoNombre = tki.Entry(self)
        self.campoNombre.place(x=165, y=110, width=125, height=23)

        lblApe = tki.Label(self, text="Apellidos:", anchor="w")
        lblApe.place(x=20, y=140, width=140, height=23)
        self.campoApellidos = tki.Entry(self)
        self.campoApellidos.place(x=165, y=140, width=125, height=23)

        lblId = tki.Label(self, text="Doc. Identidad:", anchor="w")
        lblId.place(x=20, y=170, width=140, height=23)
        self.campoID = tki.Entry(self)
        self.campoID.place(x=165, y=170, width=125, height=23)

        btnAceptar = tki.Button(self, text="Aceptar", command=lambda: self.actionPerformed("aceptar"))
        btnAceptar.place(x=20, y=205, width=125, height=27)

        btnCancelar= tki.Button(self, text="Cancelar", command=lambda: self.actionPerformed("cancelar"))
        btnCancelar.place(x=165, y=205, width=125, height=27)

    def actionPerformed(self, opcion):
        if opcion == "aceptar":
            if self.hotel.buscarHabitacionOcupada(self.numeroHabitacionReservada):
                messagebox.showinfo("Mensaje", "La habitación está ocupada", parent=self)
                return

            fechaIngresada = self.campoFechaIngreso.get()
            try:
                fecha = date.fromisoformat(fechaIngresada)
                if fecha.isoformat() != fechaIngresada:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Mensaje", "La fecha no está en el formato solicitado (aaaa-mm-dd)", parent=self
                )
                return

            nombre = self.campoNombre.get().strip()
            apellidos = self.campoApellidos.get().strip()
            try:
                documento = int(self.campoID.get())
                if not nombre or not apellidos:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Error", "Campo nulo o error en formato de número", parent=self
                )
                return

            huesped = Huesped(nombre, apellidos, documento)
            huesped.setFechaIngreso(fecha)
            habitacion = self.hotel.listaHabitaciones[self.numeroHabitacionReservada - 1]
            habitacion.setHuesped(huesped)
            habitacion.setDisponible(False)
            messagebox.showinfo("Mensaje", "El huésped ha sido registrado", parent=self)
            self.destroy()
        elif opcion == "cancelar":
            self.destroy()