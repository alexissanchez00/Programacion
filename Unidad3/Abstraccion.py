from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass

class Moto(Vehiculo):
    pass

class Camion(Vehiculo):
    pass

class Camioneta(Vehiculo):
    pass

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
auto2 = Moto("Kawasaki", "Ninja ZX-6R", 2023, "Verde")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
moto2 = Moto("Suzuki", "GSX-R750", 2022, "Azul")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
camion2 = Camion("Mercedes-Benz", "Actros", 2021, "Gris")
camioneta1 = Camioneta("Jeep", "Cherokee", 2023, "Verde")
camioneta2 = Camioneta("Toyota", "Hilux", 2022, "Roja")

# Visualización
print(auto1)
print(auto2)
print(moto1)
print(moto2)
print(camion1)
print(camion2)
print(camioneta1)
print(camioneta2)








