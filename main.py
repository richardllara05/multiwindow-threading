'''
    1. Graphing utility slot missing for + button
    2. Graphing functionally missing
    3. Calculator slots missing
    4. Number system converter
    5. Metric system converter
    6. Currency converter
    7. Language translator
'''

import sys
from PyQt5 import QtWidgets
from window_app import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window : QtWidgets.QWidget = MainWindow()
    sys.exit(app.exec_())