from PyQt5 import QtWidgets
import sys
from utilities import Calculator


class CustomWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # Needed for constructor to build window [QWidget with no argument is a window]
        self.btn = None
        self.setFixedSize(300, 100)  # x, y, width, height

        self.setToolTip('AFK')
        self.setWindowTitle('Custom Window')
        self.click_btn()
        self.quit_btn()

        self.show()

    def click_btn(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Click')

        # Signal and slot
        # Slot is the function to execute
        # Signal is the component action

        self.obj = Calculator()
        self.btn.clicked.connect(self.obj.display)
        self.btn.move(10, 70)

    def quit_btn(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Quit')
        self.btn.clicked.connect(self.close)
        self.btn.move(100, 70)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CustomWindow()
    app.exec_()
