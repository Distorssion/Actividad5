from Habitacion import Habitacion


class Hotel:
    listaHabitaciones = []

    def __init__(self):
        Hotel.listaHabitaciones = [
            Habitacion(1, True, 120000),
            Habitacion(2, True, 120000),
            Habitacion(3, True, 120000),
            Habitacion(4, True, 120000),
            Habitacion(5, True, 120000),
            Habitacion(6, True, 160000),
            Habitacion(7, True, 160000),
            Habitacion(8, True, 160000),
            Habitacion(9, True, 160000),
            Habitacion(10, True,160000),
        ]

    def buscarFechaIngresoHabitacion(self, numero):
        for habitacion in self.listaHabitaciones:
            if habitacion.getNumeroHabitacion() == numero:
                huesped = habitacion.getHuesped()
                if huesped is not None:
                    return huesped.getFechaIngreso().strftime("%Y/%m/%d")
        return ""

    def buscarHabitacionOcupada(self, numero):
        for habitacion in self.listaHabitaciones:
            if habitacion.getNumeroHabitacion() == numero and not habitacion.getDisponible():
                return True
        return False