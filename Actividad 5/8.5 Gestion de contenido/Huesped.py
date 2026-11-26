class Huesped:
    def __init__(self, nombres: str, apellidos: str, documentoIdentidad: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documentoIdentidad = documentoIdentidad
        self.fechaIngreso = None
        self.fechaSalida = None

    def setFechaSalida(self, fecha):
        self.fechaSalida = fecha
    def setFechaIngreso(self, fecha):
        self.fechaIngreso = fecha

    def getFechaIngreso(self):
        return self.fechaIngreso
    def getDiasAlojamiento(self):
        return (self.fechaSalida - self.fechaIngreso).days