class Habitacion:
    def __init__(self, numeroHabitacion: int, disponible: bool, precioDia: float):
        self.numeroHabitacion = numeroHabitacion
        self.disponible = disponible
        self.precioDia = precioDia
        self.huesped = None

    def getNumeroHabitacion(self):
        return self.numeroHabitacion
    def getDisponible(self):
        return self.disponible
    def getPrecioDia(self):
        return self.precioDia
    def getHuesped(self):
        return self.huesped

    
    def setHuesped(self, huesped):
        self.huesped = huesped
    def setDisponible(self, disponible):
        self.disponible = disponible
