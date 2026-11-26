import tkinter as tki
from tkinter import messagebox, ttk, font

from Empleado import Empleado
from TipoCargo import TipoCargo
from TipoGenero import TipoGenero


class VentanaAgregarEmpleado(tki.Toplevel):
    def __init__(self, principal, lista):
        super().__init__(principal)
        self.lista = lista
        self.inicio()
        self.title("Agregar Empleado")
        self.geometry("300x400")

    def inicio(self):
        negrita = font.Font(family="Helvetica", size=10, weight="bold")
        nomEmp = tki.Label(self, text="Nombre:", anchor="w", font = negrita)
        nomEmp.place(x=20, y=20, width=135, height=23)
        self.campoNombreEmp = tki.Entry(self)
        self.campoNombreEmp.place(x=120, y=20, width=150, height=23)

        apeEmp = tki.Label(self, text="Apellidos:", anchor="w", font = negrita)
        apeEmp.place(x=20, y=50, width=135, height=23)
        self.campoApellidos = tki.Entry(self)
        self.campoApellidos.place(x=120, y=50, width=150, height=23)

        cargoEmp = tki.Label(self, text="Cargo:", anchor="w", font = negrita)
        cargoEmp.place(x=20, y=80, width=135, height=23)
        self.campoCargo = ttk.Combobox(self, values=("Directivo", "Estratégico", "Operativo"), state="readonly")
        self.campoCargo.current(0)
        self.campoCargo.place(x=120, y=80, width=100, height=23)

        genEmp = tki.Label(self, text="Género:", anchor="w", font = negrita)
        genEmp.place(x=20, y=110, width=100, height=30)
        self.grupoGen = tki.StringVar(self, value="Masculino")
        tki.Radiobutton(
            self, text="Masculino", variable=self.grupoGen, value="Masculino", anchor="w"
        ).place(x=120, y=110, width=100, height=30)
        tki.Radiobutton(
            self, text="Femenino", variable=self.grupoGen, value="Femenino", anchor="w"
        ).place(x=120, y=140, width=100, height=30)

        dSalary=tki.Label(self, text="Salario por día:", anchor="w", font = negrita)
        dSalary.place(x=20, y=170, width=135, height=23)
        self.campoSalarioDia = tki.Entry(self)
        self.campoSalarioDia.place(x=160, y=170, width=100, height=23)

        wDays =tki.Label(self, text="Días trabajados al mes:", anchor="w", font = negrita)
        wDays.place(x=20, y=200, width=140, height=23)
        self.campowDays = ttk.Spinbox(self, from_=1, to=31)
        self.campowDays.set(30)
        self.campowDays.place(x=160, y=200, width=40, height=23)

        Ingresosvarios = tki.Label(self, text="Otros ingresos:", anchor="w", font = negrita)
        Ingresosvarios.place(x=20, y=230, width=135, height=23)
        self.campoOtrosIngresos = tki.Entry(self)
        self.campoOtrosIngresos.place(x=160, y=230, width=100, height=23)

        pSalud = tki.Label(self, text="Pagos por salud:", anchor="w",font = negrita)
        pSalud.place(x=20, y=260, width=135, height=23)
        self.campoAportesSalud = tki.Entry(self)
        self.campoAportesSalud.place(x=160, y=260, width=100, height=23)

        Aportes = tki.Label(self, text="Aportes pensiones:", anchor="w", font = negrita)
        Aportes.place(x=20, y=290, width=135, height=23)
        self.campoPensiones = tki.Entry(self)
        self.campoPensiones.place(x=160, y=290, width=100, height=23)

        btnAdd = tki.Button(self, text="Agregar", command=lambda: self.actionPerformed("agregar"))
        btnAdd.place(x=32, y=350, width=100, height=23)
        btnClear =tki.Button(self, text="Borrar", command=lambda: self.actionPerformed("limpiar"))
        btnClear.place(x=172, y=350, width=80, height=23)
    def limpiarCampos(self):
        self.campoNombreEmp.delete(0, tki.END)
        self.campoApellidos.delete(0, tki.END)
        self.campoSalarioDia.delete(0, tki.END)
        self.campowDays.set(0)
        self.campoOtrosIngresos.delete(0, tki.END)
        self.campoAportesSalud.delete(0, tki.END)
        self.campoPensiones.delete(0, tki.END)

    def actionPerformed(self, opción):
        if opción == "agregar":
            self.añadirEmpleado()
        elif opción == "limpiar":
            self.limpiarCampos()

    def añadirEmpleado(self):
        selección = self.campoCargo.get()
        if selección == "Directivo":
            cargo = TipoCargo.DIRECTIVO
        elif selección == "Estratégico":
            cargo = TipoCargo.ESTRATEGICO
        else:
            cargo = TipoCargo.OPERATIVO

        if self.grupoGen.get() == "Masculino":
            genero = TipoGenero.MASCULINO
        else:
            genero = TipoGenero.FEMENINO

        try:
            empleado = Empleado(
                nombre=self.campoNombreEmp.get(),
                apellidos=self.campoApellidos.get(),
                salarioDia=float(self.campoSalarioDia.get()),
                otrosIngresos=float(self.campoOtrosIngresos.get()),
                pagosSalud=float(self.campoAportesSalud.get()),
                diasTrabajados=int(self.campowDays.get()),
                aportePensiones=float(self.campoPensiones.get()),
                tipoCargo=cargo,
                tipoGenero=genero,
            )
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número", parent=self)
            return

        self.lista.agregarEmpleado(empleado)
        messagebox.showinfo("Mensaje", "El empleado ha sido agregado", parent=self)
        self.limpiarCampos()