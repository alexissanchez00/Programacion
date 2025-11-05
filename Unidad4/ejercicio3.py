# -*- coding: utf-8 -*-

# Agregar un atributo al objeto Alumno de Edad. Si es mayor de edad que imprima un mensaje
# (Nota: Se agrega el campo Edad a la GUI y la lógica de verificación)
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator  # Importar el validador de enteros
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        # Ajustamos el tamaño para el nuevo campo
        self.resize(350, 220) 

        # ------------------ Widgets ------------------
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")

        # --- NUEVO CAMPO: EDAD ---
        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Ej.: 21")
        # Añadimos un validador para que solo acepte números (ej. de 0 a 120)
        self.edad_edit.setValidator(QIntValidator(0, 120, self))
        # --- FIN NUEVO CAMPO ---

        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # ------------------ Layout -------------------
        form_layout = QVBoxLayout()

        # Nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)
        
        # --- NUEVO LAYOUT: EDAD ---
        fila_edad = QHBoxLayout()
        fila_edad.addWidget(QLabel("Edad:", self))
        fila_edad.addWidget(self.edad_edit)
        form_layout.addLayout(fila_edad)
        # --- FIN NUEVO LAYOUT ---

        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Ruta del archivo donde se guardarán los datos
        self.ruta_archivo = Path("alumnos.txt")

    # -------------------------------------------------
    def guardar_alumno(self):
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()
        # Obtenemos la edad como texto
        edad_str = self.edad_edit.text().strip()

        # Validamos que ningún campo esté vacío
        if not nombre or not carrera or not edad_str:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar el nombre, la carrera y la edad.",
            )
            return

        try:
            # Convertimos la edad a número
            edad_num = int(edad_str)
        except ValueError:
            QMessageBox.warning(
                self, "Error de formato", "La edad debe ser un número válido."
            )
            return
        
        mensaje_mayoria_edad = ""
        if edad_num >= 18:
            # Preparamos el mensaje
            mensaje_mayoria_edad = "El alumno es mayor de edad."
     
        linea = f"{nombre} – {carrera} – {edad_num} años\n"

        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        QMessageBox.information(
            self,
            "Guardado",
            f"Alumno guardado correctamente en '{self.ruta_archivo}'.",
        )
        
        if mensaje_mayoria_edad:
            QMessageBox.information(
                self, 
                "Verificación de Edad", 
                mensaje_mayoria_edad
            )

        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.edad_edit.clear() # Limpiamos el nuevo campo
        self.nombre_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())