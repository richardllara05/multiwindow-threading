from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1920 // 2, 1080 // 2, 200, 200) 
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Calculator')

        display = QtWidgets.QTextEdit()
        display.setReadOnly(True)

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(display, 0, 0, 1, 5, Qt.AlignmentFlag.AlignCenter)

        symbols = [
            ['%', 'CE', 'C', 'DEL'],
            ['1\u2044x', 'x\u00b2', '\u221Ax\u0305', '/'],
            ['7', '8', '9',   'X'],
            ['4', '5', '6',   '-'],
            ['1', '2', '3',   '+'],
            ['\u00b1', '0', '.', '='],
        ]

        ROW_LEN = len(symbols)
        COL_LEN = len(symbols[0])

        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                self.layout.addWidget(QtWidgets.QPushButton(symbols[row][col]), row + 1, col + 1)
            

        
        self.setLayout(self.layout)

    def display(self):
        self.show()
