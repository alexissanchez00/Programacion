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

# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
auto2 = Auto("Honda", "Civic", 2023, "Azul")
auto3 = Auto("Ford", "Mustang", 2021, "Negro")
auto4 = Auto("Chevrolet", "Spark", 2020, "Verde")
auto5 = Auto("Nissan", "Sentra", 2022, "Gris")
auto6 = Auto("Mazda", "CX-5", 2024, "Blanco")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(auto2)
print(auto3)
print(auto4)
print(auto5)
print(auto6)




