from Empleado import Empleado

class ListaEmpleados:
    def __init__(self):
        self.listaEmp = []
        self.totalNomina = 0

    def agregarEmpleado(self,empleado: Empleado):
        self.listaEmp.append(empleado)

    def calcularTotalNomina(self):
        total = 0.0
        for empleado in self.listaEmp:
            total += empleado.calcularNomina()
        return total

    def obtenerMatriz(self):
        datos = []
        for empleado in self.listaEmp:
            sueldo = empleado.calcularNomina()
            datos.append([
                empleado.getNombre(),
                empleado.getApellidos(),
                f"{sueldo:,.0f}".replace(",", "."),
            ])
        return datos

    def convertirTexto(self):
        texto = ""

        for empleado in self.listaEmp:
            texto += (
                f"Nombre: {empleado.getNombre()}\n"
                f"Apellidos: {empleado.getApellidos()}\n"
                f"Cargo: {empleado.getCargo().name}\n"
                f"Género: {empleado.getGenero().name}\n"
                f"Salario por día: ${empleado.getSalarioDia():.2f}\n"
                f"Días trabajados: {empleado.getDiasTrabajados()}\n"
                f"Otros ingresos: ${empleado.getOtrosIngresos():.2f}\n"
                f"Pagos por salud: ${empleado.getPagosSalud():.2f}\n"
                f"Aportes a pensiones: ${empleado.getAportePensiones():.2f}\n"
                "-------------------------------------------------------------"
                "\n"
            )
        texto += f"Total de la nómina: ${self.calcularTotalNomina():.2f}\n"
        return texto
