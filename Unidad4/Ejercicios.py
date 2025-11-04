# -*- coding: utf-8 -*-

class Alumno:
    #Agregar
    def __init__(self, nombre: str, numero_control: str, carrera=None):
        self.nombre = nombre                  # String: Nombre completo del alumno.
        self.numero_control = numero_control  # String: Identificador único del alumno.
        self.carrera = carrera                # Objeto Carrera: La carrera a la que está inscrito.
        self.calificaciones = {}              # Diccionario: Un diccionario para almacenar las calificaciones por materia.

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}")'


class Universidad:
    def __init__(self, nombre: str):
        self.nombre = nombre      # String: El nombre de la institución universitaria.
        self.carreras = []        # Lista: Una lista para almacenar los objetos Carrera que ofrece la universidad.
        self.alumnos = []         # Lista: Una lista para almacenar todos los objetos Alumno inscritos.
        self.profesores = []      # Lista: Una lista para almacenar los objetos Profesor que trabajan en la universidad.

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def __init__(self, nombre: str):
        self.nombre = nombre    # String: El nombre oficial de la carrera.
        self.materias = []    # Lista: Una lista para almacenar los objetos Materia que componen esta carrera.

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def __init__(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        self.nombre = nombre                # String: El nombre de la asignatura.
        self.carrera = carrera              # Objeto Carrera: La carrera a la que pertenece esta materia.
        self.calificacion_final = calificacion_final  # Float: Podría usarse para una calificación general.

    def __repr__(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def __init__(self, nombre: str, materia: Materia):
        self.nombre = nombre    # String: El nombre del profesor.
        self.materia = materia  # Objeto Materia: La materia específica que este profesor imparte.

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", {self.materia})'

if __name__ == "__main__":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001")
    luisa = Alumno("Luisa Gómez", "2023002")

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))   
    print(juan.consulta_calificacion("Física I"))   
    print(luisa.consulta_calificacion("Cálculo I")) 
    print(luisa.consulta_calificacion("Física I"))  

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])