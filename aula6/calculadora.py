
import sys

import qdarktheme
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QGridLayout,QPushButton,QLabel
import sys
from pathlib import Path
from PySide6.QtGui import QIcon
from criador import  Menu
import qdarktheme

class Calculadora(Menu):
    def __init__(self,parent=None):
      super().__init__(parent=None)
      self.menu



app=QApplication(sys.argv)
qdarktheme.setup_theme("auto")
window=Calculadora()

window.show()
app.exec()