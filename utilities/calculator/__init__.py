
from PyQt5 import QtWidgets
from PyQt5.QtCore import ( 
    Qt, 
    QObject, 
    pyqtSignal
)
class Calculator(QtWidgets.QWidget):
    terminated = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setGeometry(1920 // 2, 1080 // 2, 200, 200) 
        self.setupUI()
        self.display_value = pyqtSignal(str)

    def setupUI(self):
        self.setWindowTitle('Calculator')

        self.layout = QtWidgets.QGridLayout(self)
        # self.display  = QtWidgets.QLabel()
        # self.layout.addWidget(self.display, 0, 0, 1, 5, Qt.AlignmentFlag.AlignCenter)

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
                button = QtWidgets.QPushButton(symbols[row][col])
                button.clicked.connect(self.display_text)
                self.layout.addWidget(button, row + 1, col + 1)
            
    


    def display(self):
        self.show()

    def display_text(self):
        btn_pressed = self.sender()
        btn_text = btn_pressed.text()
        # self.display.setText(btn_text)
    
    def closeEvent(self, event):
        self.terminated.emit()

class CalculatorWorker(QObject):
    finished = pyqtSignal()
    
    def run(self):
        self.calculator = Calculator()
        self.calculator.display()
        self.calculator.terminated.connect(lambda: self.finished.emit())