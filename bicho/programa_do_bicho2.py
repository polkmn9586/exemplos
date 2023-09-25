# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programa_bicho1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(408, 336)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(Form)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(12)
        self.check_19 = QCheckBox(self.frame_3)
        self.check_19.setObjectName(u"check_19")
        sizePolicy1.setHeightForWidth(self.check_19.sizePolicy().hasHeightForWidth())
        self.check_19.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.check_19, 1, 3, 1, 1)

        self.check_11 = QCheckBox(self.frame_3)
        self.check_11.setObjectName(u"check_11")
        sizePolicy1.setHeightForWidth(self.check_11.sizePolicy().hasHeightForWidth())
        self.check_11.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.check_11, 1, 0, 1, 1)

        self.check_21 = QCheckBox(self.frame_3)
        self.check_21.setObjectName(u"check_21")
        sizePolicy1.setHeightForWidth(self.check_21.sizePolicy().hasHeightForWidth())
        self.check_21.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.check_21, 1, 4, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.check_16 = QCheckBox(self.frame_3)
        self.check_16.setObjectName(u"check_16")
        sizePolicy1.setHeightForWidth(self.check_16.sizePolicy().hasHeightForWidth())
        self.check_16.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.check_16, 1, 2, 1, 1)

        self.check_14 = QCheckBox(self.frame_3)
        self.check_14.setObjectName(u"check_14")
        sizePolicy1.setHeightForWidth(self.check_14.sizePolicy().hasHeightForWidth())
        self.check_14.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.check_14, 1, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dt_final = QLabel(self.frame_3)
        self.dt_final.setObjectName(u"dt_final")
        sizePolicy1.setHeightForWidth(self.dt_final.sizePolicy().hasHeightForWidth())
        self.dt_final.setSizePolicy(sizePolicy1)
        self.dt_final.setFont(font)
        self.dt_final.setLayoutDirection(Qt.RightToLeft)
        self.dt_final.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.dt_final, 0, 0, 1, 1)

        self.dt_inicio = QLabel(self.frame_3)
        self.dt_inicio.setObjectName(u"dt_inicio")
        sizePolicy1.setHeightForWidth(self.dt_inicio.sizePolicy().hasHeightForWidth())
        self.dt_inicio.setSizePolicy(sizePolicy1)
        self.dt_inicio.setFont(font)
        self.dt_inicio.setLayoutDirection(Qt.RightToLeft)
        self.dt_inicio.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.dt_inicio, 0, 1, 1, 1)

        self.comb_inicio = QComboBox(self.frame_3)
        self.comb_inicio.setObjectName(u"comb_inicio")
        sizePolicy1.setHeightForWidth(self.comb_inicio.sizePolicy().hasHeightForWidth())
        self.comb_inicio.setSizePolicy(sizePolicy1)
        self.comb_inicio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.comb_inicio, 1, 0, 1, 1)

        self.comb_final = QComboBox(self.frame_3)
        self.comb_final.setObjectName(u"comb_final")
        sizePolicy1.setHeightForWidth(self.comb_final.sizePolicy().hasHeightForWidth())
        self.comb_final.setSizePolicy(sizePolicy1)
        self.comb_final.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.comb_final, 1, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.push_g_sorteio = QPushButton(self.frame_2)
        self.push_g_sorteio.setObjectName(u"push_g_sorteio")
        sizePolicy1.setHeightForWidth(self.push_g_sorteio.sizePolicy().hasHeightForWidth())
        self.push_g_sorteio.setSizePolicy(sizePolicy1)
        self.push_g_sorteio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.push_g_sorteio)

        self.push_g_mais = QPushButton(self.frame_2)
        self.push_g_mais.setObjectName(u"push_g_mais")
        sizePolicy1.setHeightForWidth(self.push_g_mais.sizePolicy().hasHeightForWidth())
        self.push_g_mais.setSizePolicy(sizePolicy1)
        self.push_g_mais.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.push_g_mais)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.combo_g_sorteio = QComboBox(self.frame_2)
        self.combo_g_sorteio.setObjectName(u"combo_g_sorteio")
        sizePolicy1.setHeightForWidth(self.combo_g_sorteio.sizePolicy().hasHeightForWidth())
        self.combo_g_sorteio.setSizePolicy(sizePolicy1)
        self.combo_g_sorteio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.combo_g_sorteio)

        self.combo_g_mais = QComboBox(self.frame_2)
        self.combo_g_mais.setObjectName(u"combo_g_mais")
        sizePolicy1.setHeightForWidth(self.combo_g_mais.sizePolicy().hasHeightForWidth())
        self.combo_g_mais.setSizePolicy(sizePolicy1)
        self.combo_g_mais.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.combo_g_mais)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)
        self.label_7.setCursor(QCursor(Qt.WaitCursor))
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_7.setLineWidth(1)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.RightToLeft)
        self.label_8.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_8.setTextFormat(Qt.PlainText)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.line_data_amigo = QLineEdit(self.tab)
        self.line_data_amigo.setObjectName(u"line_data_amigo")
        sizePolicy1.setHeightForWidth(self.line_data_amigo.sizePolicy().hasHeightForWidth())
        self.line_data_amigo.setSizePolicy(sizePolicy1)
        self.line_data_amigo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.line_data_amigo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.push_amigo = QPushButton(self.tab)
        self.push_amigo.setObjectName(u"push_amigo")
        sizePolicy1.setHeightForWidth(self.push_amigo.sizePolicy().hasHeightForWidth())
        self.push_amigo.setSizePolicy(sizePolicy1)
        self.push_amigo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.push_amigo, 0, 0, 1, 2)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.RightToLeft)
        self.label_9.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_9.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_d_mais = QLabel(self.tab)
        self.label_d_mais.setObjectName(u"label_d_mais")
        sizePolicy1.setHeightForWidth(self.label_d_mais.sizePolicy().hasHeightForWidth())
        self.label_d_mais.setSizePolicy(sizePolicy1)
        self.label_d_mais.setFont(font)
        self.label_d_mais.setLayoutDirection(Qt.RightToLeft)
        self.label_d_mais.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_d_mais.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label_d_mais, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_12)

        self.line_ins_jogos = QLineEdit(self.tab_2)
        self.line_ins_jogos.setObjectName(u"line_ins_jogos")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_ins_jogos.sizePolicy().hasHeightForWidth())
        self.line_ins_jogos.setSizePolicy(sizePolicy2)
        self.line_ins_jogos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.line_ins_jogos)

        self.push_ins_jogos = QPushButton(self.tab_2)
        self.push_ins_jogos.setObjectName(u"push_ins_jogos")
        self.push_ins_jogos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.push_ins_jogos)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_10.addWidget(self.frame)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Determine a data dos jogos para consulta", None))
        self.check_19.setText(QCoreApplication.translate("Form", u"19", None))
        self.check_11.setText(QCoreApplication.translate("Form", u"11", None))
        self.check_21.setText(QCoreApplication.translate("Form", u"21", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Jogos Excluidos", None))
        self.check_16.setText(QCoreApplication.translate("Form", u"16", None))
        self.check_14.setText(QCoreApplication.translate("Form", u"14", None))
#if QT_CONFIG(tooltip)
        self.dt_final.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dt_final.setText(QCoreApplication.translate("Form", u" Data Final", None))
#if QT_CONFIG(tooltip)
        self.dt_inicio.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dt_inicio.setText(QCoreApplication.translate("Form", u"Data Inicial", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Resultado", None))
        self.push_g_sorteio.setText(QCoreApplication.translate("Form", u"Poss\u00edveis Grupos / Pr\u00f3ximo Sorteio", None))
        self.push_g_mais.setText(QCoreApplication.translate("Form", u"Grupos mais dados", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Jogo dos amigos sugest\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"data inicial do sorteio", None))
        self.line_data_amigo.setText("")
        self.push_amigo.setText(QCoreApplication.translate("Form", u"Enviar dados", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Grupos sugeridos", None))
#if QT_CONFIG(tooltip)
        self.label_d_mais.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_d_mais.setText(QCoreApplication.translate("Form", u"##########", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Form", u"Inserir jogos para o banco de jogos", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">oi</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"Copiar jogo", None))
        self.push_ins_jogos.setText(QCoreApplication.translate("Form", u"Enviar dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

