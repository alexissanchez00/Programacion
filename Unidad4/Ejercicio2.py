# -*- coding: utf-8 -*-
"""
Requisitos:
Comentar cuales son las librerias que se importan y para que funciona cada una.
"""

# Esta biblioteca proporciona acceso a variables y funciones
import sys

# Esta biblioteca se utiliza para obtener información sobre el sistema
# operativo en el que se está ejecutando el script.
import platform

# Esta biblioteca permite ejecutar nuevos procesos (comandos del sistema)
import subprocess

# Este módulo de PyQt5 contiene las clases base no gráficas,
# incluyendo el bucle de eventos, señales y ranuras 
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication, # - QApplication: Clase fundamental. Debe haber una instancia en cada
    QWidget, # - QWidget: La clase base para todos los objetos de interfaz de usuario.
    QLabel, # - QLabel: Un widget para mostrar texto o imágenes 
    QLineEdit, # - QLineEdit: Un widget de una sola línea para entrada de texto.
    QPushButton, # - QPushButton: Un widget de botón. Lo usamos para "Enviar ping".
    QTextEdit,# - QTextEdit: Un editor de texto multilínea. Lo usamos para mostrar la salida del ping. Lo hacemos de solo lectura.
    QVBoxLayout, # - QVBoxLayout: Un gestor de diseño que organiza los widgets en una columna vertical.
    QHBoxLayout,
    QMessageBox,# - QMessageBox: Un widget para mostrar cuadros de diálogo modales (mensajes de información, advertencia, error, etc.).
)

# ---------------------------------------------------------------------------
# -- CÓDIGO DE LA APLICACIÓN --
# ---------------------------------------------------------------------------

class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        # Usamos 'platform' para ver el sistema operativo
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]  # -n es para Windows
        else:  # Linux, macOS, etc.
            cmd = ["ping", "-c", "4", host]  # -c es para Unix-like

        try:
            # Usamos 'subprocess' para ejecutar el comando
            proceso = subprocess.run(
                cmd,
                capture_output=True,  # Captura stdout y stderr
                text=True,            # Decodifica la salida como texto (UTF-8)
                timeout=10,           # Tiempo límite de 10 segundos
            )
            # Muestra la salida estándar si el comando tuvo éxito (código 0)
            # o la salida de error si falló.
            salida = proceso.stdout if proceso.returncode == 0 else proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


if __name__ == "__main__":
    # 'sys.argv' es pasado a QApplication
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    # 'sys.exit' asegura que la aplicación se cierre correctamente
    sys.exit(app.exec_())