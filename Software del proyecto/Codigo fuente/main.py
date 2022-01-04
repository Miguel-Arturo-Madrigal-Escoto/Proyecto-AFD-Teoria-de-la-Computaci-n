from PySide2.QtWidgets import QApplication
from main_window import MainWindow
import sys

# Aplicación de Qt
app = QApplication()
"""Se crea una instancia a la clase MainWindow
que hereda de QMainWindow"""
window = MainWindow()
"""Se hace visible la ventana, show es un metodo
heredado de QMainWindow"""
window.show()
# Qt loop
sys.exit(app.exec_())