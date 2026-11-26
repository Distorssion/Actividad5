import tkinter as tki
from tkinter import messagebox, ttk, font

from VentanaIngreso import VentanaIngreso


class VentanaHabitaciones(tki.Toplevel):
    def __init__(self, principal, hotel):
        super().__init__(principal)
        self.principal = principal
        self.hotel = hotel
        self.inicio()
        self.title("Habitaciones")
        self.geometry("760x260")

    def inicio(self):
        #habitaciones 1-10
        cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight="bold")

        self.habitacion1 = tki.Label(self, text="Habitación 1",anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion1.place(x=20, y=30, width=130, height=23)
        self.disponibleHab1 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab1.place(x=42, y=55, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[0]
        if not habitacion.getDisponible():
            self.disponibleHab1.config(text="No disponible", font = cursiva, fg= "red")

        self.habitacion2 = tki.Label(self, text="Habitación 2", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion2.place(x=160, y=30, width=130, height=23)
        self.disponibleHab2 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab2.place(x=177, y=55, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[1]
        if not habitacion.getDisponible():
            self.disponibleHab2.config(text="No disponible", font =  cursiva, fg = "red")

        self.habitacion3 = tki.Label(self, text="Habitación 3", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion3.place(x=300, y=30, width=130, height=23)
        self.disponibleHab3 = tki.Label(self, text="Disponible", anchor="w", font =  cursiva, fg = "green3")
        self.disponibleHab3.place(x=317, y=55, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[2]
        if not habitacion.getDisponible():
            self.disponibleHab3.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion4 = tki.Label(self, text="Habitación 4", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion4.place(x=440, y=30, width=130, height=23)
        self.disponibleHab4 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab4.place(x=457, y=55, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[3]
        if not habitacion.getDisponible():
            self.disponibleHab4.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion5 = tki.Label(self, text="Habitación 5", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion5.place(x=580, y=30, width=135, height=23)
        self.disponibleHab5 = tki.Label(self, text="Disponible", anchor="w", font =  cursiva, fg = "green3")
        self.disponibleHab5.place(x=597, y=55, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[4]
        if not habitacion.getDisponible():
            self.disponibleHab5.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion6 = tki.Label(self, text="Habitación 6", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion6.place(x=20, y=120, width=130, height=23)
        self.disponibleHab6 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab6.place(x=42, y=145, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[5]
        if not habitacion.getDisponible():
            self.disponibleHab6.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion7 = tki.Label(self, text="Habitación 7", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion7.place(x=160, y=120, width=130, height=23)
        self.disponibleHab7 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab7.place(x=177, y=145, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[6]
        if not habitacion.getDisponible():
            self.disponibleHab7.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion8 = tki.Label(self, text="Habitación 8", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion8.place(x=300, y=120, width=130, height=23)
        self.disponibleHab8 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab8.place(x=317, y=145, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[7]
        if not habitacion.getDisponible():
            self.disponibleHab8.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion9 = tki.Label(self, text="Habitación 9", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion9.place(x=440, y=120, width=130, height=23)
        self.disponibleHab9 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab9.place(x=457, y=145, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[8]
        if not habitacion.getDisponible():
            self.disponibleHab9.config(text="No disponible", font = cursiva, fg = "red")

        self.habitacion10 = tki.Label(self, text="Habitación 10", anchor = "center", borderwidth="1", relief = "solid", font = cursiva)
        self.habitacion10.place(x=580, y=120, width=135, height=23)
        self.disponibleHab10 = tki.Label(self, text="Disponible", anchor="w", font = cursiva, fg = "green3")
        self.disponibleHab10.place(x=597, y=145, width=100, height=23)
        habitacion = self.hotel.listaHabitaciones[9]
        if not habitacion.getDisponible():
            self.disponibleHab10.config(text="No disponible", font = cursiva, fg = "red")


        self.habitacionSeleccionada = tki.Label(self, text="Número de habitación a reservar:", anchor="w")
        self.habitacionSeleccionada.place(x=150, y=210, width=180, height=23)

        self.campoHabitacionSeleccionada = ttk.Spinbox(self, from_=1, to=10, state="readonly")
        self.campoHabitacionSeleccionada.set(1)
        self.campoHabitacionSeleccionada.place(x=340, y=210, width=40, height=23)

        self.botonAceptar = tki.Button(self, text="Aceptar", command=self.actionPerformed)
        self.botonAceptar.place(x=433, y=210, width=100, height=23)

    def actionPerformed(self):
        habitacion = int(self.campoHabitacionSeleccionada.get())
        if self.hotel.buscarHabitacionOcupada(habitacion):
            messagebox.showinfo("Mensaje", "La habitación está ocupada", parent=self)
        else:
            VentanaIngreso(self.principal, self.hotel, habitacion)
            self.destroy()