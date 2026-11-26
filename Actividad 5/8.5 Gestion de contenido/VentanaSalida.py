import tkinter as tki
from datetime import date
from tkinter import messagebox


class VentanaSalida(tki.Toplevel):
    def __init__(self, principal, hotel, numero):
        super().__init__(principal)
        self.hotel = hotel
        self.numeroHabitacion = numero
        self.posicionHabitacion = numero - 1
        self.habitacionOcupada = hotel.listaHabitaciones[self.posicionHabitacion]
        self.huesped = self.habitacionOcupada.getHuesped()
        self.inicio()
        self.title("Salida huéspedes")
        self.geometry("280x285")

    def inicio(self):
        lblHab = tki.Label(self, text=f"Habitación: {self.numeroHabitacion}")
        lblHab.place(x=20, y=15, width=240, height=23)
        fecha = self.hotel.buscarFechaIngresoHabitacion(self.numeroHabitacion)
        
        lblInDate = tki.Label(self, text=f"Fecha de ingreso: {fecha}", anchor="w")
        lblInDate.place(x=20, y=45, width=240, height=23)

        lbloutDate = tki.Label(self, text="Fecha de salida (aaaa-mm-dd):", anchor="w")
        lbloutDate.place(x=20, y=75, width=240, height=23)

        self.fechaSalida = tki.StringVar(self)
        self.campoFechaSalida = tki.Entry(self, textvariable=self.fechaSalida)
        self.campoFechaSalida.place(x=20, y=105, width=240, height=23)

        btnCalcular = tki.Button(self, text="Calcular", command=lambda: self.actionPerformed("calcular"))
        btnCalcular.place(x=20, y=135, width=240, height=25)

        self.cantidadDias = tki.Label(self, text="Cantidad de días:", anchor="w")
        self.cantidadDias.place(x=20, y=165, width=240, height=23)

        self.totalPago = tki.Label(self, text="Total: $", anchor="w")
        self.totalPago.place(x=20, y=195, width=240, height=23)

        self.registrarSalida = tki.Button(
            self,
            text="Registrar salida",
            state="disabled",
            command=lambda: self.actionPerformed("registrarSalida"),
        )
        self.registrarSalida.place(x=20, y=225, width=240, height=25)

        self.fechaSalida.trace_add("write", self.limpiarCalculo)

    def limpiarCalculo(self, *_):
        self.cantidadDias.config(text="Cantidad de días:")
        self.totalPago.config(text="Total: $")
        self.registrarSalida.config(state="disabled")

    def actionPerformed(self, opcion):
        if self.habitacionOcupada.getHuesped() is not self.huesped:
            messagebox.showerror("Mensaje", "La ocupación de la habitación cambió", parent=self)
            self.destroy()
            return

        if opcion == "calcular":
            fechaS = self.campoFechaSalida.get()
            try:
                fecha2 = date.fromisoformat(fechaS)
                if fecha2.isoformat() != fechaS:
                    raise ValueError
            except ValueError:
                messagebox.showerror(
                    "Mensaje", "La fecha no está en el formato solicitado (aaaa-mm-dd)", parent=self
                )
                return

            fecha1 = self.huesped.getFechaIngreso()
            if fecha2 <= fecha1:
                messagebox.showerror(
                    "Mensaje", "La fecha de salida debe ser posterior a la de ingreso", parent=self
                )
                return

            self.huesped.setFechaSalida(fecha2)
            cantidad = self.huesped.getDiasAlojamiento()
            valor = cantidad * self.habitacionOcupada.getPrecioDia()
            self.cantidadDias.config(text=f"Cantidad de días: {cantidad}")
            self.totalPago.config(text=f"Total: ${valor}")
            self.registrarSalida.config(state="normal")
        elif opcion == "registrarSalida":
            self.habitacionOcupada.setHuesped(None)
            self.habitacionOcupada.setDisponible(True)
            messagebox.showinfo("Mensaje", "Se ha registrado la salida del huésped", parent=self)
            self.destroy()
