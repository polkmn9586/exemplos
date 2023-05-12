from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QHBoxLayout,QLabel,QPushButton
from PySide6.QtGui import QPixmap
import sys
import requests




app=QApplication(sys.argv)

window=QMainWindow()
janela=QWidget()
layout=QHBoxLayout()
window.setCentralWidget(janela)
janela.setLayout(layout)

label=QLabel()
def imagem1():

    imagem=QPixmap("C:/Users/merca/OneDrive/Área de Trabalho/images13.jpeg")
    label.setPixmap(imagem)
    label.setFixedSize(50,50)
    label.setScaledContents(True)
    layout.addWidget(label)

but=QPushButton("Imagem")
but.clicked.connect(imagem1)
layout.addWidget(but)







window.show()
app.exec()



