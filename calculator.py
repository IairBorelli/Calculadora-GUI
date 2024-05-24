# Importación de módulos necesarios
import re
import datetime
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from utils import format_result

# Clase principal para la calculadora
class Calculator(QWidget):
    def __init__(self):
        # Inicialización de la clase padre
        super().__init__()
        # Creación de la estructura de la ventana
        self.layout = QVBoxLayout(self)

        # Creación del campo de entrada para la expresión matemática
        self.display = QLineEdit()
        self.display.setFixedHeight(80)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Fira Code Retina",20))
        self.display.setStyleSheet("background-color: rgb(37, 39, 41); color: white; border: none;")
        self.layout.addWidget(self.display)

        # Creación del campo de historia para mostrar los resultados anteriores
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setStyleSheet("background-color: rgb(37, 39, 41); color: white; border: none;")
        self.layout.addWidget(self.history_display)

        # Creación de los botones para la entrada de la expresión matemática
        buttons = [
            ('C', '(', ')', '<'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('.', '0', '=', '+'),
        ]

        # Creación de la estructura de la ventana con botones
        grid_layout = QGridLayout()
        grid_layout.setSpacing(4)

        for row_idx, row in enumerate(buttons):
            for col_idx, label in enumerate(row):
                if label:
                    # Creación de un botón con el texto correspondiente
                    button = QPushButton(label)
                    # Asignación de la función a llamar cuando se hace clic en el botón
                    button.clicked.connect(lambda _, label=label: self.button_clicked(label))
                    button.setStyleSheet("background-color: rgb(14, 15, 15); color: white; border: none; font-size: 20px;")
                    button.setFixedSize(60, 60)
                    grid_layout.addWidget(button, row_idx, col_idx)
                else:
                    # Agregación de un espacio vacío en la estructura para mantener la alineación
                    grid_layout.addItem(QSpacerItem(60, 60), row_idx, col_idx)

        # Agregación de la estructura de botones a la ventana
        self.layout.addLayout(grid_layout)

        # Asignación de la función para validar la entrada del usuario
        self.display.textChanged.connect(self.validate_input)
        # Inicialización de la lista para almacenar la historia de operaciones
        self.history = []

    # Función para validar la entrada del usuario
    def validate_input(self):
        # Obtención del texto actual en el campo de entrada
        text = self.display.text()
        # Reemplazo de caracteres no numéricos o operadores por nada
        self.display.setText(''.join(c for c in text if c.isdigit() or c in './*-+()C<>='))
        # Movimiento del cursor al final del texto actualizado
        self.display.setCursorPosition(len(self.display.text()))

    # Función para formatear el resultado de una operación
    def format_result(self, result):
        # Si el resultado es un número flotante, lo convierte a entero si es posible
        if isinstance(result, float):
            return str(int(result)) if result.is_integer() else str(result)
        # Si el resultado no es un número, lo devuelve como cadena
        return str(result)

    # Función para manejar el clic en un botón
    def button_clicked(self, clicked_button):
        # Obtención del texto actual en el campo de entrada
        current_text = self.display.text()

        if clicked_button == '=':
            # Evaluación de la expresión matemática y actualización del campo de entrada
            try:
                result = eval(current_text)
                formatted_result = self.format_result(result)
                self.display.setText(formatted_result)
                # Agregación del resultado a la historia
                self.history.append(f"{current_text} = {formatted_result}")
                # Actualización del campo de historia
                self.update_history_display()
            except (ZeroDivisionError, SyntaxError) as e:
                # Mostrar un mensaje de error si la expresión es inválida
                QMessageBox.critical(self, "Error", str(e))
        elif clicked_button == 'C':
            # Limpieza de la historia y campo de entrada
            self.clear_history()
            self.display.setText("")
        elif clicked_button == '<':
            # Eliminación del último carácter del campo de entrada
            self.display.setText(current_text[:-1])
        else:
            # Agregación del texto del botón al campo de entrada
            self.display.setText(current_text + clicked_button)

    # Función para limpiar la historia
    def clear_history(self):
        # Limpieza de la lista de historia
        self.history = []
        # Actualización del campo de historia
        self.update_history_display()

    # Función para manejar la entrada de teclas
    def keyPressEvent(self, event):
        # Creación de un diccionario para mapear las teclas a los botones correspondientes
        key_mapping = {
            Qt.Key_Return: '=',
            Qt.Key_Enter: '=',
            Qt.Key_Backspace: '<',
            Qt.Key_Escape: 'C',
            Qt.Key_Plus: '+',
            Qt.Key_Minus: '-',
            Qt.Key_Asterisk: '*',
            Qt.Key_Slash: '/',
            Qt.Key_Period: '.',
            Qt.Key_0: '0',
            Qt.Key_1: '1',
            Qt.Key_2: '2',
            Qt.Key_3: '3',
            Qt.Key_4: '4',
            Qt.Key_5: '5',
            Qt.Key_6: '6',
            Qt.Key_7: '7',
            Qt.Key_8: '8',
            Qt.Key_9: '9',
            Qt.Key_ParenLeft: '(',
            Qt.Key_ParenRight: ')',
        }

        # Obtención de la tecla presionada
        key = event.key()
        # Obtención del texto correspondiente a la tecla presionada
        text = key_mapping.get(key)
        if text:
            # Llamada a la función para manejar el clic en un botón con el texto correspondiente
            self.button_clicked(text)

    # Función para actualizar el campo de historia
    def update_history_display(self):
        # Limpieza del campo de historia
        self.history_display.clear()
        # Agregación de la historia a la ventana
        self.history_display.setPlainText("\n".join(self.history))
        # Configuración del tamaño de la fuente del campo de historia
        self.history_display.setFont(QFont("Fira Code Retina", 14))
        