from random import randint
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from adivinhacao_tela import *


class Jogo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.computador = randint(1, 15)
        self.ui.pushButton.clicked.connect(self.funcao)

    @QtCore.pyqtSlot()
    def funcao(self):
        valor = int(self.ui.input_palpite.text())
        if valor > self.computador:
            self.ui.label_resultado.setText('MENOS')
        elif valor < self.computador:
            self.ui.label_resultado.setText('MAIS')
        else:
            self.ui.label_resultado.setText('ACERTOU')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    main_Adivinhação = Jogo()
    main_Adivinhação.show()
    qt.exec_()
