import os  # Importa el módulo os para interactuar con el sistema operativo
from PyQt5.QtGui import QIcon  # Importa la clase QIcon del módulo PyQt5.QtGui

def load_icon(icon_path):
    """
    Carga un ícono desde la ruta especificada.

    :param icon_path: Ruta relativa del ícono.
    :return: QIcon cargado desde la ruta absoluta del ícono.
    """
    script_dir = os.path.dirname(__file__)  # Obtiene el directorio del script actual
    icon_abs_path = os.path.join(script_dir, icon_path)  # Obtiene la ruta absoluta del ícono
    return QIcon(icon_abs_path)  # Retorna el ícono cargado desde la ruta absoluta

def format_result(result):
    """
    Formatea el resultado según su tipo.

    :param result: Resultado a formatear.
    :return: Resultado formateado como cadena.
    """
    if isinstance(result, float):  # Verifica si el resultado es de tipo float
        return str(int(result)) if result.is_integer() else str(result)  # Convierte y retorna el resultado como cadena
    return str(result)  # Retorna el resultado como cadena
