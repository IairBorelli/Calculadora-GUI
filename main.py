# Importamos el módulo sys para interactuar con el sistema operativo
import sys

# Importamos la clase QApplication desde el módulo QtWidgets de PyQt5 para manejar la aplicación
from PyQt5.QtWidgets import QApplication

# Importamos la clase CalculatorWindow desde un archivo llamado gui para crear la ventana de la calculadora
from gui import CalculatorWindow

# Verificamos si el script se está ejecutando directamente
if __name__ == "__main__":
    # Creamos una instancia de la aplicación QApplication, pasando los argumentos del sistema
    app = QApplication(sys.argv)
    # Creamos una instancia de la ventana de la calculadora
    calc_window = CalculatorWindow()
    # Mostramos la ventana de la calculadora en pantalla
    calc_window.show()
    # Salimos de la aplicación cuando se cierra la ventana, devolviendo el código de salida de la aplicación
    sys.exit(app.exec_())
    