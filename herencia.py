class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo= modelo
    def conducir(self):
        print("El vehículo está en marcha")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color= color

    def abrir_maletero(self):
        print("El maletero está abierto")   

mi_auto = Automovil("Toyota", "Corolla", "Rojo")
print(mi_auto.marca)
mi_auto.conducir()
mi_auto.abrir_maletero()
print(mi_auto.color)