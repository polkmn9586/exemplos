import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QComboBox, QCalendarWidget
from PySide6.QtCore import QFile
from shiboken6 import wrapInstance #wrapInstance
from datetime import datetime
from agenda_medica import Ui_MainWindow
from cadastro_salvo import Ui_Form

class Mensagem_cadastro_salvo(QWidget,Ui_Form):
    def __init__(self):
       super().__init__()
       self.setupUi(self)
       self.adjustSize()
       self.setFixedSize(self.width(),self.height())
       self.pushButton.clicked.connect(self.fechar)

    def fechar(self):
        self.abrir=ConsultaMedicaApp()
        self.abrir.show()
        self.close()
class ConsultaMedicaApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.carregar_dados()
        self.pushButton.clicked.connect(self.agendar_consulta)
        self.calendarWidget.selectionChanged.connect(self.atualizar_horas_disponiveis)
        self.pushButton_3.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    def carregar_dados(self):
        with open("dados.json", "r") as arquivo:
            self.dados = json.load(arquivo)

    def salvar_dados(self):
        with open("dados.json", "w") as arquivo:
            json.dump(self.dados, arquivo, indent=4)

    def atualizar_horas_disponiveis(self):
        dia_selecionado = self.calendarWidget.selectedDate().toString("yyyy-MM-dd") # recebe a data selecionarada
        dia_selecionado_data=datetime.strptime(dia_selecionado,"%Y-%m-%d")
        if dia_selecionado_data< datetime.now():
            self.pushButton.setEnabled(False)
        else:
            if dia_selecionado not in self.dados:
                self.dados[dia_selecionado]={
            "horas_disponiveis":["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"] ,
            "agendamentos": {}}
            self.pushButton.setEnabled(True)
            self.salvar_dados()
            horas_disponiveis = self.dados.get(dia_selecionado).get("horas_disponiveis")
            print(self.dados.get(dia_selecionado, {}))
            self.comboBox.clear()
            self.comboBox.addItems(horas_disponiveis)
        self.mensagem_cadastro_salvo = Mensagem_cadastro_salvo()
        self.mensagem_cadastro_salvo.show()
        self.close()
    def agendar_consulta(self):
        dia_selecionado = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.hora_selecionada = self.comboBox.currentText()

        # Coletar informações adicionais
        dados_agendamento = {
            "Dados de Nascimento": self.lineEdit_3.text(),
            "Número de Telefone": self.lineEdit_4.text(),
            "Gênero": self.lineEdit_5.text(),
            "E-mail": self.lineEdit.text(),
            "Plano de Saúde": self.comboBox_2.currentText(),
            "Número da Carteira do Plano": self.lineEdit_6.text()
        }

        # Verificar se o dia selecionado já possui informações de agendamento
        if dia_selecionado in self.dados:
            agendamentos = self.dados[dia_selecionado].get("agendamentos", {})
        else:
            agendamentos = {}

        # Verificar se a hora selecionada já foi agendada
        if self.hora_selecionada not in agendamentos:
            agendamentos[self.hora_selecionada] = dados_agendamento
            self.dados[dia_selecionado] = {
                "horas_disponiveis": self.atualizar_horas_disponiveis_agendamento(self.hora_selecionada),
                "agendamentos": agendamentos
            }
            self.atualizar_horas_disponiveis()
            self.salvar_dados()



    def atualizar_horas_disponiveis_agendamento(self, hora_agendada):
        dia_selecionado = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        horas_disponiveis = self.dados[dia_selecionado]["horas_disponiveis"]
        horas_disponiveis.remove(hora_agendada)
        return horas_disponiveis

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsultaMedicaApp()
    window.show()
    app.exec()
