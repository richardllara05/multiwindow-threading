from PyQt5 import QtWidgets
from utilities.calculator import Calculator
from utilities.grapher import Grapher

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # Needed for constructor to build window [QWidget with no argument is a window]
        self.setFixedSize(300, 100)
        self.setWindowTitle('Main Window')
        self.setupUI()

        self.show()


    def clickBtn(self):
        self.click_btn = QtWidgets.QPushButton(self)
        self.click_btn.setText('Calculator')

        # Signal and slot
        # Slot is the function to execute
        # Signal is the component action

        self.calculator = Calculator()
        self.click_btn.clicked.connect(self.calculator.display)
        self.click_btn.move(10, 70)

    def grapherBtn(self):
        self.grapher_btn = QtWidgets.QPushButton(self)
        self.grapher_btn.setText('Grapher')
        
        self.grapher = Grapher()
        self.grapher_btn.clicked.connect(self.grapher.display)
        self.grapher_btn.move(100, 70)
    

    def setupBtns(self):
        self.clickBtn()
        self.grapherBtn()
    
    def setupUI(self):
        self.setupBtns()
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.click_btn, 0, 0) 
        self.layout.addWidget(self.grapher_btn, 0, 1) 
        self.setLayout(self.layout)

