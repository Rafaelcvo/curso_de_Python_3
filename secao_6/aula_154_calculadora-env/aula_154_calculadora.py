import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = calculadora()
    calc.show()
    qt.exec_()
# parou  em 3:08