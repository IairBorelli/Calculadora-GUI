from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QSizePolicy
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from calculator import Calculator
from utils import load_icon


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configurar la ventana principal
        self.setWindowTitle("Calculadora")  # Establecer el título de la ventana
        self.setGeometry(100, 100, 280, 575)  # Establecer la posición y el tamaño de la ventana
        self.setStyleSheet("background-color: rgb(37, 39, 41); border-radius: 15px;")  # Establecer el color de fondo de la ventana y redondear los bordes
        
        # Cargar el icono de la aplicación
        app_icon = load_icon("icono.ico")
        self.setWindowIcon(app_icon)
        
        # Crear el widget central y establecer el diseño vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        # Crear la instancia de la calculadora y agregarla al diseño
        self.calculator = Calculator()
        self.calculator.setStyleSheet("background-color: rgb(47, 49, 51); border: 2px solid white; border-radius: 10px; padding: 10px;")
        self.layout.addWidget(self.calculator)
        self.layout.setContentsMargins(10, 10, 10, 10)
    