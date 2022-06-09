from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel
import sys

class JogoVelha(QtWidgets.QMainWindow):
    def __init__(self):
        super(JogoVelha, self).__init__()

        # contador que verifica a vez do jogador
        self.cont = 0

        # abrir o arquivo
        self.jogo = uic.loadUi("tela.ui")

        # definindo os botões
        self.button1 = self.jogo.findChild(QPushButton, "btn1")
        self.button2 = self.jogo.findChild(QPushButton, "btn2")
        self.button3 = self.jogo.findChild(QPushButton, "btn3")
        self.button4 = self.jogo.findChild(QPushButton, "btn4")
        self.button5 = self.jogo.findChild(QPushButton, "btn5")
        self.button6 = self.jogo.findChild(QPushButton, "btn6")
        self.button7 = self.jogo.findChild(QPushButton, "btn7")
        self.button8 = self.jogo.findChild(QPushButton, "btn8")
        self.button9 = self.jogo.findChild(QPushButton, "btn9")
        self.button10 = self.jogo.findChild(QPushButton, "btn10")

        self.label = self.jogo.findChild(QLabel, "label")

        # clique dos botões
        self.button1.clicked.connect(self.clicker)
        self.button2.clicked.connect(self.clicker)
        self.button3.clicked.connect(self.clicker)
        self.button4.clicked.connect(self.clicker)
        self.button5.clicked.connect(self.clicker)
        self.button6.clicked.connect(self.clicker)
        self.button7.clicked.connect(self.clicker)
        self.button8.clicked.connect(self.clicker)
        self.button9.clicked.connect(self.clicker)
        #self.button10.clicked.connect(self.reset)

        # mostrar tela
        self.jogo.show()

    def verificar_vitoria(self):
        # horizontal
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.ganhou(self.button1, self.button4, self.button7)

        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.ganhou(self.button2, self.button5, self.button8)

        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.ganhou(self.button3, self.button6, self.button9)

        # vertical
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.ganhou(self.button1, self.button2, self.button3)

        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.ganhou(self.button4, self.button5, self.button6)

        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.ganhou(self.button7, self.button8, self.button9)

        # diagonal
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.ganhou(self.button1, self.button5, self.button9)

        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.ganhou(self.button3, self.button5, self.button7)

    def ganhou(self, a, b, c):
        # mudar a cor do botão
        a.setStyleSheet('QPushButton {color: red; background-color: transparent; font-size: 24px;}')
        b.setStyleSheet('QPushButton {color: red; background-color: transparent; font-size: 24px;}')
        c.setStyleSheet('QPushButton {color: red; background-color: transparent; font-size: 24px;}')

        # add o ganhador a label
        self.label.setText(f"{a.text()} ganhou!")


    # mudar o botão ao cliclar
    def clicker(self):
        b = self.sender()
        if self.cont % 2 == 0:
            b.setText('X')
            self.label.setText("Vez do jogador X")
        else:
            b.setText('O')
            self.label.setText("Vez do jogador O")

        b.setEnabled(False)
        self.cont += 1
        self.verificar_vitoria()
		

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu = MenuPrincipal()
    app.exec()



