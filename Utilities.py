from PyQt5 import QtWidgets


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.btn = None
        self.btn_pressed = None
        self.test_btn()

    def test_btn(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Test')

    def display(self):
        self.show()
