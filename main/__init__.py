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
        self.btnModo.clicked.connect(lambda: self.cambiomodo(self.btnModo.text()))
        self.operacion = ""
        self.load()
        # Añadir zapatillas a la tabla

        self.btnAnadir.clicked.connect(self.save)
        # Boton para cambiar modo de oscuro a claro y de claro a oscuro

    def veroperacion(self, text):
        # Metodo para sacar la operacion por pantalla
        self.operacion += text
        self.txtOperacion.setText(self.operacion)

    def resultado(self):  # Este metodo recoge la informacion de lo que hemos pulsado en los botones y cuando
        # pulsamos en = lo que hace es, hacernos la operacion y nos pone el restulado abajo y nos reseta la
        # variable operacion

        # el eval lo que hace es coger una expresion y la hace matematicamente
        result = eval(self.txtOperacion.toPlainText())
        self.txtResultado.setText(str(result) + " €")
        self.txtOperacion.setText("")
        self.operacion = ""

    def cambiomodo(self, text):
        # Falta el cambio de los botones y de la calculadora las pantallas
        if text == "Modo oscuro":
            self.btnModo.setText("Modo claro")
            self.calculadora.setStyleSheet("background-color: #2596be;")
            self.pantalla.setStyleSheet("background-color: #13173E;")
        else:
            self.calculadora.setStyleSheet("background-color: white;")
            self.pantalla.setStyleSheet("background-color: #F5F4B9;")
            self.btnModo.setText("Modo oscuro")

    def load(self):  # LLenamos la tabla
        products = [
            {'marca': 'Nike', 'talla': '39', 'precio': '100'},
            {'marca': 'Nike', 'talla': '42', 'precio': '80'},
            {'marca': 'Adidas', 'talla': '33', 'precio': '60'},
            {'marca': 'Adidas', 'talla': '39', 'precio': '105'},
            {'marca': 'Reebok', 'talla': '44', 'precio': '40'},
            {'marca': 'New balance', 'talla': '38', 'precio': '80'},
            {'marca': 'Joma', 'talla': '40', 'precio': '99'},
            {'marca': 'Vans', 'talla': '39', 'precio': '70'},
        ]
        self.table.setRowCount(len(products))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(('Marca', 'talla', 'Precio'))

        index = 0
        for product in products:
            self.table.setItem(index, 0, QTableWidgetItem(product['marca']))
            self.table.setItem(index, 1, QTableWidgetItem(product['talla']))
            self.table.setItem(index, 2, QTableWidgetItem(product['precio']))
            index += 1

    def save(self):  # Metodo para añadir registros a la tabla, una vez añadido vacia los campos
        marca = self.txtMarca.text()
        talla = self.txtTalla.text()
        precio = self.txtPrecio.text()
        if marca and talla and precio is not None:
            rows = self.table.rowCount()
            self.table.insertRow(rows)
            self.table.setItem(rows, 0, QTableWidgetItem(marca))
            self.table.setItem(rows, 1, QTableWidgetItem(talla))
            self.table.setItem(rows, 2, QTableWidgetItem(precio))
        self.txtMarca.setText("")
        self.txtTalla.setText("")
        self.txtPrecio.setText("")


def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()


if __name__ == '__main__':
    main()
