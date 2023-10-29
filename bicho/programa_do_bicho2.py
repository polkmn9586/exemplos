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
    QPushButton, QRadioButton, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 683)
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
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(11, 11, 80, 20))
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setAlignment(Qt.AlignCenter)

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
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_12)

        self.line_ins_jogos = QLineEdit(self.tab_2)
        self.line_ins_jogos.setObjectName(u"line_ins_jogos")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_ins_jogos.sizePolicy().hasHeightForWidth())
        self.line_ins_jogos.setSizePolicy(sizePolicy3)
        self.line_ins_jogos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.line_ins_jogos)

        self.push_ins_jogos = QPushButton(self.tab_2)
        self.push_ins_jogos.setObjectName(u"push_ins_jogos")
        self.push_ins_jogos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.push_ins_jogos)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_18 = QVBoxLayout(self.tab_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.tab_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.lineEdit_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy6)

        self.verticalLayout_2.addWidget(self.label_18)

        self.radioButton_7 = QRadioButton(self.tab_3)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.verticalLayout_2.addWidget(self.radioButton_7)

        self.radioButton_6 = QRadioButton(self.tab_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_2.addWidget(self.radioButton_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout_2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_14.addWidget(self.label_4)

        self.radioButton_5 = QRadioButton(self.tab_3)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.tab_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_14.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_14.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.tab_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_14.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.tab_3)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_14.addWidget(self.radioButton)


        self.horizontalLayout_13.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_3.addWidget(self.label_19)

        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy5.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.lineEdit_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy7)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.lineEdit_6 = QLineEdit(self.tab_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy8)
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.lineEdit_7 = QLineEdit(self.tab_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(4)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy9)

        self.horizontalLayout_7.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.lineEdit_8 = QLineEdit(self.tab_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_12.addWidget(self.lineEdit_8)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.push_g_sorteio = QPushButton(self.tab_3)
        self.push_g_sorteio.setObjectName(u"push_g_sorteio")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.push_g_sorteio.sizePolicy().hasHeightForWidth())
        self.push_g_sorteio.setSizePolicy(sizePolicy10)
        self.push_g_sorteio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.push_g_sorteio)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_16.addLayout(self.verticalLayout)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_12 = QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.push_g_mais = QPushButton(self.tab_4)
        self.push_g_mais.setObjectName(u"push_g_mais")
        sizePolicy1.setHeightForWidth(self.push_g_mais.sizePolicy().hasHeightForWidth())
        self.push_g_mais.setSizePolicy(sizePolicy1)
        self.push_g_mais.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.push_g_mais)

        self.combo_g_mais = QComboBox(self.tab_4)
        self.combo_g_mais.setObjectName(u"combo_g_mais")
        sizePolicy1.setHeightForWidth(self.combo_g_mais.sizePolicy().hasHeightForWidth())
        self.combo_g_mais.setSizePolicy(sizePolicy1)
        self.combo_g_mais.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.combo_g_mais)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.tab_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.lineEdit = QLineEdit(self.tab_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.tab_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.lineEdit_2 = QLineEdit(self.tab_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.tab_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.tab_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_20 = QLabel(self.tab_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_20)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radioButton_8 = QRadioButton(self.tab_5)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_14.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.tab_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.radioButton_9.sizePolicy().hasHeightForWidth())
        self.radioButton_9.setSizePolicy(sizePolicy11)

        self.horizontalLayout_14.addWidget(self.radioButton_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_10.addWidget(self.pushButton)

        self.label_17 = QLabel(self.tab_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.textEdit = QTextEdit(self.tab_5)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_11.addWidget(self.textEdit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_10.addWidget(self.frame)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


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
        self.label_3.setText(QCoreApplication.translate("Form", u"POSS\u00cdVEIS GRUPOS", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"TIPO DE JOGO", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"TERNO", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"QUADRA", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"QUANTIDADE DE GRUPOS", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"3", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"5", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"6", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"7", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"VALOR PAGO", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"R$", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"VALOR INICIAL", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"VALOR FINAL", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"QUANTIDADE DE GRUPOS SORTEADOS", None))
        self.label_5.setText("")
        self.push_g_sorteio.setText(QCoreApplication.translate("Form", u"Poss\u00edveis Grupos / Pr\u00f3ximo Sorteio", None))
        self.label_8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Page", None))
        self.push_g_mais.setText(QCoreApplication.translate("Form", u"Grupos mais dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Page", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"VALOR INICIAL ", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"VALOR FINAL", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"QUANTIDADE DE GRUPOS SORTEADOS", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"TIPO DE JOGO", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"TERNO", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"QUADRA", None))
        self.label_16.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_17.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Page", None))
    # retranslateUi

