class Auto:
    # Guarda la marca y la velocidad máxima, y pone la velocidad actual en 0.
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca           # atributo privado
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    # obtiene velocidad
    # No permite modificarla, solo verla
    # Es un getter: permite consultar la velocidad actual del auto.
    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # método para acelerar
    # Aumenta la velocidad actual según el valor de aumento.
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

    # método para frenar
    # Reduce la velocidad actual según el valor de reduccion.
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion

auto1 = Auto("Toyota", 180)
auto2 = Auto("Maclaren",200)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

#Encapsulamiento
# _marca = variables privadas
# marca = variables que se pueden mandar a llamar declarando primero a la clase o funcion
# marca 