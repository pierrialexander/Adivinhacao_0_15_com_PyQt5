# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Adivinhacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(302, 206)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_palpite = QtWidgets.QLineEdit(self.centralwidget)
        self.input_palpite.setGeometry(QtCore.QRect(10, 60, 281, 41))
        self.input_palpite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.input_palpite.setObjectName("input_palpite")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(20, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(11)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 120, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(46, 255, 242);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton.setObjectName("pushButton")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(10, 130, 141, 51))
        self.label_resultado.setStyleSheet("font: 30pt \"DFPOP1-W9\";")
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo da Adivinhação!"))
        self.titulo.setText(_translate("MainWindow", "Entre 0 e 15! Qual o valor?"))
        self.pushButton.setText(_translate("MainWindow", "TENTAR"))