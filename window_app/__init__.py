from PyQt5 import QtWidgets, QtCore
from utilities.calculator import Calculator, CalculatorWorker
from utilities.grapher import Grapher, GrapherWorker


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        # Needed for constructor to build window [QWidget with no argument is a window]
        super().__init__()
        self.calc_btn = QtWidgets.QPushButton(self)
        self.grapher_btn = QtWidgets.QPushButton(self)

        self.calc_btn.move(100, 70)
        self.grapher_btn.move(100, 70)
        
        self.setFixedSize(300, 100)
        self.setWindowTitle('Main Window')
        self.setupUI()
        self.label = QtWidgets.QLabel()

        self.calc_btn.setText('Calculator')
        self.calc_btn.clicked.connect(self.calcClick)

        self.grapher_btn.setText('Grapher')
        self.grapher_btn.clicked.connect(self.grapherClick)

        self.show()

    def calcClick(self):

        # Signal and slot
        # Slot is the function to execute
        # Signal is the component action
        # self.calc_btn.move(10, 70)
        self.calc = Calculator()

        self.calc_thread = QtCore.QThread()
        self.calc_worker = CalculatorWorker()

        self.calc_worker.moveToThread(self.calc_thread)

        self.calc_thread.started.connect(self.calc_worker.run)
        self.calc_worker.finished.connect(self.calc_thread.quit)
        self.calc_thread.finished.connect(self.calc_thread.deleteLater)
        self.calc_worker.finished.connect(self.calc_worker.deleteLater)
        self.calc_thread.finished.connect(
            lambda: self.calc_btn.setEnabled(True))

        self.calc_thread.start()
        self.calc_btn.setEnabled(False)

    def grapherClick(self):
        self.grapher = Grapher()

        self.graph_thread = QtCore.QThread()
        self.graph_worker = GrapherWorker()

        self.graph_worker.moveToThread(self.graph_thread)

        self.graph_thread.started.connect(self.graph_worker.run)
        self.graph_worker.finished.connect(self.graph_thread.quit)
        self.graph_thread.finished.connect(self.graph_thread.deleteLater)
        self.graph_worker.finished.connect(self.graph_worker.deleteLater)
        self.graph_thread.finished.connect(
            lambda: self.grapher_btn.setEnabled(True))

        self.graph_thread.start()
        self.grapher_btn.setEnabled(False)

    def setupUI(self):
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.calc_btn, 0, 0)
        self.layout.addWidget(self.grapher_btn, 0, 1)
