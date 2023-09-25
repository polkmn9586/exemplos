import sys
from PySide6.QtCore import Slot,Qt
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QGridLayout,QPushButton,QLabel,QLineEdit
import sys
from pathlib import Path
from PySide6.QtGui import QIcon



class Criador(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.center_widget=QWidget()
        self.lay=QGridLayout()
        self.setCentralWidget(self.center_widget)
        self.center_widget.setLayout(self.lay)


    @Slot()
    def criar_Pushbutton(self,layout:QGridLayout,texto,x,y,funcao=None):
        nome = QPushButton(texto)
        nome.clicked.connect(funcao)
        layout.addWidget(nome, x, y)
        return nome

    @Slot()
    def criar_label(self,layout, texto, x, y):
        nome=QLabel(texto)
        layout.addWidget(nome, x, y)
        return nome
    def estilo_label(self,nome:QLabel,larguraM=None,alturaM=None, maresquerda=None,marcima=None,mardireita=None,marbaixo=None):
        nome.setMinimumWidth(larguraM)
        nome.setMinimumHeight(alturaM)
        nome.setContentsMargins(maresquerda,marcima,mardireita,marbaixo)
        nome.setAlignment(Qt.AlignmentFlag.AlignRight,Qt.AlignmentFlag.AlignTop)

    @Slot()
    def criar_line(self, layout:QGridLayout, x, y, l, c):
        nome = QLineEdit()
        nome.setStyleSheet("font-color: Blue ; font-size:10px")
        nome.setAlignment(Qt.AlignmentFlag.AlignRight)
        nome.setMinimumHeight(30)
        nome.setMinimumWidth(100)
        nome.setTextMargins(5,5,5,5)
        layout.addWidget(nome, x, y,l,c)
        return nome


    @Slot()
    def adicionar_widgets(self,nome,l,c):
        self.lay.addWidget(nome, l, c)

    @Slot()
    def ajustar_tela(self):
     self.adjustSize()
     self.setFixedSize(self.width(), self.height())


class Menu(Criador):
    def __init__(self,parent):
        super().__init__(parent)
    @property
    def menu(self):
        self.criar_line(self.lay, 1, 1, 1, 4)
        self.criar_Pushbutton(self.lay,"1", 2, 1)
        self.criar_Pushbutton(self.lay,"2", 2, 2)
        self.criar_Pushbutton(self.lay,"3", 2, 3)
        self.criar_Pushbutton(self.lay,"+", 2, 4)
        self.criar_Pushbutton(self.lay,"4", 3, 1)
        self.criar_Pushbutton(self.lay,"5", 3, 2)
        self.criar_Pushbutton(self.lay,"6", 3, 3)
        self.criar_Pushbutton(self.lay,"-", 3, 4)
        self.criar_Pushbutton(self.lay,"7", 4, 1)
        self.criar_Pushbutton(self.lay,"8", 4, 2)
        self.criar_Pushbutton(self.lay,"9", 4, 3)
        self.criar_Pushbutton(self.lay,"*", 4, 4)
        self.criar_Pushbutton(self.lay,"C", 5, 1)
        self.criar_Pushbutton(self.lay,"AC", 5, 2)
        self.criar_Pushbutton(self.lay,"=", 5, 3)
        self.criar_Pushbutton(self.lay,"/", 5, 4)
        self.ajustar_tela()
        return None