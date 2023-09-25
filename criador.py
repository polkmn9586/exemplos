import sys
from PySide6.QtCore import Slot,Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QTextEdit, QWidget,QGridLayout,QPushButton,QLabel,QLineEdit,QComboBox,QCheckBox
import sys
from pathlib import Path
from PySide6.QtGui import QIcon



class Criador(QWidget):
    def __init__(self):
        ...



    @Slot()
    def criar_Pushbutton(self,layout:QGridLayout,texto,x,y,funcao=None):
        nome = QPushButton(texto)
        nome.clicked.connect(funcao)
        layout.addWidget(nome, x, y)
        return nome

    @Slot()
    def criar_label(self,layout, texto=None, x=None, y=None,l=None,c=None):
        nome=QLabel(texto)
        layout.addWidget(nome, x, y,l,c)
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
    def criar_text_edit(self,layout:QGridLayout,textoInicial, x, y,l,c):
        nome = QTextEdit()
        nome.setText(textoInicial)
        nome.setVerticalScrollBarPolicy
        layout.addWidget(nome, x, y,l,c)
        return nome

    def criar_comboBox(self,layout:QGridLayout,lista,x,y,c=1,l=1):
        nome=QComboBox()
        nome.addItems(lista)


        layout.addWidget(nome,x,y,c,l)
        return nome



    @Slot()
    def adicionar_widgets(self,nome,l,c):
        self.lay.addWidget(nome, l, c)
    @Slot()
    def criar_checkBox(self,layout,titulo,x,y):
     nome = QCheckBox(titulo)
     layout.addWidget(nome, x, y)
     return nome
    @Slot()
    def ajustar_tela(self):
     self.adjustSize()
     self.setFixedSize(self.width(), self.height())

