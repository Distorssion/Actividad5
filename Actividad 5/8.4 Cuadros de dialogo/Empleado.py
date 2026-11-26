# Ejercicio 8.4 "cuadros de dialogo" pag. 517 sin parte propuesta
from TipoCargo import TipoCargo
from TipoGenero import TipoGenero
class Empleado:
    def __init__(self, nombre:str,apellidos:str, salarioDia: float, otrosIngresos: float,pagosSalud:float,
                 diasTrabajados: int, aportePensiones:float, tipoCargo: TipoCargo =  None, tipoGenero: TipoGenero = None,):
        self.nombre = nombre
        self.apellidos = apellidos
        self.tCargo = tipoCargo 
        self.tGenero = tipoGenero
        self.salarioDia = salarioDia
        self.diasTrabajados = diasTrabajados
        self.otrosIngresos = otrosIngresos
        self.pagosSalud = pagosSalud
        self.aportePensiones = aportePensiones

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getCargo(self):
        return self.tCargo

    def getGenero(self):
        return self.tGenero

    def getSalarioDia(self):
        return self.salarioDia

    def getDiasTrabajados(self):
        return self.diasTrabajados

    def getOtrosIngresos(self):
        return self.otrosIngresos

    def getPagosSalud(self):
        return self.pagosSalud

    def getAportePensiones(self):
        return self.aportePensiones

    def calcularNomina(self):
        return (self.salarioDia * self.diasTrabajados + self.otrosIngresos - self.pagosSalud- self.aportePensiones)