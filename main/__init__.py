import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("mygui.ui", self)
        self.show()  # Conectamos todos los botones al mismo metodo para poder obtener el texto del boton que
        # que presionamos
        # Esto son todos los botones de la calculadora
        self.btn1.clicked.connect(lambda: self.veroperacion(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.veroperacion(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.veroperacion(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.veroperacion(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.veroperacion(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.veroperacion(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.veroperacion(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.veroperacion(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.veroperacion(self.btn9.text()))
        self.btn0.clicked.connect(lambda: self.veroperacion(self.btn0.text()))
        self.btn0.clicked.connect(lambda: self.veroperacion(self.btn0.text()))
        self.btnSumar.clicked.connect(lambda: self.veroperacion(self.btnSumar.text()))
        self.btnMultiplicar.clicked.connect(lambda: self.veroperacion(self.btnMultiplicar.text()))
        self.btnRestar.clicked.connect(lambda: self.veroperacion(self.btnRestar.text()))
        self.btnDividir.clicked.connect(lambda: self.veroperacion(self.btnDividir.text()))
        self.btnIgual.clicked.connect(self.resultado)
        self.operacion = ""

    def veroperacion(self, text):
        # Metodo para sacar la operacion por pantalla
        self.operacion += text
        self.txtOperacion.setText(self.operacion)

    def resultado(self):  # Este metodo recoge la informacion de lo que hemos pulsado en los botones y cuando
        # pulsamos en = lo que hace es, hacernos la operacion y nos pone el restulado abajo y nos reseta la
        # variable operacion
        result = eval(self.txtOperacion.toPlainText())
        self.txtResultado.setText(str(result) + " €")
        self.txtOperacion.setText("")
        self.operacion = ""


def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()


if __name__ == '__main__':
    main()
