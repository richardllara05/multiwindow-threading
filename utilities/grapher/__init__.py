from PyQt5 import QtWidgets
from PyQt5.QtCore import ( 
    Qt,
    QObject,
    pyqtSignal
)


class Grapher(QtWidgets.QWidget):
    terminated = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setGeometry(1920 // 2, 1080 // 2, 800, 800) 
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Grapher')

        self.main_layout = QtWidgets.QGridLayout()
        formula_layout = QtWidgets.QVBoxLayout()

        display = QtWidgets.QTextEdit()
        display.setReadOnly(True)

        add_btn = QtWidgets.QPushButton("+")
        add_btn.setFixedWidth(100)
        add_btn.setFixedHeight(20)

        self.main_layout.addWidget(display, 0, 0, 1, 1)
        self.main_layout.addWidget(add_btn, 2, 0)

        formula_entry = QtWidgets.QTextEdit()
        formula_entry.setFixedWidth(100)
        formula_entry.setFixedHeight(20)
        formula_layout.addWidget(formula_entry)


        self.main_layout.addLayout(formula_layout, 3, 0)
        self.setLayout(self.main_layout)

    def display(self):
        self.show()

    def closeEvent(self, event):
        self.terminated.emit()

class GrapherWorker(QObject):
    finished = pyqtSignal()
    
    def run(self):
        self.grapher = Grapher()
        self.grapher.display()
        self.grapher.terminated.connect(lambda: self.finished.emit())