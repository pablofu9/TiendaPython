import os
import sys
import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap, QStandardItemModel, QStandardItem
from PyQt5 import uic
from PyQt5.uic.properties import QtGui


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
        
        self.btnSumar.clicked.connect(lambda: self.veroperacion(self.btnSumar.text()))
        self.btnMultiplicar.clicked.connect(lambda: self.veroperacion(self.btnMultiplicar.text()))
        self.btnRestar.clicked.connect(lambda: self.veroperacion(self.btnRestar.text()))
        self.btnDividir.clicked.connect(lambda: self.veroperacion(self.btnDividir.text()))
        self.btnIgual.clicked.connect(self.resultado)

        # Variable que vamos a usar para las expresiones matematicas de la calculadora
        self.operacion = ""
        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # Para que la tabla se pueda hacer click pero no editar
        self.table.itemClicked.connect(self.tablaclick)
        self.table.itemClicked.connect(self.transfer)
        self.table.itemClicked.connect(self.delete_row)
        # Metodos enlazados a las tablas
        self.load()  # Metodo para cargar el array de productos de venta
        self.btnReset.clicked.connect(self.reset)  # Metodo del boton reset para setear la factura
        self.listaconfig()
        self.btnPagar.clicked.connect(self.irpago)  # Metodo para ir al pago de la factura
        # Añadir zapatillas a la tabla
        self.btnGenerar.clicked.connect(self.resetear)  # Boton para generar la factura de forma manual
        self.btnAnadir.clicked.connect(self.save)  # Boton para añadir nuevos objetos a la tabla
        # Boton para cambiar modo de oscuro a claro y de claro a oscuro

    def veroperacion(self, text):
        # Metodo para sacar la operacion por pantalla
        self.operacion += text
        self.txtOperacion.setText(self.operacion)

    def resultado(self):  # Este metodo recoge la informacion de lo que hemos pulsado en los botones y cuando
        # pulsamos en = lo que hace es, hacernos la operacion y nos pone el restulado abajo y nos reseta la
        # variable operacion
        if self.txtOperacion.toPlainText() == "":
            msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
            msg_box.setWindowTitle("Error")
            msg_box.setText("No hay nada que calcular")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.exec_()
        else:  # Aqui lo que hacemos es comprobar que el primer caracter que presionemos sea un numero, para evitar errores
            first = self.txtOperacion.toPlainText()[0]
            if '0' <= first <= '9':
                result = eval(self.txtOperacion.toPlainText())
                self.txtResultado.setText(str(result))
                self.txtOperacion.setText("")
                self.operacion = ""
            else:
                error2 = QMessageBox(self)
                error2.setWindowTitle("Error")
                error2.setText("Error en comienzo de cadena")
                error2.setIcon(QMessageBox.Critical)
                error2.exec_()
                self.txtOperacion.setText("")
                self.txtResultado.setText("")
                self.operacion = ""

            # el eval lo que hace es coger una expresion y la hace matematicamente

    def load(self):  # LLenamos la tabla
        products = [
            {'marca': 'Nike', 'talla': '39', 'precio': '100'},
            {'marca': 'Nike', 'talla': '42', 'precio': '80'},
            {'marca': 'Adidas', 'talla': '33', 'precio': '60'},
            {'marca': 'Adidas', 'talla': '39', 'precio': '105'},
            {'marca': 'Vans', 'talla': '44', 'precio': '40'},
            {'marca': 'New balance', 'talla': '38', 'precio': '80'},
            {'marca': 'New balance', 'talla': '40', 'precio': '99'},
            {'marca': 'Vans', 'talla': '39', 'precio': '70'},
        ]
        self.table.setRowCount(len(products))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(('Marca', 'talla', 'Precio'))

        index = 0  # Vamos a recorrer el array de productos para ir llenando la tabla
        for product in products:
            self.table.setItem(index, 0, QTableWidgetItem(product['marca']))
            self.table.setItem(index, 1, QTableWidgetItem(product['talla']))
            self.table.setItem(index, 2, QTableWidgetItem(product['precio']))
            index += 1

    def save(self):  # Metodo para añadir registros a la tabla, una vez añadido vacia los campos
        marca = " "  # Tenemos esta variable que se recoge mediante los radio buttons, que estran en el mismo radiogroup
        if self.rdNike.isChecked():
            marca = "Nike"
        elif self.rdAdidas.isChecked():
            marca = "Adidas"
        elif self.rdVans.isChecked():
            marca = "Vans"
        else:
            marca = "New balance"
        talla = self.txtTalla.text()
        precio = self.txtPrecio.text()
        if marca and talla and precio is not None:
            if re.match(r"^\d+$", talla) and re.match(r"^\d+$", precio):  # Comprobando que talla y precio son numeros
                rows = self.table.rowCount()
                self.table.insertRow(rows)
                self.table.setItem(rows, 0, QTableWidgetItem(marca))
                self.table.setItem(rows, 1, QTableWidgetItem(talla))
                self.table.setItem(rows, 2, QTableWidgetItem(precio))
            else:
                msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
                msg_box.setWindowTitle("Error")
                msg_box.setText("Talla y precio deben ser numeros")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.exec_()
        # Una vez esta hecho, vaciamos los campos de texto
        self.txtTalla.setText("")
        self.txtPrecio.setText("")

    def tablaclick(self, item):  # Metodo que te dice que item de la tabla has clickado
        # Seteamos los labels con la row que seleccionemos
        rows = item.row()
        img = self.table.item(rows, 0).text()  # al clickar en la tabla ponemos las imagenes que corresponden a la marca
        talla = self.table.item(rows, 1).text()
        precio = self.table.item(rows, 2).text()
        if img == 'Nike':
            self.imagen.setStyleSheet(
                "background-image: url('./nike.png');background-size: contain; background-repeat: no-repeat;")
        elif img == "Adidas":
            self.imagen.setStyleSheet(
                "background-image: url('./adidas.png');background-size: contain; background-repeat: no-repeat;")
        elif img == "Vans":
            self.imagen.setStyleSheet(
                "background-image: url('./vans.png');background-size: contain; background-repeat: no-repeat;")
        elif img == "New balance":
            self.imagen.setStyleSheet(
                "background-image: url('./newbalance.png');background-size: contain; background-repeat: no-repeat;")

    def transfer(self, item):
        total = 0
        rows = item.row()
        # Transferimos la informacion de una tabla a la otra, cuando pinchamos en la primera de ellas
        marca = self.table.item(rows, 0).text()
        talla = self.table.item(rows, 1).text()
        precio = self.table.item(rows, 2).text()

        rows = self.lista.rowCount()
        self.lista.insertRow(rows)
        self.lista.setItem(rows, 0, QTableWidgetItem(marca))
        self.lista.setItem(rows, 1, QTableWidgetItem(talla))
        self.lista.setItem(rows, 2, QTableWidgetItem(precio))
        for row in range(self.lista.rowCount()):  # Recorremos la tabla de la factura y acumulamos la columa de precio
            value = int(self.lista.item(row, 2).text())
            total += value  # Incrementamos el total de la factura con la columna precio de la tabla que se llama lista
        self.precioTotal.setText(str(total) + " €")

    def delete_row(self):  # Borra la fila que seleccionemos
        selected = self.table.selectedIndexes()
        if selected:
            row = selected[0].row()
            self.table.removeRow(row)

    def listaconfig(self):  # Para setear la configuración de la tabla de la factura
        self.lista.setColumnCount(3)
        self.lista.setHorizontalHeaderLabels(('Marca', 'talla', 'Precio'))

    def reset(self):  # Volvemos a llenar la tabla principal y despues vaciamos la tabla de la factura
        # Este metodo esta enlazado al boton de reset
        self.load()
        self.lista.setRowCount(0)
        self.precioTotal.setText("")

    def irpago(self, item):  # Metodo enlazado al boton de ir al pago, si hemos seleccionado generar la factura manual
        # Nos lo hara de una manera distinta
        if self.btnPagar.text() == "PAGAR":
            if self.precioTotal.text() == "":
                msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
                msg_box.setWindowTitle("No products")
                msg_box.setText("Debes seleccionar algun producto")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
                msg_box.setWindowTitle("Su factura")
                msg_box.setText("Aqui tiene sus productos")
                msg_box.setIcon(QMessageBox.Information)
                info = ""
                for i in range(self.lista.rowCount()):
                    for j in range(self.lista.columnCount()):
                        item = self.lista.item(i, j)
                        if item is not None:
                            info += item.text() + "\n"
                msg_box.setInformativeText(info)
                msg_box.setDetailedText("Total " + self.precioTotal.text())

                msg_box.exec_()
                sys.exit(0)
        else:
            if self.txtResultado.toPlainText() == "":
                msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
                msg_box.setWindowTitle("Nada que hacer...")
                msg_box.setText("Realiza una operación")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.exec_()
            else:
                self.precioTotal.setText(self.txtResultado.toPlainText())
                msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
                msg_box.setWindowTitle("Su factura")
                msg_box.setText("TOTAL A PAGAR --> " + self.precioTotal.text() + " €")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.exec_()
                sys.exit(0)

    def resetear(self):  # Metodo para que seleccionemos si queremos la factura manual o autogenerada
        msg_box = QMessageBox(self)  # Si no hay productos seleccionados salta error
        msg_box.setWindowTitle("Factura manual")
        msg_box.setText("¿Desde generar la factura de forma manual?")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        respuesta = msg_box.exec_()
        if respuesta == QMessageBox.Ok:
            self.btnPagar.setText("€€")
            self.precioTotal.setText("")
        elif respuesta == QMessageBox.Cancel:
            self.btnPagar.setText("PAGAR")


def main():  # Iniciamos la app
    app = QApplication([])
    window = MyGui()
    window.setFixedSize(1100, 600)
    app.exec_()


if __name__ == '__main__':
    main()
