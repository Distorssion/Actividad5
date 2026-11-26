from Hotel import Hotel
from VentanaPrincipal import VentanaPrincipal


class Principal:
    def main():
        hotel = Hotel()
        ventana = VentanaPrincipal(hotel)
        ventana.mainloop()

if __name__ == "__main__":
    Principal.main()